# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserTmpIdentityForPartnerRequest(DaraModel):
    def __init__(
        self,
        auth_purpose: str = None,
        biz_id: str = None,
        extend: str = None,
        service_linked_role: str = None,
        user_id: str = None,
    ):
        self.auth_purpose = auth_purpose
        self.biz_id = biz_id
        self.extend = extend
        self.service_linked_role = service_linked_role
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_purpose is not None:
            result['AuthPurpose'] = self.auth_purpose

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPurpose') is not None:
            self.auth_purpose = m.get('AuthPurpose')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

