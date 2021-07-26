# thestaticturtle.fr.dynamic
Source code of the dynamic version of https://thestaticturtle.fr

Docker comose file:
```yml
web_main_dynamic:
    image: thestaticturtle_django:latest
    environment:
      DJANGO_ALLOWED_HOSTS: 'beta.fr.thestaticturtle.fr,fr.thestaticturtle.fr,thestaticturtle.fr'
      DEBUG: 'False'
      DJANGO_SECRET_KEY: fake
    networks:
      - frontend
      - backend
    volumes:
      - ./data/web-dynamic:/app/database
```

Reminders:
  - Needs to run database migrations and insert the nessesary key for the pages to work
  - Database will be readonly unless a `chmod www-data:root /app/database/ -R` is executed
