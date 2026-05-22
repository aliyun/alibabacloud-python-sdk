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
        # Configuration ID.
        self.config_id = config_id
        # Configuration type, with the following values:
        # - global: Global configuration.
        # - rule: Rule-based configuration.
        self.config_type = config_type
        # Request ID.
        self.request_id = request_id
        # Modify response headers, supporting add, delete, and modify operations.
        self.response_header_modification = response_header_modification
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Possible values are:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # Rule execution order. The smaller the value, the higher the priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites that have enabled configuration version management, you can use this parameter to specify the effective version of the site configuration, defaulting to version 0.
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
        # Response header name.
        self.name = name
        # Operation method. Possible values are:
        # 
        # - add: Add.
        # - del: Delete
        # - modify: Modify.
        self.operation = operation
        self.type = type
        # Response header value.
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

