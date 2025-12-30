# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressRemarkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_id: str = None,
        client_token: str = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The ID of the address. This ID uniquely identifies the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The input parameter serves as the updated note; if an empty value is passed, the note will be deleted.
        self.remark = remark

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

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

