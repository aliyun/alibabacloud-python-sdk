# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListStandardsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListStandardsRequestListQuery = None,
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
            temp_model = main_models.ListStandardsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListStandardsRequestListQuery(DaraModel):
    def __init__(
        self,
        directory: str = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        standard_set_id_list: List[int] = None,
        standard_stage: str = None,
        standard_status_list: List[str] = None,
        standard_template_id_list: List[int] = None,
        standard_type_list: List[str] = None,
        user_id: str = None,
    ):
        self.directory = directory
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.standard_set_id_list = standard_set_id_list
        # This parameter is required.
        self.standard_stage = standard_stage
        self.standard_status_list = standard_status_list
        self.standard_template_id_list = standard_template_id_list
        self.standard_type_list = standard_type_list
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.standard_set_id_list is not None:
            result['StandardSetIdList'] = self.standard_set_id_list

        if self.standard_stage is not None:
            result['StandardStage'] = self.standard_stage

        if self.standard_status_list is not None:
            result['StandardStatusList'] = self.standard_status_list

        if self.standard_template_id_list is not None:
            result['StandardTemplateIdList'] = self.standard_template_id_list

        if self.standard_type_list is not None:
            result['StandardTypeList'] = self.standard_type_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StandardSetIdList') is not None:
            self.standard_set_id_list = m.get('StandardSetIdList')

        if m.get('StandardStage') is not None:
            self.standard_stage = m.get('StandardStage')

        if m.get('StandardStatusList') is not None:
            self.standard_status_list = m.get('StandardStatusList')

        if m.get('StandardTemplateIdList') is not None:
            self.standard_template_id_list = m.get('StandardTemplateIdList')

        if m.get('StandardTypeList') is not None:
            self.standard_type_list = m.get('StandardTypeList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

