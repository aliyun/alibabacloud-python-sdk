# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodAIDataRequest(DaraModel):
    def __init__(
        self,
        aitype: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        start_time: str = None,
    ):
        # The type of video AI. If you leave this parameter empty, statistics on video AI of all types are returned. Separate multiple types with commas (,). Valid values:
        # 
        # *   **AIVideoCensor**: automated review
        # *   **AIVideoFPShot**: media fingerprinting
        # *   **AIVideoTag**: smart tagging
        self.aitype = aitype
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region in which you want to query data. If you leave this parameter empty, data in all regions is returned. Separate multiple regions with commas (,). Valid values:
        # 
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-beijing**: China (Beijing)
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **ap-southeast-1**: Singapore
        self.region = region
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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
        if self.aitype is not None:
            result['AIType'] = self.aitype

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIType') is not None:
            self.aitype = m.get('AIType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

