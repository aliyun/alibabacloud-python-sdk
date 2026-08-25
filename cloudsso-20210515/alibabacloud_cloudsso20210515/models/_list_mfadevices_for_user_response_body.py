# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListMFADevicesForUserResponseBody(DaraModel):
    def __init__(
        self,
        mfadevices: List[main_models.ListMFADevicesForUserResponseBodyMFADevices] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The MFA device list.
        self.mfadevices = mfadevices
        # The request ID.
        self.request_id = request_id
        # The total number of MFA devices.
        self.total_counts = total_counts

    def validate(self):
        if self.mfadevices:
            for v1 in self.mfadevices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MFADevices'] = []
        if self.mfadevices is not None:
            for k1 in self.mfadevices:
                result['MFADevices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mfadevices = []
        if m.get('MFADevices') is not None:
            for k1 in m.get('MFADevices'):
                temp_model = main_models.ListMFADevicesForUserResponseBodyMFADevices()
                self.mfadevices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListMFADevicesForUserResponseBodyMFADevices(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        effective_time: str = None,
        last_use_time: str = None,
        user_id: str = None,
    ):
        # The MFA device ID.
        self.device_id = device_id
        # The MFA device name.
        self.device_name = device_name
        # The MFA device type. Valid values:
        # - TOTP: a virtual MFA device based on the Time-based One-Time Password algorithm.
        # - CrossPlatformPasskey: a cross-platform passkey.
        # - PlatformPasskey: a platform built-in passkey.
        self.device_type = device_type
        # The effective period. The time is in UTC and follows the RFC 3339 format (YYYY-MM-DDTHH:mm:ssZ).
        self.effective_time = effective_time
        # The last time the MFA device was used.
        self.last_use_time = last_use_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.last_use_time is not None:
            result['LastUseTime'] = self.last_use_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('LastUseTime') is not None:
            self.last_use_time = m.get('LastUseTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

