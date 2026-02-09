# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetSavingPlanUserDeductRuleRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids: List[main_models.GetSavingPlanUserDeductRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.GetSavingPlanUserDeductRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')

        return self

class GetSavingPlanUserDeductRuleRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
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

