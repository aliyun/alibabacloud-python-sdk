# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityRulesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListQualityRulesRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The paged query conditions, including paging parameters.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator ID.
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
            temp_model = main_models.ListQualityRulesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListQualityRulesRequestListQuery(DaraModel):
    def __init__(
        self,
        catalog_list: List[str] = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        rule_strength_list: List[str] = None,
        status_list: List[str] = None,
        template_id_list: List[int] = None,
        test_run_task_status_list: List[str] = None,
        test_run_task_validate_result_list: List[str] = None,
        watch_id: int = None,
    ):
        # The rule type. Valid values: CONSISTENT (Consistency), EFFECTIVE (Effectiveness), TIMELINESE (Timeliness), ACCURATE (Accuracy), UNIQUENESS (Uniqueness), COMPLETENESS (Completeness), STABILITY (Stability), and CUSTOM (Custom).
        self.catalog_list = catalog_list
        # The search keyword. Supports searching by rule name and validation object.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The rule strength. Valid values: STRONG (Strong) and WEAK (Weak).
        self.rule_strength_list = rule_strength_list
        # The effective status of the rule. Valid values: ENABLE (Enabled) and DISABLE (Disabled).
        self.status_list = status_list
        # The rule template.
        self.template_id_list = template_id_list
        # The task status. Valid values: NOT_RUN (Not run), WAITING (Waiting), RUNNING (Running), SUCCESS (Succeeded), FAILED (Failed), CANCEL (Canceled), TIMEOUT (Timed out), and OFFLINE (Offline).
        self.test_run_task_status_list = test_run_task_status_list
        # The validation result of the rule test run. Valid values: NOT_RUN (Not run), WAITING (Waiting), RUNNING (Running), PASS (Passed), NOT_PASS (Not passed), FAILED (Failed), OFFLINE (Offline, requires restart), CANCEL (Canceled), and TIMEOUT (Timed out).
        self.test_run_task_validate_result_list = test_run_task_validate_result_list
        # The monitoring ID.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.template_id_list is not None:
            result['TemplateIdList'] = self.template_id_list

        if self.test_run_task_status_list is not None:
            result['TestRunTaskStatusList'] = self.test_run_task_status_list

        if self.test_run_task_validate_result_list is not None:
            result['TestRunTaskValidateResultList'] = self.test_run_task_validate_result_list

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TemplateIdList') is not None:
            self.template_id_list = m.get('TemplateIdList')

        if m.get('TestRunTaskStatusList') is not None:
            self.test_run_task_status_list = m.get('TestRunTaskStatusList')

        if m.get('TestRunTaskValidateResultList') is not None:
            self.test_run_task_validate_result_list = m.get('TestRunTaskValidateResultList')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

