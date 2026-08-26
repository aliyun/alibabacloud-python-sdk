# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotLiveRtcStreamRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        audio_msid: str = None,
        connection_timeout: str = None,
        domain_name: str = None,
        media_timeout: str = None,
        owner_id: int = None,
        region_code: str = None,
        region_id: str = None,
        stream_name: str = None,
        video_msid: str = None,
    ):
        # The application name of the live stream to prefetch.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The audio Msid.
        # 
        # This parameter is required.
        self.audio_msid = audio_msid
        # The duration to maintain the prefetch connection. Unit: milliseconds. The default value, 0, means the connection is always maintained.
        self.connection_timeout = connection_timeout
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The custom timeout period for a timeout event. Unit: milliseconds.
        self.media_timeout = media_timeout
        self.owner_id = owner_id
        # The prefetch area. For more information, see the RegionCode lookup table.
        # 
        # > For regions within China, specify the corresponding code from the "Region codes for China" table. For all other regions, specify the country code.
        # >
        # > - If the CodeRegionHasNoNode error is returned after you specify a RegionCode, the corresponding area is not covered by L1 nodes and cannot be prefetched. In this case, specify a different RegionCode.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The region ID.
        self.region_id = region_id
        # The name of the live stream to prefetch.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        # The video Msid.
        # 
        # This parameter is required.
        self.video_msid = video_msid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.audio_msid is not None:
            result['AudioMsid'] = self.audio_msid

        if self.connection_timeout is not None:
            result['ConnectionTimeout'] = self.connection_timeout

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.media_timeout is not None:
            result['MediaTimeout'] = self.media_timeout

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.video_msid is not None:
            result['VideoMsid'] = self.video_msid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AudioMsid') is not None:
            self.audio_msid = m.get('AudioMsid')

        if m.get('ConnectionTimeout') is not None:
            self.connection_timeout = m.get('ConnectionTimeout')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('MediaTimeout') is not None:
            self.media_timeout = m.get('MediaTimeout')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('VideoMsid') is not None:
            self.video_msid = m.get('VideoMsid')

        return self

