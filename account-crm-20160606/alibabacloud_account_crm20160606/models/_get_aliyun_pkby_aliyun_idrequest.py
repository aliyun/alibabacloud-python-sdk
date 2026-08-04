# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAliyunPKByAliyunIDRequest(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        email: str = None,
        havana_id: str = None,
        mobile: str = None,
        pk: str = None,
    ):
        # This parameter is required.
        self.aliyun_id = aliyun_id
        self.email = email
        self.havana_id = havana_id
        self.mobile = mobile
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.email is not None:
            result['Email'] = self.email

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.pk is not None:
            result['PK'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        return self

