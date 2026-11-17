# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySourceUsageTrendShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        end_time: str = None,
        event_type: str = None,
        granularity: str = None,
        knowledge_base_ids_shrink: str = None,
        scope_type: str = None,
        source_ids_shrink: str = None,
        source_name: str = None,
        start_time: str = None,
        tenant_id: str = None,
        time_zone: str = None,
    ):
        # The ID of the collaboration group to which the resource belongs, such as cg_101. If this parameter is specified, a group workspace task is created, and the caller must be a valid group member. If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The actual end timestamp of the live stream, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event type.
        self.event_type = event_type
        # The aggregation granularity. Valid values: hourly and daily.
        self.granularity = granularity
        # The IDs of the knowledge base folders.
        self.knowledge_base_ids_shrink = knowledge_base_ids_shrink
        # The role scope type. Valid values:
        # - **ALL_VISIBLE**: All members.
        # - **PART_VISIBLE**: Partial members.
        # 
        # This parameter is required.
        self.scope_type = scope_type
        # The IDs of the resource sources.
        self.source_ids_shrink = source_ids_shrink
        # The resume channel source.
        self.source_name = source_name
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # The time zone.
        self.time_zone = time_zone

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

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.knowledge_base_ids_shrink is not None:
            result['knowledgeBaseIds'] = self.knowledge_base_ids_shrink

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.source_ids_shrink is not None:
            result['sourceIds'] = self.source_ids_shrink

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('knowledgeBaseIds') is not None:
            self.knowledge_base_ids_shrink = m.get('knowledgeBaseIds')

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('sourceIds') is not None:
            self.source_ids_shrink = m.get('sourceIds')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

