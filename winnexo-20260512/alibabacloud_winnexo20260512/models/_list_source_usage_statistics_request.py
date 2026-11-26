# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSourceUsageStatisticsRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        end_time: str = None,
        event_type: str = None,
        knowledge_base_ids: List[str] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        scope_type: str = None,
        sort_by: str = None,
        sort_order: str = None,
        source_ids: List[str] = None,
        source_name: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The ID of the collaboration group to which the resource belongs, such as cg_101. If specified, a group workspace task is created, and the caller must be a valid group member. If left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The actual end timestamp, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event type.
        self.event_type = event_type
        # The root IDs of enterprise knowledge bases, available only for TENANT. The IDs are filtered based on current directory bindings rather than historical ownership. A maximum of 100 items are supported.
        self.knowledge_base_ids = knowledge_base_ids
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The current page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The report perspective. Valid values: TENANT for enterprise knowledge, GROUP for a single workspace, and ALL_GROUPS for all workspaces of the current tenant (available only to platform super administrators).
        # 
        # This parameter is required.
        self.scope_type = scope_type
        # The content of the sort clause.
        self.sort_by = sort_by
        # Specifies the sort order. This parameter takes effect only when sortBy is specified. Valid values: ASC and DESC. The values are case-insensitive.
        self.sort_order = sort_order
        # The associated source IDs.
        self.source_ids = source_ids
        # The name of the source.
        self.source_name = source_name
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The effective tenant ID.
        self.tenant_id = tenant_id

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

        if self.knowledge_base_ids is not None:
            result['knowledgeBaseIds'] = self.knowledge_base_ids

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('knowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('knowledgeBaseIds')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('sourceIds') is not None:
            self.source_ids = m.get('sourceIds')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

