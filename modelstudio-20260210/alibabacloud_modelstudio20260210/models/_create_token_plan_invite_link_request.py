# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTokenPlanInviteLinkRequest(DaraModel):
    def __init__(
        self,
        expire_type: str = None,
        sso_source: str = None,
    ):
        # The expiration period. Default value: DAYS_7. Valid values:
        # 
        # - DAYS_7
        # - DAYS_30
        # - MONTHS_6
        # - YEAR_1
        self.expire_type = expire_type
        # The SSO logon method bound to the invitation link. Valid values:
        # 
        # - SAML
        # - DINGTALK
        # 
        # This parameter is required.
        self.sso_source = sso_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_type is not None:
            result['ExpireType'] = self.expire_type

        if self.sso_source is not None:
            result['SsoSource'] = self.sso_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireType') is not None:
            self.expire_type = m.get('ExpireType')

        if m.get('SsoSource') is not None:
            self.sso_source = m.get('SsoSource')

        return self

