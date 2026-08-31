# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListComputeClustersRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListComputeClustersRequestListQuery = None,
        max_results: int = None,
        next_token: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query conditions.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The maximum number of records to return in this response.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListComputeClustersRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListComputeClustersRequestListQuery(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        type_version_list: List[str] = None,
    ):
        # The keyword for filtering.
        self.keyword = keyword
        # The page number. The value must be greater than 0.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of records per page. The value must be greater than 0.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The list of cluster versions.
        self.type_version_list = type_version_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.type_version_list is not None:
            result['TypeVersionList'] = self.type_version_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TypeVersionList') is not None:
            self.type_version_list = m.get('TypeVersionList')

        return self

