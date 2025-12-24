# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForbidLiveStreamRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        oneshot: str = None,
        owner_id: int = None,
        region_id: str = None,
        resume_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The ingest domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether the live stream is ingested by a streamer or played by a viewer. Set the value to **publisher**.
        # 
        # This parameter is required.
        self.live_stream_type = live_stream_type
        # Specifies whether to only interrupt the live stream without adding the ingest URL of the live stream to the blacklist. Valid values:
        # 
        # *   **yes**: interrupts the live stream but does not add the ingest URL of the live stream to the blacklist. This value is available only when the live stream is ingested or played in the upstream.
        # *   **no**: disables the live stream and adds the ingest URL of the live stream to the blacklist.
        # 
        # >  If you do not specify this parameter, the default value no is used.
        self.oneshot = oneshot
        self.owner_id = owner_id
        self.region_id = region_id
        # The time when the live stream is resumed. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > 
        # 
        # *   If you set the **Oneshot** parameter to **no** and do not specify this parameter, the live stream is disabled for six months by default.
        # 
        # *   If you specify this parameter, the live stream is resumed at the specified point in time.
        self.resume_time = resume_time
        # The name of the ingested stream. You can view the stream name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
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

        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type

        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')

        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

