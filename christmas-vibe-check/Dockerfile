FROM python:3.9-slim

# 1. Receive the flag from cmgr during build 
ARG FLAG

# 2. Setup Challenge and Cheat Detection
# We create the directory for metadata
RUN install -d -m 0700 /challenge/

# Copy and run the setup script to generate the specific instance flag
COPY setup_challenge.py /challenge/setup_challenge.py
RUN python3 /challenge/setup_challenge.py

# 3. Application Setup
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
COPY templates/ templates/

RUN tar czvf /challenge/artifacts.tar.gz main.py

# 4. Security
RUN useradd -m ctf
RUN chown -R ctf:ctf /challenge
RUN chown -R ctf:ctf /app
USER ctf

# 5. CMGR Network Configuration
# The guide requires EXPOSE followed by the PUBLISH comment 
EXPOSE 8080
# PUBLISH 8080 AS website

CMD ["python", "main.py"]