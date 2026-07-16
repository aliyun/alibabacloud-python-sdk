# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOpenSourcePermissionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        user_name: str = None,
        vhost: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The username.
        # 
        # This parameter is required.
        self.user_name = user_name
        # The vhost name.
        # 
        # This parameter is required.
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        return self

