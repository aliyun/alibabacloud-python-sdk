# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCheckTimeDimensionStatisticRequest(DaraModel):
    def __init__(
        self,
        end_time_stamp: int = None,
        start_time_stamp: int = None,
        statistic_type: str = None,
        vendors: List[str] = None,
    ):
        # End time, in timestamp format.
        self.end_time_stamp = end_time_stamp
        # Start time, in timestamp format.
        self.start_time_stamp = start_time_stamp
        # Type of statistical data. Values:
        # - **CheckPassRate**: Check item pass rate.
        # - **AssetPassRate**: Asset pass rate.
        self.statistic_type = statistic_type
        # List of cloud vendors.
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp

        if self.statistic_type is not None:
            result['StatisticType'] = self.statistic_type

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')

        if m.get('StatisticType') is not None:
            self.statistic_type = m.get('StatisticType')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

