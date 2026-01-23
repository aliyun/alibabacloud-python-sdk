# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityTemplatesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityTemplatesRequestListQuery = None,
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
            temp_model = main_models.ListQualityTemplatesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListQualityTemplatesRequestListQuery(DaraModel):
    def __init__(
        self,
        catalog_list: List[str] = None,
        current_user_owned: bool = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        support_data_source_type_list: List[str] = None,
        template_owner_list: List[str] = None,
        template_source_list: List[str] = None,
        template_type_list: List[str] = None,
        watch_type_list: List[str] = None,
    ):
        self.catalog_list = catalog_list
        self.current_user_owned = current_user_owned
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.support_data_source_type_list = support_data_source_type_list
        self.template_owner_list = template_owner_list
        self.template_source_list = template_source_list
        self.template_type_list = template_type_list
        self.watch_type_list = watch_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_list is not None:
            result['CatalogList'] = self.catalog_list

        if self.current_user_owned is not None:
            result['CurrentUserOwned'] = self.current_user_owned

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.support_data_source_type_list is not None:
            result['SupportDataSourceTypeList'] = self.support_data_source_type_list

        if self.template_owner_list is not None:
            result['TemplateOwnerList'] = self.template_owner_list

        if self.template_source_list is not None:
            result['TemplateSourceList'] = self.template_source_list

        if self.template_type_list is not None:
            result['TemplateTypeList'] = self.template_type_list

        if self.watch_type_list is not None:
            result['WatchTypeList'] = self.watch_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogList') is not None:
            self.catalog_list = m.get('CatalogList')

        if m.get('CurrentUserOwned') is not None:
            self.current_user_owned = m.get('CurrentUserOwned')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SupportDataSourceTypeList') is not None:
            self.support_data_source_type_list = m.get('SupportDataSourceTypeList')

        if m.get('TemplateOwnerList') is not None:
            self.template_owner_list = m.get('TemplateOwnerList')

        if m.get('TemplateSourceList') is not None:
            self.template_source_list = m.get('TemplateSourceList')

        if m.get('TemplateTypeList') is not None:
            self.template_type_list = m.get('TemplateTypeList')

        if m.get('WatchTypeList') is not None:
            self.watch_type_list = m.get('WatchTypeList')

        return self

