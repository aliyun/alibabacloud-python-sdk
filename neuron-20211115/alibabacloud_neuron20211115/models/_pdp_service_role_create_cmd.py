# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpServiceRoleCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        name: str = None,
        pbc_id: int = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.company_id = company_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.pbc_id = pbc_id
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.name is not None:
            result['name'] = self.name

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

