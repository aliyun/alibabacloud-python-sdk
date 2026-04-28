# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        consumer_id: str = None,
        key_type: str = None,
        request_id: str = None,
    ):
        self.api_key = api_key
        self.consumer_id = consumer_id
        self.key_type = key_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

