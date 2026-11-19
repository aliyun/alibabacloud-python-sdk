# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        max_results: int = None,
        next_token: str = None,
        session_id: str = None,
        source: str = None,
        team_id: str = None,
        types: str = None,
        updated_at_from: str = None,
        updated_at_to: str = None,
        user_id: str = None,
        valid: bool = None,
    ):
        # The agent ID. If not specified, all agents are matched. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*).
        self.agent_id = agent_id
        # The maximum number of records per page. Default value: 50. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The session ID. If not specified, all sessions are matched. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*).
        self.session_id = session_id
        # The source of the memory. Valid values:
        # - session_extraction: Extracted from session events.
        # - content_extraction: Extracted from text or messages.
        # - direct: Written directly.
        self.source = source
        # The business team ID defined by the caller.
        self.team_id = team_id
        # The memory content types. Specify the value as a JSON array string, such as ["skill"]. Valid values: semantic, skill, user_profile, and session_summary. If this parameter is omitted or set to [], all types are queried. The value auto is not supported. Keep the filter conditions consistent when you retrieve subsequent pages.
        self.types = types
        # The start time for filtering by update time. The time must be in RFC 3339 format with a time zone.
        self.updated_at_from = updated_at_from
        # The end time for filtering by update time. The time must be in RFC 3339 format with a time zone.
        self.updated_at_to = updated_at_to
        # The user ID. If not specified, all users are matched. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*).
        self.user_id = user_id
        # Specifies whether the memory is valid. Default value: true. If this parameter is omitted, only valid records are returned. If set to false, revoked records are returned.
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.source is not None:
            result['source'] = self.source

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.types is not None:
            result['types'] = self.types

        if self.updated_at_from is not None:
            result['updatedAtFrom'] = self.updated_at_from

        if self.updated_at_to is not None:
            result['updatedAtTo'] = self.updated_at_to

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.valid is not None:
            result['valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('types') is not None:
            self.types = m.get('types')

        if m.get('updatedAtFrom') is not None:
            self.updated_at_from = m.get('updatedAtFrom')

        if m.get('updatedAtTo') is not None:
            self.updated_at_to = m.get('updatedAtTo')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('valid') is not None:
            self.valid = m.get('valid')

        return self

