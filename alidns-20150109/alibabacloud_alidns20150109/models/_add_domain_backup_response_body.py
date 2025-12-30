# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDomainBackupResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        period_type: str = None,
        request_id: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The backup cycle.
        self.period_type = period_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

