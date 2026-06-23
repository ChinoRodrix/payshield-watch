# PayShield Watch

## Overview

PayShield Watch is the monitoring and observability service of the PayShield Platform. It ingests decision events from payment flows (approvals, declines, reviews and errors) and produces aggregated metrics including total transactions, approval/decline counts, average latency and fraud incidents. It exposes a simple REST API to register events and to query the current statistics. This service demonstrates how to build a lightweight monitoring pipeline for payments.

## Architecture / Arquitetura

```
Origem (Core/Risk services)
    |
    | POST /event (decision, latency, timestamp)
    v
Aggregation Service (FastAPI)
    |
    |---> Metrics store (memory / MongoDB / Prometheus)
    |
    +---> Aggregators (count, average latency, fraud counts)
            |
            v
        GET /stats -> JSON metrics
```

## OpenAPI / Swagger

This service uses FastAPI to auto-generate API documentation. After running (`uvicorn main:app --reload`), open `http://localhost:8000/docs` to view the Swagger UI, test the `/event` and `/stats` endpoints, and inspect request/response models. For raw OpenAPI JSON, use `/openapi.json`.

## Use Cases

- **Record decision events** – register approvals, reviews, declines and errors from PayShield Core and PayShield Risk to build metrics.
- **Retrieve aggregated statistics** – query current totals and latencies to feed dashboards like Grafana or Prometheus.
- **Extend for alerts** – adapt the service to publish metrics to a time-series database or trigger alerts based on thresholds.

## Roadmap

- Persist events to MongoDB to support history and retention.
- Add authentication and API keys for ingestion endpoints.
- Integrate with Prometheus / Grafana for real-time dashboards and alerting.
- Support configurable alert thresholds and webhooks.

## Screenshots

*To be added.* Future updates may include screenshots of Grafana dashboards and API documentation.

## Disclaimer

This repository is an educational project. It uses simulated data and naive aggregation solely for learning purposes. No real transaction data is processed or stored. Do not use this code in production environments.

---

# PayShield Watch

## Visão Geral

O PayShield Watch é o serviço de monitoramento e observabilidade da plataforma PayShield. Ele ingere eventos de decisão de pagamentos (aprovações, recusas, revisões e erros) e produz métricas agregadas, incluindo total de transações, contagens de aprovações/recusas, latência média e incidentes de fraude. Ele expõe uma API REST simples para registrar eventos e consultar as estatísticas atuais. Este serviço demonstra como construir um pipeline de monitoramento leve para pagamentos.

## Arquitetura / Architecture

```
Origem (serviços Core/Risk)
    |
    | POST /event (decisão, latência, timestamp)
    v
Serviço de Agregação (FastAPI)
    |
    |---> Armazenamento de métricas (memória / MongoDB / Prometheus)
    |
    +---> Agregadores (contagem, latência média, fraudes)
            |
            v
        GET /stats -> JSON de métricas
```

## OpenAPI / Swagger

O serviço usa FastAPI para gerar automaticamente a documentação da API. Após executar (`uvicorn main:app --reload`), abra `http://localhost:8000/docs` para ver a interface Swagger, testar os endpoints `/event` e `/stats` e inspecionar os modelos de requisição/resposta. Para o JSON do OpenAPI, use `/openapi.json`.

## Casos de Uso

- **Registrar eventos de decisão** – registre aprovações, revisões, recusas e erros do PayShield Core e do PayShield Risk para construir métricas.
- **Recuperar estatísticas agregadas** – consulte os totais e latências atuais para alimentar dashboards como Grafana ou Prometheus.
- **Estender para alertas** – adapte o serviço para publicar métricas em um banco de séries temporais ou disparar alertas com base em limiares.

## Roadmap

- Persistir eventos em MongoDB para suportar histórico e retenção.
- Adicionar autenticação e chaves de API para os endpoints de ingesção.
- Integrar com Prometheus / Grafana para dashboards e alertas em tempo real.
- Suportar limiares de alerta configuráveis e webhooks.

## Screenshots

*A serem adicionadas.* Atualizações futuras podem incluir capturas de tela de dashboards no Grafana e documentação da API.

## Aviso

Este repositório é um projeto educacional. Ele usa dados simulados e agregações ingênuas apenas para fins de aprendizado. Nenhum dado real de transação é processado ou armazenado. Não utilize este código em ambientes de produção.
