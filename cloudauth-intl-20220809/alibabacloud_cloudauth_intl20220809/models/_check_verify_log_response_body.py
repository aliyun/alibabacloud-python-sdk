# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class CheckVerifyLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CheckVerifyLogResponseBodyResult = None,
    ):
        # The backend error code.
        self.code = code
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CheckVerifyLogResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CheckVerifyLogResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_info: str = None,
        interrupt_page: str = None,
        interrupt_page_en: str = None,
        log_info: List[str] = None,
        log_info_en: List[str] = None,
        log_statistics_info: str = None,
        passed: str = None,
        sub_code: str = None,
        verify_error_code: str = None,
        verify_status: str = None,
    ):
        # The extended information.
        self.ext_info = ext_info
        # The last page where the authentication was interrupted. Valid values:
        # 
        # - The page is not started.
        # - The OCR guide page.
        # - The OCR camera authorization page.
        # - The OCR document capture page.
        # - The OCR recognition loading page.
        # - The OCR recognition result editing page.
        # - The OCR recognition result editing loading page.
        # - The liveness detection guide page.
        # - The liveness detection camera authorization page.
        # - The liveness detection page.
        # - The liveness detection fallback page.
        # - The liveness detection retry page.
        # - The liveness detection loading page.
        self.interrupt_page = interrupt_page
        # The last page where the authentication was interrupted, in English. Valid values:
        # 
        # - LOADING
        # 
        # - GUIDE
        # 
        # - FACE
        # 
        # - OCR_SCAN
        # 
        # - OCR_RESULT
        # 
        # - NFC_INPUT
        # 
        # - NFC_READ
        self.interrupt_page_en = interrupt_page_en
        # The details of the SDK runtime logs.
        self.log_info = log_info
        # The details of the SDK runtime trace logs in English. The format of this field is the same as that of **LogInfo**.
        self.log_info_en = log_info_en
        # The statistical details of the SDK runtime logs.
        self.log_statistics_info = log_statistics_info
        # Indicates whether the authentication is passed. Valid values:
        # 
        # - Y: Passed.
        # - N: Not passed.
        self.passed = passed
        # The sub-result code.
        self.sub_code = sub_code
        # The error code for authentication interruption. Valid values:
        # 
        # - 1000: The user completed the face scanning process, and the recommended authentication result is passed.
        # - 1001: The user completed the face scanning process, and the recommended authentication result is not passed.
        # - 1002: A system error occurred.
        # - 1003: SDK initialization failed. Check whether the client time is correct.
        # - 1004: A camera permission error occurred.
        # - 1005: A network error occurred.
        # - 1006: The user exited.
        # - 1007: The TransactionId is invalid.
        # - 1009: The client timestamp is incorrect.
        # - 1011: The submitted document type is incorrect.
        # - 1012: The recognized key information of the document is missing or the format verification failed.
        # - 1013: The image quality is poor.
        # - 1014: The number of errors exceeded the upper limit.
        # - 1015: The Android system version is too low.
        # - 1016: Camera permissions are not obtained.
        # - 9999: The authentication process is suspected to be interrupted.
        self.verify_error_code = verify_error_code
        # The authentication status. Valid values:
        # 
        # - 0: finished. The authentication is completed.
        # - 1: unfinished. The authentication is interrupted.
        # - 2: notstart. The authentication is not started.
        self.verify_status = verify_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.interrupt_page is not None:
            result['InterruptPage'] = self.interrupt_page

        if self.interrupt_page_en is not None:
            result['InterruptPageEn'] = self.interrupt_page_en

        if self.log_info is not None:
            result['LogInfo'] = self.log_info

        if self.log_info_en is not None:
            result['LogInfoEn'] = self.log_info_en

        if self.log_statistics_info is not None:
            result['LogStatisticsInfo'] = self.log_statistics_info

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.verify_error_code is not None:
            result['VerifyErrorCode'] = self.verify_error_code

        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('InterruptPage') is not None:
            self.interrupt_page = m.get('InterruptPage')

        if m.get('InterruptPageEn') is not None:
            self.interrupt_page_en = m.get('InterruptPageEn')

        if m.get('LogInfo') is not None:
            self.log_info = m.get('LogInfo')

        if m.get('LogInfoEn') is not None:
            self.log_info_en = m.get('LogInfoEn')

        if m.get('LogStatisticsInfo') is not None:
            self.log_statistics_info = m.get('LogStatisticsInfo')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('VerifyErrorCode') is not None:
            self.verify_error_code = m.get('VerifyErrorCode')

        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')

        return self

