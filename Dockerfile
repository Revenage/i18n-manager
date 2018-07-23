FROM nginx

RUN mkdir -p /app
COPY nginx.conf /etc/nginx/nginx.conf
RUN service nginx start