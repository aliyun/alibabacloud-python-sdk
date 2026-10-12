# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetHiMarketConsumerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHiMarketConsumerResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetHiMarketConsumerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetHiMarketConsumerResponseBodyData(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        description: str = None,
        is_primary: bool = None,
        name: str = None,
    ):
        # The consumer ID.
        self.consumer_id = consumer_id
        # The description of the consumer.
        self.description = description
        # Indicates whether the consumer is the primary consumer.
        self.is_primary = is_primary
        # The name of the consumer.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.description is not None:
            result['description'] = self.description

        if self.is_primary is not None:
            result['isPrimary'] = self.is_primary

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isPrimary') is not None:
            self.is_primary = m.get('isPrimary')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

