# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryCostByCostCenterResponseBody(DaraModel):
    def __init__(
        self,
        consume_amount_list: List[main_models.QueryCostByCostCenterResponseBodyConsumeAmountList] = None,
        metadata: Any = None,
        request_id: str = None,
        total_amount: str = None,
    ):
        self.consume_amount_list = consume_amount_list
        self.metadata = metadata
        self.request_id = request_id
        self.total_amount = total_amount

    def validate(self):
        if self.consume_amount_list:
            for v1 in self.consume_amount_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumeAmountList'] = []
        if self.consume_amount_list is not None:
            for k1 in self.consume_amount_list:
                result['ConsumeAmountList'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consume_amount_list = []
        if m.get('ConsumeAmountList') is not None:
            for k1 in m.get('ConsumeAmountList'):
                temp_model = main_models.QueryCostByCostCenterResponseBodyConsumeAmountList()
                self.consume_amount_list.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        return self

class QueryCostByCostCenterResponseBodyConsumeAmountList(DaraModel):
    def __init__(
        self,
        allocated_amount: str = None,
        cost_center_code: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        direct_amount: str = None,
        level: int = None,
        owner_account_id: int = None,
        owner_account_name: str = None,
        parent_cost_center_id: int = None,
        pre_cost_center_id: int = None,
        total_allocated_amount: str = None,
        total_allocated_amount_percent: str = None,
    ):
        self.allocated_amount = allocated_amount
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.direct_amount = direct_amount
        self.level = level
        self.owner_account_id = owner_account_id
        self.owner_account_name = owner_account_name
        self.parent_cost_center_id = parent_cost_center_id
        self.pre_cost_center_id = pre_cost_center_id
        self.total_allocated_amount = total_allocated_amount
        self.total_allocated_amount_percent = total_allocated_amount_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_amount is not None:
            result['AllocatedAmount'] = self.allocated_amount

        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code

        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name

        if self.direct_amount is not None:
            result['DirectAmount'] = self.direct_amount

        if self.level is not None:
            result['Level'] = self.level

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        if self.pre_cost_center_id is not None:
            result['PreCostCenterId'] = self.pre_cost_center_id

        if self.total_allocated_amount is not None:
            result['TotalAllocatedAmount'] = self.total_allocated_amount

        if self.total_allocated_amount_percent is not None:
            result['TotalAllocatedAmountPercent'] = self.total_allocated_amount_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedAmount') is not None:
            self.allocated_amount = m.get('AllocatedAmount')

        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')

        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('DirectAmount') is not None:
            self.direct_amount = m.get('DirectAmount')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        if m.get('PreCostCenterId') is not None:
            self.pre_cost_center_id = m.get('PreCostCenterId')

        if m.get('TotalAllocatedAmount') is not None:
            self.total_allocated_amount = m.get('TotalAllocatedAmount')

        if m.get('TotalAllocatedAmountPercent') is not None:
            self.total_allocated_amount_percent = m.get('TotalAllocatedAmountPercent')

        return self

