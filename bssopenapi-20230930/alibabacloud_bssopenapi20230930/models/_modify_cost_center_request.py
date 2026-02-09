# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyCostCenterRequest(DaraModel):
    def __init__(
        self,
        cost_center_entity_list: List[main_models.ModifyCostCenterRequestCostCenterEntityList] = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list = cost_center_entity_list
        self.nbid = nbid

    def validate(self):
        if self.cost_center_entity_list:
            for v1 in self.cost_center_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CostCenterEntityList'] = []
        if self.cost_center_entity_list is not None:
            for k1 in self.cost_center_entity_list:
                result['CostCenterEntityList'].append(k1.to_map() if k1 else None)

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_entity_list = []
        if m.get('CostCenterEntityList') is not None:
            for k1 in m.get('CostCenterEntityList'):
                temp_model = main_models.ModifyCostCenterRequestCostCenterEntityList()
                self.cost_center_entity_list.append(temp_model.from_map(k1))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

class ModifyCostCenterRequestCostCenterEntityList(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        owner_account_id: int = None,
    ):
        # This parameter is required.
        self.cost_center_id = cost_center_id
        # This parameter is required.
        self.cost_center_name = cost_center_name
        # This parameter is required.
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        return self

