# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateFileProtectClientRuleRequest(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        client_token: str = None,
        exclude_users: List[str] = None,
        file_ops: List[str] = None,
        file_paths: List[str] = None,
        file_types: List[str] = None,
        platform: str = None,
        proc_paths: List[str] = None,
        rule_action: str = None,
        rule_name: str = None,
        status: int = None,
        switch_id: str = None,
    ):
        # The alert notification level. Valid values:
        # 
        # - 0: no alert
        # - 1: reminder
        # - 2: suspicious
        # - 3: high-risk.
        self.alert_level = alert_level
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The list of excluded users.
        self.exclude_users = exclude_users
        # The list of operations performed on files.
        # 
        # This parameter is required.
        self.file_ops = file_ops
        # The list of monitored file paths. Wildcards are supported.
        # 
        # This parameter is required.
        self.file_paths = file_paths
        # The list of monitored file types.
        self.file_types = file_types
        # The operating system type. Valid values:
        # 
        # - **windows**: Windows.
        # - **linux**: Linux.
        self.platform = platform
        # The list of process monitoring paths. Wildcards are supported.
        # 
        # This parameter is required.
        self.proc_paths = proc_paths
        # The action to take when the policy is hit. Valid values:
        # 
        # - **monitor**: Alert.
        # - **block**: Block.
        # - **pass**: Allow.
        # 
        # This parameter is required.
        self.rule_action = rule_action
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        # 
        # This parameter is required.
        self.status = status
        # The switch ID associated with the rule.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.exclude_users is not None:
            result['ExcludeUsers'] = self.exclude_users

        if self.file_ops is not None:
            result['FileOps'] = self.file_ops

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        if self.file_types is not None:
            result['FileTypes'] = self.file_types

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExcludeUsers') is not None:
            self.exclude_users = m.get('ExcludeUsers')

        if m.get('FileOps') is not None:
            self.file_ops = m.get('FileOps')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        if m.get('FileTypes') is not None:
            self.file_types = m.get('FileTypes')

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

