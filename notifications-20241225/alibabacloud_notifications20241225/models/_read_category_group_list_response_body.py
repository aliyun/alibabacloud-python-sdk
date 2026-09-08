# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadCategoryGroupListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadCategoryGroupListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned by the system. For more information about error codes, see Error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The message returned when the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. true: The call was successful. false: The call failed.
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
                temp_model = main_models.ReadCategoryGroupListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadCategoryGroupListResponseBodyData(DaraModel):
    def __init__(
        self,
        group_code: str = None,
        group_name: str = None,
    ):
        # The category group code.
        self.group_code = group_code
        # The group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

