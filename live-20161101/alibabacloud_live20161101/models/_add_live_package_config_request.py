# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLivePackageConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        ignore_transcode: bool = None,
        owner_id: int = None,
        part_duration: int = None,
        protocol: str = None,
        region_id: str = None,
        segment_duration: int = None,
        segment_num: int = None,
        stream_name: str = None,
    ):
        # The AppName must match the AppName in the ingest URL for the template to take effect. The AppName can be up to 255 characters in length and can contain digits, uppercase letters, lowercase letters, hyphens (-), and underscores (_). A hyphen or an underscore cannot be the first character. You can also set this parameter to a single asterisk (\\*) to match all AppNames.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The live streaming domain name. This is the primary playback domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to ignore transcoded streams. Valid values:
        # 
        # - **true** (default): Ignore transcoded streams.
        # 
        # - **false**: Do not ignore transcoded streams.
        self.ignore_transcode = ignore_transcode
        self.owner_id = owner_id
        # The length of the part segment, in milliseconds.
        # 
        # - If SegmentDuration is 1 s, the valid values are 100 to 500. The default value is 350.
        # 
        # - If SegmentDuration is 2 s, the valid values are 100 to 1000. The default value is 700.
        # 
        # - This parameter is valid only when you set Protocol to LLHLS_\\*.
        self.part_duration = part_duration
        # The live streaming protocol and container format. Valid values:
        # 
        # - **HLS_CMAF**
        # 
        # - **LLHLS_TS**
        #   (low latency)
        # 
        # - **LLHLS_CMAF** (low latency)
        # 
        # - **DASH_CMAF**
        # 
        # - **HLSDASH_CMAF**
        # 
        # This parameter is required.
        self.protocol = protocol
        # The region ID.
        self.region_id = region_id
        # The segment length, in seconds.
        # 
        # - If you set Protocol to HLS_CMAF, the valid values are 1 to 10. The default value is 5.
        # 
        # - If you set Protocol to LLHLS_\\*, the valid values are 1 to 2. The default value is 1.
        self.segment_duration = segment_duration
        # The number of M3U8 segments for live streaming.
        # 
        # - Valid values: 3 to 10.
        # 
        # - Default value: 3.
        self.segment_num = segment_num
        # The StreamName must match the StreamName in the ingest URL for the template to take effect. The StreamName can be up to 255 characters in length and can contain digits, uppercase letters, lowercase letters, hyphens (-), and underscores (_). A hyphen or an underscore cannot be the first character. You can also set this parameter to a single asterisk (\\*) to match all StreamNames.
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

        if self.ignore_transcode is not None:
            result['IgnoreTranscode'] = self.ignore_transcode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.part_duration is not None:
            result['PartDuration'] = self.part_duration

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        if self.segment_num is not None:
            result['SegmentNum'] = self.segment_num

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IgnoreTranscode') is not None:
            self.ignore_transcode = m.get('IgnoreTranscode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PartDuration') is not None:
            self.part_duration = m.get('PartDuration')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        if m.get('SegmentNum') is not None:
            self.segment_num = m.get('SegmentNum')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

