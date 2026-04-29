# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AddPolarClawMCPServerRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        server_config: Dict[str, Any] = None,
        server_name: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.server_config = server_config
        # This parameter is required.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.server_config is not None:
            result['ServerConfig'] = self.server_config

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ServerConfig') is not None:
            self.server_config = m.get('ServerConfig')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

