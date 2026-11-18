# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodPlayerDimensionDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dimension: str = None,
        end_time: str = None,
        region: str = None,
        start_time: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The dimension type. Valid values:
        # 
        # - Os: Operating system.
        # - AppVersion: App version.
        # - SdkVersion: SDK version.
        # - Codec: Codec.
        # - VideoType: Video format.
        # - Network: Network type.
        # - Isp: ISP.
        # - VideoDefinition: Resolution.
        # - Domain: Domain name.
        # - Country: Country.
        # - Province: Province.
        # - ErrorCode: Error code.
        # - IsHw: Hardware decoding.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The end time of the query. Format: yyyy-mm-ddThh:mm:ssZ (UTC).
        self.end_time = end_time
        # The region used to limit the query scope when querying the metadata for the Province and ISP dimensions. Valid values:
        # 
        # - ALL (default): All regions.
        # - CN: China.
        # - OVERSEAS: Outside China.
        self.region = region
        # The start time of the query. Format: <i>yyyy-mm-dd</i>T<i>hh:mm:ss</i>Z (UTC).
        # > 
        # > - You can query playback data history for the past year.
        # > - The time range for a single query cannot exceed 31 days.
        # > - The time interval is left-closed and right-open [StartTime, EndTime).
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

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

