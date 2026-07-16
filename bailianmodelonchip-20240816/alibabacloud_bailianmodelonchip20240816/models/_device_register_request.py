# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeviceRegisterRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        nonce: str = None,
        request_time: str = None,
        signature: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.nonce is not None:
            result['nonce'] = self.nonce

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.signature is not None:
            result['signature'] = self.signature

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

