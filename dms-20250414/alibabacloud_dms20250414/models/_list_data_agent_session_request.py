# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentSessionRequest(DaraModel):
    def __init__(
        self,
        create_end_time: int = None,
        create_start_time: int = None,
        custom_agent_id: str = None,
        dmsunit: str = None,
        is_saved: bool = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.create_end_time = create_end_time
        self.create_start_time = create_start_time
        self.custom_agent_id = custom_agent_id
        self.dmsunit = dmsunit
        self.is_saved = is_saved
        self.page_number = page_number
        self.page_size = page_size
        self.query_type = query_type
        self.title = title
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_end_time is not None:
            result['CreateEndTime'] = self.create_end_time

        if self.create_start_time is not None:
            result['CreateStartTime'] = self.create_start_time

        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.is_saved is not None:
            result['IsSaved'] = self.is_saved

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateEndTime') is not None:
            self.create_end_time = m.get('CreateEndTime')

        if m.get('CreateStartTime') is not None:
            self.create_start_time = m.get('CreateStartTime')

        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('IsSaved') is not None:
            self.is_saved = m.get('IsSaved')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

