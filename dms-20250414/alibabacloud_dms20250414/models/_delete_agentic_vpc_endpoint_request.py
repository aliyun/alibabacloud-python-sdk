# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgenticVpcEndpointRequest(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
    ):
        # The ID of the endpoint to be deleted. You can delete the endpoint even if it has associated data sources, but this may interrupt access.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        return self

