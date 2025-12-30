# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBizEntitiesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListBizEntitiesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
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
            temp_model = main_models.ListBizEntitiesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListBizEntitiesRequestListQuery(DaraModel):
    def __init__(
        self,
        filter_criteria: main_models.ListBizEntitiesRequestListQueryFilterCriteria = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.filter_criteria = filter_criteria
        self.keyword = keyword
        self.page = page
        self.page_size = page_size

    def validate(self):
        if self.filter_criteria:
            self.filter_criteria.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_criteria is not None:
            result['FilterCriteria'] = self.filter_criteria.to_map()

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterCriteria') is not None:
            temp_model = main_models.ListBizEntitiesRequestListQueryFilterCriteria()
            self.filter_criteria = temp_model.from_map(m.get('FilterCriteria'))

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListBizEntitiesRequestListQueryFilterCriteria(DaraModel):
    def __init__(
        self,
        biz_unit_id_list: List[int] = None,
        biz_unit_name_list: List[str] = None,
        data_domain_id_list: List[int] = None,
        data_domain_name_list: List[str] = None,
        has_table_ref: bool = None,
        owner_user_id_list: List[str] = None,
        status_list: List[str] = None,
        sub_type_list: List[str] = None,
    ):
        self.biz_unit_id_list = biz_unit_id_list
        self.biz_unit_name_list = biz_unit_name_list
        self.data_domain_id_list = data_domain_id_list
        self.data_domain_name_list = data_domain_name_list
        self.has_table_ref = has_table_ref
        self.owner_user_id_list = owner_user_id_list
        self.status_list = status_list
        self.sub_type_list = sub_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id_list is not None:
            result['BizUnitIdList'] = self.biz_unit_id_list

        if self.biz_unit_name_list is not None:
            result['BizUnitNameList'] = self.biz_unit_name_list

        if self.data_domain_id_list is not None:
            result['DataDomainIdList'] = self.data_domain_id_list

        if self.data_domain_name_list is not None:
            result['DataDomainNameList'] = self.data_domain_name_list

        if self.has_table_ref is not None:
            result['HasTableRef'] = self.has_table_ref

        if self.owner_user_id_list is not None:
            result['OwnerUserIdList'] = self.owner_user_id_list

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.sub_type_list is not None:
            result['SubTypeList'] = self.sub_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitIdList') is not None:
            self.biz_unit_id_list = m.get('BizUnitIdList')

        if m.get('BizUnitNameList') is not None:
            self.biz_unit_name_list = m.get('BizUnitNameList')

        if m.get('DataDomainIdList') is not None:
            self.data_domain_id_list = m.get('DataDomainIdList')

        if m.get('DataDomainNameList') is not None:
            self.data_domain_name_list = m.get('DataDomainNameList')

        if m.get('HasTableRef') is not None:
            self.has_table_ref = m.get('HasTableRef')

        if m.get('OwnerUserIdList') is not None:
            self.owner_user_id_list = m.get('OwnerUserIdList')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('SubTypeList') is not None:
            self.sub_type_list = m.get('SubTypeList')

        return self

