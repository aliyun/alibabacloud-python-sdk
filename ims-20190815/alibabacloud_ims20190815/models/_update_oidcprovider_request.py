# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOIDCProviderRequest(DaraModel):
    def __init__(
        self,
        client_ids: str = None,
        issuance_limit_time: int = None,
        new_description: str = None,
        oidcprovider_name: str = None,
    ):
        # The ID of the client. If you want to specify multiple client IDs, separate the client IDs with commas (,).
        # 
        # A client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # A client ID can be up to 128 characters in length.
        # 
        # >  If you specify this parameter, all the client IDs of the OIDC IdP are replaced. If you need to only add or remove a client ID, call the AddClientIdToOIDCProvider or RemoveClientIdFromOIDCProvider operation. For more information, see [AddClientIdToOIDCProvider](https://help.aliyun.com/document_detail/332057.html) or [RemoveClientIdFromOIDCProvider](https://help.aliyun.com/document_detail/332058.html).
        self.client_ids = client_ids
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.new_description = new_description
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        return self

