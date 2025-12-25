# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetEntityStoreDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[List[str]] = None,
        header: List[str] = None,
        request_id: str = None,
        response_status: main_models.GetEntityStoreDataResponseBodyResponseStatus = None,
    ):
        # Total list of returned data
        self.data = data
        # List of request headers
        self.header = header
        # Request ID
        self.request_id = request_id
        # Result status
        self.response_status = response_status

    def validate(self):
        if self.response_status:
            self.response_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.header is not None:
            result['header'] = self.header

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.response_status is not None:
            result['responseStatus'] = self.response_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('responseStatus') is not None:
            temp_model = main_models.GetEntityStoreDataResponseBodyResponseStatus()
            self.response_status = temp_model.from_map(m.get('responseStatus'))

        return self

class GetEntityStoreDataResponseBodyResponseStatus(DaraModel):
    def __init__(
        self,
        execution_states: str = None,
        level: str = None,
        result: str = None,
        retry_policy: str = None,
        status_item: List[main_models.GetEntityStoreDataResponseBodyResponseStatusStatusItem] = None,
    ):
        # Information during the execution process
        self.execution_states = execution_states
        # Status level
        self.level = level
        # Execution result
        self.result = result
        # Retry policy
        self.retry_policy = retry_policy
        # Detailed status information list
        self.status_item = status_item

    def validate(self):
        if self.status_item:
            for v1 in self.status_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_states is not None:
            result['executionStates'] = self.execution_states

        if self.level is not None:
            result['level'] = self.level

        if self.result is not None:
            result['result'] = self.result

        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy

        result['statusItem'] = []
        if self.status_item is not None:
            for k1 in self.status_item:
                result['statusItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionStates') is not None:
            self.execution_states = m.get('executionStates')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')

        self.status_item = []
        if m.get('statusItem') is not None:
            for k1 in m.get('statusItem'):
                temp_model = main_models.GetEntityStoreDataResponseBodyResponseStatusStatusItem()
                self.status_item.append(temp_model.from_map(k1))

        return self

class GetEntityStoreDataResponseBodyResponseStatusStatusItem(DaraModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        suggestion: str = None,
    ):
        # Status code
        self.code = code
        # Status level
        self.level = level
        # Calculation execution information
        self.message = message
        # Suggestions when an error occurs during execution
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.level is not None:
            result['level'] = self.level

        if self.message is not None:
            result['message'] = self.message

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self

