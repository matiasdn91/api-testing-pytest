import pytest
from datetime import datetime
import os

# Crear la carpeta reports si no existe
if not os.path.exists("reports"):
    os.makedirs("reports")

# Generar timestamp para el nombre del reporte
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"reports/report_{timestamp}.html"

# Ejecutar pytest con reporte HTML
pytest_args = [
    "tests",
    "-v",
    f"--html={report_file}",
    "--self-contained-html"
]

# Ejecutar pytest
exit_code = pytest.main(pytest_args)

# Mensaje de finalización
print(f"\nReporte generado: {report_file}")
exit(exit_code)