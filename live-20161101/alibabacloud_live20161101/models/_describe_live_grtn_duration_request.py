# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveGrtnDurationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        area: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the application. Separate multiple application IDs with commas (,). You can specify up to 30 application IDs. By default, the aggregated data of all applications is returned.
        self.app_id = app_id
        # The ID of the billable region. Valid values:
        # 
        # *   CN: Chinese mainland
        # *   OverSeas: countries and regions outside the Chinese mainland
        # *   AP1: Asia Pacific 1, including Hong Kong (China), Macao (China), Taiwan (China), Japan, and other Southeast Asia countries and regions except Vietnam and Indonesia
        # *   AP2: Asia Pacific 2, including Indonesia, South Korea, and Vietnam
        # *   AP3: Asia Pacific 3, including Australia and New Zealand
        # *   NA: North America, including US and Canada
        # *   SA: South America, specifically meaning Brazil
        # *   EU: Europe, including Ukraine, UK, France, Netherlands, Spain, Italy, Sweden, and Germany
        # *   MEAA: Middle East and Africa, including South Africa, Oman, UAE, and Kuwait
        # 
        # If you do not specify this parameter, data of all regions is aggregated and returned by default.
        self.area = area
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. The time range that can be specified is greater than or equal to 5 minutes and less than or equal to 31 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   300
        # *   3600
        # *   86400
        # 
        # If you specify an invalid value or do not specify this parameter, the default value 3600 is used.
        self.interval = interval
        self.owner_id = owner_id
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.area is not None:
            result['Area'] = self.area

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

