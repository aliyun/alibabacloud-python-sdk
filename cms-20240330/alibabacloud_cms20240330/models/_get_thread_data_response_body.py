# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetThreadDataResponseBody(DaraModel):
    def __init__(
        self,
        digital_employee_name: str = None,
        max_results: int = None,
        messages: List[main_models.GetThreadDataResponseBodyMessages] = None,
        next_token: str = None,
        request_id: str = None,
        thread_id: str = None,
    ):
        self.digital_employee_name = digital_employee_name
        self.max_results = max_results
        self.messages = messages
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.thread_id = thread_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.GetThreadDataResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

class GetThreadDataResponseBodyMessages(DaraModel):
    def __init__(
        self,
        caller_uid: str = None,
        digital_employee_name: str = None,
        items: List[Dict[str, Any]] = None,
        message_id: str = None,
        owner_uid: str = None,
        parent_message_id: str = None,
        region: str = None,
        role: str = None,
        run_id: str = None,
        thread_id: str = None,
        timestamp: str = None,
        trace_id: str = None,
        variables: Dict[str, str] = None,
    ):
        self.caller_uid = caller_uid
        self.digital_employee_name = digital_employee_name
        self.items = items
        self.message_id = message_id
        self.owner_uid = owner_uid
        self.parent_message_id = parent_message_id
        self.region = region
        self.role = role
        self.run_id = run_id
        self.thread_id = thread_id
        self.timestamp = timestamp
        self.trace_id = trace_id
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.items is not None:
            result['items'] = self.items

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.owner_uid is not None:
            result['ownerUid'] = self.owner_uid

        if self.parent_message_id is not None:
            result['parentMessageId'] = self.parent_message_id

        if self.region is not None:
            result['region'] = self.region

        if self.role is not None:
            result['role'] = self.role

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        if self.variables is not None:
            result['variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('ownerUid') is not None:
            self.owner_uid = m.get('ownerUid')

        if m.get('parentMessageId') is not None:
            self.parent_message_id = m.get('parentMessageId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        return self

