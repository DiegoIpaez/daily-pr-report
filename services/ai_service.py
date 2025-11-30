import datetime
import google.generativeai as genai
from utils.constants import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.logger import ai_log

genai.configure(api_key=GEMINI_API_KEY)

def generate_professional_report(reporte_raw):
    currentDate = datetime.datetime.now(datetime.UTC).strftime("%d/%m/%Y")

    prompt = (
        f"DR {currentDate}\n\n"
        "## 📄 Generador de Reporte de Pull Requests y Commits\n"
        "**ROL:** Eres un asistente profesional de desarrollo de software especializado en la redacción de informes técnicos.\n"
        "**TAREA:** A continuación, se proporciona una lista detallada de Pull Requests (PRs) con sus respectivos commits.\n"
        "Tu objetivo es generar un reporte consolidado, formal y profesional en español, siguiendo **ESTRICTAMENTE** el formato de salida solicitado.\n\n"
        "### INSTRUCCIONES DE PROCESAMIENTO:\n"
        "1.  **Traducción y Resumen:** Por cada commit, traduce el título del commit al español y genera un **resumen conciso y formal** de la acción realizada (ej: 'Se añade', 'Se corrige', 'Se actualiza').\n"
        "2.  **Consolidación:** Agrupa todos los commits bajo el PR al que pertenecen.\n"
        "3.  **Eliminación de Detalles Crudos:** NO incluyas SHAs de commit, URLs, estados de PR, autores, fechas, labels, ni la información de 'Repositorio' dentro del detalle del commit. Solo usa el nombre del repositorio y el título del PR para la cabecera.\n\n"
        "### FORMATO DE SALIDA REQUERIDO (Estricto):\n"
        "```\n"
        "DR {currentDate}\n"
        "- [Nombre del Repositorio] - [Título del Pull Request]\n"
        "+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.\n"
        "+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.\n"
        "\n"
        "- [Nombre del Repositorio] - [Otro Título del Pull Request]\n"
        "+ [Resumen Formal del Commit en Español]: Traducción completa del título original del commit.\n"
        "```\n\n"
        f"--- DATOS DE ENTRADA (Reporte Crudo) ---\n"
        f"{reporte_raw}"
    )

    model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
    response = model.generate_content([prompt])
    resumen_str = str(response.candidates[0].content.parts[0].text).strip()

    ai_log(response)
    return resumen_str