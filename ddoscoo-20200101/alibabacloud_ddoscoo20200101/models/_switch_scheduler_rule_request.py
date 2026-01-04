# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchSchedulerRuleRequest(DaraModel):
    def __init__(
        self,
        rule_name: str = None,
        rule_type: int = None,
        switch_data: str = None,
    ):
        # The name of the scheduling rule to manage.
        # 
        # > You can call the [DescribeSchedulerRules](https://help.aliyun.com/document_detail/157481.html) operation to query the names of all scheduling rules.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the scheduling rule. Valid values:
        # 
        # *   **2**: tiered protection rule
        # *   **3**: network acceleration rule
        # *   **5**: Alibaba Cloud CDN (CDN) interaction rule
        # *   **6**: cloud service interaction rule
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The configuration that is used to switch service traffic. This parameter is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that includes the following parameters:
        # 
        # *   **Value**: required. The IP address of the associated resource. Data type: string.
        # 
        # *   **State**: required. The operation type. Data type: integer. Valid values:
        # 
        #     *   **0**: switches service traffic from the associated resource to your Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing.
        #     *   **1**: switches service traffic back to the associated cloud resource.
        # 
        # *   **Interval**: optional. The waiting time that is required before the service traffic is switched back. Unit: minutes. Data type: integer. Usage notes:
        # 
        #     *   If the **State** parameter is set to **0**, you must set this parameter to \\*\\*-1\\*\\*. Otherwise, the call fails.
        #     *   If the **State** parameter is set to **1**, you do not need to set this parameter.
        # 
        # This parameter is required.
        self.switch_data = switch_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.switch_data is not None:
            result['SwitchData'] = self.switch_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SwitchData') is not None:
            self.switch_data = m.get('SwitchData')

        return self

