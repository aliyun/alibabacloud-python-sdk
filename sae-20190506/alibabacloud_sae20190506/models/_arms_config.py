# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ArmsConfig(DaraModel):
    def __init__(
        self,
        agent_version: str = None,
        app_id: str = None,
        license_key: str = None,
    ):
        self.agent_version = agent_version
        self.app_id = app_id
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.license_key is not None:
            result['licenseKey'] = self.license_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')

        return self

