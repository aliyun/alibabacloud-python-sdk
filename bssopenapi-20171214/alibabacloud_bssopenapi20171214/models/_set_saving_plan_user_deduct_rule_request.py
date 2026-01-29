# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class SetSavingPlanUserDeductRuleRequest(DaraModel):
    def __init__(
        self,
        ec_id_account_ids: List[main_models.SetSavingPlanUserDeductRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
        spn_instance_code: str = None,
        user_deduct_rules: List[main_models.SetSavingPlanUserDeductRuleRequestUserDeductRules] = None,
    ):
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.spn_instance_code = spn_instance_code
        self.user_deduct_rules = user_deduct_rules

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()
        if self.user_deduct_rules:
            for v1 in self.user_deduct_rules:
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

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code

        result['UserDeductRules'] = []
        if self.user_deduct_rules is not None:
            for k1 in self.user_deduct_rules:
                result['UserDeductRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.SetSavingPlanUserDeductRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')

        self.user_deduct_rules = []
        if m.get('UserDeductRules') is not None:
            for k1 in m.get('UserDeductRules'):
                temp_model = main_models.SetSavingPlanUserDeductRuleRequestUserDeductRules()
                self.user_deduct_rules.append(temp_model.from_map(k1))

        return self

class SetSavingPlanUserDeductRuleRequestUserDeductRules(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        module_code: str = None,
        skip_deduct: bool = None,
    ):
        self.commodity_code = commodity_code
        self.module_code = module_code
        self.skip_deduct = skip_deduct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.skip_deduct is not None:
            result['SkipDeduct'] = self.skip_deduct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('SkipDeduct') is not None:
            self.skip_deduct = m.get('SkipDeduct')

        return self

class SetSavingPlanUserDeductRuleRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
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

