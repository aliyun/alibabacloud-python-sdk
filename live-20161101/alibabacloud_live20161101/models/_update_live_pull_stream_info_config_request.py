# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLivePullStreamInfoConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The streaming domain used as the streamer\\"s stream domain.
        # > - When you specify DomainName, make sure that the domain is a live streaming domain and that the user calling this operation has the permission to operate on the specified domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time of stream pulling.
        # 
        # The interval between StartTime and EndTime must be within 7 days, and EndTime must be later than the current time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The full URL of the origin server where the live stream resides. You can specify multiple origin URLs separated by semicolons (;).
        # 
        # This parameter is required.
        self.source_url = source_url
        # The start time of stream pulling.
        # 
        # The interval between StartTime and EndTime must be within 7 days. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the live stream.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

