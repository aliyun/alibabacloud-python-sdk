# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetMqttTicketRequest(DaraModel):
    def __init__(
        self,
        client_os: str = None,
        client_type: int = None,
        client_version: str = None,
        properties: Dict[str, Any] = None,
        uuid: str = None,
    ):
        # The client operating system.
        # 
        # This parameter is required.
        self.client_os = client_os
        # The client type. Valid values: 0: hardware terminal; 1: Windows software terminal; 2: macOS software terminal; 3: iOS client; 4: Android client; 5: web client; 6: tenant console.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The client version.
        # 
        # This parameter is required.
        self.client_version = client_version
        # The extended properties of the client, represented as a JSON object where both keys and values are strings. Example: `{"a":"1","b":"2"}`. If this parameter is not specified, it is processed as an empty property set.
        self.properties = properties
        # The device UUID.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

