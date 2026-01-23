# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityRuleTasksRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityRuleTasksRequestListQuery = None,
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
            temp_model = main_models.ListQualityRuleTasksRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListQualityRuleTasksRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        catalog_list: List[str] = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        rule_strength_list: List[str] = None,
        rule_tag_list: List[str] = None,
        status_list: List[str] = None,
        validate_result_list: List[str] = None,
        watch_task_id: int = None,
    ):
        self.biz_date = biz_date
        self.catalog_list = catalog_list
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.rule_strength_list = rule_strength_list
        self.rule_tag_list = rule_tag_list
        self.status_list = status_list
        self.validate_result_list = validate_result_list
        self.watch_task_id = watch_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.catalog_list is not None:
            result['CatalogList'] = self.catalog_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_strength_list is not None:
            result['RuleStrengthList'] = self.rule_strength_list

        if self.rule_tag_list is not None:
            result['RuleTagList'] = self.rule_tag_list

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.validate_result_list is not None:
            result['ValidateResultList'] = self.validate_result_list

        if self.watch_task_id is not None:
            result['WatchTaskId'] = self.watch_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('CatalogList') is not None:
            self.catalog_list = m.get('CatalogList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleStrengthList') is not None:
            self.rule_strength_list = m.get('RuleStrengthList')

        if m.get('RuleTagList') is not None:
            self.rule_tag_list = m.get('RuleTagList')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('ValidateResultList') is not None:
            self.validate_result_list = m.get('ValidateResultList')

        if m.get('WatchTaskId') is not None:
            self.watch_task_id = m.get('WatchTaskId')

        return self

