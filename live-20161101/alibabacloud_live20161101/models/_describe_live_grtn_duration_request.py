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
        # Application ID. You can query multiple application IDs separated by commas (half-width). A maximum of 30 IDs can be queried. By default, aggregated data for all applications is returned.
        self.app_id = app_id
        # The area code. Valid values:
        # - CN: Chinese mainland.
        # - OverSeas: Overseas regions.
        # - AP1: Asia Pacific 1, including Hong Kong (China), Macao (China), Taiwan (China), Japan, and Southeast Asian countries except Vietnam and Indonesia.
        # - AP2: Asia Pacific 2, including Indonesia, South Korea, and Vietnam.
        # - AP3: Asia Pacific 3, including Australia and New Zealand.
        # - NA: North America, including the United States and Canada.
        # - SA: South America, specifically Brazil.
        # - EU: Europe, including Ukraine, the United Kingdom, France, the Netherlands, Spain, Italy, Sweden, and Germany.
        # - MEAA: Middle East and Africa, including South Africa, Oman, the United Arab Emirates, and Kuwait.
        # 
        # If not specified, aggregated data for all areas is returned by default.
        self.area = area
        # The end time must be later than the start time. The query granularity must be ≥ 5 minutes and ≤ 31 days. The date format follows the ISO 8601 notation and uses UTC time in the format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity for querying data. Unit: seconds. Valid values:
        # 
        # - 300
        # - 3600
        # - 86400
        # 
        # If not specified or an unsupported value is passed, the default value of 3600 seconds is used.
        self.interval = interval
        self.owner_id = owner_id
        # Region ID.
        self.region_id = region_id
        # The start time for data retrieval. The date format follows the ISO 8601 notation and uses UTC time in the format: YYYY-MM-DDThh:mm:ssZ.
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

