# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class QueryDataTrackResultDownloadStatusResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        status_result: main_models.QueryDataTrackResultDownloadStatusResponseBodyStatusResult = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The information about the download progress.
        self.status_result = status_result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.status_result:
            self.status_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_result is not None:
            result['StatusResult'] = self.status_result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusResult') is not None:
            temp_model = main_models.QueryDataTrackResultDownloadStatusResponseBodyStatusResult()
            self.status_result = temp_model.from_map(m.get('StatusResult'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDataTrackResultDownloadStatusResponseBodyStatusResult(DaraModel):
    def __init__(
        self,
        download_status: str = None,
        download_url: str = None,
        status_desc: str = None,
        total_count: int = None,
    ):
        # The status of the download task. Valid values:
        # 
        # *   **INIT**: The download task is being initialized.
        # *   **LISTING**: The download task is in a transient intermediate state during the initialization.
        # *   **DOWNLOADING**: The download task is being processed.
        # *   **DOWNLOAD_SUCCESS**: The download task was successfully processed.
        # *   **DOWNLOAD_FAIL**: The download task failed.
        self.download_status = download_status
        # The URL that is used to download data tracking logs. This parameter is returned only when the value of DownloadStatus is DOWNLOAD_SUCCESS.
        self.download_url = download_url
        # The description of the state.
        self.status_desc = status_desc
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_status is not None:
            result['DownloadStatus'] = self.download_status

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadStatus') is not None:
            self.download_status = m.get('DownloadStatus')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

