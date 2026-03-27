# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrometheusInstanceResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_instance_id: str = None,
        request_id: str = None,
    ):
        # Instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # ID of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

