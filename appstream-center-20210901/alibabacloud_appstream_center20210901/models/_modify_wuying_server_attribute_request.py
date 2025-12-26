# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWuyingServerAttributeRequest(DaraModel):
    def __init__(
        self,
        password: str = None,
        wuying_server_id: str = None,
        wuying_server_name: str = None,
    ):
        # Workstation login password.
        self.password = password
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id
        # The name.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')

        return self

