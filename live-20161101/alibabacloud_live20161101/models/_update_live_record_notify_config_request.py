# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveRecordNotifyConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        need_status_notify: bool = None,
        notify_auth_key: str = None,
        notify_req_auth: bool = None,
        notify_url: str = None,
        on_demand_url: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to enable callbacks for recording status. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.need_status_notify = need_status_notify
        self.notify_auth_key = notify_auth_key
        self.notify_req_auth = notify_req_auth
        # The callback URL that is used to receive notifications about recording events and status.
        # 
        # > 
        # 
        # *   The URL must start with `http://` or `https://`.
        # 
        # *   You must use URLEncoder for encoding. This way, the system can identify Chinese characters, spaces, and special characters.
        # 
        # This parameter is required.
        self.notify_url = notify_url
        # The callback URL for on-demand recordings.
        # 
        # > 
        # 
        # *   The URL must start with `http://` or `https://`.
        # 
        # *   You must use URLEncoder for encoding. This way, the system can identify Chinese characters, spaces, and special characters.
        self.on_demand_url = on_demand_url
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.need_status_notify is not None:
            result['NeedStatusNotify'] = self.need_status_notify

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_req_auth is not None:
            result['NotifyReqAuth'] = self.notify_req_auth

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.on_demand_url is not None:
            result['OnDemandUrl'] = self.on_demand_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NeedStatusNotify') is not None:
            self.need_status_notify = m.get('NeedStatusNotify')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyReqAuth') is not None:
            self.notify_req_auth = m.get('NotifyReqAuth')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OnDemandUrl') is not None:
            self.on_demand_url = m.get('OnDemandUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

