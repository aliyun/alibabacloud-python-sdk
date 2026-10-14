# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetC2paSignResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_message: str = None,
        failed_count: int = None,
        http_status_code: int = None,
        message: str = None,
        report_file_url: str = None,
        report_object_key: str = None,
        request_id: str = None,
        signed_file_url: str = None,
        status: str = None,
        succeeded_count: int = None,
        success: bool = None,
        task_id: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        # The business error code for the API call. OK is returned when the call succeeds.
        self.code = code
        # The error code for task failure. This parameter is returned only when Status is FAILED.
        self.error_code = error_code
        # The error message for task failure. This parameter is returned only when Status is FAILED.
        self.error_message = error_message
        # The number of objects that failed to be signed, were skipped, or were terminated in the Bucket task. This parameter is returned only when the Bucket task is in the SUCCEEDED or CANCELED state.
        self.failed_count = failed_count
        # The HTTP status code. 200 is returned when the API call succeeds.
        self.http_status_code = http_status_code
        # The additional information. success is returned when the API call succeeds.
        self.message = message
        # The temporary download URL returned when a Bucket task enters the CANCELED state and the JSON report is successfully generated. The report covers only the objects discovered before termination.
        self.report_file_url = report_file_url
        # The object key of the final standard JSON report for the Bucket task. This parameter is returned only when the Bucket task succeeds.
        self.report_object_key = report_object_key
        # The request ID of the OpenAPI call.
        self.request_id = request_id
        # The temporary download URL of the signature file. This parameter is returned only when Status is SUCCEEDED.
        self.signed_file_url = signed_file_url
        # The task status. Valid values: PROCESSING, SUCCEEDED, and FAILED.
        self.status = status
        # The number of successfully signed objects in the Bucket task. This parameter is returned only when the Bucket task is in the SUCCEEDED or CANCELED state.
        self.succeeded_count = succeeded_count
        # Indicates whether the query call is successful. This value may still be true even if the task itself fails.
        self.success = success
        # The C2PA signing task ID.
        self.task_id = task_id
        # The task type. Valid values: FILE and BUCKET.
        self.task_type = task_type
        # The total number of objects scanned by the Bucket task. This parameter is returned only when the Bucket task is in the SUCCEEDED or CANCELED state.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.report_file_url is not None:
            result['ReportFileUrl'] = self.report_file_url

        if self.report_object_key is not None:
            result['ReportObjectKey'] = self.report_object_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signed_file_url is not None:
            result['SignedFileUrl'] = self.signed_file_url

        if self.status is not None:
            result['Status'] = self.status

        if self.succeeded_count is not None:
            result['SucceededCount'] = self.succeeded_count

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReportFileUrl') is not None:
            self.report_file_url = m.get('ReportFileUrl')

        if m.get('ReportObjectKey') is not None:
            self.report_object_key = m.get('ReportObjectKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignedFileUrl') is not None:
            self.signed_file_url = m.get('SignedFileUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SucceededCount') is not None:
            self.succeeded_count = m.get('SucceededCount')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

