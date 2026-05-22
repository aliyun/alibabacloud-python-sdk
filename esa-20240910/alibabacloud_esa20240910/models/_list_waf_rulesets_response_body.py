# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafRulesetsResponseBody(DaraModel):
    def __init__(
        self,
        instance_usage: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rulesets: List[main_models.ListWafRulesetsResponseBodyRulesets] = None,
        site_usage: int = None,
        total_count: int = None,
    ):
        # Number of WAF rule sets used by the instance in this WAF operation phase.
        self.instance_usage = instance_usage
        # Current page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # List of rule set information, containing detailed information about the rule sets.
        self.rulesets = rulesets
        # Number of WAF rule sets used by the site in this WAF operation phase.
        self.site_usage = site_usage
        # Total number of filtered records.
        self.total_count = total_count

    def validate(self):
        if self.rulesets:
            for v1 in self.rulesets:
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

        result['Rulesets'] = []
        if self.rulesets is not None:
            for k1 in self.rulesets:
                result['Rulesets'].append(k1.to_map() if k1 else None)

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

        self.rulesets = []
        if m.get('Rulesets') is not None:
            for k1 in m.get('Rulesets'):
                temp_model = main_models.ListWafRulesetsResponseBodyRulesets()
                self.rulesets.append(temp_model.from_map(k1))

        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWafRulesetsResponseBodyRulesets(DaraModel):
    def __init__(
        self,
        fields: List[str] = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        status: str = None,
        target: str = None,
        types: List[str] = None,
        update_time: str = None,
    ):
        # List of match objects.
        self.fields = fields
        # ID of the WAF rule set.
        self.id = id
        # Name of the rule set.
        self.name = name
        # WAF operation phase.
        self.phase = phase
        # Status of the rule set.
        self.status = status
        # Protection target type in http_bot.
        self.target = target
        # List of rule types.
        self.types = types
        # Last modification time of the rule set.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.types is not None:
            result['Types'] = self.types

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

