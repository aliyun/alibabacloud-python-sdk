# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFundAccountPayRelationShrinkRequest(DaraModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        fund_account_id: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

