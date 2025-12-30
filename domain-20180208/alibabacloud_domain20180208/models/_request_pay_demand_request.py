# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RequestPayDemandRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        message: str = None,
        price: float = None,
        produce_type: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.domain_name = domain_name
        self.message = message
        # This parameter is required.
        self.price = price
        self.produce_type = produce_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.message is not None:
            result['Message'] = self.message

        if self.price is not None:
            result['Price'] = self.price

        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')

        return self

