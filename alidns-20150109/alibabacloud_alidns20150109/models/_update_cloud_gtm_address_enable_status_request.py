# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressEnableStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_id: str = None,
        client_token: str = None,
        enable_status: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US: English
        self.accept_language = accept_language
        # The unique ID of the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # A client-generated token that is used to ensure the idempotence of the request. Make sure that the token is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The enabled status of the address:
        # 
        # - enable: The address can be used for DNS resolution if its health check is normal.
        # 
        # - disable: The address cannot be used for DNS resolution, regardless of its health check status.
        # 
        # This parameter is required.
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

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        return self

