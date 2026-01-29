# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class AllocateCostUnitResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AllocateCostUnitResourceResponseBodyData = None,
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
        # Indicates whether the request was successful.
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
            temp_model = main_models.AllocateCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AllocateCostUnitResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        is_success: bool = None,
        to_unit_id: int = None,
        to_unit_user_id: int = None,
    ):
        # Indicates whether resources are allocated to the specified cost center. Valid values:
        # 
        # *   true: The resources are allocated to the specified cost center.
        # *   false: The resources fail to be allocated to the specified cost center.
        self.is_success = is_success
        # The ID of the destination cost center.
        self.to_unit_id = to_unit_id
        # The user ID of the owner of the destination cost center.
        self.to_unit_user_id = to_unit_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id

        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')

        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')

        return self

