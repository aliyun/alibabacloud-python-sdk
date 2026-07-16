# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAppLlmApiKeyForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        client_token: str = None,
        description: str = None,
        ip_white_list: List[str] = None,
    ):
        # Business ID of the application instance
        self.biz_id = biz_id
        # Idempotent token (reserved)
        self.client_token = client_token
        # Description of the API key usage
        self.description = description
        # Caller-defined IP address whitelist (the backend appends the system default IP segment)
        self.ip_white_list = ip_white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')

        return self

