# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileProtectClientRuleStatusRequest(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        exclude_id_list: List[int] = None,
        id_list: List[int] = None,
        platform: str = None,
        rule_action: str = None,
        rule_name: str = None,
        select_all: bool = None,
        status: int = None,
    ):
        self.alert_level = alert_level
        self.exclude_id_list = exclude_id_list
        self.id_list = id_list
        self.platform = platform
        self.rule_action = rule_action
        self.rule_name = rule_name
        # This parameter is required.
        self.select_all = select_all
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.exclude_id_list is not None:
            result['ExcludeIdList'] = self.exclude_id_list

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.select_all is not None:
            result['SelectAll'] = self.select_all

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('ExcludeIdList') is not None:
            self.exclude_id_list = m.get('ExcludeIdList')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SelectAll') is not None:
            self.select_all = m.get('SelectAll')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

