# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuerySourceUsageSummaryRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        end_time: str = None,
        event_type: str = None,
        knowledge_base_ids: List[str] = None,
        scope_type: str = None,
        source_ids: List[str] = None,
        source_name: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        # The ID of the collaboration group to which the resource belongs, such as cg_101. If you specify this parameter, a group workspace task is created, and the caller must be a valid group member. If you leave this parameter empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The actual end timestamp of the live stream, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event type.
        self.event_type = event_type
        # The ID of the knowledge base folder.
        self.knowledge_base_ids = knowledge_base_ids
        # The role scope type. Valid values:
        # - **ALL_VISIBLE**: All members.
        # - **PART_VISIBLE**: Partial members.
        # 
        # This parameter is required.
        self.scope_type = scope_type
        # The source ID.
        self.source_ids = source_ids
        # The resume channel source.
        self.source_name = source_name
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The tenant ID, which is a common parameter. If you use winnexo-cli, pass this parameter explicitly by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.knowledge_base_ids is not None:
            result['knowledgeBaseIds'] = self.knowledge_base_ids

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.source_ids is not None:
            result['sourceIds'] = self.source_ids

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('knowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('knowledgeBaseIds')

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('sourceIds') is not None:
            self.source_ids = m.get('sourceIds')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

