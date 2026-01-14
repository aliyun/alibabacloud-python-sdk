# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppDomainDnsRecordRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        purpose: str = None,
    ):
        self.biz_id = biz_id
        self.domain_name = domain_name
        self.purpose = purpose

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

        if self.purpose is not None:
            result['Purpose'] = self.purpose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Purpose') is not None:
            self.purpose = m.get('Purpose')

        return self

