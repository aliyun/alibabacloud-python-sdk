# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSecurityIdentifyResultsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListSecurityIdentifyResultsRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.list_query = list_query
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
            temp_model = main_models.ListSecurityIdentifyResultsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListSecurityIdentifyResultsRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_unit_name_list: List[str] = None,
        classify_id: int = None,
        datasource_name_list: List[str] = None,
        env: str = None,
        is_locked: bool = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        project_name_list: List[str] = None,
        status: str = None,
    ):
        self.biz_unit_name_list = biz_unit_name_list
        self.classify_id = classify_id
        self.datasource_name_list = datasource_name_list
        self.env = env
        self.is_locked = is_locked
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.project_name_list = project_name_list
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_name_list is not None:
            result['BizUnitNameList'] = self.biz_unit_name_list

        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.datasource_name_list is not None:
            result['DatasourceNameList'] = self.datasource_name_list

        if self.env is not None:
            result['Env'] = self.env

        if self.is_locked is not None:
            result['IsLocked'] = self.is_locked

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name_list is not None:
            result['ProjectNameList'] = self.project_name_list

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitNameList') is not None:
            self.biz_unit_name_list = m.get('BizUnitNameList')

        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('DatasourceNameList') is not None:
            self.datasource_name_list = m.get('DatasourceNameList')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('IsLocked') is not None:
            self.is_locked = m.get('IsLocked')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectNameList') is not None:
            self.project_name_list = m.get('ProjectNameList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

