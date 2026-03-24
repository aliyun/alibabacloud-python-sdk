# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetCdnDomainConfigRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain names. You can specify multiple accelerated domain names and separate them with commas (,).
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The features that you want to configure. Format:
        # 
        # *   **functionName**: the name of the feature. This parameter is required. Separate multiple values with commas (,). For more information, see [Parameters for configuring features for domain names](https://help.aliyun.com/document_detail/388460.html).
        # *   **argName**: the feature parameter for **functionName**. This parameter is required. You can specify multiple feature parameters.
        # *   **argValue**: the parameter value that is specified for **functionName**. This parameter is required.
        # *   **parentid**: the rule condition ID. This parameter is optional. You can use the **condition** rule engine to create a rule condition. For information, see [Parameters for configuring features for domain names](https://help.aliyun.com/document_detail/388460.html). A rule condition can identify parameters that are included in requests and filter requests based on the identified parameters. After you create a rule condition, a [configid](https://help.aliyun.com/document_detail/388994.html) is generated. A configid can be used as parentId that is referenced by other features. This way, you can combine rule conditions and features for flexible configurations.
        # 
        # If the **ParentId** parameter is \\*\\*-1\\*\\*, the existing rule conditions in the configurations are deleted.
        # 
        # ```[{
        #    "functionArgs": [{
        #      "argName": "Parameter A", 
        #      "argValue": "Value of parameter A"
        #     }, 
        #   {
        #     "argName": "Parameter B", 
        #     "argValue": "Value of parameter B"
        #      }], 
        #  "functionName": "Feature name"
        #  "parentId": Optional. parentId corresponds to configid of the referenced rule condition
        # }]
        # ```
        # 
        # The following code provides a sample configuration if **parentId** is not used. In this example, the **origin_request_header** feature is used to add back-to-origin HTTP headers, and the rule condition whose configuration ID is **configid=222728944812032** is referenced.
        # 
        # ```[{
        #         "functionArgs": [{
        #             "argName": "header_operation_type",
        #             "argValue": "add"
        #         }, {
        #             "argName": "header_name",
        #             "argValue": "Accept-Encoding"
        #         }, {
        #             "argName": "header_value",
        #             "argValue": "gzip"
        #         }, {
        #             "argName": "duplicate",
        #             "argValue": "off"
        #         }],
        #         "functionName": "origin_request_header"
        # }]
        # ```
        # 
        # The following code shows a sample configuration if **parentId** is used. In this example, the **origin_request_header** feature is used to add back-to-origin HTTP headers, and the rule condition whose configuration ID is **222728944812032** is referenced.
        # 
        # ```[{
        #         "functionArgs": [{
        #             "argName": "header_operation_type",
        #             "argValue": "add"
        #         }, {
        #             "argName": "header_name",
        #             "argValue": "Accept-Encoding"
        #         }, {
        #             "argName": "header_value",
        #             "argValue": "gzip"
        #         }, {
        #             "argName": "duplicate",
        #             "argValue": "off"
        #         }],
        #         "functionName": "origin_request_header",
        #         "parentId": 222728944812032
        # }]
        # ```
        # 
        # The following code provides a sample configuration that deletes the reference to **parentId** for a feature that uses **parentId**. This example shows how to delete the rule condition that has a configuration ID of **222728944812032** and is referenced when **origin_request_header** feature is used to add back-to-origin HTTP headers.
        # 
        # ```[{
        #         "functionArgs": [{
        #             "argName": "header_operation_type",
        #             "argValue": "add"
        #         }, {
        #             "argName": "header_name",
        #             "argValue": "Accept-Encoding"
        #         }, {
        #             "argName": "header_value",
        #             "argValue": "gzip"
        #         }, {
        #             "argName": "duplicate",
        #             "argValue": "off"
        #         }],
        #         "functionName": "origin_request_header",
        #         "parentId": -1
        # }]
        # ```
        # 
        # This parameter is required.
        self.functions = functions
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.functions is not None:
            result['Functions'] = self.functions

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('Functions') is not None:
            self.functions = m.get('Functions')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

