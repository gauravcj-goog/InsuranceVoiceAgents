FROM nginx:alpine

# Copy static assets from the repository to Nginx web root /static
COPY app/static /usr/share/nginx/html/static

# Move index.html to the root so it's served at /
RUN mv /usr/share/nginx/html/static/index.html /usr/share/nginx/html/index.html

# Configure Nginx to listen on port 8080 (Cloud Run requirement)
RUN sed -i 's/listen       80;/listen       8080;/g' /etc/nginx/conf.d/default.conf

# Expose port 8080
EXPOSE 8080

# (Optional) Add a script to inject environment variables into config.js at runtime
# For now, we rely on the config.js being present or overwritten by volume/configmap.
