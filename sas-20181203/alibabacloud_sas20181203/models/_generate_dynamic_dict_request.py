# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDynamicDictRequest(DaraModel):
    def __init__(
        self,
        arg_keywords: str = None,
        domains: str = None,
        names: str = None,
        source_ip: str = None,
    ):
        # The keyword of the dictionary.
        self.arg_keywords = arg_keywords
        # The domain name for custom weak passwords.
        self.domains = domains
        # The company name for custom weak passwords.
        self.names = names
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg_keywords is not None:
            result['ArgKeywords'] = self.arg_keywords

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.names is not None:
            result['Names'] = self.names

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgKeywords') is not None:
            self.arg_keywords = m.get('ArgKeywords')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

