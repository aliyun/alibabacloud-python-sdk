# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRtmpKeyRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key

        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time

        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key

        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')

        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')

        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')

        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')

        return self

