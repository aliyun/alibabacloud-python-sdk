# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDomainSpecialBizCredentialsRequest(DaraModel):
    def __init__(
        self,
        biz_id: int = None,
        credentials: str = None,
        extend: str = None,
        user_client_ip: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The certificate information.
        self.credentials = credentials
        # The extended information.
        self.extend = extend
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.credentials is not None:
            result['Credentials'] = self.credentials

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Credentials') is not None:
            self.credentials = m.get('Credentials')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

