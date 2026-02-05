# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeJobDataParsingTaskProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        progress: main_models.DescribeJobDataParsingTaskProgressResponseBodyProgress = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.progress = progress
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.progress:
            self.progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            temp_model = main_models.DescribeJobDataParsingTaskProgressResponseBodyProgress()
            self.progress = temp_model.from_map(m.get('Progress'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeJobDataParsingTaskProgressResponseBodyProgress(DaraModel):
    def __init__(
        self,
        fail_error_code: str = None,
        fail_reason: str = None,
        feedback_url: str = None,
        handled_job_count: int = None,
        status: str = None,
        total_job_count: int = None,
    ):
        self.fail_error_code = fail_error_code
        self.fail_reason = fail_reason
        self.feedback_url = feedback_url
        self.handled_job_count = handled_job_count
        self.status = status
        self.total_job_count = total_job_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_error_code is not None:
            result['FailErrorCode'] = self.fail_error_code

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.feedback_url is not None:
            result['FeedbackUrl'] = self.feedback_url

        if self.handled_job_count is not None:
            result['HandledJobCount'] = self.handled_job_count

        if self.status is not None:
            result['Status'] = self.status

        if self.total_job_count is not None:
            result['TotalJobCount'] = self.total_job_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailErrorCode') is not None:
            self.fail_error_code = m.get('FailErrorCode')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('FeedbackUrl') is not None:
            self.feedback_url = m.get('FeedbackUrl')

        if m.get('HandledJobCount') is not None:
            self.handled_job_count = m.get('HandledJobCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalJobCount') is not None:
            self.total_job_count = m.get('TotalJobCount')

        return self

