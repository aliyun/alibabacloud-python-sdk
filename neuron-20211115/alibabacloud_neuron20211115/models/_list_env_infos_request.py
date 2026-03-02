# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvInfosRequest(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
        env: str = None,
        pbc_id: int = None,
        region: str = None,
    ):
        self.enterprise_id = enterprise_id
        self.env = env
        self.pbc_id = pbc_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

