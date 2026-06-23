# PayShield Watch

**English**

PayShield Watch is a lightweight monitoring and observability service for payment workflows. It ingests
decision events from other components (such as PayShield Core and PayShield Risk) and exposes basic
operational metrics such as total transactions, approvals, declines, reviews and average latency. A
simple `/stats` endpoint returns the aggregated statistics and can be hooked into dashboards like
Grafana or Prometheus for real‑time visualization.

This repository is part of the **PayShield Platform**, which simulates a complete payment ecosystem
for educational purposes. No real cardholder data is processed or stored.

**Disclaimer**: This is an educational project. The implementation uses in‑memory counters and naive
logic. It is not intended for production use.

---

**Português**

PayShield Watch é um serviço leve de monitoramento e observabilidade para fluxos de pagamento. Ele
ingere eventos de decisão de outros componentes (como PayShield Core e PayShield Risk) e expõe
métricas operacionais básicas, como total de transações, aprovações, recusas, revisões e latência média.
Um endpoint simples `/stats` retorna as estatísticas agregadas e pode ser integrado a dashboards como
Grafana ou Prometheus para visualização em tempo real.

Este repositório faz parte da **Plataforma PayShield**, que simula um ecossistema completo de
pagamentos para fins educacionais. Nenhum dado real de portadores de cartão é processado ou armazenado.

**Aviso**: Este é um projeto educacional. A implementação utiliza contadores em memória e lógica
ingînua. Não é destinada ao uso em produção.
