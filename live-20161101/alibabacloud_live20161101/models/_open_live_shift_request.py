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
        # The name of the application to which the live stream belongs. You can specify an asterisk (\\*) as the value to match all applications under the domain name. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        self.app_name = app_name
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The length of a TS segment for HTTP Live Streaming (HLS). Unit: seconds.
        self.duration = duration
        # Specifies whether to disable time shifting for the transcoded stream. Valid values:
        # 
        # *   **true**: disables time shifting for the transcoded stream.
        # *   **false**: enables time shifting for the transcoded stream.
        # 
        # Default value: true.
        self.ignore_transcode = ignore_transcode
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream. You can specify an asterisk (\\*) as the value to match all streams in the application. You can view the stream name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        self.stream_name = stream_name
        # The duration for which data is retained. Default value: 7. Unit: day.
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

