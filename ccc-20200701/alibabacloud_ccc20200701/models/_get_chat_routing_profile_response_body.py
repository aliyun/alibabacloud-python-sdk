# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetChatRoutingProfileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetChatRoutingProfileResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetChatRoutingProfileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetChatRoutingProfileResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_concurrency_settings: str = None,
        chat_settings: str = None,
        distribution_settings: str = None,
        routing_type: str = None,
    ):
        self.agent_concurrency_settings = agent_concurrency_settings
        self.chat_settings = chat_settings
        self.distribution_settings = distribution_settings
        self.routing_type = routing_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_concurrency_settings is not None:
            result['AgentConcurrencySettings'] = self.agent_concurrency_settings

        if self.chat_settings is not None:
            result['ChatSettings'] = self.chat_settings

        if self.distribution_settings is not None:
            result['DistributionSettings'] = self.distribution_settings

        if self.routing_type is not None:
            result['RoutingType'] = self.routing_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentConcurrencySettings') is not None:
            self.agent_concurrency_settings = m.get('AgentConcurrencySettings')

        if m.get('ChatSettings') is not None:
            self.chat_settings = m.get('ChatSettings')

        if m.get('DistributionSettings') is not None:
            self.distribution_settings = m.get('DistributionSettings')

        if m.get('RoutingType') is not None:
            self.routing_type = m.get('RoutingType')

        return self

