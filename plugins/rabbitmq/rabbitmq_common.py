from common import (
    checks,
)

RMQ_SERVICES_EXPRS = [
    r"beam.smp",
    r"epmd",
    r"rabbitmq-server",
]
RMQ_PACKAGES = [
    r"rabbitmq-server",
]


class RabbitMQChecksBase(checks.ServiceChecksBase):

    def __init__(self):
        super().__init__(RMQ_SERVICES_EXPRS, hint_range=(0, 3))
