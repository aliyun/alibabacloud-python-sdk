# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadNumGroupTotalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadNumGroupTotalResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned when the call fails. For more information, see Error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The error message returned when the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true and false. true: The call was successful. false: The call failed.
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
                temp_model = main_models.ReadNumGroupTotalResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadNumGroupTotalResponseBodyData(DaraModel):
    def __init__(
        self,
        group_code: str = None,
        id: int = None,
        read_count: int = None,
        total_count: int = None,
        un_read_count: int = None,
    ):
        # The group code.
        self.group_code = group_code
        # The message category ID.
        self.id = id
        # The number of read messages under the category.
        self.read_count = read_count
        # The total number of messages under the category.
        self.total_count = total_count
        # The number of unread messages under the category.
        self.un_read_count = un_read_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.id is not None:
            result['Id'] = self.id

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.un_read_count is not None:
            result['UnReadCount'] = self.un_read_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UnReadCount') is not None:
            self.un_read_count = m.get('UnReadCount')

        return self

