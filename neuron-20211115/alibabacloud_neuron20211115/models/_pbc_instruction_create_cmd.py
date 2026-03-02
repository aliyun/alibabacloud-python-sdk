# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcInstructionCreateCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        document: str = None,
        id: int = None,
        market_id: int = None,
        pbc_version_id: int = None,
    ):
        self.company_id = company_id
        self.document = document
        self.id = id
        self.market_id = market_id
        self.pbc_version_id = pbc_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.document is not None:
            result['document'] = self.document

        if self.id is not None:
            result['id'] = self.id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        return self

