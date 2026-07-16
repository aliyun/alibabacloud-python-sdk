# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetHttpResponseHeaderModificationRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        request_id: str = None,
        response_header_modification: List[main_models.GetHttpResponseHeaderModificationRuleResponseBodyResponseHeaderModification] = None,
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
        # - `global`: global configuration.
        # 
        # - `rule`: rule configuration.
        self.config_type = config_type
        # The request ID.
        self.request_id = request_id
        # A list of modifications to apply to the response header.
        self.response_header_modification = response_header_modification
        # The rule content, a conditional expression used to match user requests. This parameter applies only to rule configurations. The expression can be:
        # 
        # - `true`: Matches all incoming requests.
        # 
        # - A custom expression, such as `(http.host eq "video.example.com")`: Matches specific requests.
        self.rule = rule
        # The rule switch. This parameter applies only to rule configurations. Valid values:
        # 
        # - `on`: The rule is enabled.
        # 
        # - `off`: The rule is disabled.
        self.rule_enable = rule_enable
        # The rule name. This parameter applies only to rule configurations.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The version of the site configuration. If configuration versioning is enabled for the site, this parameter specifies the version to which this configuration applies. The default value is 0.
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
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.response_header_modification = []
        if m.get('ResponseHeaderModification') is not None:
            for k1 in m.get('ResponseHeaderModification'):
                temp_model = main_models.GetHttpResponseHeaderModificationRuleResponseBodyResponseHeaderModification()
                self.response_header_modification.append(temp_model.from_map(k1))

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

class GetHttpResponseHeaderModificationRuleResponseBodyResponseHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        type: str = None,
        value: str = None,
    ):
        # The response header name.
        self.name = name
        # The operation. Valid values:
        # 
        # - `add`: Adds a header.
        # 
        # - `del`: Deletes a header.
        # 
        # - `modify`: Modifies a header.
        self.operation = operation
        # The value type. Valid values:
        # 
        # - `static`: static mode.
        # 
        # - `dynamic`: dynamic mode.
        self.type = type
        # The response header value.
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

