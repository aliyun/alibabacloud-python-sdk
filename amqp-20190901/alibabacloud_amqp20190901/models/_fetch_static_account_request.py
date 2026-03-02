# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FetchStaticAccountRequest(DaraModel):
    def __init__(
        self,
        account_access_key: str = None,
        console_session_id: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        remark: str = None,
        skey: str = None,
        secret_sign: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.account_access_key = account_access_key
        self.console_session_id = console_session_id
        # This parameter is required.
        self.create_time_stamp = create_time_stamp
        # This parameter is required.
        self.instance_id = instance_id
        self.remark = remark
        # This parameter is required.
        self.skey = skey
        # This parameter is required.
        self.secret_sign = secret_sign
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_access_key is not None:
            result['AccountAccessKey'] = self.account_access_key

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.skey is not None:
            result['SKey'] = self.skey

        if self.secret_sign is not None:
            result['SecretSign'] = self.secret_sign

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAccessKey') is not None:
            self.account_access_key = m.get('AccountAccessKey')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SKey') is not None:
            self.skey = m.get('SKey')

        if m.get('SecretSign') is not None:
            self.secret_sign = m.get('SecretSign')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

