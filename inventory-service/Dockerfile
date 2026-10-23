FROM amazoncorretto:21-alpine
WORKDIR /app
COPY ./target/*.war app.war
EXPOSE 8092
ENTRYPOINT ["java", "-jar", "app.war"]