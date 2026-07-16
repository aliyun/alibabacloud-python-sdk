# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceCloudGtmAddressPoolAddressShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_id: str = None,
        addresses_shrink: str = None,
        client_token: str = None,
    ):
        # The response language. Valid values:
        # 
        # - **zh-CN**: Chinese
        # 
        # - **en-US** (Default): English
        self.accept_language = accept_language
        # The unique ID of the address pool to update.
        self.address_pool_id = address_pool_id
        # The list of addresses.
        self.addresses_shrink = addresses_shrink
        # The client token that is used to ensure the idempotence of the request. Ensure the client token is unique for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.addresses_shrink is not None:
            result['Addresses'] = self.addresses_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('Addresses') is not None:
            self.addresses_shrink = m.get('Addresses')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

