# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateCostCenterResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_dto_list: List[main_models.CreateCostCenterResponseBodyCostCenterDtoList] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.cost_center_dto_list = cost_center_dto_list
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        if self.cost_center_dto_list:
            for v1 in self.cost_center_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CostCenterDtoList'] = []
        if self.cost_center_dto_list is not None:
            for k1 in self.cost_center_dto_list:
                result['CostCenterDtoList'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_dto_list = []
        if m.get('CostCenterDtoList') is not None:
            for k1 in m.get('CostCenterDtoList'):
                temp_model = main_models.CreateCostCenterResponseBodyCostCenterDtoList()
                self.cost_center_dto_list.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCostCenterResponseBodyCostCenterDtoList(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id

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

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        return self

