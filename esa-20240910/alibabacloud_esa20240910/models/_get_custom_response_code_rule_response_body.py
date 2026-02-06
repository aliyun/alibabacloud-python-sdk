# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomResponseCodeRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        page_id: str = None,
        request_id: str = None,
        return_code: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
    ):
        self.config_id = config_id
        self.config_type = config_type
        self.page_id = page_id
        self.request_id = request_id
        self.return_code = return_code
        self.rule = rule
        self.rule_enable = rule_enable
        self.rule_name = rule_name
        self.sequence = sequence
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.return_code is not None:
            result['ReturnCode'] = self.return_code

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

