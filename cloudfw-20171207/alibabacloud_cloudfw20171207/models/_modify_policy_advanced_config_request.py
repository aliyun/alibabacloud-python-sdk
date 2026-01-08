# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyPolicyAdvancedConfigRequest(DaraModel):
    def __init__(
        self,
        eips: List[str] = None,
        internet_switch: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The IP addresses. The versions of the IP addresses must be the same. You can specify a maximum of 100 IP addresses.
        self.eips = eips
        # Specifies whether to enable the strict mode for the access control policy. Valid values:
        # 
        # *   **on**: enables the strict mode.
        # *   **off**: disables the strict mode.
        # 
        # This parameter is required.
        self.internet_switch = internet_switch
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eips is not None:
            result['Eips'] = self.eips

        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eips') is not None:
            self.eips = m.get('Eips')

        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

