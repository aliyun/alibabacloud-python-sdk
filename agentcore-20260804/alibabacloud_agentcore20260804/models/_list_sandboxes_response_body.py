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
        # The business status code. The value is SUCCESS if the request is successful.
        self.code = code
        # The HTTP status code. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The list of sandboxes that meet the filter conditions.
        self.items = items
        # The maximum number of records per page for this query.
        self.max_results = max_results
        # The response message. The value is success if the request is successful.
        self.message = message
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates success, and a value of false indicates failure.
        self.success = success
        # The total number of records that meet the query conditions.
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
        harness_version: str = None,
        last_active_at: str = None,
        last_heartbeat_at: str = None,
        last_rebuild_operation_id: str = None,
        max_concurrent_sessions: int = None,
        phase: str = None,
        sandbox_id: str = None,
        update_available: bool = None,
        update_failed: bool = None,
    ):
        # The number of active sessions in the sandbox.
        self.active_session_count = active_session_count
        # The time when the sandbox was created. The time is in RFC 3339 UTC format.
        self.created_at = created_at
        # The tag of the actual observed image of the currently returned instance. This parameter is empty if the tag cannot be parsed.
        self.harness_version = harness_version
        # The time of the last activity of the sandbox. The time is in RFC 3339 UTC format.
        self.last_active_at = last_active_at
        # The time of the last heartbeat of the sandbox. The time is in RFC 3339 UTC format.
        self.last_heartbeat_at = last_heartbeat_at
        # Used to continue calling GetSandboxRebuildOperation to query the overall result after the page is refreshed. This parameter is empty if there is no historical rebuild. Do not use the ID of a subsequently created task instead.
        self.last_rebuild_operation_id = last_rebuild_operation_id
        # The maximum number of concurrent sessions allowed for the sandbox, which is obtained from the effective auto-scaling configuration at runtime. This parameter is empty if auto-scaling is disabled or the configuration is unavailable.
        self.max_concurrent_sessions = max_concurrent_sessions
        # The current running phase of the sandbox.
        self.phase = phase
        # The sandbox ID. You can query it by calling ListSandboxes.
        self.sandbox_id = sandbox_id
        # The server compares the actual image tag of the instance with the target image tag of the pool. The value is true if the tags are different during the RUNNING, HIBERNATED, or FAILED phase. The value is false if the tags are the same or during other known phases. This parameter is empty if the tag or phase cannot be confirmed, and it cannot be treated as false. The version sequence is not determined by the tag size.
        self.update_available = update_available
        # A value of true indicates that the most recent rebuild corresponding to the current instance generation failed as a whole. A value of false indicates that there is no historical rebuild or the rebuild succeeded as a whole. This parameter is empty if the rebuild is in progress, canceled, replaced, the generation does not match, or the result cannot be confirmed.
        self.update_failed = update_failed

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

        if self.harness_version is not None:
            result['harnessVersion'] = self.harness_version

        if self.last_active_at is not None:
            result['lastActiveAt'] = self.last_active_at

        if self.last_heartbeat_at is not None:
            result['lastHeartbeatAt'] = self.last_heartbeat_at

        if self.last_rebuild_operation_id is not None:
            result['lastRebuildOperationId'] = self.last_rebuild_operation_id

        if self.max_concurrent_sessions is not None:
            result['maxConcurrentSessions'] = self.max_concurrent_sessions

        if self.phase is not None:
            result['phase'] = self.phase

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        if self.update_available is not None:
            result['updateAvailable'] = self.update_available

        if self.update_failed is not None:
            result['updateFailed'] = self.update_failed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeSessionCount') is not None:
            self.active_session_count = m.get('activeSessionCount')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('harnessVersion') is not None:
            self.harness_version = m.get('harnessVersion')

        if m.get('lastActiveAt') is not None:
            self.last_active_at = m.get('lastActiveAt')

        if m.get('lastHeartbeatAt') is not None:
            self.last_heartbeat_at = m.get('lastHeartbeatAt')

        if m.get('lastRebuildOperationId') is not None:
            self.last_rebuild_operation_id = m.get('lastRebuildOperationId')

        if m.get('maxConcurrentSessions') is not None:
            self.max_concurrent_sessions = m.get('maxConcurrentSessions')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        if m.get('updateAvailable') is not None:
            self.update_available = m.get('updateAvailable')

        if m.get('updateFailed') is not None:
            self.update_failed = m.get('updateFailed')

        return self

