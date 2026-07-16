# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListTenantMembersRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListTenantMembersRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # The request object.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListTenantMembersRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListTenantMembersRequestListQuery(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        role_list: List[str] = None,
        search_text: str = None,
        user_group_id_list: List[str] = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The member roles:
        # - SUPER_ADMIN: Dataphin super administrator
        # - SYSTEM_ADMIN: system administrator
        # - COMMON_USER: Dataphin user
        # - DATA_ADMIN: Dataphin data administrator
        # - EXPORT_ADMIN: export administrator
        # - SECURITY_ADMIN: security administrator
        # - DATASOURCE_MANAGER: data source administrator
        # - QUALITY_MANAGER: asset quality manager
        # - DATA_STANDARD_MANAGER: data standard administrator
        # - LABELS_BUSINESS_PLANNER: tag business planner
        # - BUSINESS_MEMBER: general business user
        # - DATAPRO_OPERATE_SUPER_ADMIN: operations super administrator
        # - DATAPRO_OPERATE_ADMIN: operations administrator
        # - DATAPRO_OPERATE_MEMBER: operations member
        # - DATAPRO_BUSINESS_ANALYST: business analyst
        # - LABELS_BUSINESS_MEMBER: tag business member
        # - DATAPRO_BUSINESS_MEMBER: DATAPRO general business user
        self.role_list = role_list
        # The search keyword.
        self.search_text = search_text
        # The IDs of the user groups to which the member belongs.
        self.user_group_id_list = user_group_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_list is not None:
            result['RoleList'] = self.role_list

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        if self.user_group_id_list is not None:
            result['UserGroupIdList'] = self.user_group_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        if m.get('UserGroupIdList') is not None:
            self.user_group_id_list = m.get('UserGroupIdList')

        return self

