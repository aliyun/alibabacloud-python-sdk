# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListGovernObjectsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListGovernObjectsRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The paged query conditions.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListGovernObjectsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListGovernObjectsRequestListQuery(DaraModel):
    def __init__(
        self,
        govern_item_type: str = None,
        keyword: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_names: List[str] = None,
        status_list: List[str] = None,
        view_type: str = None,
    ):
        # The governance item type. Valid values:
        # 
        # - TABLE
        # - DATASOURCE_TABLE
        # - DATASOURCE
        # - INDEX
        # - REALTIME_LOGICAL_TABLE
        # - QD_FEATURE
        # 
        # This parameter is required.
        self.govern_item_type = govern_item_type
        # The search keyword.
        self.keyword = keyword
        # The owner.
        self.owner = owner
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 20.
        self.page_size = page_size
        # The list of project names used to filter results.
        self.project_names = project_names
        # The list of governance object statuses. Valid values:
        # 
        # - NEW
        # - VERIFY
        # - FINISHED
        # - IGNORE
        self.status_list = status_list
        # The view type. Valid values:
        # 
        # - ALL
        # - OWNER
        # - PROJECT
        self.view_type = view_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.govern_item_type is not None:
            result['GovernItemType'] = self.govern_item_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_names is not None:
            result['ProjectNames'] = self.project_names

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.view_type is not None:
            result['ViewType'] = self.view_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernItemType') is not None:
            self.govern_item_type = m.get('GovernItemType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectNames') is not None:
            self.project_names = m.get('ProjectNames')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('ViewType') is not None:
            self.view_type = m.get('ViewType')

        return self

