# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWhitelistSettingRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        lang: str = None,
        service_code: str = None,
        source_ip: str = None,
    ):
        # List of rule IDs to be deleted.
        # 
        # This parameter is required.
        self.ids = ids
        # Specify the language of the user information to be deleted. Values: -**zh**: Chinese. -**en**: English.
        self.lang = lang
        # ServiceCode for the real-person cloud product, only takes the value: **antcloudauth**.
        # 
        # This parameter is required.
        self.service_code = service_code
        # Set the source IP address of the visitor. Supports IP addresses in CIDR and IPv4 formats. Example: 10.0.3.0/24.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

