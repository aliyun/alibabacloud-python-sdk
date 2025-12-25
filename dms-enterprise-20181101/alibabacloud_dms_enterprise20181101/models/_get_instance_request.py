# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceRequest(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        real_login_user_uid: str = None,
        sid: str = None,
        tid: int = None,
    ):
        # The endpoint of the database instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) operation to obtain the endpoint.
        # 
        # This parameter is required.
        self.host = host
        # The port number that is used to connect to the database instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) operation to obtain the port number.
        # 
        # This parameter is required.
        self.port = port
        self.real_login_user_uid = real_login_user_uid
        # The system ID (SID) of the database instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) operation to obtain the SID.
        self.sid = sid
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

