# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddYikeUserCreditRequest(DaraModel):
    def __init__(
        self,
        credit: int = None,
        yike_user_id: str = None,
    ):
        # This parameter is required.
        self.credit = credit
        # This parameter is required.
        self.yike_user_id = yike_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit is not None:
            result['Credit'] = self.credit

        if self.yike_user_id is not None:
            result['YikeUserId'] = self.yike_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credit') is not None:
            self.credit = m.get('Credit')

        if m.get('YikeUserId') is not None:
            self.yike_user_id = m.get('YikeUserId')

        return self

