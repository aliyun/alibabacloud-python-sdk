# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateKibanaPvlNetworkRequest(DaraModel):
    def __init__(
        self,
        endpoint_name: str = None,
        security_groups: List[str] = None,
        client_token: str = None,
        pvl_id: str = None,
    ):
        self.endpoint_name = endpoint_name
        self.security_groups = security_groups
        self.client_token = client_token
        self.pvl_id = pvl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.security_groups is not None:
            result['securityGroups'] = self.security_groups

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.pvl_id is not None:
            result['pvlId'] = self.pvl_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('securityGroups') is not None:
            self.security_groups = m.get('securityGroups')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('pvlId') is not None:
            self.pvl_id = m.get('pvlId')

        return self

