# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateFileProtectRuleRequest(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        file_ops: List[str] = None,
        file_paths: List[str] = None,
        platform: str = None,
        proc_paths: List[str] = None,
        rule_action: str = None,
        rule_name: str = None,
        status: int = None,
        switch_id: str = None,
    ):
        # The severity of alerts. Valid values:
        # 
        # *   0: does not generate alerts
        # *   1: sends notifications
        # *   2: suspicious
        # *   3: high-risk
        self.alert_level = alert_level
        # The operations that you want to perform on the files.
        # 
        # This parameter is required.
        self.file_ops = file_ops
        # The paths to the files that you want to monitor. Wildcard characters are supported.
        # 
        # This parameter is required.
        self.file_paths = file_paths
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        self.platform = platform
        # The paths to the processes that you want to monitor. Wildcard characters are supported.
        # 
        # This parameter is required.
        self.proc_paths = proc_paths
        # The handling method of the rule. Valid values:
        # 
        # *   pass: allow
        # *   alert
        # 
        # This parameter is required.
        self.rule_action = rule_action
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether to enable the rule. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.status = status
        # The switch ID of the rule.
        self.switch_id = switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.file_ops is not None:
            result['FileOps'] = self.file_ops

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.proc_paths is not None:
            result['ProcPaths'] = self.proc_paths

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('FileOps') is not None:
            self.file_ops = m.get('FileOps')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProcPaths') is not None:
            self.proc_paths = m.get('ProcPaths')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self

