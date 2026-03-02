# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcSchemaCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        id: int = None,
        market_id: int = None,
        pbc_name: str = None,
        pbc_version: str = None,
        schema: str = None,
    ):
        self.company_id = company_id
        self.id = id
        self.market_id = market_id
        self.pbc_name = pbc_name
        self.pbc_version = pbc_version
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.id is not None:
            result['id'] = self.id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.pbc_version is not None:
            result['pbcVersion'] = self.pbc_version

        if self.schema is not None:
            result['schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('pbcVersion') is not None:
            self.pbc_version = m.get('pbcVersion')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        return self

