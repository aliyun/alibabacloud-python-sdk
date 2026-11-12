# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstancePasswordsSettingResponseBody(DaraModel):
    def __init__(
        self,
        instance_password_setting: bool = None,
        request_id: str = None,
        vnc_password_setting: bool = None,
    ):
        # Indicates whether a logon password is set for the simple application server.
        self.instance_password_setting = instance_password_setting
        # The request ID.
        self.request_id = request_id
        # Indicates whether a VNC connection password is set for the simple application server.
        self.vnc_password_setting = vnc_password_setting

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_password_setting is not None:
            result['InstancePasswordSetting'] = self.instance_password_setting

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vnc_password_setting is not None:
            result['VncPasswordSetting'] = self.vnc_password_setting

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstancePasswordSetting') is not None:
            self.instance_password_setting = m.get('InstancePasswordSetting')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VncPasswordSetting') is not None:
            self.vnc_password_setting = m.get('VncPasswordSetting')

        return self

