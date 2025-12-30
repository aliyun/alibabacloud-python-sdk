# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateLiveTranscodeJobRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        name: str = None,
        stream_input: main_models.UpdateLiveTranscodeJobRequestStreamInput = None,
        timed_config: main_models.UpdateLiveTranscodeJobRequestTimedConfig = None,
        transcode_output: main_models.UpdateLiveTranscodeJobRequestTranscodeOutput = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The name of the job.
        self.name = name
        # The information about the input stream.
        self.stream_input = stream_input
        # The configuration of a timed transcoding job.
        self.timed_config = timed_config
        # The information about the transcoding output.
        self.transcode_output = transcode_output

    def validate(self):
        if self.stream_input:
            self.stream_input.validate()
        if self.timed_config:
            self.timed_config.validate()
        if self.transcode_output:
            self.transcode_output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.timed_config is not None:
            result['TimedConfig'] = self.timed_config.to_map()

        if self.transcode_output is not None:
            result['TranscodeOutput'] = self.transcode_output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StreamInput') is not None:
            temp_model = main_models.UpdateLiveTranscodeJobRequestStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TimedConfig') is not None:
            temp_model = main_models.UpdateLiveTranscodeJobRequestTimedConfig()
            self.timed_config = temp_model.from_map(m.get('TimedConfig'))

        if m.get('TranscodeOutput') is not None:
            temp_model = main_models.UpdateLiveTranscodeJobRequestTranscodeOutput()
            self.transcode_output = temp_model.from_map(m.get('TranscodeOutput'))

        return self

class UpdateLiveTranscodeJobRequestTranscodeOutput(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        type: str = None,
    ):
        # The streaming domain name of ApsaraVideo Live.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The type of the output stream. A value of LiveCenter indicates that the URL of the output stream is generated based on the domain name of ApsaraVideo Live. The value can only be LiveCenter.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateLiveTranscodeJobRequestTimedConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The stop time of the transcoding job. Note: The time span between the stop time and the current time cannot exceed seven days.
        self.end_time = end_time
        # The start time of the transcoding job. Note: The time span between the start time and the current time cannot exceed seven days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class UpdateLiveTranscodeJobRequestStreamInput(DaraModel):
    def __init__(
        self,
        input_url: str = None,
        type: str = None,
    ):
        # The URL of the input stream.
        # 
        # This parameter is required.
        self.input_url = input_url
        # The type of the input stream. The value can only be rtmp.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_url is not None:
            result['InputUrl'] = self.input_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputUrl') is not None:
            self.input_url = m.get('InputUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

