# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitializeAutoShowListTaskRequest(DaraModel):
    def __init__(
        self,
        call_back_url: str = None,
        caster_config: str = None,
        domain_name: str = None,
        end_time: int = None,
        owner_id: int = None,
        region_id: str = None,
        resource_ids: str = None,
        start_time: int = None,
    ):
        # The callback URL.
        self.call_back_url = call_back_url
        # The production studio configuration. This includes:
        # 
        # - (Required) CasterTemplate: the output resolution of the production studio.
        # 
        # - (Optional) LiveTemplate: the list of output transcoding tasks.
        # 
        # >A JSON-formatted string. Use upper camel case (PascalCase) for the field names within the struct.
        # 
        # This parameter is required.
        self.caster_config = caster_config
        # The output streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The list of video-on-demand media asset file IDs in the playlist. Currently, only MP4 video files from the video-on-demand platform are supported.
        # 
        # A maximum of three programs are supported. Each program is played in the order of the list until EndTime, at which point playback automatically ends. This parameter is required. If it is missing, a MissingParameter error is returned.
        # >- You can obtain the video file ID from the console or from the response parameters of an API operation. For more information, see [Media asset management](https://help.aliyun.com/document_detail/86057.html) or [Obtain the upload URL and credential for audio and video files](https://help.aliyun.com/document_detail/55407.html).- If all programs finish playing before EndTime, the last frame of the last program is displayed until the scheduled end time.
        self.resource_ids = resource_ids
        # The start timestamp. Unit: milliseconds.
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
        if self.call_back_url is not None:
            result['CallBackUrl'] = self.call_back_url

        if self.caster_config is not None:
            result['CasterConfig'] = self.caster_config

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBackUrl') is not None:
            self.call_back_url = m.get('CallBackUrl')

        if m.get('CasterConfig') is not None:
            self.caster_config = m.get('CasterConfig')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

