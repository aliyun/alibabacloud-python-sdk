# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetSmartClipTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSmartClipTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # Task response
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Error description
        self.message = message
        # Unique identifier of the request
        self.request_id = request_id
        # Indicates whether the operation succeeded. true indicates success. false indicates failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSmartClipTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSmartClipTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        status: str = None,
        sub_jobs: List[main_models.GetSmartClipTaskResponseBodyDataSubJobs] = None,
    ):
        # Error message
        self.error_message = error_message
        # Task status:
        # PENDING: Pending
        # RUNNING: Running
        # SUCCESSED: Succeeded
        # FAILED: Failed
        # CANCELED: Canceled
        self.status = status
        # List of subtasks
        self.sub_jobs = sub_jobs

    def validate(self):
        if self.sub_jobs:
            for v1 in self.sub_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        result['SubJobs'] = []
        if self.sub_jobs is not None:
            for k1 in self.sub_jobs:
                result['SubJobs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_jobs = []
        if m.get('SubJobs') is not None:
            for k1 in m.get('SubJobs'):
                temp_model = main_models.GetSmartClipTaskResponseBodyDataSubJobs()
                self.sub_jobs.append(temp_model.from_map(k1))

        return self

class GetSmartClipTaskResponseBodyDataSubJobs(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        file_attr: main_models.GetSmartClipTaskResponseBodyDataSubJobsFileAttr = None,
        file_key: str = None,
        status: str = None,
        sub_job_id: str = None,
    ):
        # Error message
        self.error_message = error_message
        # File attributes
        self.file_attr = file_attr
        # File key
        self.file_key = file_key
        # Subtask status:
        # PENDING: Pending
        # RUNNING: Running
        # SUCCESSED: Succeeded
        # FAILED: Failed
        # CANCELED: Canceled
        self.status = status
        # Subtask ID
        self.sub_job_id = sub_job_id

    def validate(self):
        if self.file_attr:
            self.file_attr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_attr is not None:
            result['FileAttr'] = self.file_attr.to_map()

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_job_id is not None:
            result['SubJobId'] = self.sub_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileAttr') is not None:
            temp_model = main_models.GetSmartClipTaskResponseBodyDataSubJobsFileAttr()
            self.file_attr = temp_model.from_map(m.get('FileAttr'))

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubJobId') is not None:
            self.sub_job_id = m.get('SubJobId')

        return self

class GetSmartClipTaskResponseBodyDataSubJobsFileAttr(DaraModel):
    def __init__(
        self,
        duration: float = None,
        file_length: str = None,
        file_name: str = None,
        height: int = None,
        tmp_url: str = None,
        width: int = None,
    ):
        # Video duration in seconds
        self.duration = duration
        # Video file size
        self.file_length = file_length
        # Video file name
        self.file_name = file_name
        # Video height
        self.height = height
        # Temporary URL to access the video file. Expires in one hour.
        self.tmp_url = tmp_url
        # Video width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_length is not None:
            result['FileLength'] = self.file_length

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.height is not None:
            result['Height'] = self.height

        if self.tmp_url is not None:
            result['TmpUrl'] = self.tmp_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileLength') is not None:
            self.file_length = m.get('FileLength')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('TmpUrl') is not None:
            self.tmp_url = m.get('TmpUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

