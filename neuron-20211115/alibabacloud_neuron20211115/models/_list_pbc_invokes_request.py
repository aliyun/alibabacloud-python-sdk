# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPbcInvokesRequest(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        company_id: int = None,
        market_id: int = None,
        pbc_id: int = None,
    ):
        self.applicant = applicant
        self.company_id = company_id
        self.market_id = market_id
        self.pbc_id = pbc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        return self

