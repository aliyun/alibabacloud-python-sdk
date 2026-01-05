# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        endpoint_id: str = None,
        net_type: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # This parameter is required.
        self.net_type = net_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        return self

