# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetVodDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The accelerated domain names for ApsaraVideo VOD. Separate multiple domain names with commas (,). You can configure up to 50 domain names at a time.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The list of features.
        # - functionName (feature name, required): For the features that can be configured and their feature name parameters, see [Domain name configuration features](https://help.aliyun.com/document_detail/2411639.html).
        # - argName (parameter name, required): The configuration items of functionName. You can configure multiple configuration items.
        # - argValue (parameter value, required): The values of the configuration items of functionName.
        # 
        # For detailed information about the features that can be configured for accelerated domain names, including feature names and parameter names, see [Domain name configuration features](https://help.aliyun.com/document_detail/2411639.html).
        # 
        # > Some features, such as filetype_based_ttl_set (file expiration time), support multiple configuration rules. To update a specific configuration rule, specify the configId of that rule. Example:
        # `[{"functionArgs":[{"argName":"file_type","argValue":"jpg"},{"argName":"ttl","argValue":"18"},{"argName":"weight","argValue":"30"}],"functionName":"filetype_based_ttl_set","configId":5068995}]`
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

