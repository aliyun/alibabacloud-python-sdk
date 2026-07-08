# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStreamURLRequest(DaraModel):
    def __init__(
        self,
        auth: bool = None,
        auth_key: str = None,
        end_time: int = None,
        expire: int = None,
        id: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        start_time: int = None,
        transcode: str = None,
        type: str = None,
    ):
        # Specifies whether to generate a signed URL. Valid values:
        # 
        # - true
        # 
        # - false
        self.auth = auth
        # The primary key associated with the playback domain name. This key is used to generate the authentication URL.
        # 
        # > Call the [DescribeVsDomainConfigs](https://next.api.aliyun.com/document/vs/2018-12-12/DescribeVsDomainConfigs) operation to query the \\`AuthKey\\` information.
        self.auth_key = auth_key
        # The end time. This parameter applies to \\`vod\\` streams.<br>
        # A UNIX timestamp. Unit: seconds.<br>
        self.end_time = end_time
        # The time-to-live (TTL) of the URL. Unit: seconds.
        self.expire = expire
        # The stream ID.
        # 
        # This parameter is required.
        self.id = id
        # The playback protocol for the stream. Valid values:
        # 
        # - rtmp
        # 
        # - flv
        # 
        # - hls
        # 
        # This parameter is required.
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        # The start time. This parameter applies to \\`vod\\` streams.<br>
        # A UNIX timestamp. Unit: seconds.<br>
        self.start_time = start_time
        # The name of the transcoding rule. This parameter is valid only after a transcoding template is attached.
        self.transcode = transcode
        # The type of the stream. The default value is \\`live\\`. Valid values:
        # 
        # - \\`live\\`: a live stream.
        # 
        # - \\`vod\\`: a video-on-demand (VOD) stream, such as a historical stream from a Network Video Recorder (NVR).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.id is not None:
            result['Id'] = self.id

        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.transcode is not None:
            result['Transcode'] = self.transcode

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

