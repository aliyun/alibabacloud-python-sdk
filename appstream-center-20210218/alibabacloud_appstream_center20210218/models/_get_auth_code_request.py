# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuthCodeRequest(DaraModel):
    def __init__(
        self,
        auto_create_user: bool = None,
        end_user_id: str = None,
        external_user_id: str = None,
        policy: str = None,
    ):
        self.auto_create_user = auto_create_user
        self.end_user_id = end_user_id
        self.external_user_id = external_user_id
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_user is not None:
            result['AutoCreateUser'] = self.auto_create_user

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateUser') is not None:
            self.auto_create_user = m.get('AutoCreateUser')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

