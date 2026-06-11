# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCmsServiceRequest(DaraModel):
    def __init__(
        self,
        product: str = None,
        service: str = None,
    ):
        # prometheus: Checks the activation status of the Prometheus service. The service is billed by reported data volume or written data volume.
        self.product = product
        # prometheus: Checks whether the Prometheus product that is billed by reported data volume is activated.prometheusgb: Checks whether the Prometheus product that is billed by written data volume is activated.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['product'] = self.product

        if self.service is not None:
            result['service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('service') is not None:
            self.service = m.get('service')

        return self

