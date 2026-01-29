# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class ModifyCostUnitResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ModifyCostUnitResponseBodyData] = None,
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
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ModifyCostUnitResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyCostUnitResponseBodyData(DaraModel):
    def __init__(
        self,
        is_success: bool = None,
        owner_uid: int = None,
        unit_id: int = None,
    ):
        # Indicates whether the cost center was modified.
        self.is_success = is_success
        # The user ID of the cost center owner.
        self.owner_uid = owner_uid
        # The ID of the cost center.
        self.unit_id = unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        return self

