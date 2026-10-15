# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppDomainRedirectRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        record_id: int = None,
    ):
        # The business ID of the application instance.
        self.biz_id = biz_id
        # aliyun.com
        self.domain_name = domain_name
        # The ID of the domain name redirect record.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        return self

