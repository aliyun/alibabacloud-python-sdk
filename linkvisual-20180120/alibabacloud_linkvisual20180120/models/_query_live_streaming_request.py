# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLiveStreamingRequest(DaraModel):
    def __init__(
        self,
        cache_duration: int = None,
        device_name: str = None,
        enable_stun: bool = None,
        encrypt_type: int = None,
        force_iframe: bool = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        play_un_limited: bool = None,
        product_key: str = None,
        scheme: str = None,
        should_encrypt: bool = None,
        stream_type: int = None,
        url_valid_duration: int = None,
    ):
        # The duration of video cached data. Valid values: 0 to 10000. Unit: milliseconds. Default value: 0.
        self.cache_duration = cache_duration
        # The DeviceName of the IPC device. You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        self.enable_stun = enable_stun
        # The encryption type. Valid values:
        # - **1** (default): Keyframe encryption.
        # - **0**: No encryption.
        self.encrypt_type = encrypt_type
        # Specifies whether to send a force I-frame command to the device. Valid values:
        # 
        # - **true**: Sent.
        # - **false** (default): Not sent.
        self.force_iframe = force_iframe
        # The IotId of the IPC device. The IotId is the globally unique identifier that is issued by IoT Platform to the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the globally unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If an ID value is displayed, you must specify this parameter. Otherwise, the call fails.
        # - If the <props="intl"><ph>**Instance Overview** page or </ph>ID value is not displayed, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # Specifies whether the playback URL can be used for an unlimited number of times within the validity period. Valid values:
        # - **true**: Allowed.
        # - **false** (default): Not allowed.
        self.play_un_limited = play_un_limited
        # The ProductKey of the product to which the IPC device belongs. You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The playback protocol type. Valid values:
        # 
        # - **rtmp** (default): RTMP.
        # - **hls**: HLS.
        # - **flv**: HTTP-FLV.
        self.scheme = scheme
        # Specifies whether to encrypt the stream. Valid values:
        # 
        # - **true**: Encrypted.
        # - **false** (default): Not encrypted.
        self.should_encrypt = should_encrypt
        # The stream type. Valid values:
        # - **0** (default): Main stream.
        # - **1**: Sub stream.
        self.stream_type = stream_type
        # The validity period of the URL. Valid values: 10 to 14400. Unit: seconds. Default value: 10.
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_duration is not None:
            result['CacheDuration'] = self.cache_duration

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.force_iframe is not None:
            result['ForceIFrame'] = self.force_iframe

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

        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheDuration') is not None:
            self.cache_duration = m.get('CacheDuration')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('ForceIFrame') is not None:
            self.force_iframe = m.get('ForceIFrame')

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

        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')

        return self

