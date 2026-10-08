# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveBatchTaskForGenerateDomainCertificateShrinkRequest(DaraModel):
    def __init__(
        self,
        domain_names_shrink: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_names_shrink = domain_names_shrink
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names_shrink is not None:
            result['DomainNames'] = self.domain_names_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names_shrink = m.get('DomainNames')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

