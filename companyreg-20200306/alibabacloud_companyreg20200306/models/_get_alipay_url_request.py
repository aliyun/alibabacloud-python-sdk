# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlipayUrlRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        order_id: int = None,
        return_url: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.order_id = order_id
        self.return_url = return_url
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

