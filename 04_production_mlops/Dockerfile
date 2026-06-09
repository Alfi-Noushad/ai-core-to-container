# TODO: Step 1 - Define the lightweight Python base image.
# Use the official 'python:3.10-slim' repository track.
FROM python:3.10-slim

# TODO: Step 2 - Establish an internal isolated execution workspace directory.
# Set the target folder path inside the container to '/app'.
WORKDIR /app

# Copy the requirements file into the current working directory (/app)
COPY requirements.txt .

# TODO: Step 3 - Execute a RUN command using pip to install the requirements file.
# Hint: Execute: pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all local scripts and assets directly into the container folder space
COPY . .

# TODO: Step 4 - Inform the engine network overlay that the container listens on port 8000.
# Use the EXPOSE keyword.
EXPOSE 8000

# TODO: Step 5 - Specify the core runtime execution command.
# Pass an array of strings that executes uvicorn pointing to 'day24_ops:app' 
# bound globally to host '0.0.0.0' on port '8000'.
# Structure hint: CMD ["uvicorn", "day24_ops:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "day24_ops:app", "--host", "0.0.0.0", "--port", "8000"]