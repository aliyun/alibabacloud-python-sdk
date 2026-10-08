# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForDeletingDSRecordRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # Domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Key tag, used to identify DNSSEC records. It is an integer value less than 65536.
        # 
        # This parameter is required.
        self.key_tag = key_tag
        # Language of error messages returned by the API. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        # 
        # Default value: **en**.
        self.lang = lang
        # User IP address.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

