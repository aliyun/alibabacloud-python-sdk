# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateHttpIncomingRequestHeaderModificationRuleRequest(DaraModel):
    def __init__(
        self,
        request_header_modification: List[main_models.CreateHttpIncomingRequestHeaderModificationRuleRequestRequestHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # An array of objects, where each object defines a modification to a request header.
        # 
        # This parameter is required.
        self.request_header_modification = request_header_modification
        # The conditional expression that the Rule uses to match incoming requests. This parameter is not required for a Global configuration. There are two use cases:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, use a custom expression. For example: `(http.host eq "video.example.com")`
        self.rule = rule
        # Specifies whether the Rule is enabled. This parameter is not required for a Global configuration. Valid values:
        # 
        # - `on`: The Rule is enabled.
        # 
        # - `off`: The Rule is disabled.
        self.rule_enable = rule_enable
        # The name of the Rule. This parameter is not required for a Global configuration.
        self.rule_name = rule_name
        # The execution order of the Rule. A lower value indicates a higher priority.
        self.sequence = sequence
        # The ID of the Site. You can obtain this value by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The Version of the Site configuration. For Sites with configuration versioning enabled, this parameter specifies the Version to which the Rule applies. The default value is 0.
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
        result['RequestHeaderModification'] = []
        if self.request_header_modification is not None:
            for k1 in self.request_header_modification:
                result['RequestHeaderModification'].append(k1.to_map() if k1 else None)

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
        self.request_header_modification = []
        if m.get('RequestHeaderModification') is not None:
            for k1 in m.get('RequestHeaderModification'):
                temp_model = main_models.CreateHttpIncomingRequestHeaderModificationRuleRequestRequestHeaderModification()
                self.request_header_modification.append(temp_model.from_map(k1))

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

class CreateHttpIncomingRequestHeaderModificationRuleRequestRequestHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the request header.
        # 
        # This parameter is required.
        self.name = name
        # The Operation to perform. Valid values:
        # 
        # - `add`: Adds a header.
        # 
        # - `del`: Deletes a header.
        # 
        # - `modify`: Modifies a header.
        # 
        # This parameter is required.
        self.operation = operation
        # The type of the header value. Valid values:
        # 
        # - `static`: Static mode.
        # 
        # - `dynamic`: Dynamic mode.
        self.type = type
        # The value to set for the request header. This parameter is not required if the `Operation` is `del`.
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

