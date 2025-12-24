# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeLiveStreamRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        owner_id: int = None,
        security_token: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs. You can specify an asterisk (\\*) as the value to match all applications. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The ingest domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether the live stream is ingested by a streamer or played by a client. Set the value to **publisher**, which specifies that the live stream is ingested by a streamer.
        # 
        # This parameter is required.
        self.live_stream_type = live_stream_type
        self.owner_id = owner_id
        self.security_token = security_token
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

