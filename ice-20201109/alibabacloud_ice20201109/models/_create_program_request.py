# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProgramRequest(DaraModel):
    def __init__(
        self,
        ad_breaks: str = None,
        channel_name: str = None,
        clip_range: str = None,
        program_name: str = None,
        source_location_name: str = None,
        source_name: str = None,
        source_type: str = None,
        transition: str = None,
    ):
        # The information about ad breaks.
        self.ad_breaks = ad_breaks
        # The name of the channel.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # Extracts a clip from the source.
        self.clip_range = clip_range
        # The name of the program.
        # 
        # This parameter is required.
        self.program_name = program_name
        # The source location.
        # 
        # This parameter is required.
        self.source_location_name = source_location_name
        # The name of the source.
        # 
        # This parameter is required.
        self.source_name = source_name
        # The source type of the program.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The program transition method.
        # 
        # This parameter is required.
        self.transition = transition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_breaks is not None:
            result['AdBreaks'] = self.ad_breaks

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.clip_range is not None:
            result['ClipRange'] = self.clip_range

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.transition is not None:
            result['Transition'] = self.transition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdBreaks') is not None:
            self.ad_breaks = m.get('AdBreaks')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ClipRange') is not None:
            self.clip_range = m.get('ClipRange')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Transition') is not None:
            self.transition = m.get('Transition')

        return self

