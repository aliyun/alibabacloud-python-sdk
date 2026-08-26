# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveStreamsNotifyUrlConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        exception_notify_url: str = None,
        notify_auth_key: str = None,
        notify_req_auth: str = None,
        notify_url: str = None,
        owner_id: int = None,
        switch_notify_url: str = None,
    ):
        # The ingest domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The callback URL for exception events.
        self.exception_notify_url = exception_notify_url
        # The authentication key.
        # 
        # > This parameter is required when the NotifyReqAuth request parameter is set to **yes**.
        # 
        # Value requirements:
        # 
        # - 16 to 64 characters in length.
        # 
        # - Supports uppercase letters, lowercase letters, and digits.
        self.notify_auth_key = notify_auth_key
        # Specifies whether to enable authentication. Valid values:
        # 
        # - **yes**: Enabled. If you set this parameter to **yes**, you must also set the NotifyAuthKey request parameter.
        # - **no**: Disabled.
        # 
        # > If this parameter is not specified, the default value is **no**.
        # 
        # For the authentication logic, see **Stream ingest callback authentication description** below.
        self.notify_req_auth = notify_req_auth
        # The URL to which live stream information is pushed.
        self.notify_url = notify_url
        self.owner_id = owner_id
        # The callback URL for stream switching information.
        self.switch_notify_url = switch_notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.exception_notify_url is not None:
            result['ExceptionNotifyUrl'] = self.exception_notify_url

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_req_auth is not None:
            result['NotifyReqAuth'] = self.notify_req_auth

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.switch_notify_url is not None:
            result['SwitchNotifyUrl'] = self.switch_notify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExceptionNotifyUrl') is not None:
            self.exception_notify_url = m.get('ExceptionNotifyUrl')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyReqAuth') is not None:
            self.notify_req_auth = m.get('NotifyReqAuth')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SwitchNotifyUrl') is not None:
            self.switch_notify_url = m.get('SwitchNotifyUrl')

        return self

