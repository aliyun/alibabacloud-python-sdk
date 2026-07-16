# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressPoolRemarkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_id: str = None,
        client_token: str = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The unique ID of the address pool.
        self.address_pool_id = address_pool_id
        # A client token to ensure the idempotence of the request. Generate a unique value from your client. The token can contain only ASCII characters and must be no more than 64 characters in length.
        self.client_token = client_token
        # The new remarks for the address pool. If you leave this parameter empty, the remarks are deleted.
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

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

