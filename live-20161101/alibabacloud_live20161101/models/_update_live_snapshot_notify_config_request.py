# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveSnapshotNotifyConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        notify_auth_key: str = None,
        notify_req_auth: str = None,
        notify_url: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The callback authentication key. The key can be 16 to 32 characters in length and can contain only letters and digits.
        # 
        # >  This parameter is required if you set the NotifyReqAuth parameter to **yes**.
        self.notify_auth_key = notify_auth_key
        # Specifies whether to enable callback authentication. Valid values:
        # 
        # *   **yes**: enables callback authentication
        # *   **no**: disables callback authentication
        # 
        # >  Default value: **no**. If you set this parameter to **yes**, the NotifyAuthKey parameter is required.
        self.notify_req_auth = notify_req_auth
        # The callback URL. Specify a valid URL that is up to 500 characters in length.
        self.notify_url = notify_url
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_req_auth is not None:
            result['NotifyReqAuth'] = self.notify_req_auth

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyReqAuth') is not None:
            self.notify_req_auth = m.get('NotifyReqAuth')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

