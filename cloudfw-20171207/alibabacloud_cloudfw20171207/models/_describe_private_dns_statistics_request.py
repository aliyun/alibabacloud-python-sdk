# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrivateDnsStatisticsRequest(DaraModel):
    def __init__(
        self,
        domain_name_created_end_time: int = None,
        domain_name_created_start_time: int = None,
    ):
        self.domain_name_created_end_time = domain_name_created_end_time
        self.domain_name_created_start_time = domain_name_created_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name_created_end_time is not None:
            result['DomainNameCreatedEndTime'] = self.domain_name_created_end_time

        if self.domain_name_created_start_time is not None:
            result['DomainNameCreatedStartTime'] = self.domain_name_created_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNameCreatedEndTime') is not None:
            self.domain_name_created_end_time = m.get('DomainNameCreatedEndTime')

        if m.get('DomainNameCreatedStartTime') is not None:
            self.domain_name_created_start_time = m.get('DomainNameCreatedStartTime')

        return self

