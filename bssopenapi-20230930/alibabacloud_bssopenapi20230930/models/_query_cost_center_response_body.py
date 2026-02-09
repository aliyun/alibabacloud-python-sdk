# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryCostCenterResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_dto_list: List[main_models.QueryCostCenterResponseBodyCostCenterDtoList] = None,
        current_page: int = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cost_center_dto_list = cost_center_dto_list
        self.current_page = current_page
        self.metadata = metadata
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_dto_list = []
        if m.get('CostCenterDtoList') is not None:
            for k1 in m.get('CostCenterDtoList'):
                temp_model = main_models.QueryCostCenterResponseBodyCostCenterDtoList()
                self.cost_center_dto_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryCostCenterResponseBodyCostCenterDtoList(DaraModel):
    def __init__(
        self,
        cost_center_code: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        level: int = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
        prev_cost_center_id: int = None,
    ):
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.level = level
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id
        self.prev_cost_center_id = prev_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code

        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name

        if self.level is not None:
            result['Level'] = self.level

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        if self.prev_cost_center_id is not None:
            result['PrevCostCenterId'] = self.prev_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')

        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        if m.get('PrevCostCenterId') is not None:
            self.prev_cost_center_id = m.get('PrevCostCenterId')

        return self

