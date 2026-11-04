# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryStreamPushJobListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryStreamPushJobListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # - **200**: The call was successful.
        # - Other values: error codes. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The data returned if the call is successful.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.QueryStreamPushJobListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryStreamPushJobListResponseBodyData(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.QueryStreamPushJobListResponseBodyDataJobList] = None,
        total: int = None,
    ):
        # The job list information.
        self.job_list = job_list
        # The total number of jobs.
        self.total = total

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.QueryStreamPushJobListResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryStreamPushJobListResponseBodyDataJobList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        job_id: str = None,
        job_type: int = None,
        push_status: int = None,
        push_url: str = None,
        stream_type: int = None,
    ):
        # The time when the job was created. Unit: seconds.
        self.create_time = create_time
        # The ID of the job.
        self.job_id = job_id
        # The type of the stream push job. Valid values:
        # 
        # - **1**: continuous job.
        # - **2**: triggered job. The job ends after it is interrupted.
        self.job_type = job_type
        # The current stream push status. Valid values:
        # 
        # - **1**: pushing.
        # - **2**: waiting to push.
        # - **3**: push ended.
        self.push_status = push_status
        # The stream push URL.
        self.push_url = push_url
        # The stream type. Valid values:
        # 
        # - **0**: main stream.
        # - **1**: sub stream.
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.push_status is not None:
            result['PushStatus'] = self.push_status

        if self.push_url is not None:
            result['PushUrl'] = self.push_url

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')

        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

