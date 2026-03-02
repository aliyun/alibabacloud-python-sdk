# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RuntimeToken(DaraModel):
    def __init__(
        self,
        env: str = None,
        pbc_id: int = None,
        pbc_name: str = None,
        service_id: int = None,
        service_name: str = None,
        token: str = None,
    ):
        self.env = env
        self.pbc_id = pbc_id
        self.pbc_name = pbc_name
        self.service_id = service_id
        self.service_name = service_name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

