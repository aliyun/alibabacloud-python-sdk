# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class SubmitSlaCouponApplyRequest(DaraModel):
    def __init__(
        self,
        damaged_ids: List[str] = None,
        ec_id_account_ids: List[main_models.SubmitSlaCouponApplyRequestEcIdAccountIds] = None,
        month: int = None,
        nbid: str = None,
    ):
        # The IDs of the damaged records. This parameter is optional.
        self.damaged_ids = damaged_ids
        # The list of enterprises and accounts. If this parameter is left empty, the current account is queried.
        self.ec_id_account_ids = ec_id_account_ids
        # The claim month. This parameter is required. Format: yyyyMM.
        # 
        # This parameter is required.
        self.month = month
        # The primary marketplace ID. If this parameter is left empty, the marketplace ID of the current user is used by default.
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
        if self.damaged_ids is not None:
            result['DamagedIds'] = self.damaged_ids

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.month is not None:
            result['Month'] = self.month

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DamagedIds') is not None:
            self.damaged_ids = m.get('DamagedIds')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.SubmitSlaCouponApplyRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

class SubmitSlaCouponApplyRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of accounts to access. If this parameter is left empty, all accounts under the current entity ID are selected.
        self.account_ids = account_ids
        # The enterprise entity ID.
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

