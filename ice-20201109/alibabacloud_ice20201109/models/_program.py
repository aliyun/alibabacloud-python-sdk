# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class Program(DaraModel):
    def __init__(
        self,
        ad_breaks: List[main_models.ProgramAdBreaks] = None,
        arn: str = None,
        channel_name: str = None,
        clip_range: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        program_name: str = None,
        source_location_name: str = None,
        source_name: str = None,
        source_type: str = None,
        transition: str = None,
    ):
        self.ad_breaks = ad_breaks
        self.arn = arn
        self.channel_name = channel_name
        self.clip_range = clip_range
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.program_name = program_name
        self.source_location_name = source_location_name
        self.source_name = source_name
        self.source_type = source_type
        self.transition = transition

    def validate(self):
        if self.ad_breaks:
            for v1 in self.ad_breaks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdBreaks'] = []
        if self.ad_breaks is not None:
            for k1 in self.ad_breaks:
                result['AdBreaks'].append(k1.to_map() if k1 else None)

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.clip_range is not None:
            result['ClipRange'] = self.clip_range

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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
        self.ad_breaks = []
        if m.get('AdBreaks') is not None:
            for k1 in m.get('AdBreaks'):
                temp_model = main_models.ProgramAdBreaks()
                self.ad_breaks.append(temp_model.from_map(k1))

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ClipRange') is not None:
            self.clip_range = m.get('ClipRange')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

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

class ProgramAdBreaks(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        message_type: str = None,
        offset_millis: int = None,
        program_name: str = None,
        source_location_name: str = None,
        source_name: str = None,
        splice_insert_settings: str = None,
        time_signal_settings: str = None,
    ):
        self.channel_name = channel_name
        self.message_type = message_type
        self.offset_millis = offset_millis
        self.program_name = program_name
        self.source_location_name = source_location_name
        self.source_name = source_name
        self.splice_insert_settings = splice_insert_settings
        self.time_signal_settings = time_signal_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.offset_millis is not None:
            result['OffsetMillis'] = self.offset_millis

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.splice_insert_settings is not None:
            result['SpliceInsertSettings'] = self.splice_insert_settings

        if self.time_signal_settings is not None:
            result['TimeSignalSettings'] = self.time_signal_settings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('OffsetMillis') is not None:
            self.offset_millis = m.get('OffsetMillis')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SpliceInsertSettings') is not None:
            self.splice_insert_settings = m.get('SpliceInsertSettings')

        if m.get('TimeSignalSettings') is not None:
            self.time_signal_settings = m.get('TimeSignalSettings')

        return self

