# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetConsumerGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetConsumerGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = main_models.GetConsumerGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetConsumerGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        consumer_count: int = None,
        consumer_group_id: str = None,
        create_timestamp: int = None,
        description: str = None,
        gateway_type: str = None,
        name: str = None,
        update_timestamp: int = None,
    ):
        self.consumer_count = consumer_count
        self.consumer_group_id = consumer_group_id
        self.create_timestamp = create_timestamp
        self.description = description
        self.gateway_type = gateway_type
        self.name = name
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_count is not None:
            result['consumerCount'] = self.consumer_count

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['description'] = self.description

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.name is not None:
            result['name'] = self.name

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerCount') is not None:
            self.consumer_count = m.get('consumerCount')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

