# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeActionShrinkRequest(DaraModel):
    def __init__(
        self,
        action_id: str = None,
        action_version: str = None,
        auth_config_shrink: str = None,
        body_shrink: str = None,
        connector_id: str = None,
        connector_version: str = None,
        headers_shrink: str = None,
        path_shrink: str = None,
        query_shrink: str = None,
        stream: bool = None,
    ):
        # The action ID.
        # 
        # This parameter is required.
        self.action_id = action_id
        # The action version.
        self.action_version = action_version
        # The authentication information for the action.
        self.auth_config_shrink = auth_config_shrink
        # The request body for the action.
        self.body_shrink = body_shrink
        # The connector ID.
        # 
        # This parameter is required.
        self.connector_id = connector_id
        # The connector version.
        self.connector_version = connector_version
        # The request header parameters for the action.
        self.headers_shrink = headers_shrink
        # The path parameters for the action.
        self.path_shrink = path_shrink
        # The query parameters for the action.
        self.query_shrink = query_shrink
        # Specifies whether to use streaming output.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_id is not None:
            result['ActionId'] = self.action_id

        if self.action_version is not None:
            result['ActionVersion'] = self.action_version

        if self.auth_config_shrink is not None:
            result['AuthConfig'] = self.auth_config_shrink

        if self.body_shrink is not None:
            result['Body'] = self.body_shrink

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        if self.headers_shrink is not None:
            result['Headers'] = self.headers_shrink

        if self.path_shrink is not None:
            result['Path'] = self.path_shrink

        if self.query_shrink is not None:
            result['Query'] = self.query_shrink

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
            self.auth_config_shrink = m.get('AuthConfig')

        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        if m.get('Headers') is not None:
            self.headers_shrink = m.get('Headers')

        if m.get('Path') is not None:
            self.path_shrink = m.get('Path')

        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

