# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class SaveCostCenterShareRuleRequest(DaraModel):
    def __init__(
        self,
        create_share_rule_list: List[main_models.SaveCostCenterShareRuleRequestCreateShareRuleList] = None,
        modify_share_rule_list: List[main_models.SaveCostCenterShareRuleRequestModifyShareRuleList] = None,
        nbid: str = None,
        owner_account_id: int = None,
        remove_share_rule_list: List[int] = None,
    ):
        self.create_share_rule_list = create_share_rule_list
        self.modify_share_rule_list = modify_share_rule_list
        self.nbid = nbid
        self.owner_account_id = owner_account_id
        self.remove_share_rule_list = remove_share_rule_list

    def validate(self):
        if self.create_share_rule_list:
            for v1 in self.create_share_rule_list:
                 if v1:
                    v1.validate()
        if self.modify_share_rule_list:
            for v1 in self.modify_share_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreateShareRuleList'] = []
        if self.create_share_rule_list is not None:
            for k1 in self.create_share_rule_list:
                result['CreateShareRuleList'].append(k1.to_map() if k1 else None)

        result['ModifyShareRuleList'] = []
        if self.modify_share_rule_list is not None:
            for k1 in self.modify_share_rule_list:
                result['ModifyShareRuleList'].append(k1.to_map() if k1 else None)

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.remove_share_rule_list is not None:
            result['RemoveShareRuleList'] = self.remove_share_rule_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_share_rule_list = []
        if m.get('CreateShareRuleList') is not None:
            for k1 in m.get('CreateShareRuleList'):
                temp_model = main_models.SaveCostCenterShareRuleRequestCreateShareRuleList()
                self.create_share_rule_list.append(temp_model.from_map(k1))

        self.modify_share_rule_list = []
        if m.get('ModifyShareRuleList') is not None:
            for k1 in m.get('ModifyShareRuleList'):
                temp_model = main_models.SaveCostCenterShareRuleRequestModifyShareRuleList()
                self.modify_share_rule_list.append(temp_model.from_map(k1))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('RemoveShareRuleList') is not None:
            self.remove_share_rule_list = m.get('RemoveShareRuleList')

        return self

class SaveCostCenterShareRuleRequestModifyShareRuleList(DaraModel):
    def __init__(
        self,
        from_cost_center_list: List[int] = None,
        share_ratio_list: List[float] = None,
        share_rule_id: int = None,
        share_rule_name: str = None,
        share_type: str = None,
        to_cost_center_list: List[int] = None,
    ):
        self.from_cost_center_list = from_cost_center_list
        self.share_ratio_list = share_ratio_list
        # This parameter is required.
        self.share_rule_id = share_rule_id
        self.share_rule_name = share_rule_name
        # This parameter is required.
        self.share_type = share_type
        self.to_cost_center_list = to_cost_center_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_cost_center_list is not None:
            result['FromCostCenterList'] = self.from_cost_center_list

        if self.share_ratio_list is not None:
            result['ShareRatioList'] = self.share_ratio_list

        if self.share_rule_id is not None:
            result['ShareRuleId'] = self.share_rule_id

        if self.share_rule_name is not None:
            result['ShareRuleName'] = self.share_rule_name

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.to_cost_center_list is not None:
            result['ToCostCenterList'] = self.to_cost_center_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterList') is not None:
            self.from_cost_center_list = m.get('FromCostCenterList')

        if m.get('ShareRatioList') is not None:
            self.share_ratio_list = m.get('ShareRatioList')

        if m.get('ShareRuleId') is not None:
            self.share_rule_id = m.get('ShareRuleId')

        if m.get('ShareRuleName') is not None:
            self.share_rule_name = m.get('ShareRuleName')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('ToCostCenterList') is not None:
            self.to_cost_center_list = m.get('ToCostCenterList')

        return self

class SaveCostCenterShareRuleRequestCreateShareRuleList(DaraModel):
    def __init__(
        self,
        from_cost_center_list: List[int] = None,
        share_ratio_list: List[float] = None,
        share_rule_name: str = None,
        share_type: str = None,
        to_cost_center_list: List[int] = None,
    ):
        self.from_cost_center_list = from_cost_center_list
        self.share_ratio_list = share_ratio_list
        self.share_rule_name = share_rule_name
        # This parameter is required.
        self.share_type = share_type
        self.to_cost_center_list = to_cost_center_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_cost_center_list is not None:
            result['FromCostCenterList'] = self.from_cost_center_list

        if self.share_ratio_list is not None:
            result['ShareRatioList'] = self.share_ratio_list

        if self.share_rule_name is not None:
            result['ShareRuleName'] = self.share_rule_name

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.to_cost_center_list is not None:
            result['ToCostCenterList'] = self.to_cost_center_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterList') is not None:
            self.from_cost_center_list = m.get('FromCostCenterList')

        if m.get('ShareRatioList') is not None:
            self.share_ratio_list = m.get('ShareRatioList')

        if m.get('ShareRuleName') is not None:
            self.share_rule_name = m.get('ShareRuleName')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('ToCostCenterList') is not None:
            self.to_cost_center_list = m.get('ToCostCenterList')

        return self

