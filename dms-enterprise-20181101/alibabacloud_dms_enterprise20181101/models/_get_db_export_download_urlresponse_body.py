# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDbExportDownloadURLResponseBody(DaraModel):
    def __init__(
        self,
        download_urlresult: main_models.GetDbExportDownloadURLResponseBodyDownloadURLResult = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The download URL of the exported file.
        self.download_urlresult = download_urlresult
        # The error code returned.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request succeeded.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.download_urlresult:
            self.download_urlresult.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_urlresult is not None:
            result['DownloadURLResult'] = self.download_urlresult.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadURLResult') is not None:
            temp_model = main_models.GetDbExportDownloadURLResponseBodyDownloadURLResult()
            self.download_urlresult = temp_model.from_map(m.get('DownloadURLResult'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDbExportDownloadURLResponseBodyDownloadURLResult(DaraModel):
    def __init__(
        self,
        has_result: bool = None,
        tip_message: str = None,
        url: str = None,
    ):
        # Indicates whether export results are available for download. Valid values:
        # 
        # *   **true**: Export results are available for download.
        # *   **false**: No export results are available for download.
        self.has_result = has_result
        # The message that indicates an exception.
        self.tip_message = tip_message
        # The download URL of the exported file.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_result is not None:
            result['HasResult'] = self.has_result

        if self.tip_message is not None:
            result['TipMessage'] = self.tip_message

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasResult') is not None:
            self.has_result = m.get('HasResult')

        if m.get('TipMessage') is not None:
            self.tip_message = m.get('TipMessage')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

