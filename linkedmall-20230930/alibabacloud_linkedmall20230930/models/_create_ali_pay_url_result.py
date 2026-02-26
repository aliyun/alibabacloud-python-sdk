# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAliPayUrlResult(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        member_id: str = None,
        zft_withhold_sign_url: str = None,
    ):
        self.account_id = account_id
        self.member_id = member_id
        self.zft_withhold_sign_url = zft_withhold_sign_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.member_id is not None:
            result['memberId'] = self.member_id

        if self.zft_withhold_sign_url is not None:
            result['zftWithholdSignUrl'] = self.zft_withhold_sign_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')

        if m.get('zftWithholdSignUrl') is not None:
            self.zft_withhold_sign_url = m.get('zftWithholdSignUrl')

        return self

