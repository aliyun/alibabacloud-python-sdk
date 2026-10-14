# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebPreciseAccessRuleRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        expires: int = None,
        resource_group_id: str = None,
        rules: str = None,
    ):
        # The domain of the website.
        # 
        # > You must configure a forwarding rule for the domain. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domains.
        # 
        # This parameter is required.
        self.domain = domain
        # The validity period of the rule, in seconds. This parameter applies only when **action** is set to **block**. Requests that match the rule are blocked for the specified duration. If you do not specify this parameter, the rule is permanently effective.
        self.expires = expires
        # The ID of the resource group to which the Anti-DDoS Pro instance belongs. If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The configuration of the precise access control rule, specified as a JSON-formatted string. The string has the following structure:
        # 
        # - **action**: String. Required. The action to perform on matching requests. Valid values:
        # 
        #   - **accept**: Allows the request.
        # 
        #   - **block**: Blocks the request.
        # 
        #   - **challenge**: Initiates a challenge to verify the request.
        # 
        #   - **watch**: Monitors the request.
        # 
        # - **name**: String. Required. The name of the rule.
        # 
        # - **condition**: Map. Required. The match conditions. The structure is as follows:
        # 
        #   > If you specify multiple match conditions, they are evaluated with a logical AND.
        # 
        #   - **field**: String. Required. The match field.
        # 
        #   - **match_method**: String. Required. The match method.
        # 
        #     > For information about the valid values for **field** and **match_method**, see the "Additional information about request parameters" section.
        # 
        #   - **content**: String. The value to match. You can specify either this parameter or `content_list`.
        # 
        #   - **content_list**: String. A list of values to match. You can specify either this parameter or `content`.
        # 
        #   > For information about the valid values for **match_method** and **content/content_list**, see the "Additional information about request parameters" section.
        # 
        # - **header_name**: String. Optional. The name of the request header. This parameter applies only when **field** is set to **header**.
        # 
        # - **case_insensitive**: Boolean. Optional. The default value is false. Valid values:
        # 
        #   - **false**: case-sensitive
        # 
        #   - **true**: case-insensitive
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expires is not None:
            result['Expires'] = self.expires

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

