# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAppSeoIndexRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain: str = None,
        se_type: str = None,
        submit_later: bool = None,
    ):
        self.biz_id = biz_id
        self.domain = domain
        self.se_type = se_type
        self.submit_later = submit_later

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.se_type is not None:
            result['SeType'] = self.se_type

        if self.submit_later is not None:
            result['SubmitLater'] = self.submit_later

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('SeType') is not None:
            self.se_type = m.get('SeType')

        if m.get('SubmitLater') is not None:
            self.submit_later = m.get('SubmitLater')

        return self

