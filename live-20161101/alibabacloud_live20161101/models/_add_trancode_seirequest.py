# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTrancodeSEIRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        delay: int = None,
        domain_name: str = None,
        owner_id: int = None,
        pattern: str = None,
        region_id: str = None,
        repeat: int = None,
        stream_name: str = None,
        text: str = None,
    ):
        # The name of the application to which the live stream belongs. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The time period after which the SEI is inserted after the request is received. Unit: milliseconds.
        # 
        # This parameter is required.
        self.delay = delay
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # Specifies whether to append the SEI to each keyframe or frame. Valid values:
        # 
        # *   **keyframe**
        # *   **frame**
        # 
        # This parameter is required.
        self.pattern = pattern
        self.region_id = region_id
        # The number of times that the SEI is repeatedly inserted. A value of -1 specifies infinite times.
        # 
        # This parameter is required.
        self.repeat = repeat
        # The name of the live stream.
        # 
        # >  The value of this parameter must be the name of the source stream. This way, the SEI is inserted to all the transcoded streams.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        # The SEI text. It can be up to 4,000 bytes in length.
        # 
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat is not None:
            result['Repeat'] = self.repeat

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

