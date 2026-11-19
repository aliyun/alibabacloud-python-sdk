# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListMemoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListMemoriesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of memories.
        self.items = items
        # The maximum number of records per page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of records.
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
                temp_model = main_models.ListMemoriesResponseBodyItems()
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

class ListMemoriesResponseBodyItems(DaraModel):
    def __init__(
        self,
        content: main_models.ListMemoriesResponseBodyItemsContent = None,
        created_at: str = None,
        memory_id: str = None,
        metadata: Dict[str, str] = None,
        scope: main_models.ListMemoriesResponseBodyItemsScope = None,
        source: str = None,
        type: str = None,
        updated_at: str = None,
        valid: bool = None,
    ):
        # The memory content.
        self.content = content
        # The creation time. The time is in RFC 3339 format. The Z at the end of the example indicates the UTC time zone.
        self.created_at = created_at
        # The long-term memory ID.
        self.memory_id = memory_id
        # The memory metadata.
        self.metadata = metadata
        # The memory scope.
        self.scope = scope
        # The source of the memory. Valid values:
        # - session_extraction: Extracted from session events.
        # - content_extraction: Extracted from text or messages.
        # - direct: Written directly.
        self.source = source
        # The memory content type. Valid values:
        # - semantic: Semantic memory.
        # - skill: Skill.
        # - user_profile: User preference.
        # - session_summary: Session summary.
        self.type = type
        # The last update time. The time is in RFC 3339 format. The Z at the end of the example indicates the UTC time zone.
        self.updated_at = updated_at
        # Indicates whether the memory is valid. A value of false indicates that the memory is revoked and is not included in valid memory retrieval.
        self.valid = valid

    def validate(self):
        if self.content:
            self.content.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.valid is not None:
            result['valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = main_models.ListMemoriesResponseBodyItemsContent()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('scope') is not None:
            temp_model = main_models.ListMemoriesResponseBodyItemsScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('valid') is not None:
            self.valid = m.get('valid')

        return self

class ListMemoriesResponseBodyItemsScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with an agent ID.
        self.agent_id = agent_id
        # The session ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with a session ID.
        self.session_id = session_id
        # The business team ID defined by the caller. This field cannot be empty when provided and can be up to 128 UTF-8 bytes in length.
        self.team_id = team_id
        # The user ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with a user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ListMemoriesResponseBodyItemsContent(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        # The memory text.
        # 
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

