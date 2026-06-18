# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetHttpRequestHeaderModificationRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        request_header_modification: List[main_models.GetHttpRequestHeaderModificationRuleResponseBodyRequestHeaderModification] = None,
        request_id: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The configuration type. Valid values:
        # 
        # - global: A global configuration.
        # 
        # - rule: A rule-based configuration.
        self.config_type = config_type
        # The request header modifications. The add, delete, and modify operations are supported.
        self.request_header_modification = request_header_modification
        # The request ID.
        self.request_id = request_id
        # The content of the rule, which uses a conditional expression to match user requests. This parameter is not required for global configurations. There are two scenarios:
        # 
        # - To match all incoming requests, set the value to true.
        # 
        # - To match specific requests, set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # Specifies whether the rule is enabled. This parameter is not required for global configurations. Valid values:
        # 
        # - on: The rule is enabled.
        # 
        # - off: The rule is disabled.
        self.rule_enable = rule_enable
        # The name of the rule. This parameter is not required for global configurations.
        self.rule_name = rule_name
        # The execution order of the rule. Rules with smaller values are executed first.
        self.sequence = sequence
        # The version number of the site configuration. For sites with version management enabled, this parameter specifies the site version to which the configuration applies. The default value is 0.
        self.site_version = site_version

    def validate(self):
        if self.request_header_modification:
            for v1 in self.request_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        result['RequestHeaderModification'] = []
        if self.request_header_modification is not None:
            for k1 in self.request_header_modification:
                result['RequestHeaderModification'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        self.request_header_modification = []
        if m.get('RequestHeaderModification') is not None:
            for k1 in m.get('RequestHeaderModification'):
                temp_model = main_models.GetHttpRequestHeaderModificationRuleResponseBodyRequestHeaderModification()
                self.request_header_modification.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class GetHttpRequestHeaderModificationRuleResponseBodyRequestHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the request header.
        self.name = name
        # The operation to perform. Valid values:
        # 
        # - add: Adds a header.
        # 
        # - del: Deletes a header.
        # 
        # - modify: Modifies a header.
        self.operation = operation
        # The type of the value. Valid values:
        # 
        # - static: A static value.
        # 
        # - dynamic: A dynamic value.
        self.type = type
        # The value of the request header.
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

