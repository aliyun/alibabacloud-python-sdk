# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccessTokenModel(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        comment: str = None,
        created_at: str = None,
        expired_at: str = None,
        status: str = None,
    ):
        self.access_token = access_token
        self.comment = comment
        self.created_at = created_at
        self.expired_at = expired_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.expired_at is not None:
            result['ExpiredAt'] = self.expired_at

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('ExpiredAt') is not None:
            self.expired_at = m.get('ExpiredAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

