# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyPersonasOsStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyPersonasOsStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Processing result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyPersonasOsStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyPersonasOsStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        all_device_cnt: int = None,
        device_android_cnt: int = None,
        device_android_rate: str = None,
        device_ios_cnt: int = None,
        device_ios_rate: str = None,
    ):
        # Total number of authenticated devices.
        self.all_device_cnt = all_device_cnt
        # Number of authenticated Android devices.
        self.device_android_cnt = device_android_cnt
        # Proportion of Android devices.
        self.device_android_rate = device_android_rate
        # Number of authenticated iOS devices.
        self.device_ios_cnt = device_ios_cnt
        # Proportion of iOS devices.
        self.device_ios_rate = device_ios_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_device_cnt is not None:
            result['AllDeviceCnt'] = self.all_device_cnt

        if self.device_android_cnt is not None:
            result['DeviceAndroidCnt'] = self.device_android_cnt

        if self.device_android_rate is not None:
            result['DeviceAndroidRate'] = self.device_android_rate

        if self.device_ios_cnt is not None:
            result['DeviceIosCnt'] = self.device_ios_cnt

        if self.device_ios_rate is not None:
            result['DeviceIosRate'] = self.device_ios_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDeviceCnt') is not None:
            self.all_device_cnt = m.get('AllDeviceCnt')

        if m.get('DeviceAndroidCnt') is not None:
            self.device_android_cnt = m.get('DeviceAndroidCnt')

        if m.get('DeviceAndroidRate') is not None:
            self.device_android_rate = m.get('DeviceAndroidRate')

        if m.get('DeviceIosCnt') is not None:
            self.device_ios_cnt = m.get('DeviceIosCnt')

        if m.get('DeviceIosRate') is not None:
            self.device_ios_rate = m.get('DeviceIosRate')

        return self

