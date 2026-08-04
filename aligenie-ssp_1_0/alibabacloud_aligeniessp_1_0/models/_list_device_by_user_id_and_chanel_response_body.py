# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListDeviceByUserIdAndChanelResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListDeviceByUserIdAndChanelResponseBodyResult] = None,
    ):
        # The returned error code. The value 200 indicates that the call succeeded.
        self.code = code
        # Return Result of invoking this API.
        self.message = message
        # Request ID
        self.request_id = request_id
        # List of information
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDeviceByUserIdAndChanelResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDeviceByUserIdAndChanelResponseBodyResult(DaraModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[main_models.ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds] = None,
    ):
        # The openId corresponding to the Device Information.
        self.device_open_id = device_open_id
        # List of information
        self.device_union_ids = device_union_ids

    def validate(self):
        if self.device_union_ids:
            for v1 in self.device_union_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k1 in self.device_union_ids:
                result['DeviceUnionIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k1 in m.get('DeviceUnionIds'):
                temp_model = main_models.ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k1))

        return self

class ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds(DaraModel):
    def __init__(
        self,
        device_union_id: str = None,
        organization_id: str = None,
    ):
        # The UnionId of the device.
        self.device_union_id = device_union_id
        # Organization ID.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

