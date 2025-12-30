# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitLiveTranscodeJobShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        start_mode: int = None,
        stream_input_shrink: str = None,
        template_id: str = None,
        timed_config_shrink: str = None,
        transcode_output_shrink: str = None,
    ):
        # The name of the transcoding job.
        # 
        # This parameter is required.
        self.name = name
        # The start mode of the transcoding job.
        # 
        # *   0: The transcoding job immediately starts.
        # *   1: The transcoding job starts at the scheduled time.
        # 
        # This parameter is required.
        self.start_mode = start_mode
        # The information about the input stream.
        # 
        # This parameter is required.
        self.stream_input_shrink = stream_input_shrink
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The configuration of a timed transcoding job. This parameter is required if you set StartMode to 1.
        self.timed_config_shrink = timed_config_shrink
        # The information about the transcoding output.
        # 
        # This parameter is required.
        self.transcode_output_shrink = transcode_output_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.start_mode is not None:
            result['StartMode'] = self.start_mode

        if self.stream_input_shrink is not None:
            result['StreamInput'] = self.stream_input_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.timed_config_shrink is not None:
            result['TimedConfig'] = self.timed_config_shrink

        if self.transcode_output_shrink is not None:
            result['TranscodeOutput'] = self.transcode_output_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartMode') is not None:
            self.start_mode = m.get('StartMode')

        if m.get('StreamInput') is not None:
            self.stream_input_shrink = m.get('StreamInput')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TimedConfig') is not None:
            self.timed_config_shrink = m.get('TimedConfig')

        if m.get('TranscodeOutput') is not None:
            self.transcode_output_shrink = m.get('TranscodeOutput')

        return self

