# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnUserBillPredictionRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        dimension: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The billable region. Valid values:
        # 
        # *   **CN**: the Chinese mainland
        # *   **OverSeas**: outside the Chinese mainland
        # *   **AP1**: Asia Pacific 1
        # *   **AP2**: Asia Pacific 2
        # *   **AP3**: Asia Pacific 3
        # *   **NA**: North America
        # *   **SA**: South America
        # *   **EU**: Europe
        # *   **MEAA**: Middle East and Africa
        # 
        # By default, the value of this parameter is determined by the metering method that is currently used. Regions inside and outside the Chinese mainland are classified into the **CN** and **OverSeas** billable regions. Billable regions inside the Chinese mainland include **CN**. Billable regions outside the Chinese mainland include **AP1**, **AP2**, **AP3**, **NA**, **SA**, **EU**, and **MEAA**.
        # 
        # > For more information about billable regions, see [Billable regions](https://help.aliyun.com/document_detail/142221.html).
        self.area = area
        # The billable item. A value of flow specifies bandwidth.
        self.dimension = dimension
        # The end time of the estimation. The default value is the current time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The start time of the estimation. The default value is 00:00 on the first day of the current month. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

