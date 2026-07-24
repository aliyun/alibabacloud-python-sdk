# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class TicketingCheckHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_airticket_access_token: str = None,
        x_acs_airticket_language: str = None,
    ):
        self.common_headers = common_headers
        # access_token.
        # 
        # This parameter is required.
        self.x_acs_airticket_access_token = x_acs_airticket_access_token
        # The language. Defaults to the buyer account configuration.
        self.x_acs_airticket_language = x_acs_airticket_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token

        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')

        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')

        return self

