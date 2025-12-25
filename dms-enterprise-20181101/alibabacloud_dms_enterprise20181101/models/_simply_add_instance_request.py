# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SimplyAddInstanceRequest(DaraModel):
    def __init__(
        self,
        database_password: str = None,
        database_user: str = None,
        host: str = None,
        instance_id: str = None,
        instance_region: str = None,
        port: int = None,
        real_login_user_uid: str = None,
    ):
        # This parameter is required.
        self.database_password = database_password
        # This parameter is required.
        self.database_user = database_user
        self.host = host
        self.instance_id = instance_id
        self.instance_region = instance_region
        self.port = port
        self.real_login_user_uid = real_login_user_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password

        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region

        if self.port is not None:
            result['Port'] = self.port

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')

        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        return self

