# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RealTimeRecordCommandRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        command: str = None,
        domain_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the stream belongs. You can view the AppName on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The operation action. Valid values:
        # 
        # - **start**: forcibly starts recording. This must be called as the first operation and cannot be called again before stopping.
        # - **stop**: forcibly pauses recording. After the stream interruption delay (180 seconds by default) elapses, a recording is generated. This can only be called after start or restart. To generate the file immediately after calling stop, call cancel_delay.
        # - **cancel_delay**: immediately terminates the wait and generates a recording, completely stopping recording. This must be called after stop to generate the file in advance.
        # - **restart**: forcibly restarts recording. If recording is in progress before restart, a file is immediately generated. This can only be called when the task is in the started or stopped state.
        # 
        # This parameter is required.
        self.command = command
        # The streamer\\"s streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The stream name. Make sure that the StreamName is correct. You can view the StreamName on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # > This operation supports only single-stream operations and does not support wildcards.
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

        if self.command is not None:
            result['Command'] = self.command

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

