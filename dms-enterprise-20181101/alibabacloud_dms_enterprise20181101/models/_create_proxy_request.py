# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProxyRequest(DaraModel):
    def __init__(
        self,
        instance_id: int = None,
        password: str = None,
        tid: int = None,
        username: str = None,
    ):
        # The ID of the database instance. You can call the [ListInstances](https://www.alibabacloud.com/help/en/data-management-service/latest/listinstances) or [GetInstance](https://www.alibabacloud.com/help/en/data-management-service/latest/getinstance) operation to query the database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The password of the database account.
        # 
        # This parameter is required.
        self.password = password
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://www.alibabacloud.com/help/en/data-management-service/latest/getuseractivetenant) operation to query the tenant ID.
        self.tid = tid
        # The username of the database account.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

