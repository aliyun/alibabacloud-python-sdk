# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeJobErrorCodeResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        item: main_models.DescribeJobErrorCodeResponseBodyItem = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the error code.
        self.item = item
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.item is not None:
            result['Item'] = self.item.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Item') is not None:
            temp_model = main_models.DescribeJobErrorCodeResponseBodyItem()
            self.item = temp_model.from_map(m.get('Item'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeJobErrorCodeResponseBodyItem(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        job_state: str = None,
        job_type: str = None,
        language: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The standardized error message.
        self.error_message = error_message
        # The ID of the full backup or restore job.
        self.job_id = job_id
        # The state of the job.
        self.job_state = job_state
        # The internal job type ID in DBS.
        self.job_type = job_type
        # The language of the error message.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_state is not None:
            result['JobState'] = self.job_state

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

