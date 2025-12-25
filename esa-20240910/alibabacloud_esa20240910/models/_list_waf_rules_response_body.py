# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafRulesResponseBody(DaraModel):
    def __init__(
        self,
        instance_usage: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.ListWafRulesResponseBodyRules] = None,
        site_usage: int = None,
        total_count: int = None,
    ):
        # Number of rules used in this WAF phase for the corresponding instance of the site.
        self.instance_usage = instance_usage
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned list of rules.
        self.rules = rules
        # Site usage.
        self.site_usage = site_usage
        # Total number of rules after filtering.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_usage is not None:
            result['InstanceUsage'] = self.instance_usage

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceUsage') is not None:
            self.instance_usage = m.get('InstanceUsage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListWafRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWafRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        characteristics_fields: List[str] = None,
        config: main_models.WafRuleConfig = None,
        fields: List[str] = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        ruleset_id: int = None,
        skip: str = None,
        status: str = None,
        tags: List[str] = None,
        timer: main_models.WafTimer = None,
        type: str = None,
        update_time: str = None,
    ):
        # The action corresponding to the rule.
        self.action = action
        # List of statistical objects for frequency control rules.
        self.characteristics_fields = characteristics_fields
        # Rule configuration.
        self.config = config
        # List of fields for rule matching
        self.fields = fields
        # Rule ID.
        self.id = id
        # Rule name.
        self.name = name
        # WAF phase.
        self.phase = phase
        # Position order of the rule in the corresponding ruleset.
        self.position = position
        # Ruleset ID.
        self.ruleset_id = ruleset_id
        # Skip attribute for whitelist rules.
        self.skip = skip
        # Rule status.
        self.status = status
        # List of WAF phases to be skipped by whitelist rules.
        self.tags = tags
        # Configuration for the effective time of the rule.
        self.timer = timer
        # Rule type.
        self.type = type
        # Modification time.
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.characteristics_fields is not None:
            result['CharacteristicsFields'] = self.characteristics_fields

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.position is not None:
            result['Position'] = self.position

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timer is not None:
            result['Timer'] = self.timer.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CharacteristicsFields') is not None:
            self.characteristics_fields = m.get('CharacteristicsFields')

        if m.get('Config') is not None:
            temp_model = main_models.WafRuleConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Timer') is not None:
            temp_model = main_models.WafTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

