# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        deletion_protection: bool = None,
        host_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        password: str = None,
        user_data: str = None,
    ):
        self.deletion_protection = deletion_protection
        # The hostname of the ECS instance. The hostname must be 2 to 64 characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). The hostname cannot contain consecutive periods (.) or hyphens (-), and cannot start or end with a period (.) or a hyphen (-).
        self.host_name = host_name
        # The ID of the instance to modify. Only a single instance is supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        self.instance_name = instance_name
        # The password of the instance.
        self.password = password
        # The instance user data, which must be Base64-encoded. The size of the raw data before encoding cannot exceed 16 KB. Do not pass in sensitive information such as passwords or private keys in plaintext. If you must pass in sensitive information, encode it before Base64-encoding it, and decode it in the same way inside the instance.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.password is not None:
            result['Password'] = self.password

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

