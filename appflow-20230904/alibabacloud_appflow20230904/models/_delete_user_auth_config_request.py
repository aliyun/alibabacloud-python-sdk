# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserAuthConfigRequest(DaraModel):
    def __init__(
        self,
        auth_config_id: str = None,
        connector_id: str = None,
        connector_version: str = None,
    ):
        # This parameter is required.
        self.auth_config_id = auth_config_id
        # This parameter is required.
        self.connector_id = connector_id
        self.connector_version = connector_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config_id is not None:
            result['AuthConfigId'] = self.auth_config_id

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfigId') is not None:
            self.auth_config_id = m.get('AuthConfigId')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        return self

