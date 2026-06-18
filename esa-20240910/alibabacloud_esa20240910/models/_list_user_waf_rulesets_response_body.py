# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListUserWafRulesetsResponseBody(DaraModel):
    def __init__(
        self,
        instance_usage: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rulesets: List[main_models.ListUserWafRulesetsResponseBodyRulesets] = None,
        total_count: int = None,
    ):
        # The instance usage.
        self.instance_usage = instance_usage
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # A list of WAF ruleset objects.
        self.rulesets = rulesets
        # The total number of records after filtering.
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
                temp_model = main_models.ListUserWafRulesetsResponseBodyRulesets()
                self.rulesets.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserWafRulesetsResponseBodyRulesets(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        status: str = None,
    ):
        # The WAF ruleset description.
        self.description = description
        # The WAF ruleset ID.
        self.id = id
        # The WAF ruleset name.
        self.name = name
        # The WAF rule execution phase. Possible values:
        # 
        # - `http_whitelist`: Whitelist rule
        # 
        # - `http_custom`: Custom rule
        # 
        # - `http_managed`: Managed rule
        # 
        # - `http_anti_scan`: Scan protection rule
        # 
        # - `http_ratelimit`: Rate limit rule
        # 
        # - `ip_access_rule`: IP access rule
        # 
        # - `http_bot`: Bot rule
        # 
        # - `http_security_level_rule`: Security rule
        self.phase = phase
        # The WAF ruleset position.
        self.position = position
        # The WAF ruleset status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.position is not None:
            result['Position'] = self.position

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

