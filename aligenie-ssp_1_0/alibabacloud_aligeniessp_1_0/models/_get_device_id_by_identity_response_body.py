# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetDeviceIdByIdentityResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetDeviceIdByIdentityResponseBodyResult = None,
    ):
        # The error code returned. A value of 200 indicates that the invocation succeeded.
        self.code = code
        # The return result of invoking this API.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Detailed information returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetDeviceIdByIdentityResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetDeviceIdByIdentityResponseBodyResult(DaraModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[main_models.GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds] = None,
    ):
        # The openId corresponding to the device.
        self.device_open_id = device_open_id
        # Organization ID and UnionId information corresponding to the device.
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
                temp_model = main_models.GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k1))

        return self

class GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds(DaraModel):
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

