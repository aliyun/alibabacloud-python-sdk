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
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The validity period of the rule. Unit: seconds. This parameter takes effect only when **action** of a rule is **block**. Access requests that match the rule are blocked within the specified validity period of the rule. If you do not specify this parameter, this rule takes effect all the time.
        self.expires = expires
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The settings of the accurate access control rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **action**: the action that is performed if the rule is matched. This field is required and must be of the string type. Valid values:
        # 
        #     *   **accept**: allows the requests that match the rule.
        #     *   **block**: blocks the requests that match the rule.
        #     *   **challenge**: implements a CAPTCHA for the requests that match the rule.
        # 
        # *   **name**: the name of the rule. This field is required and must be of the string type.
        # 
        # *   **condition**: the match conditions. This field is required and must be of the map type. A match condition contains the following parameters.
        # 
        #     **
        # 
        #     **Note**The AND logical operator is used to define the relationship among multiple match conditions.
        # 
        #     *   **field**: the match field. This parameter is required and must be of the string type.
        # 
        #     *   **match_method**: the logical relation. This parameter is required and must be of the string type.
        # 
        #         **
        # 
        #         **Note**For information about the mappings between the **field** and **match_method** parameters, see the Mappings between the field and match_method parameters table in this topic.
        # 
        #     *   **content**: the match content. This parameter is required and must be of the string type.
        # 
        # *   **header_name**: the HTTP header. This parameter is optional and must be of the string type. This parameter takes effect only when **field** is **header**.
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

