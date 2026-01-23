# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateQualityRuleSwitchRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateQualityRuleSwitchRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateQualityRuleSwitchRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateQualityRuleSwitchRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        open: bool = None,
        rule_id_list: List[int] = None,
    ):
        # This parameter is required.
        self.open = open
        # This parameter is required.
        self.rule_id_list = rule_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open is not None:
            result['Open'] = self.open

        if self.rule_id_list is not None:
            result['RuleIdList'] = self.rule_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('RuleIdList') is not None:
            self.rule_id_list = m.get('RuleIdList')

        return self

