# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class BatchQueryVisionDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BatchQueryVisionDeviceInfoResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.BatchQueryVisionDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchQueryVisionDeviceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        device_info_list: List[main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList] = None,
    ):
        self.device_info_list = device_info_list

    def validate(self):
        if self.device_info_list:
            for v1 in self.device_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k1 in self.device_info_list:
                result['DeviceInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k1 in m.get('DeviceInfoList'):
                temp_model = main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k1))

        return self

class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList(DaraModel):
    def __init__(
        self,
        description: str = None,
        device_type: int = None,
        gb_device_info: main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo = None,
        iot_id: str = None,
        rtmp_device_info: main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo = None,
    ):
        self.description = description
        self.device_type = device_type
        self.gb_device_info = gb_device_info
        self.iot_id = iot_id
        self.rtmp_device_info = rtmp_device_info

    def validate(self):
        if self.gb_device_info:
            self.gb_device_info.validate()
        if self.rtmp_device_info:
            self.rtmp_device_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.gb_device_info is not None:
            result['GbDeviceInfo'] = self.gb_device_info.to_map()

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.rtmp_device_info is not None:
            result['RtmpDeviceInfo'] = self.rtmp_device_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('GbDeviceInfo') is not None:
            temp_model = main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo()
            self.gb_device_info = temp_model.from_map(m.get('GbDeviceInfo'))

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('RtmpDeviceInfo') is not None:
            temp_model = main_models.BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo()
            self.rtmp_device_info = temp_model.from_map(m.get('RtmpDeviceInfo'))

        return self

class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo(DaraModel):
    def __init__(
        self,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        push_url_sample: str = None,
        stream_name: str = None,
        stream_status: int = None,
    ):
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.push_url_sample = push_url_sample
        self.stream_name = stream_name
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key

        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time

        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key

        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time

        if self.push_url_sample is not None:
            result['PushUrlSample'] = self.push_url_sample

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')

        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')

        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')

        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')

        if m.get('PushUrlSample') is not None:
            self.push_url_sample = m.get('PushUrlSample')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')

        return self

class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo(DaraModel):
    def __init__(
        self,
        device_protocol: int = None,
        gb_id: str = None,
        net_protocol: int = None,
        nick_name: str = None,
        password: str = None,
        sub_product_key: str = None,
    ):
        self.device_protocol = device_protocol
        self.gb_id = gb_id
        self.net_protocol = net_protocol
        self.nick_name = nick_name
        self.password = password
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_protocol is not None:
            result['DeviceProtocol'] = self.device_protocol

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.net_protocol is not None:
            result['NetProtocol'] = self.net_protocol

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.password is not None:
            result['Password'] = self.password

        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceProtocol') is not None:
            self.device_protocol = m.get('DeviceProtocol')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('NetProtocol') is not None:
            self.net_protocol = m.get('NetProtocol')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')

        return self

