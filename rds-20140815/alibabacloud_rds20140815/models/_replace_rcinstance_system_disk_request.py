# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceRCInstanceSystemDiskRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        instance_id: str = None,
        is_local_disk: bool = None,
        key_pair_name: str = None,
        password: str = None,
        region_id: str = None,
    ):
        # The image ID that is used when you reinstall the OS.
        self.image_id = image_id
        # The instance ID.
        self.instance_id = instance_id
        # The reserved parameter. This parameter is not supported.
        self.is_local_disk = is_local_disk
        # The name of the new key pair. If you do not specify this parameter, you must reset the key pair after the OS is reinstalled.
        self.key_pair_name = key_pair_name
        # The new logon password of the RDS Custom instance. If you do not specify this parameter, you must reset the logon password after the OS is reinstalled.
        # 
        # *   The value must be 8 to 30 characters in length.
        # *   The value must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ( ) \\` ~ ! @ # $ % ^ & \\* - _ + =
        self.password = password
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_local_disk is not None:
            result['IsLocalDisk'] = self.is_local_disk

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsLocalDisk') is not None:
            self.is_local_disk = m.get('IsLocalDisk')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

