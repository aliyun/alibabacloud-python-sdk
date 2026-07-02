# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel


def _get_web_socket_utils_models():
    from alibabacloud_tea_openapi import websocketUtils_models as web_socket_utils_models

    return web_socket_utils_models

class MultiModalGuardWsResponse(DaraModel):
    def __init__(
        self,
        web_socket_client = None,
    ):
        self.web_socket_client = web_socket_client

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.web_socket_client is not None:
            result['webSocketClient'] = self.web_socket_client.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('webSocketClient') is not None:
            web_socket_utils_models = _get_web_socket_utils_models()
            temp_model = web_socket_utils_models.WebSocketClient()
            self.web_socket_client = temp_model.from_map(m.get('webSocketClient'))

        return self
