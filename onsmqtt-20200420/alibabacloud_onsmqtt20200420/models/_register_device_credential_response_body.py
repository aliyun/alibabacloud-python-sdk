# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class RegisterDeviceCredentialResponseBody(DaraModel):
    def __init__(
        self,
        device_credential: main_models.RegisterDeviceCredentialResponseBodyDeviceCredential = None,
        request_id: str = None,
    ):
        # The access credential of the device.
        self.device_credential = device_credential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = main_models.RegisterDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m.get('DeviceCredential'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RegisterDeviceCredentialResponseBodyDeviceCredential(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        create_time: int = None,
        device_access_key_id: str = None,
        device_access_key_secret: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The client ID of the device.
        self.client_id = client_id
        # The timestamp that indicates when the access credential of the device was created. Unit: milliseconds.
        self.create_time = create_time
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id
        # The timestamp that indicates when the access credential of the device was last updated. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id

        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')

        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

