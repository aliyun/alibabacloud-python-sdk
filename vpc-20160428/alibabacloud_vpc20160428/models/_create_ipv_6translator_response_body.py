# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIPv6TranslatorResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6translator_id: str = None,
        name: str = None,
        order_id: int = None,
        request_id: str = None,
        spec: str = None,
    ):
        # The ID of the IPv6 Translation Service instance.
        self.ipv_6translator_id = ipv_6translator_id
        # The name of the IPv6 Translation Service instance.
        self.name = name
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The specification of the IPv6 Translation Service instance.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6translator_id is not None:
            result['Ipv6TranslatorId'] = self.ipv_6translator_id

        if self.name is not None:
            result['Name'] = self.name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6TranslatorId') is not None:
            self.ipv_6translator_id = m.get('Ipv6TranslatorId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

