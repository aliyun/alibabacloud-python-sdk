# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetAgentWorkLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        logs: List[main_models.GetAgentWorkLogResponseBodyLogs] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The agent operation records in reverse chronological order. If no records are saved, an empty list is returned.
        self.logs = logs
        # The error message.
        self.message = message
        # The current page number, starting from 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of filtered operation log entries.
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['logs'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.logs = []
        if m.get('logs') is not None:
            for k1 in m.get('logs'):
                temp_model = main_models.GetAgentWorkLogResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetAgentWorkLogResponseBodyLogs(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, and ARTIFACT.
        self.action = action
        # The saved raw record content. Tool invocations and artifact metadata are represented as JSON strings.
        self.detail = detail
        # The duration of this operation record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the node to which the record belongs. This is not the session ID.
        self.node_id = node_id
        # The time when the event was recorded, in ISO 8601 format. If the source record has no time, an empty string is returned.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

