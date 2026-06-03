# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForModifyingDSRecordRequest(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.algorithm = algorithm
        # This parameter is required.
        self.digest = digest
        # This parameter is required.
        self.digest_type = digest_type
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.key_tag = key_tag
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.digest_type is not None:
            result['DigestType'] = self.digest_type

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
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

