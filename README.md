# Link Checker

Checks links for a given domain

Experimenting during Dockercon19 workshop

## Run

```sh
docker run --rm -it theremix/linkchecker https://airshipcms.io
```

## Build and Run

```
docker build -t dockercon19/linkchecker:v1.0 .
docker run --rm -it dockercon19/linkchecker:v1.0 https://airshipcms.io
```

