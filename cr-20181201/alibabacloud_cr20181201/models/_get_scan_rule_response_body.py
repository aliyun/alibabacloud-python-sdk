# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetScanRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        scan_rule: main_models.GetScanRuleResponseBodyScanRule = None,
    ):
        # Return value
        self.code = code
        # Indicates whether the API call was successful, valid values:
        # 
        # - `true`: The API call was successful
        # 
        # - `false`: The API call failed
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The scan rule.
        self.scan_rule = scan_rule

    def validate(self):
        if self.scan_rule:
            self.scan_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_rule is not None:
            result['ScanRule'] = self.scan_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanRule') is not None:
            temp_model = main_models.GetScanRuleResponseBodyScanRule()
            self.scan_rule = temp_model.from_map(m.get('ScanRule'))

        return self

class GetScanRuleResponseBodyScanRule(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        namespaces: List[str] = None,
        repo_names: List[str] = None,
        repo_tag_filter_pattern: str = None,
        rule_name: str = None,
        scan_rule_id: str = None,
        scan_scope: str = None,
        scan_type: str = None,
        trigger_type: str = None,
        update_time: int = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # Names of namespaces where the event is effective.
        self.namespaces = namespaces
        # Names of repositories where the event is effective.
        self.repo_names = repo_names
        # Tag filter pattern for event triggering.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The event rule name.
        self.rule_name = rule_name
        # The scan rule ID.
        self.scan_rule_id = scan_rule_id
        # The scan scope.
        self.scan_scope = scan_scope
        # The vulnerability type: 
        # 
        # - `cve`: System vulnerability
        # 
        # - `sca`: Application vulnerability
        self.scan_type = scan_type
        # The trigger type, valid values:
        # 
        # - `ALL`: All triggers
        # 
        # - `TAG_LISTTAG`: Trigger
        # 
        # - `TAG_REG_EXP`: Expression trigger
        self.trigger_type = trigger_type
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.repo_names is not None:
            result['RepoNames'] = self.repo_names

        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scan_rule_id is not None:
            result['ScanRuleId'] = self.scan_rule_id

        if self.scan_scope is not None:
            result['ScanScope'] = self.scan_scope

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('RepoNames') is not None:
            self.repo_names = m.get('RepoNames')

        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ScanRuleId') is not None:
            self.scan_rule_id = m.get('ScanRuleId')

        if m.get('ScanScope') is not None:
            self.scan_scope = m.get('ScanScope')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

