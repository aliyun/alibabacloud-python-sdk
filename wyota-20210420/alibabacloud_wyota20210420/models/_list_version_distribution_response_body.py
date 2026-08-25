# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class ListVersionDistributionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListVersionDistributionResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 is returned if the call is successful. An error code is returned if the call fails.
        self.code = code
        # The list of version distribution information.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. This parameter is empty if the call is successful.
        self.message = message
        # The request ID.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
                temp_model = main_models.ListVersionDistributionResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVersionDistributionResponseBodyData(DaraModel):
    def __init__(
        self,
        device_count: int = None,
        percentage: float = None,
        version: str = None,
    ):
        # The number of terminals corresponding to this version.
        self.device_count = device_count
        # The version percentage. Valid values: 0 to 1.
        self.percentage = percentage
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

