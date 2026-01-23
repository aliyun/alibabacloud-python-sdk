# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListScanRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        scan_rules: List[main_models.ListScanRuleResponseBodyScanRules] = None,
        total_count: int = None,
    ):
        # The HTTP status code
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # Request Id
        self.request_id = request_id
        # The list of scan rules.
        self.scan_rules = scan_rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scan_rules:
            for v1 in self.scan_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScanRules'] = []
        if self.scan_rules is not None:
            for k1 in self.scan_rules:
                result['ScanRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scan_rules = []
        if m.get('ScanRules') is not None:
            for k1 in m.get('ScanRules'):
                temp_model = main_models.ListScanRuleResponseBodyScanRules()
                self.scan_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScanRuleResponseBodyScanRules(DaraModel):
    def __init__(
        self,
        create_time: int = None,
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
        # The list of namespaces.
        self.namespaces = namespaces
        # The repository name.
        self.repo_names = repo_names
        # The tag that triggers the scan matches the regular expression.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The rule name.
        self.rule_name = rule_name
        # The scan rule id.
        self.scan_rule_id = scan_rule_id
        # The scan scope.
        self.scan_scope = scan_scope
        # The scan type. Valid values:
        # 
        # *   `VUL`: Products Cloud Security Scanner
        # *   `SBOM`: Product Content Analysis
        self.scan_type = scan_type
        # The trigger type.
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

