# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetCustomizedVoiceJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCustomizedVoiceJobResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned if the request was successful.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetCustomizedVoiceJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomizedVoiceJobResponseBodyData(DaraModel):
    def __init__(
        self,
        customized_voice_job: main_models.GetCustomizedVoiceJobResponseBodyDataCustomizedVoiceJob = None,
    ):
        # The information about the human voice cloning job.
        self.customized_voice_job = customized_voice_job

    def validate(self):
        if self.customized_voice_job:
            self.customized_voice_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customized_voice_job is not None:
            result['CustomizedVoiceJob'] = self.customized_voice_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedVoiceJob') is not None:
            temp_model = main_models.GetCustomizedVoiceJobResponseBodyDataCustomizedVoiceJob()
            self.customized_voice_job = temp_model.from_map(m.get('CustomizedVoiceJob'))

        return self

class GetCustomizedVoiceJobResponseBodyDataCustomizedVoiceJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        gender: str = None,
        job_id: str = None,
        message: str = None,
        scenario: str = None,
        status: str = None,
        type: str = None,
        voice_desc: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # The time when the job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        self.gender = gender
        # The ID of the human voice cloning job.
        self.job_id = job_id
        # The status description.
        self.message = message
        # The scenario. Valid values:
        # 
        # *   story
        # *   interaction
        # *   navigation
        self.scenario = scenario
        # The job state. Valid values:
        # 
        # *   Initialization
        # *   AudioDetecting
        # *   PreTraining
        # *   Training
        # *   Success
        # *   Fail
        self.status = status
        # The type of the human voice cloning job. Valid values:
        # 
        # *   Basic
        # *   Standard
        self.type = type
        # The voice description.
        self.voice_desc = voice_desc
        # The voice ID.
        self.voice_id = voice_id
        # The voice name.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.voice_desc is not None:
            result['VoiceDesc'] = self.voice_desc

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VoiceDesc') is not None:
            self.voice_desc = m.get('VoiceDesc')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

