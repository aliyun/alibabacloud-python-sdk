# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseProduceAuthorizationRequest(DaraModel):
    def __init__(
        self,
        authorized_user_id: str = None,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.authorized_user_id = authorized_user_id
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        return self

