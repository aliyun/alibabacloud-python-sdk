# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataTrackJobDegreeResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_degree: main_models.GetDataTrackJobDegreeResponseBodyJobDegree = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The progress details of the data tracking task.
        self.job_degree = job_degree
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.job_degree:
            self.job_degree.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_degree is not None:
            result['JobDegree'] = self.job_degree.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobDegree') is not None:
            temp_model = main_models.GetDataTrackJobDegreeResponseBodyJobDegree()
            self.job_degree = temp_model.from_map(m.get('JobDegree'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataTrackJobDegreeResponseBodyJobDegree(DaraModel):
    def __init__(
        self,
        download_completion_degree: float = None,
        filter_completion_degree: float = None,
        job_status: str = None,
        list_completion_degree: float = None,
        status_desc: str = None,
    ):
        # The progress of binary log download. Valid values: 0 to 1. A value of 1 indicates that binary log download is complete.
        self.download_completion_degree = download_completion_degree
        # The progress of binary log parsing. Valid values: 0 to 1. A value of 1 indicates that binary log parsing is complete.
        self.filter_completion_degree = filter_completion_degree
        # The status of the data tracking task. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **LISTING**: The binary logs are being obtained.
        # *   **LIST_SUCCESS**: The binary logs are successfully obtained.
        # *   **DOWNLOADING**: The binary logs are being downloaded.
        # *   **DOWNLOAD_FAIL**: The binary logs failed to be downloaded.
        # *   **DOWNLOAD_SUCCESS**: The binary logs are successfully downloaded.
        # *   **FILTERING**: The binary logs are being parsed.
        # *   **FILTER_FAIL**: The binary logs failed to be parsed.
        # *   **FILTER_SUCCESS**: The binary logs are successfully parsed.
        self.job_status = job_status
        # The progress of binary log obtaining. Valid values: 0 to 1. A value of 1 indicates that binary log obtaining is complete.
        self.list_completion_degree = list_completion_degree
        # The description of the task status.
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_completion_degree is not None:
            result['DownloadCompletionDegree'] = self.download_completion_degree

        if self.filter_completion_degree is not None:
            result['FilterCompletionDegree'] = self.filter_completion_degree

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.list_completion_degree is not None:
            result['ListCompletionDegree'] = self.list_completion_degree

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadCompletionDegree') is not None:
            self.download_completion_degree = m.get('DownloadCompletionDegree')

        if m.get('FilterCompletionDegree') is not None:
            self.filter_completion_degree = m.get('FilterCompletionDegree')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('ListCompletionDegree') is not None:
            self.list_completion_degree = m.get('ListCompletionDegree')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

