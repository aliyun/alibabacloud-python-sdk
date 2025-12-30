# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckZoneNameRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        zone_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The name of the zone. This parameter is required.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

