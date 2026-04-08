# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class InvokeActionRequest(DaraModel):
    def __init__(
        self,
        action_id: str = None,
        action_version: str = None,
        auth_config: main_models.InvokeActionRequestAuthConfig = None,
        body: Dict[str, Any] = None,
        connector_id: str = None,
        connector_version: str = None,
        headers: Dict[str, str] = None,
        path: Dict[str, str] = None,
        query: Dict[str, str] = None,
        stream: bool = None,
    ):
        # This parameter is required.
        self.action_id = action_id
        self.action_version = action_version
        self.auth_config = auth_config
        self.body = body
        # This parameter is required.
        self.connector_id = connector_id
        self.connector_version = connector_version
        self.headers = headers
        self.path = path
        self.query = query
        self.stream = stream

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_id is not None:
            result['ActionId'] = self.action_id

        if self.action_version is not None:
            result['ActionVersion'] = self.action_version

        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config.to_map()

        if self.body is not None:
            result['Body'] = self.body

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.path is not None:
            result['Path'] = self.path

        if self.query is not None:
            result['Query'] = self.query

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')

        if m.get('ActionVersion') is not None:
            self.action_version = m.get('ActionVersion')

        if m.get('AuthConfig') is not None:
            temp_model = main_models.InvokeActionRequestAuthConfig()
            self.auth_config = temp_model.from_map(m.get('AuthConfig'))

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self



class InvokeActionRequestAuthConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: Any = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

