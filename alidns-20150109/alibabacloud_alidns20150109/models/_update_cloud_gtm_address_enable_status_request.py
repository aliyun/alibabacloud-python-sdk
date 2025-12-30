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
        # The language of the returned results. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US: English
        self.accept_language = accept_language
        # The ID of the address. This ID uniquely identifies the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enabling state of the address. Valid values:
        # 
        # *   enable: The address is enabled and the address can be used for Domain Name System (DNS) resolution if the address passes health checks.
        # *   disable: The address is disabled and the address cannot be used for DNS resolution regardless of whether the address passes health checks or not.
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

