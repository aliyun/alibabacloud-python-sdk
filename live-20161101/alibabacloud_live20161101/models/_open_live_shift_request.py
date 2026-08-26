# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenLiveShiftRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        duration: int = None,
        ignore_transcode: bool = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
        vision: int = None,
    ):
        # The name of the application. The wildcard character (\\*) is supported. An asterisk (\\*) represents all applications under the specified domain name. For more information, see [Stream management](https://help.aliyun.com/document_detail/197397.html).
        self.app_name = app_name
        # The streaming domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The duration of an HTTP Live Streaming (HLS) transport stream (TS) segment. Unit: seconds.
        self.duration = duration
        # Specifies whether to enable time shifting for transcoded streams. Valid values:
        # 
        # - **true**: Time shifting is disabled for transcoded streams.
        # 
        # - **false**: Time shifting is enabled for transcoded streams.
        # 
        # Default value: true.
        self.ignore_transcode = ignore_transcode
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The name of the stream. The wildcard character (\\*) is supported. An asterisk (\\*) represents all streams under the specified application. For more information, see [Stream management](https://help.aliyun.com/document_detail/197397.html).
        self.stream_name = stream_name
        # The data retention period. The default value is 7. Unit: days.
        self.vision = vision

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

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.ignore_transcode is not None:
            result['IgnoreTranscode'] = self.ignore_transcode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.vision is not None:
            result['Vision'] = self.vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('IgnoreTranscode') is not None:
            self.ignore_transcode = m.get('IgnoreTranscode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Vision') is not None:
            self.vision = m.get('Vision')

        return self

