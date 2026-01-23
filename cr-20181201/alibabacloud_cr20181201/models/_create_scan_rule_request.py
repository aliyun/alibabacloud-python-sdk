# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScanRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        namespaces: List[str] = None,
        repo_names: List[str] = None,
        repo_tag_filter_pattern: str = None,
        rule_name: str = None,
        scan_scope: str = None,
        scan_type: str = None,
        trigger_type: str = None,
    ):
        # The instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of namespaces.
        # 
        # *   When the scan scope is NAMESPACE, this parameter cannot be empty.
        # *   If the scan scope is REPO, you must specify a unique Namespace for this parameter.
        self.namespaces = namespaces
        # The list of repositories.
        # 
        # *   When the scan scope is NAMESPACE, this parameter must be empty.
        # *   When the scan scope is REPO, this parameter cannot be empty.
        self.repo_names = repo_names
        # The tag that triggers the scan matches the regular expression
        # 
        # This parameter is required.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The rule name
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The scan scope
        # 
        # Valid values:
        # 
        # *   NAMESPACE: namespace.
        # *   REPO: repository.
        # 
        # This parameter is required.
        self.scan_scope = scan_scope
        # The scan type. Valid values:
        # 
        # *   `VUL`: Products Cloud Security Scanner
        # *   `SBOM`: Product Content Analysis
        # 
        # Default value: `VUL`
        self.scan_type = scan_type
        # Trigger type
        # 
        # Valid values:
        # 
        # *   AUTO: automatically trigger.
        # *   MANUAL: manually trigger.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.scan_scope is not None:
            result['ScanScope'] = self.scan_scope

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ScanScope') is not None:
            self.scan_scope = m.get('ScanScope')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

