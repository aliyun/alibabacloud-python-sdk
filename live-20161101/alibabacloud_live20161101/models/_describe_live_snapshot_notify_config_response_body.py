# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveSnapshotNotifyConfigResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        notify_auth_key: str = None,
        notify_req_auth: str = None,
        notify_url: str = None,
        request_id: str = None,
    ):
        # The main streaming domain.
        self.domain_name = domain_name
        # The callback authentication key.
        self.notify_auth_key = notify_auth_key
        # Indicates whether callback authentication is enabled. Valid values:
        # 
        # *   **yes**: Callback authentication is enabled.
        # *   **no**: Callback authentication is disabled.
        self.notify_req_auth = notify_req_auth
        # The callback URL.
        self.notify_url = notify_url
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

