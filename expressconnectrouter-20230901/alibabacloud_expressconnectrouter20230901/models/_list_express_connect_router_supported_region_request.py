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
        # A client token to ensure the idempotence of the request.
        # 
        # Generate a value that is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** as the **ClientToken**. Each request has a unique **RequestId**.
        self.client_token = client_token
        # The type of network instance. Valid values:
        # 
        # - **TR**: transit router instance.
        # 
        # - **VBR**: virtual border router instance.
        # 
        # - **VPC**: virtual private cloud instance.
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

