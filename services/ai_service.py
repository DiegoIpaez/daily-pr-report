import datetime
import google.generativeai as genai
from utils.constants import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.logger import ai_log, app_log

genai.configure(api_key=GEMINI_API_KEY)


def generate_professional_report(reporte_raw):
    currentDate = datetime.datetime.now(datetime.UTC).strftime("%d/%m/%Y")

    prompt = f"""
## 📄 Generador de Reporte de Pull Requests y Commits
**ROL:** Eres un asistente profesional de desarrollo de software especializado en la redacción de informes técnicos.
**TAREA:** A continuación, se proporciona una lista detallada de Pull Requests (PRs) con sus respectivos commits. Tu objetivo es generar un reporte consolidado, formal y profesional en español, siguiendo **ESTRICTAMENTE** el formato de salida solicitado.
### INSTRUCCIONES DE PROCESAMIENTO:
1.  **Traducción y Resumen:** Por cada commit, traduce el título del commit al español y genera un **resumen conciso y formal** de la acción realizada (ej: 'Se añade', 'Se corrige', 'Se actualiza').
2.  **Consolidación:** Agrupa todos los commits bajo el PR al que pertenecen.
3.  **Eliminación de Detalles Crudos:** NO incluyas SHAs de commit, URLs, estados de PR, autores, fechas, labels, ni la información de 'Repositorio' dentro del detalle del commit. Solo usa el nombre del repositorio y el título del PR para la cabecera.
### FORMATO DE SALIDA REQUERIDO (Estricto):
```
DR {currentDate}
- [Nombre del Repositorio] - [Título del Pull Request]
+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.
+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.

- [Nombre del Repositorio] - [Otro Título del Pull Request]
+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.
```
--- DATOS DE ENTRADA (Reporte Crudo) ---
{reporte_raw}
    """
    app_log(prompt)

    model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
    response = model.generate_content(
        [prompt],
        safety_settings=None,
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 2048,
        },
        request_options={"timeout": 20},
    )
    
    resumen_str = str(response.candidates[0].content.parts[0].text).strip()
    ai_log(response)
    return resumen_str
