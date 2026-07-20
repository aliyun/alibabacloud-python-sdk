# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class IntlFlightReShopCreateHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_corp_token: str = None,
    ):
        self.common_headers = common_headers
        # The enterprise access token.
        # 
        # - When calling this operation over HTTP, this parameter is required and must be appended to the request URL. For more information about how to obtain the token, see [Enterprise access token](https://openapi.alibtrip.com/doc/toDocDetail?spm=openapi-amp.newDocPublishment.0.0.5e2a281frQyDQ8&docId=3769985).
        # - When appending the token, use crop_token=value instead.
        self.x_acs_btrip_corp_token = x_acs_btrip_corp_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_acs_btrip_corp_token is not None:
            result['x-acs-btrip-corp-token'] = self.x_acs_btrip_corp_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('x-acs-btrip-corp-token') is not None:
            self.x_acs_btrip_corp_token = m.get('x-acs-btrip-corp-token')

        return self

