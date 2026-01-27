# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFingerPrintTemplateRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        index: int = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client token to ensure the idempotence of the request. You can use the client to generate the value, but you ensure sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The index.
        # 
        # This parameter is required.
        self.index = index
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.index is not None:
            result['Index'] = self.index

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

