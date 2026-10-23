FROM amazoncorretto:21-alpine
WORKDIR /app
COPY ./target/*.war app.war
EXPOSE 8090
ENTRYPOINT ["java", "-jar", "app.war"]