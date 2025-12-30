# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressPoolEnableStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_id: str = None,
        client_token: str = None,
        enable_status: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The ID of the address pool. This ID uniquely identifies the address pool.
        self.address_pool_id = address_pool_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enabling state of the address pool. Valid values:
        # 
        # *   enable: The address pool is enabled, and the addresses in the address pool are returned for DNS resolution when the health check results are normal.
        # *   disable: The address pool is disabled, and the addresses in the address pool are not returned for DNS resolution regardless of whether the health check results are normal or not.
        self.enable_status = enable_status

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        return self

