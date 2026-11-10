# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayQuotaRuleSubjectUsageExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID of this OpenAPI query call, which is used to troubleshoot call issues. This is different from the request_id of each consumption record in the exported file.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        gateway_id: str = None,
        processed_count: int = None,
        result: main_models.GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyDataResult = None,
        rule_id: str = None,
        status: str = None,
        subject_id: str = None,
        subject_name: str = None,
        task_id: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        # The error summary when the task fails, which is used to troubleshoot issues such as disabled logs, query failures, exceeded detail limits, processing timeouts, or file generation failures. This field may be omitted when no errors occur.
        self.error_message = error_message
        # The gateway ID recorded when the task was created.
        self.gateway_id = gateway_id
        # The number of detail rows written to the exported file, excluding the header. This value is used to check the processing progress. Even if this value equals totalCount, you should determine whether the file is downloadable based on status=Success.
        self.processed_count = processed_count
        # The export conditions and file results determined when the task was created. The time range, format, and metering dimension may be returned even in non-Success states. File and download information is available only after success. Fields with values of 0, false, or empty strings are omitted.
        self.result = result
        # The quota rule ID recorded when the task was created.
        self.rule_id = rule_id
        # The current status of the task. Valid values:
        # - Pending: The task is submitted and waiting to be processed.
        # - Running: The task is querying details, generating files, or uploading files.
        # - Success: The file is generated and uploaded. You still need to check whether the file is expired.
        # - Failed: The task failed. For the cause, see errorMessage.
        # 
        # Tasks that are not completed within 10 minutes after creation are processed as Failed. After a file expires, the task remains in the Success state.
        self.status = status
        # The consumer or consumer group ID recorded when the task was created.
        self.subject_id = subject_id
        # The subject name recorded when the task was created, which is used to match consumption logs. Subsequent changes to the subject name do not modify the name recorded for this task.
        self.subject_name = subject_name
        # The export task ID, which is the same as the taskId request parameter.
        self.task_id = task_id
        # The task type. The value is fixed as FinOpsUsageDetailExport, which indicates the export of quota rule subject consumption details.
        self.task_type = task_type
        # The total number of detail rows to be exported as counted by backend queries, excluding the CSV header. This value may be 0 before the counting is completed. You cannot determine whether the result is empty or the task is completed based solely on this value.
        self.total_count = total_count

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.processed_count is not None:
            result['processedCount'] = self.processed_count

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.status is not None:
            result['status'] = self.status

        if self.subject_id is not None:
            result['subjectId'] = self.subject_id

        if self.subject_name is not None:
            result['subjectName'] = self.subject_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('processedCount') is not None:
            self.processed_count = m.get('processedCount')

        if m.get('result') is not None:
            temp_model = main_models.GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subjectId') is not None:
            self.subject_id = m.get('subjectId')

        if m.get('subjectName') is not None:
            self.subject_name = m.get('subjectName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetGatewayQuotaRuleSubjectUsageExportTaskResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        download_url_expired_at: int = None,
        effective_window_start: int = None,
        file_expired: bool = None,
        file_expired_at: int = None,
        file_size: int = None,
        filter_failed_requests: bool = None,
        format: str = None,
        query_window_end: int = None,
        query_window_start: int = None,
        quota_dimension: str = None,
        row_count: int = None,
    ):
        # The temporary signed download URL of the exported file. It is returned only when status=Success and the file is not expired. It is dynamically generated for each query and is valid for 10 minutes from the generation time. If the link expires but fileExpiredAt is not reached, you can call this operation again to obtain the link. You do not need to pass the internal storage path as a request parameter.
        self.download_url = download_url
        # The expiration time of the downloadUrl returned in this response. It is a UNIX timestamp in seconds. It is provided only when a download link is returned and is approximately 10 minutes after the link generation time. It can be updated by querying again and cannot be used to replace fileExpiredAt.
        self.download_url_expired_at = download_url_expired_at
        # The start time of the actual export time range. It is a UNIX timestamp in seconds. The actual start time is also limited by the rule creation time, rule reset, or the effective start time of clearing history records. No details are available if the start time is not earlier than the end time.
        self.effective_window_start = effective_window_start
        # Indicates whether the exported file has exceeded the server-side period for providing download links. A value of true indicates that the file has expired, downloadUrl and downloadUrlExpiredAt are not returned, and you need to create a new export task. This field may be omitted when the value is false. To determine whether the file is downloadable, check both status and downloadUrl.
        self.file_expired = file_expired
        # The time when the file stops providing new download links. It is a UNIX timestamp in seconds and is usually 24 hours after the file is successfully uploaded. After this time, this operation returns fileExpired=true and no longer generates downloadUrl. The task remains in the Success state. This time is different from the downloadUrlExpiredAt of a single signed link.
        self.file_expired_at = file_expired_at
        # The size of the successfully generated and uploaded GZIP compressed file, in bytes. This field may be omitted when the task is not successful.
        self.file_size = file_size
        # Specifies whether to filter out requests with failed or zero usage, which is specified when the task is created. A value of true filters out records with 0 usage and retains only records with usage. This field may be omitted when the value is false.
        self.filter_failed_requests = filter_failed_requests
        # The format of the exported file. The value is currently fixed as CSV_GZIP. The downloaded file is a .csv.gz file, which becomes a CSV file after decompression.
        self.format = format
        # The end time of the request time range determined when the task was created. It is a UNIX timestamp in seconds and does not include this moment. If no time range is specified, this value is the task creation time and is not updated when the task is queried.
        self.query_window_end = query_window_end
        # The start time of the request time range determined when the task was created. It is a UNIX timestamp in seconds and includes this moment. If only one time parameter is passed, this value may be derived from the rule period. For the actual export start time, see effectiveWindowStart.
        self.query_window_start = query_window_start
        # The quota metering dimension determined when the task was created. token indicates token usage, and credit indicates credit usage. The CSV file outputs the corresponding columns based on this dimension. Credit usage retains decimal places.
        self.quota_dimension = quota_dimension
        # The number of successfully exported consumption detail rows, excluding the CSV header. This field may be omitted when the task is not successful or the export result contains 0 rows. If the task is successful but no matching details exist, the file contains only the header.
        self.row_count = row_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.download_url_expired_at is not None:
            result['downloadUrlExpiredAt'] = self.download_url_expired_at

        if self.effective_window_start is not None:
            result['effectiveWindowStart'] = self.effective_window_start

        if self.file_expired is not None:
            result['fileExpired'] = self.file_expired

        if self.file_expired_at is not None:
            result['fileExpiredAt'] = self.file_expired_at

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.filter_failed_requests is not None:
            result['filterFailedRequests'] = self.filter_failed_requests

        if self.format is not None:
            result['format'] = self.format

        if self.query_window_end is not None:
            result['queryWindowEnd'] = self.query_window_end

        if self.query_window_start is not None:
            result['queryWindowStart'] = self.query_window_start

        if self.quota_dimension is not None:
            result['quotaDimension'] = self.quota_dimension

        if self.row_count is not None:
            result['rowCount'] = self.row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('downloadUrlExpiredAt') is not None:
            self.download_url_expired_at = m.get('downloadUrlExpiredAt')

        if m.get('effectiveWindowStart') is not None:
            self.effective_window_start = m.get('effectiveWindowStart')

        if m.get('fileExpired') is not None:
            self.file_expired = m.get('fileExpired')

        if m.get('fileExpiredAt') is not None:
            self.file_expired_at = m.get('fileExpiredAt')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('filterFailedRequests') is not None:
            self.filter_failed_requests = m.get('filterFailedRequests')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('queryWindowEnd') is not None:
            self.query_window_end = m.get('queryWindowEnd')

        if m.get('queryWindowStart') is not None:
            self.query_window_start = m.get('queryWindowStart')

        if m.get('quotaDimension') is not None:
            self.quota_dimension = m.get('quotaDimension')

        if m.get('rowCount') is not None:
            self.row_count = m.get('rowCount')

        return self

