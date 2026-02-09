# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class PushQueryDeviceStateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PushQueryDeviceStateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
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
            temp_model = main_models.PushQueryDeviceStateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PushQueryDeviceStateResponseBodyData(DaraModel):
    def __init__(
        self,
        delivery_token: str = None,
        device_id: str = None,
        manufacturer: str = None,
        platform: str = None,
        statue: str = None,
        third_token: str = None,
        user_id: str = None,
    ):
        self.delivery_token = delivery_token
        self.device_id = device_id
        self.manufacturer = manufacturer
        self.platform = platform
        self.statue = statue
        self.third_token = third_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.statue is not None:
            result['Statue'] = self.statue

        if self.third_token is not None:
            result['ThirdToken'] = self.third_token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Statue') is not None:
            self.statue = m.get('Statue')

        if m.get('ThirdToken') is not None:
            self.third_token = m.get('ThirdToken')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

