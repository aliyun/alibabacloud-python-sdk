# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class CreateCostUnitResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCostUnitResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateCostUnitResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateCostUnitResponseBodyData(DaraModel):
    def __init__(
        self,
        cost_unit_dto_list: List[main_models.CreateCostUnitResponseBodyDataCostUnitDtoList] = None,
    ):
        # The list of cost center entities.
        self.cost_unit_dto_list = cost_unit_dto_list

    def validate(self):
        if self.cost_unit_dto_list:
            for v1 in self.cost_unit_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k1 in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_unit_dto_list = []
        if m.get('CostUnitDtoList') is not None:
            for k1 in m.get('CostUnitDtoList'):
                temp_model = main_models.CreateCostUnitResponseBodyDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k1))

        return self

class CreateCostUnitResponseBodyDataCostUnitDtoList(DaraModel):
    def __init__(
        self,
        owner_uid: int = None,
        parent_unit_id: int = None,
        unit_id: int = None,
        unit_name: str = None,
    ):
        # The user ID of the owner of the cost center.
        self.owner_uid = owner_uid
        # The ID of the parent cost center. A value of -1 indicates the root cost center.
        self.parent_unit_id = parent_unit_id
        # The ID of the cost center.
        self.unit_id = unit_id
        # The name of the cost center.
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id

        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        if self.unit_name is not None:
            result['UnitName'] = self.unit_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')

        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')

        return self

