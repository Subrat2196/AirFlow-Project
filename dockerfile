FROM apache/airflow:2.6.3

# COPY Requirements

COPY requirements.txt /

# Official way to install packages
RUN bash -c "pip install --user --no-cache-dir -r /requirements.txt"

# Set PYTHONPATH to include DAGs directory so 'scripts is importable'

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/dags"

