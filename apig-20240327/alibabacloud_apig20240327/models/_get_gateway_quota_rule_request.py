# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGatewayQuotaRuleRequest(DaraModel):
    def __init__(
        self,
        consumer_page_number: str = None,
        consumer_page_size: str = None,
        with_consumers: bool = None,
    ):
        self.consumer_page_number = consumer_page_number
        self.consumer_page_size = consumer_page_size
        self.with_consumers = with_consumers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_page_number is not None:
            result['consumerPageNumber'] = self.consumer_page_number

        if self.consumer_page_size is not None:
            result['consumerPageSize'] = self.consumer_page_size

        if self.with_consumers is not None:
            result['withConsumers'] = self.with_consumers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerPageNumber') is not None:
            self.consumer_page_number = m.get('consumerPageNumber')

        if m.get('consumerPageSize') is not None:
            self.consumer_page_size = m.get('consumerPageSize')

        if m.get('withConsumers') is not None:
            self.with_consumers = m.get('withConsumers')

        return self

