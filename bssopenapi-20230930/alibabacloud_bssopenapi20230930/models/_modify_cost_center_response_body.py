# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyCostCenterResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_operate_dto: List[main_models.ModifyCostCenterResponseBodyCostCenterOperateDto] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.cost_center_operate_dto = cost_center_operate_dto
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        if self.cost_center_operate_dto:
            for v1 in self.cost_center_operate_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CostCenterOperateDto'] = []
        if self.cost_center_operate_dto is not None:
            for k1 in self.cost_center_operate_dto:
                result['CostCenterOperateDto'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_operate_dto = []
        if m.get('CostCenterOperateDto') is not None:
            for k1 in m.get('CostCenterOperateDto'):
                temp_model = main_models.ModifyCostCenterResponseBodyCostCenterOperateDto()
                self.cost_center_operate_dto.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyCostCenterResponseBodyCostCenterOperateDto(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        is_success: bool = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.is_success = is_success
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

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        return self

