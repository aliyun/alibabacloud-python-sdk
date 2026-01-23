# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitQualityRuleTasksRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        submit_command: main_models.SubmitQualityRuleTasksRequestSubmitCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.submit_command = submit_command

    def validate(self):
        if self.submit_command:
            self.submit_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.submit_command is not None:
            result['SubmitCommand'] = self.submit_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SubmitCommand') is not None:
            temp_model = main_models.SubmitQualityRuleTasksRequestSubmitCommand()
            self.submit_command = temp_model.from_map(m.get('SubmitCommand'))

        return self

class SubmitQualityRuleTasksRequestSubmitCommand(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        is_test_run: bool = None,
        partition_expression: str = None,
        partition_expression_from: str = None,
        schedule_id: int = None,
        watch_rule_id_list: List[main_models.SubmitQualityRuleTasksRequestSubmitCommandWatchRuleIdList] = None,
    ):
        self.biz_date = biz_date
        # This parameter is required.
        self.is_test_run = is_test_run
        self.partition_expression = partition_expression
        self.partition_expression_from = partition_expression_from
        self.schedule_id = schedule_id
        # This parameter is required.
        self.watch_rule_id_list = watch_rule_id_list

    def validate(self):
        if self.watch_rule_id_list:
            for v1 in self.watch_rule_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.is_test_run is not None:
            result['IsTestRun'] = self.is_test_run

        if self.partition_expression is not None:
            result['PartitionExpression'] = self.partition_expression

        if self.partition_expression_from is not None:
            result['PartitionExpressionFrom'] = self.partition_expression_from

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        result['WatchRuleIdList'] = []
        if self.watch_rule_id_list is not None:
            for k1 in self.watch_rule_id_list:
                result['WatchRuleIdList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('IsTestRun') is not None:
            self.is_test_run = m.get('IsTestRun')

        if m.get('PartitionExpression') is not None:
            self.partition_expression = m.get('PartitionExpression')

        if m.get('PartitionExpressionFrom') is not None:
            self.partition_expression_from = m.get('PartitionExpressionFrom')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        self.watch_rule_id_list = []
        if m.get('WatchRuleIdList') is not None:
            for k1 in m.get('WatchRuleIdList'):
                temp_model = main_models.SubmitQualityRuleTasksRequestSubmitCommandWatchRuleIdList()
                self.watch_rule_id_list.append(temp_model.from_map(k1))

        return self

class SubmitQualityRuleTasksRequestSubmitCommandWatchRuleIdList(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        watch_id: int = None,
    ):
        # This parameter is required.
        self.rule_id = rule_id
        # This parameter is required.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

