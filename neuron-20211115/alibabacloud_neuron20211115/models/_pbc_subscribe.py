# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcSubscribe(DaraModel):
    def __init__(
        self,
        developer_id: str = None,
        id: int = None,
        pbc_name: str = None,
        purpose: str = None,
        sub_pbc_name: str = None,
    ):
        self.developer_id = developer_id
        self.id = id
        self.pbc_name = pbc_name
        self.purpose = purpose
        self.sub_pbc_name = sub_pbc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.id is not None:
            result['id'] = self.id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.purpose is not None:
            result['purpose'] = self.purpose

        if self.sub_pbc_name is not None:
            result['subPbcName'] = self.sub_pbc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('purpose') is not None:
            self.purpose = m.get('purpose')

        if m.get('subPbcName') is not None:
            self.sub_pbc_name = m.get('subPbcName')

        return self

