# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListSandboxesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListSandboxesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.items = items
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListSandboxesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListSandboxesResponseBodyItems(DaraModel):
    def __init__(
        self,
        active_session_count: int = None,
        created_at: str = None,
        last_active_at: str = None,
        last_heartbeat_at: str = None,
        max_concurrent_sessions: int = None,
        phase: str = None,
        sandbox_id: str = None,
    ):
        self.active_session_count = active_session_count
        self.created_at = created_at
        self.last_active_at = last_active_at
        self.last_heartbeat_at = last_heartbeat_at
        self.max_concurrent_sessions = max_concurrent_sessions
        self.phase = phase
        self.sandbox_id = sandbox_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_count is not None:
            result['activeSessionCount'] = self.active_session_count

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.last_active_at is not None:
            result['lastActiveAt'] = self.last_active_at

        if self.last_heartbeat_at is not None:
            result['lastHeartbeatAt'] = self.last_heartbeat_at

        if self.max_concurrent_sessions is not None:
            result['maxConcurrentSessions'] = self.max_concurrent_sessions

        if self.phase is not None:
            result['phase'] = self.phase

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeSessionCount') is not None:
            self.active_session_count = m.get('activeSessionCount')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastActiveAt') is not None:
            self.last_active_at = m.get('lastActiveAt')

        if m.get('lastHeartbeatAt') is not None:
            self.last_heartbeat_at = m.get('lastHeartbeatAt')

        if m.get('maxConcurrentSessions') is not None:
            self.max_concurrent_sessions = m.get('maxConcurrentSessions')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        return self

