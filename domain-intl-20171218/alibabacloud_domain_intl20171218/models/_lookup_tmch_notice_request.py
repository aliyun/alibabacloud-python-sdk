# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LookupTmchNoticeRequest(DaraModel):
    def __init__(
        self,
        claim_key: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.claim_key = claim_key
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

