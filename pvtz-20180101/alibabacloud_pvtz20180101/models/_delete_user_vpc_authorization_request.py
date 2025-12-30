# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserVpcAuthorizationRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_user_id: int = None,
    ):
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   NORMAL: cloud service-related authorization
        # 
        # Default value: NORMAL.
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        return self

