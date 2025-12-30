# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAvatarTrainingJobsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAvatarTrainingJobsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
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
            temp_model = main_models.ListAvatarTrainingJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAvatarTrainingJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        avatar_training_job_list: List[main_models.ListAvatarTrainingJobsResponseBodyDataAvatarTrainingJobList] = None,
        total_count: int = None,
    ):
        # The list of digital human training jobs.
        self.avatar_training_job_list = avatar_training_job_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.avatar_training_job_list:
            for v1 in self.avatar_training_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvatarTrainingJobList'] = []
        if self.avatar_training_job_list is not None:
            for k1 in self.avatar_training_job_list:
                result['AvatarTrainingJobList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avatar_training_job_list = []
        if m.get('AvatarTrainingJobList') is not None:
            for k1 in m.get('AvatarTrainingJobList'):
                temp_model = main_models.ListAvatarTrainingJobsResponseBodyDataAvatarTrainingJobList()
                self.avatar_training_job_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAvatarTrainingJobsResponseBodyDataAvatarTrainingJobList(DaraModel):
    def __init__(
        self,
        avatar_description: str = None,
        avatar_id: str = None,
        avatar_name: str = None,
        avatar_type: str = None,
        create_time: str = None,
        first_training_time: str = None,
        job_id: str = None,
        last_training_time: str = None,
        message: str = None,
        portrait: str = None,
        status: str = None,
    ):
        # The description of the digital human.
        self.avatar_description = avatar_description
        # The ID of the digital human.
        self.avatar_id = avatar_id
        # The name of the digital human.
        self.avatar_name = avatar_name
        # The type of the digital human.
        self.avatar_type = avatar_type
        # *   The time when the job was created.
        # *   The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # *   The time when the first training was initiated.
        # *   The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.first_training_time = first_training_time
        # The ID of the digital human training job.
        self.job_id = job_id
        # *   The time when the last training was initiated.
        # *   The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.last_training_time = last_training_time
        # The status description.
        self.message = message
        # The media asset ID of the portrait image.
        self.portrait = portrait
        # The state of the digital human training job.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_description is not None:
            result['AvatarDescription'] = self.avatar_description

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.avatar_name is not None:
            result['AvatarName'] = self.avatar_name

        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.first_training_time is not None:
            result['FirstTrainingTime'] = self.first_training_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.last_training_time is not None:
            result['LastTrainingTime'] = self.last_training_time

        if self.message is not None:
            result['Message'] = self.message

        if self.portrait is not None:
            result['Portrait'] = self.portrait

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarDescription') is not None:
            self.avatar_description = m.get('AvatarDescription')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('AvatarName') is not None:
            self.avatar_name = m.get('AvatarName')

        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FirstTrainingTime') is not None:
            self.first_training_time = m.get('FirstTrainingTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('LastTrainingTime') is not None:
            self.last_training_time = m.get('LastTrainingTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

