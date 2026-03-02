# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcApiSchemaCreateCmd(DaraModel):
    def __init__(
        self,
        api_schema: str = None,
        company_id: int = None,
        market_id: int = None,
        pbc_version_id: int = None,
    ):
        self.api_schema = api_schema
        self.company_id = company_id
        self.market_id = market_id
        self.pbc_version_id = pbc_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_schema is not None:
            result['apiSchema'] = self.api_schema

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiSchema') is not None:
            self.api_schema = m.get('apiSchema')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        return self

