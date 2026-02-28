# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterDevicesRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
        password: str = None,
        user_id_list_json: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.password = password
        self.user_id_list_json = user_id_list_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.user_id_list_json is not None:
            result['UserIdListJson'] = self.user_id_list_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserIdListJson') is not None:
            self.user_id_list_json = m.get('UserIdListJson')

        return self

