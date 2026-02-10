# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetClientRatioStatisticRequest(DaraModel):
    def __init__(
        self,
        resource_directory_account_id: int = None,
        statistic_types: List[str] = None,
        time_end: int = None,
        time_start: int = None,
    ):
        # The ID of the primary account of the Resource Directory member account.
        # > call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) interface to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # An array that consists of the details of a statistical type.
        self.statistic_types = statistic_types
        # The timestamp that specifies the end of the time range to collect statistics. Unit: milliseconds.
        self.time_end = time_end
        # The timestamp that specifies the beginning of the time range to collect statistics. Unit: milliseconds.
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.statistic_types is not None:
            result['StatisticTypes'] = self.statistic_types

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        if self.time_start is not None:
            result['TimeStart'] = self.time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('StatisticTypes') is not None:
            self.statistic_types = m.get('StatisticTypes')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')

        return self

