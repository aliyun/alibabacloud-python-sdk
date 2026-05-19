# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileProtectClientRuleRequest(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        exclude_users: List[str] = None,
        file_ops: List[str] = None,
        file_paths: List[str] = None,
        file_types: List[str] = None,
        id: int = None,
        proc_paths: List[str] = None,
        rule_action: str = None,
        rule_name: str = None,
        status: int = None,
    ):
        self.alert_level = alert_level
        self.exclude_users = exclude_users
        # This parameter is required.
        self.file_ops = file_ops
        # This parameter is required.
        self.file_paths = file_paths
        self.file_types = file_types
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.proc_paths = proc_paths
        # This parameter is required.
        self.rule_action = rule_action
        # This parameter is required.
        self.rule_name = rule_name
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

        if self.exclude_users is not None:
            result['ExcludeUsers'] = self.exclude_users

        if self.file_ops is not None:
            result['FileOps'] = self.file_ops

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        if self.file_types is not None:
            result['FileTypes'] = self.file_types

        if self.id is not None:
            result['Id'] = self.id

        if self.proc_paths is not None:
            result['ProcPaths'] = self.proc_paths

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('ExcludeUsers') is not None:
            self.exclude_users = m.get('ExcludeUsers')

        if m.get('FileOps') is not None:
            self.file_ops = m.get('FileOps')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        if m.get('FileTypes') is not None:
            self.file_types = m.get('FileTypes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcPaths') is not None:
            self.proc_paths = m.get('ProcPaths')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

