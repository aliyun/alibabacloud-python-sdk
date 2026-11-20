# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecretTransferRecordRequest(DaraModel):
    def __init__(
        self,
        last_partner_key: str = None,
        number_list: str = None,
        origin_partner_key: str = None,
    ):
        # 迁移后的新号码池key
        self.last_partner_key = last_partner_key
        # 指定号码（单一、批量）迁移;一次最多可迁移500个号码，号码间请换行隔开.
        self.number_list = number_list
        # 要迁移的原号码池key
        self.origin_partner_key = origin_partner_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_partner_key is not None:
            result['LastPartnerKey'] = self.last_partner_key

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.origin_partner_key is not None:
            result['OriginPartnerKey'] = self.origin_partner_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPartnerKey') is not None:
            self.last_partner_key = m.get('LastPartnerKey')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('OriginPartnerKey') is not None:
            self.origin_partner_key = m.get('OriginPartnerKey')

        return self

