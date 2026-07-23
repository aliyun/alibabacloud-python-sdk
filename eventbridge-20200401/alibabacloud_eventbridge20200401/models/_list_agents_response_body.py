# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListAgentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAgentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The API status code or POP error code. Valid values: Success: The operation was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID. Alibaba Cloud generates a unique identifier for the request.
        self.request_id = request_id
        # Returns true if the operation is successful.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAgentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAgentsResponseBodyData(DaraModel):
    def __init__(
        self,
        agents: List[main_models.Agent] = None,
        first_id: str = None,
        has_more: str = None,
        last_id: str = None,
    ):
        # The list of agents.
        self.agents = agents
        # The ID of the first record.
        self.first_id = first_id
        # Indicates whether more pages are available. Valid values:
        # 
        # - true: More pages are available.
        # 
        # - false: No more pages are available.
        self.has_more = has_more
        # The ID of the last record.
        self.last_id = last_id

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['Agents'].append(k1.to_map() if k1 else None)

        if self.first_id is not None:
            result['FirstId'] = self.first_id

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.last_id is not None:
            result['LastId'] = self.last_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('Agents') is not None:
            for k1 in m.get('Agents'):
                temp_model = main_models.Agent()
                self.agents.append(temp_model.from_map(k1))

        if m.get('FirstId') is not None:
            self.first_id = m.get('FirstId')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('LastId') is not None:
            self.last_id = m.get('LastId')

        return self

