# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetAgentMJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentMJobInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of **200** indicates success. Any other value indicates failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: The request was successful.
        # - false/null: The request failed.
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
            temp_model = main_models.GetAgentMJobInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgentMJobInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_mdetail_response: main_models.GetAgentMJobInfoResponseBodyDataAgentMDetailResponse = None,
        data_end_time: str = None,
        data_start_time: str = None,
        id: int = None,
        message: str = None,
        status: str = None,
        task_end_time: str = None,
        task_id: str = None,
        task_start_time: str = None,
    ):
        # The details of the task processing result.
        self.agent_mdetail_response = agent_mdetail_response
        # The end time of the scan range.
        self.data_end_time = data_end_time
        # The start time of the scan range.
        self.data_start_time = data_start_time
        # The task ID.
        self.id = id
        # The error message returned when an error occurs.
        self.message = message
        # The task status. Valid values:
        # - queing: queuing.
        # - readyAnalysis: pending analysis.
        # - running: running.
        # - error: failed.
        # - finish: completed.
        # - fileUploadUser: user-specified file upload completed.
        # - fileUploadSystem: system-generated file upload completed.
        # - expired: expired.
        self.status = status
        # The actual end time of the task.
        self.task_end_time = task_end_time
        # The scheduled task ID.
        self.task_id = task_id
        # The actual start time of the task.
        self.task_start_time = task_start_time

    def validate(self):
        if self.agent_mdetail_response:
            self.agent_mdetail_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_mdetail_response is not None:
            result['AgentMDetailResponse'] = self.agent_mdetail_response.to_map()

        if self.data_end_time is not None:
            result['DataEndTime'] = self.data_end_time

        if self.data_start_time is not None:
            result['DataStartTime'] = self.data_start_time

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentMDetailResponse') is not None:
            temp_model = main_models.GetAgentMJobInfoResponseBodyDataAgentMDetailResponse()
            self.agent_mdetail_response = temp_model.from_map(m.get('AgentMDetailResponse'))

        if m.get('DataEndTime') is not None:
            self.data_end_time = m.get('DataEndTime')

        if m.get('DataStartTime') is not None:
            self.data_start_time = m.get('DataStartTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        return self

class GetAgentMJobInfoResponseBodyDataAgentMDetailResponse(DaraModel):
    def __init__(
        self,
        summary: str = None,
        summary_urls: List[main_models.GetAgentMJobInfoResponseBodyDataAgentMDetailResponseSummaryUrls] = None,
    ):
        # The execution summary.
        self.summary = summary
        # The list of result files. Each item contains complete file fields.
        self.summary_urls = summary_urls

    def validate(self):
        if self.summary_urls:
            for v1 in self.summary_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary is not None:
            result['Summary'] = self.summary

        result['SummaryUrls'] = []
        if self.summary_urls is not None:
            for k1 in self.summary_urls:
                result['SummaryUrls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        self.summary_urls = []
        if m.get('SummaryUrls') is not None:
            for k1 in m.get('SummaryUrls'):
                temp_model = main_models.GetAgentMJobInfoResponseBodyDataAgentMDetailResponseSummaryUrls()
                self.summary_urls.append(temp_model.from_map(k1))

        return self

class GetAgentMJobInfoResponseBodyDataAgentMDetailResponseSummaryUrls(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: str = None,
        oss_url: str = None,
    ):
        # The file name.
        self.file_name = file_name
        # The file type.
        self.file_type = file_type
        # The file URL.
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        return self

