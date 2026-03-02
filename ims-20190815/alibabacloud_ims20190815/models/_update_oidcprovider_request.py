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
        self.client_ids = client_ids
        self.issuance_limit_time = issuance_limit_time
        self.new_description = new_description
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

