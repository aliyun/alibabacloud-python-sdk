# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class RemoveQualityRuleSchedulesRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command: main_models.RemoveQualityRuleSchedulesRequestRemoveCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command = remove_command

    def validate(self):
        if self.remove_command:
            self.remove_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.remove_command is not None:
            result['RemoveCommand'] = self.remove_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RemoveCommand') is not None:
            temp_model = main_models.RemoveQualityRuleSchedulesRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m.get('RemoveCommand'))

        return self

class RemoveQualityRuleSchedulesRequestRemoveCommand(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        schedule_id_list: List[int] = None,
        watch_id: int = None,
    ):
        # This parameter is required.
        self.rule_id = rule_id
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.schedule_id_list is not None:
            result['ScheduleIdList'] = self.schedule_id_list

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('ScheduleIdList') is not None:
            self.schedule_id_list = m.get('ScheduleIdList')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

