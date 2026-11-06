# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationSessionLogsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        items: main_models.DescribeApplicationSessionLogsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The application ID.
        self.application_id = application_id
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of log records returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of log records that meet the query conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeApplicationSessionLogsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeApplicationSessionLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeApplicationSessionLogsResponseBodyItemsItems] = None,
    ):
        self.items = items

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeApplicationSessionLogsResponseBodyItemsItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeApplicationSessionLogsResponseBodyItemsItems(DaraModel):
    def __init__(
        self,
        agent: str = None,
        api: str = None,
        content: str = None,
        detail_duration_ms: int = None,
        detail_is_error: bool = None,
        detail_status: str = None,
        id: str = None,
        model: str = None,
        parent_id: str = None,
        provider: str = None,
        role: str = None,
        session_id: str = None,
        status: str = None,
        stop_reason: str = None,
        text: str = None,
        thinking: str = None,
        thinking_signature: str = None,
        time: str = None,
        timestamp: str = None,
        tool_name: str = None,
        total_tokens: int = None,
        type: str = None,
        usage_cache_read: int = None,
        usage_cache_write: int = None,
        usage_cost_cache_read: int = None,
        usage_cost_cache_write: int = None,
        usage_cost_input: int = None,
        usage_cost_output: int = None,
        usage_cost_total: int = None,
        usage_input: int = None,
        usage_output: int = None,
        usage_total_tokens: int = None,
    ):
        self.agent = agent
        self.api = api
        self.content = content
        self.detail_duration_ms = detail_duration_ms
        self.detail_is_error = detail_is_error
        self.detail_status = detail_status
        self.id = id
        self.model = model
        self.parent_id = parent_id
        self.provider = provider
        self.role = role
        self.session_id = session_id
        self.status = status
        self.stop_reason = stop_reason
        self.text = text
        self.thinking = thinking
        self.thinking_signature = thinking_signature
        self.time = time
        self.timestamp = timestamp
        self.tool_name = tool_name
        self.total_tokens = total_tokens
        self.type = type
        self.usage_cache_read = usage_cache_read
        self.usage_cache_write = usage_cache_write
        self.usage_cost_cache_read = usage_cost_cache_read
        self.usage_cost_cache_write = usage_cost_cache_write
        self.usage_cost_input = usage_cost_input
        self.usage_cost_output = usage_cost_output
        self.usage_cost_total = usage_cost_total
        self.usage_input = usage_input
        self.usage_output = usage_output
        self.usage_total_tokens = usage_total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent

        if self.api is not None:
            result['Api'] = self.api

        if self.content is not None:
            result['Content'] = self.content

        if self.detail_duration_ms is not None:
            result['DetailDurationMs'] = self.detail_duration_ms

        if self.detail_is_error is not None:
            result['DetailIsError'] = self.detail_is_error

        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status

        if self.id is not None:
            result['Id'] = self.id

        if self.model is not None:
            result['Model'] = self.model

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.role is not None:
            result['Role'] = self.role

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_reason is not None:
            result['StopReason'] = self.stop_reason

        if self.text is not None:
            result['Text'] = self.text

        if self.thinking is not None:
            result['Thinking'] = self.thinking

        if self.thinking_signature is not None:
            result['ThinkingSignature'] = self.thinking_signature

        if self.time is not None:
            result['Time'] = self.time

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.type is not None:
            result['Type'] = self.type

        if self.usage_cache_read is not None:
            result['UsageCacheRead'] = self.usage_cache_read

        if self.usage_cache_write is not None:
            result['UsageCacheWrite'] = self.usage_cache_write

        if self.usage_cost_cache_read is not None:
            result['UsageCostCacheRead'] = self.usage_cost_cache_read

        if self.usage_cost_cache_write is not None:
            result['UsageCostCacheWrite'] = self.usage_cost_cache_write

        if self.usage_cost_input is not None:
            result['UsageCostInput'] = self.usage_cost_input

        if self.usage_cost_output is not None:
            result['UsageCostOutput'] = self.usage_cost_output

        if self.usage_cost_total is not None:
            result['UsageCostTotal'] = self.usage_cost_total

        if self.usage_input is not None:
            result['UsageInput'] = self.usage_input

        if self.usage_output is not None:
            result['UsageOutput'] = self.usage_output

        if self.usage_total_tokens is not None:
            result['UsageTotalTokens'] = self.usage_total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DetailDurationMs') is not None:
            self.detail_duration_ms = m.get('DetailDurationMs')

        if m.get('DetailIsError') is not None:
            self.detail_is_error = m.get('DetailIsError')

        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopReason') is not None:
            self.stop_reason = m.get('StopReason')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Thinking') is not None:
            self.thinking = m.get('Thinking')

        if m.get('ThinkingSignature') is not None:
            self.thinking_signature = m.get('ThinkingSignature')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsageCacheRead') is not None:
            self.usage_cache_read = m.get('UsageCacheRead')

        if m.get('UsageCacheWrite') is not None:
            self.usage_cache_write = m.get('UsageCacheWrite')

        if m.get('UsageCostCacheRead') is not None:
            self.usage_cost_cache_read = m.get('UsageCostCacheRead')

        if m.get('UsageCostCacheWrite') is not None:
            self.usage_cost_cache_write = m.get('UsageCostCacheWrite')

        if m.get('UsageCostInput') is not None:
            self.usage_cost_input = m.get('UsageCostInput')

        if m.get('UsageCostOutput') is not None:
            self.usage_cost_output = m.get('UsageCostOutput')

        if m.get('UsageCostTotal') is not None:
            self.usage_cost_total = m.get('UsageCostTotal')

        if m.get('UsageInput') is not None:
            self.usage_input = m.get('UsageInput')

        if m.get('UsageOutput') is not None:
            self.usage_output = m.get('UsageOutput')

        if m.get('UsageTotalTokens') is not None:
            self.usage_total_tokens = m.get('UsageTotalTokens')

        return self

