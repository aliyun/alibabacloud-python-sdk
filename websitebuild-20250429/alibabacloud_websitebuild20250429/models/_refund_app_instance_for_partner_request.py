# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefundAppInstanceForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        client_token: str = None,
        refund_reason: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.client_token = client_token
        self.refund_reason = refund_reason
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.refund_reason is not None:
            result['RefundReason'] = self.refund_reason

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RefundReason') is not None:
            self.refund_reason = m.get('RefundReason')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

