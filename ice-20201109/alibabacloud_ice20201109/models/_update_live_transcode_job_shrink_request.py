# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveTranscodeJobShrinkRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        name: str = None,
        stream_input_shrink: str = None,
        timed_config_shrink: str = None,
        transcode_output_shrink: str = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The name of the job.
        self.name = name
        # The information about the input stream.
        self.stream_input_shrink = stream_input_shrink
        # The configuration of a timed transcoding job.
        self.timed_config_shrink = timed_config_shrink
        # The information about the transcoding output.
        self.transcode_output_shrink = transcode_output_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.stream_input_shrink is not None:
            result['StreamInput'] = self.stream_input_shrink

        if self.timed_config_shrink is not None:
            result['TimedConfig'] = self.timed_config_shrink

        if self.transcode_output_shrink is not None:
            result['TranscodeOutput'] = self.transcode_output_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StreamInput') is not None:
            self.stream_input_shrink = m.get('StreamInput')

        if m.get('TimedConfig') is not None:
            self.timed_config_shrink = m.get('TimedConfig')

        if m.get('TranscodeOutput') is not None:
            self.transcode_output_shrink = m.get('TranscodeOutput')

        return self

