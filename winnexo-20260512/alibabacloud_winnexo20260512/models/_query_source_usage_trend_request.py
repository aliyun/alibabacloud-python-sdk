# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuerySourceUsageTrendRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        end_time: str = None,
        event_type: str = None,
        granularity: str = None,
        knowledge_base_ids: List[str] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        scope_type: str = None,
        source_ids: List[str] = None,
        source_name: str = None,
        start_time: str = None,
        tenant_id: str = None,
        time_zone: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the associated collaboration group, such as cg_101. If you specify this parameter, a group workspace task is created, and the caller must be a valid group member. If you leave this parameter empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The actual end timestamp of the live stream, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event type.
        self.event_type = event_type
        # The trend aggregation granularity. Valid values: DAY (daily), WEEK (weekly), and MONTH (monthly).
        self.granularity = granularity
        # The IDs of the knowledge base folders.
        self.knowledge_base_ids = knowledge_base_ids
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The role scope type. Valid values:
        # - **ALL_VISIBLE**: All members.
        # - **PART_VISIBLE**: Partial members.
        # 
        # This parameter is required.
        self.scope_type = scope_type
        # The IDs of the resource sources.
        self.source_ids = source_ids
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.knowledge_base_ids is not None:
            result['knowledgeBaseIds'] = self.knowledge_base_ids

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('knowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('knowledgeBaseIds')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

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

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

