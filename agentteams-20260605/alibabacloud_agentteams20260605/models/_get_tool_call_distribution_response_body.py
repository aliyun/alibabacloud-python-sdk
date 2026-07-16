# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetToolCallDistributionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetToolCallDistributionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetToolCallDistributionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetToolCallDistributionResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetToolCallDistributionResponseBodyDataItems] = None,
        total_calls: int = None,
    ):
        self.items = items
        self.total_calls = total_calls

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetToolCallDistributionResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        return self

class GetToolCallDistributionResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        call_count: int = None,
        tool_name: str = None,
    ):
        self.call_count = call_count
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        return self

