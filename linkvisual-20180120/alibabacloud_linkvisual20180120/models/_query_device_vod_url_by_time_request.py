# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDeviceVodUrlByTimeRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        enable_stun: bool = None,
        encrypt_type: int = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        play_un_limited: bool = None,
        product_key: str = None,
        scheme: str = None,
        seek_time: int = None,
        should_encrypt: bool = None,
        url_valid_duration: int = None,
    ):
        # The recording start time. The value must be a 10-digit UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The DeviceName of the IPC device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        self.enable_stun = enable_stun
        # The encryption type. Only I-frame encryption is supported. Set the value to 0.
        self.encrypt_type = encrypt_type
        # The recording end time. The value must be a 10-digit UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the IPC device. The ID is issued by IoT Platform and uniquely identifies the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** uniquely identifies the device and has a one-to-one mapping with the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If the instance has an ID, you must specify this ID. Otherwise, the call fails.
        # - If the instance does not have an <props="intl"><ph>**Instance Overview** page or </ph>ID, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # Specifies whether the playback URL can be used an unlimited number of times. Valid values:
        # 
        # - **true**: The URL can be used an unlimited number of times within 10 seconds.
        # - **false**: The URL can be used only once. This is the default value.
        self.play_un_limited = play_un_limited
        # The ProductKey of the product to which the IPC device belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The protocol type. Valid values:
        # - **rtmp**: RTMP.
        # - **flv**: HTTP-FLV.
        # - **hls**: HLS.
        #  > For more information about the limits of HLS, see [Cloud development](https://help.aliyun.com/document_detail/208584.html).
        self.scheme = scheme
        # The offset relative to the recording start time specified by **BeginTime**. Unit: seconds. Default value: 0.
        self.seek_time = seek_time
        # Specifies whether to encrypt the stream. Valid values:
        # - **true**: Encrypts the stream.
        # - **false**: Does not encrypt the stream. This is the default value.
        self.should_encrypt = should_encrypt
        # The validity period of the URL. Valid values: 10 to 14400. Unit: seconds. Default value: 10.
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time

        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt

        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')

        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')

        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')

        return self

