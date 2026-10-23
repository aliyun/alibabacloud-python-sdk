# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallPluginRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        client_token: str = None,
        force: bool = None,
    ):
        # The names of the system plug-ins to uninstall.
        self.body = body
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to forcibly uninstall the plug-ins. You can use this parameter to cancel the installation of plug-ins that are being installed. This parameter is only applicable to instances that use the new architecture. Default value: false.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.force is not None:
            result['force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('force') is not None:
            self.force = m.get('force')

        return self

