# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppSeoStatusRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain: str = None,
        se_auth_info: str = None,
        se_type: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Domain Name
        self.domain = domain
        self.se_auth_info = se_auth_info
        # Search Engine Type
        self.se_type = se_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.se_auth_info is not None:
            result['SeAuthInfo'] = self.se_auth_info

        if self.se_type is not None:
            result['SeType'] = self.se_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('SeAuthInfo') is not None:
            self.se_auth_info = m.get('SeAuthInfo')

        if m.get('SeType') is not None:
            self.se_type = m.get('SeType')

        return self

