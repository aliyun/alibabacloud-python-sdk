# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCloudGtmAddressRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_id: str = None,
        client_token: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US (default): English.
        self.accept_language = accept_language
        # The unique ID of the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # A client token that ensures the idempotence of the request. The token must be unique among different requests. The token can be up to 64 ASCII characters long.
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

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

