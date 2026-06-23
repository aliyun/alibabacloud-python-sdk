# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CommercializeFetchRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        data: str = None,
        product_id: str = None,
        request_id: str = None,
        secret_key: str = None,
        sign: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.data = data
        # This parameter is required.
        self.product_id = product_id
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.secret_key = secret_key
        # This parameter is required.
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['channelId'] = self.channel_id

        if self.data is not None:
            result['data'] = self.data

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.secret_key is not None:
            result['secretKey'] = self.secret_key

        if self.sign is not None:
            result['sign'] = self.sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')

        if m.get('sign') is not None:
            self.sign = m.get('sign')

        return self

