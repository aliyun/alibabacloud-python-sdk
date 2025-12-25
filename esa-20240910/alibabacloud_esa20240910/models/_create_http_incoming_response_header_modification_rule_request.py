# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateHttpIncomingResponseHeaderModificationRuleRequest(DaraModel):
    def __init__(
        self,
        response_header_modification: List[main_models.CreateHttpIncomingResponseHeaderModificationRuleRequestResponseHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The configurations of modifying response headers. You can add, delete, or modify a response header.
        # 
        # This parameter is required.
        self.response_header_modification = response_header_modification
        # The content of the rule. A conditional expression is used to match a user request. You do not need to set this parameter when you add global configuration. Use cases:
        # 
        # *   true: Match all incoming requests.
        # *   Set the value to a custom expression, for example: (http.host eq "video.example.com"): Match the specified request
        self.rule = rule
        # Specifies whether to enable the rule. Valid values: You do not need to set this parameter when you add global configuration. Valid values:
        # 
        # *   on
        # *   off
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when you add global configuration.
        self.rule_name = rule_name
        # The order in which the rule is executed. A smaller value gives priority to the rule.
        self.sequence = sequence
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the website configurations. You can use this parameter to specify a version of your website to apply the feature settings. By default, version 0 is used.
        self.site_version = site_version

    def validate(self):
        if self.response_header_modification:
            for v1 in self.response_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResponseHeaderModification'] = []
        if self.response_header_modification is not None:
            for k1 in self.response_header_modification:
                result['ResponseHeaderModification'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.response_header_modification = []
        if m.get('ResponseHeaderModification') is not None:
            for k1 in m.get('ResponseHeaderModification'):
                temp_model = main_models.CreateHttpIncomingResponseHeaderModificationRuleRequestResponseHeaderModification()
                self.response_header_modification.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

class CreateHttpIncomingResponseHeaderModificationRuleRequestResponseHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the response header.
        # 
        # This parameter is required.
        self.name = name
        # The action. Valid values:
        # 
        # *   add: adds a response header.
        # *   del: deletes a response header.
        # *   modify: modifies a response header.
        # 
        # This parameter is required.
        self.operation = operation
        # The type of the value. Valid values:
        # 
        # *   static
        # *   dynamic
        self.type = type
        # The value of the response header.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

