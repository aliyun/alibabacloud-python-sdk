# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveStreamPreloadTasksRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        domain_name: str = None,
        owner_id: int = None,
        play_url: str = None,
        preloaded_end_time: str = None,
        preloaded_start_time: str = None,
        region_id: str = None,
    ):
        # The acceleration region where you want to prefetch the live content. Valid values:
        # 
        # *   domestic: regions in the Chinese mainland.
        # *   overseas: regions outside the Chinese mainland.
        # *   global: regions in and outside the Chinese mainland.
        # 
        # If you do not specify this parameter, the acceleration region configured for the domain name is used.
        self.area = area
        # The streaming domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The streaming URL. You can specify up to 100 streaming URLs in a request. Separate multiple streaming URLs with commas (,).
        # 
        # This parameter is required.
        self.play_url = play_url
        # The end time of the prefetch task. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2016-06-30T19:00:00Z. The interval between the start time and end time cannot exceed 6 hours.
        self.preloaded_end_time = preloaded_end_time
        # The start time of the prefetch task. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2016-06-29T19:00:00Z. If you do not specify this parameter, the prefetch task runs for 1 hour by default.
        self.preloaded_start_time = preloaded_start_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.preloaded_end_time is not None:
            result['PreloadedEndTime'] = self.preloaded_end_time

        if self.preloaded_start_time is not None:
            result['PreloadedStartTime'] = self.preloaded_start_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('PreloadedEndTime') is not None:
            self.preloaded_end_time = m.get('PreloadedEndTime')

        if m.get('PreloadedStartTime') is not None:
            self.preloaded_start_time = m.get('PreloadedStartTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

