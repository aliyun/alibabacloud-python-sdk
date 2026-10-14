# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageAICLoginRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        instance_id: str = None,
        key_group: str = None,
        key_name: str = None,
    ):
        # The management action.
        # When this parameter is set to open, the AIC instance must be in the running state. You can call DescribeAICInstances to query the state.
        # 
        # This parameter is required.
        self.action_name = action_name
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The group of the public key.
        # When you set ActionName to open and use the public key to log on, you must first upload the public key by calling UploadAICPublicKey and provide the corresponding KeyName and KeyGroup.
        self.key_group = key_group
        # The name of the public key.
        # When you set ActionName to open and use the public key to log on, you must first upload the public key by calling UploadAICPublicKey and provide the corresponding KeyName and KeyGroup.
        self.key_name = key_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        return self

