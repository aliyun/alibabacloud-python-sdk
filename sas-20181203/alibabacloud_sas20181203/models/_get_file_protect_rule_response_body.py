# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileProtectRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileProtectRuleResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileProtectRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileProtectRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        alert_level: int = None,
        file_ops: List[str] = None,
        file_paths: List[str] = None,
        id: int = None,
        platform: str = None,
        proc_paths: List[str] = None,
        rule_name: str = None,
        status: int = None,
        switch_id: str = None,
    ):
        # The handling method of the rule. Valid values:
        # 
        # 1.  pass: allow
        # 2.  alert
        self.action = action
        # The severity of alerts. Valid values:
        # 
        # *   0: does not generate alerts
        # *   1: sends notifications
        # *   2: suspicious
        # *   3: high-risk
        self.alert_level = alert_level
        # The operations performed on the files.
        self.file_ops = file_ops
        # The paths to the monitored files.
        self.file_paths = file_paths
        # The ID of the rule.
        self.id = id
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        self.platform = platform
        # The paths to the monitored processes.
        self.proc_paths = proc_paths
        # The name of the rule.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # 1.  0: disabled
        # 2.  1: enabled
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
        if self.action is not None:
            result['Action'] = self.action

        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.file_ops is not None:
            result['FileOps'] = self.file_ops

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        if self.id is not None:
            result['Id'] = self.id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.proc_paths is not None:
            result['ProcPaths'] = self.proc_paths

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('FileOps') is not None:
            self.file_ops = m.get('FileOps')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProcPaths') is not None:
            self.proc_paths = m.get('ProcPaths')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self

