# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        job_info_list: List[main_models.ListJobInfoResponseBodyJobInfoList] = None,
        job_type: str = None,
        media_id: str = None,
        request_id: str = None,
    ):
        # The historical tasks of the last 6 months.
        self.job_info_list = job_info_list
        # The type of the task. Valid values:
        # 
        # *   transcode
        # *   snapshot
        # *   ai
        self.job_type = job_type
        # The ID of the media asset.
        self.media_id = media_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_info_list:
            for v1 in self.job_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobInfoList'] = []
        if self.job_info_list is not None:
            for k1 in self.job_info_list:
                result['JobInfoList'].append(k1.to_map() if k1 else None)

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('JobInfoList') is not None:
            for k1 in m.get('JobInfoList'):
                temp_model = main_models.ListJobInfoResponseBodyJobInfoList()
                self.job_info_list.append(temp_model.from_map(k1))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListJobInfoResponseBodyJobInfoList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        job_id: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # The time when the task was complete.
        self.complete_time = complete_time
        # The time when the task was created. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the task.
        self.job_id = job_id
        # The status of the task.
        self.status = status
        # The ID of the user who submitted the task.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

