# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecognizeDataByRuleTypeRequest(DaraModel):
    def __init__(
        self,
        recognize_rules_type: str = None,
        tenant_id: str = None,
    ):
        # The type of a sensitive data identification rule. You can call the [QueryRecognizeRulesType](https://help.aliyun.com/document_detail/2746905.html) operation to obtain the type of the rule.
        # 
        # *   1: regular expression
        # *   2: built-in rule
        # *   3: sample library
        # *   4: self-generated data identification model
        # 
        # This parameter is required.
        self.recognize_rules_type = recognize_rules_type
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recognize_rules_type is not None:
            result['RecognizeRulesType'] = self.recognize_rules_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecognizeRulesType') is not None:
            self.recognize_rules_type = m.get('RecognizeRulesType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

