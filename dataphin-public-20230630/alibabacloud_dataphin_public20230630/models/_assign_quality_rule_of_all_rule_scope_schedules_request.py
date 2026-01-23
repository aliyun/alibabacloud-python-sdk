# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AssignQualityRuleOfAllRuleScopeSchedulesRequest(DaraModel):
    def __init__(
        self,
        assign_command: main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequestAssignCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.assign_command = assign_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.assign_command:
            self.assign_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_command is not None:
            result['AssignCommand'] = self.assign_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignCommand') is not None:
            temp_model = main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequestAssignCommand()
            self.assign_command = temp_model.from_map(m.get('AssignCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AssignQualityRuleOfAllRuleScopeSchedulesRequestAssignCommand(DaraModel):
    def __init__(
        self,
        rule_id_list: List[int] = None,
        schedule_id_list: List[int] = None,
        watch_id: int = None,
    ):
        # This parameter is required.
        self.rule_id_list = rule_id_list
        # This parameter is required.
        self.schedule_id_list = schedule_id_list
        # This parameter is required.
        self.watch_id = watch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id_list is not None:
            result['RuleIdList'] = self.rule_id_list

        if self.schedule_id_list is not None:
            result['ScheduleIdList'] = self.schedule_id_list

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleIdList') is not None:
            self.rule_id_list = m.get('RuleIdList')

        if m.get('ScheduleIdList') is not None:
            self.schedule_id_list = m.get('ScheduleIdList')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

