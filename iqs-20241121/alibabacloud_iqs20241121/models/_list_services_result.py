# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class ListServicesResult(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        services: main_models.LrOrder = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.services = services
        self.total = total

    def validate(self):
        if self.services:
            self.services.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.services is not None:
            result['services'] = self.services.to_map()

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('services') is not None:
            temp_model = main_models.LrOrder()
            self.services = temp_model.from_map(m.get('services'))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

