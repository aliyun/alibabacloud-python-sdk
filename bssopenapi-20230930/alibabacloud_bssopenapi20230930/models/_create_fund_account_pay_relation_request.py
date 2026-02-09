# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateFundAccountPayRelationRequest(DaraModel):
    def __init__(
        self,
        ec_id_account_ids: List[main_models.CreateFundAccountPayRelationRequestEcIdAccountIds] = None,
        fund_account_id: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.ec_id_account_ids = ec_id_account_ids
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.CreateFundAccountPayRelationRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

class CreateFundAccountPayRelationRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # This parameter is required.
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

