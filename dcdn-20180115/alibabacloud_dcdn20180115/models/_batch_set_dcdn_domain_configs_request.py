# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetDcdnDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain names. Specify multiple accelerated domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The features that you want to configure. Format:
        # 
        # *   **functionName**: The name of the feature. Separate multiple values with commas (,). For more information, see [A list of features](https://help.aliyun.com/document_detail/410622.html).
        # 
        # *   **argName**: The feature parameters for **functionName**.
        # *   **argValue**: The parameter values set for **functionName**.
        # *   **parentid**: the rule ID. This parameter is optional. You can use the **condition** rules engine to create a rule. For information, see [Feature settings for domain names](https://help.aliyun.com/document_detail/388460.html). A rule can identify parameters that are included in requests and filter requests based on the identified parameters. After you create a rule, a [configid](https://help.aliyun.com/document_detail/388994.html) is generated. A configid can be used as parentId that is referenced by other features. This way, you can combine rules and features for flexible configurations.
        # 
        # If the **parentId** parameter is **-1**, the existing rules in the configurations are deleted.
        # 
        # ````[
        #  {
        #    "functionArgs": [
        #     {
        #      "argName": "Parameter A", 
        #      "argValue": Value of parameter A"
        #     }, 
        #   {
        #     "argName": "Parameter B", 
        #     "argValue": "Value of Parameter B"
        #      }
        #  ], 
        #  "functionName": "Feature name"
        #     }
        # ]```
        # ````
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

