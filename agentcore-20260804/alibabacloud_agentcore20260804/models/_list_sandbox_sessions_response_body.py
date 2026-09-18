# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListSandboxSessionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListSandboxSessionsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code. The value SUCCESS is returned if the request was successful.
        self.code = code
        # The HTTP status code. The value 200 is returned if the request was successful.
        self.http_status_code = http_status_code
        # The list of active sessions in the sandbox.
        self.items = items
        # The maximum number of records per page for this query.
        self.max_results = max_results
        # The response message. The value success is returned if the request was successful.
        self.message = message
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The total number of records that match the query conditions.
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
                temp_model = main_models.ListSandboxSessionsResponseBodyItems()
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

class ListSandboxSessionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        session_id: str = None,
        source_type: str = None,
    ):
        # The external channel type, such as DINGTALK, FEISHU, or WECOM. This parameter is empty for non-external channels.
        self.channel_type = channel_type
        # The unique identifier of the active session.
        self.session_id = session_id
        # The session source type. Valid values:
        # - API: API call.
        # - CONSOLE_DEBUG: Console debugging.
        # - EXTERNAL_CHANNEL: External channel.
        # - UNKNOWN: Unknown source.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

