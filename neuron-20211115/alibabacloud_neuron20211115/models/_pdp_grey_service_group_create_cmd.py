# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpGreyServiceGroupCreateCmd(DaraModel):
    def __init__(
        self,
        env: str = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

