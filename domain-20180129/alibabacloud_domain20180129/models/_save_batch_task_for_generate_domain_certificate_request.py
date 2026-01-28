# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveBatchTaskForGenerateDomainCertificateRequest(DaraModel):
    def __init__(
        self,
        domain_names: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # The domain names.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The language of the error message to return if the request fails. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

