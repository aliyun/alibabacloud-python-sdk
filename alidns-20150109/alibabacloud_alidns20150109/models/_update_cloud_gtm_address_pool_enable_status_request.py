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
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The unique ID of the address pool.
        self.address_pool_id = address_pool_id
        # A client token to ensure the idempotence of the request. Generate a unique value from your client for this parameter. The client token can contain only ASCII characters and must be no more than 64 characters in length.
        self.client_token = client_token
        # The enabled status of the address pool:
        # 
        # - enable: Enables the address pool. If the health check is normal, the address pool is included in DNS resolution.
        # 
        # - disable: Disables the address pool. The address pool is not included in DNS resolution, regardless of its health check status.
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

