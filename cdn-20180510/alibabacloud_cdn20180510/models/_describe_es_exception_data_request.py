# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEsExceptionDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        rule_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The script ID. You can call the [DescribeCdnDomainConfigs](https://help.aliyun.com/document_detail/90924.html) operation to query script IDs.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

