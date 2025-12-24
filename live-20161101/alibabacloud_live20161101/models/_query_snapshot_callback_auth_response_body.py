# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySnapshotCallbackAuthResponseBody(DaraModel):
    def __init__(
        self,
        callback_auth_key: str = None,
        callback_req_auth: str = None,
        domain_name: str = None,
        request_id: str = None,
    ):
        # The callback authentication key.
        self.callback_auth_key = callback_auth_key
        # Indicates whether callback authentication is enabled. Valid values:
        # 
        # *   **yes**: Callback authentication is enabled.
        # *   **no**: Callback authentication is disabled.
        self.callback_req_auth = callback_req_auth
        # The main streaming domain.
        self.domain_name = domain_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_auth_key is not None:
            result['CallbackAuthKey'] = self.callback_auth_key

        if self.callback_req_auth is not None:
            result['CallbackReqAuth'] = self.callback_req_auth

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackAuthKey') is not None:
            self.callback_auth_key = m.get('CallbackAuthKey')

        if m.get('CallbackReqAuth') is not None:
            self.callback_req_auth = m.get('CallbackReqAuth')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

