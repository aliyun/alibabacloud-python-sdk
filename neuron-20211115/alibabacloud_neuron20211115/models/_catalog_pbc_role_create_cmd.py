# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CatalogPbcRoleCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        market_id: int = None,
        market_resource: str = None,
        name: str = None,
        pbc_resource: str = None,
    ):
        # This parameter is required.
        self.company_id = company_id
        # This parameter is required.
        self.market_id = market_id
        # This parameter is required.
        self.market_resource = market_resource
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.pbc_resource = pbc_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.market_resource is not None:
            result['marketResource'] = self.market_resource

        if self.name is not None:
            result['name'] = self.name

        if self.pbc_resource is not None:
            result['pbcResource'] = self.pbc_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('marketResource') is not None:
            self.market_resource = m.get('marketResource')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pbcResource') is not None:
            self.pbc_resource = m.get('pbcResource')

        return self

