# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        begin_day: str = None,
        biz_type: str = None,
        device_id: str = None,
        expired_day: str = None,
        request_id: str = None,
        user_device_id: str = None,
    ):
        # If the Duration in the request parameters is not empty, this field represents the start time of the authorization after the device validity period has been extended. One year of Duration is calculated as 365 days. Example: 20180101.
        self.begin_day = begin_day
        # Corresponds to the BizType in the request parameters.
        self.biz_type = biz_type
        # Corresponds to the DeviceId in the request parameters.
        self.device_id = device_id
        # If the Duration in the request parameters is not empty, this field represents the expiration time of the authorization after the device validity period has been extended. One year of Duration is calculated as 365 days. Example: 20180101.
        self.expired_day = expired_day
        # The ID of this request.
        self.request_id = request_id
        # Corresponds to the UserDeviceId in the request parameters.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')

        return self

