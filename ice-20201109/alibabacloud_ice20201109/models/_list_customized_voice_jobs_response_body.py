# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListCustomizedVoiceJobsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCustomizedVoiceJobsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true false
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
            temp_model = main_models.ListCustomizedVoiceJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCustomizedVoiceJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        customized_voice_job_list: List[main_models.ListCustomizedVoiceJobsResponseBodyDataCustomizedVoiceJobList] = None,
        total_count: int = None,
    ):
        # The queried human voice cloning jobs.
        self.customized_voice_job_list = customized_voice_job_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.customized_voice_job_list:
            for v1 in self.customized_voice_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomizedVoiceJobList'] = []
        if self.customized_voice_job_list is not None:
            for k1 in self.customized_voice_job_list:
                result['CustomizedVoiceJobList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customized_voice_job_list = []
        if m.get('CustomizedVoiceJobList') is not None:
            for k1 in m.get('CustomizedVoiceJobList'):
                temp_model = main_models.ListCustomizedVoiceJobsResponseBodyDataCustomizedVoiceJobList()
                self.customized_voice_job_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomizedVoiceJobsResponseBodyDataCustomizedVoiceJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        gender: str = None,
        gmt_create: str = None,
        job_id: str = None,
        message: str = None,
        scenario: str = None,
        status: str = None,
        type: str = None,
        voice_desc: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # *   The time when the job was created.
        # *   The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        self.gender = gender
        # The time when the job was created.
        self.gmt_create = gmt_create
        # The ID of the human voice cloning job.
        self.job_id = job_id
        # The returned message.
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
        # *   The voice type. Valid values:
        # 
        #     *   Basic
        #     *   Standard
        self.type = type
        # The voice description.
        # 
        # *   The description can be up to 256 characters in length.
        self.voice_desc = voice_desc
        # The voice ID.
        self.voice_id = voice_id
        # The voice name.
        # 
        # *   The name can be up to 32 characters in length.
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

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

