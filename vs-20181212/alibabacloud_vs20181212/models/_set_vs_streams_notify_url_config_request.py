# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVsStreamsNotifyUrlConfigRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_type: str = None,
        domain_name: str = None,
        notify_url: str = None,
        owner_id: int = None,
    ):
        self.auth_key = auth_key
        self.auth_type = auth_type
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.notify_url = notify_url
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

