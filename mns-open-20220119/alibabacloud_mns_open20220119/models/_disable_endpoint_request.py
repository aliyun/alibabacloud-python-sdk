# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableEndpointRequest(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
    ):
        # The type of the endpoint. Valid value:
        # 
        # - **public**: The Internet endpoint. Currently, only public is supported.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

