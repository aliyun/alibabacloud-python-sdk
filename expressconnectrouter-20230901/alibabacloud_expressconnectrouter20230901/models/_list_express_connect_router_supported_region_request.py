# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExpressConnectRouterSupportedRegionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        node_type: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The type of the network instance. Valid values:
        # 
        # *   **TR**
        # *   **VBR**
        # *   **VPC**
        # 
        # This parameter is required.
        self.node_type = node_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

