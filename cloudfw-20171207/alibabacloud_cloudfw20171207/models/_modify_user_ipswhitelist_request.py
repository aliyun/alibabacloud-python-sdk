# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserIPSWhitelistRequest(DaraModel):
    def __init__(
        self,
        direction: int = None,
        ip_version: str = None,
        lang: str = None,
        list_type: int = None,
        list_value: str = None,
        source_ip: str = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.ip_version = ip_version
        self.lang = lang
        self.list_type = list_type
        self.list_value = list_value
        self.source_ip = source_ip
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.list_value is not None:
            result['ListValue'] = self.list_value

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.white_type is not None:
            result['WhiteType'] = self.white_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')

        return self

