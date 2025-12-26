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
        # Backend error code.
        self.code = code
        # Return message
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result.
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
        # Extended information
        self.ext_info = ext_info
        # Records the last page where the authentication was interrupted.
        # 
        # - Page not started
        # - OCR guide page
        # - OCR camera authorization
        # - OCR document capture page
        # - OCR recognition loading
        # - OCR recognition result editing page
        # - OCR recognition result editing loading
        # - Liveness detection guide page
        # - Liveness detection camera authorization page
        # - Liveness detection page
        # - Liveness detection fallback page
        # - Liveness detection retry
        # - Liveness detection loading
        self.interrupt_page = interrupt_page
        # The page where the authentication process stops. Possible English values:
        # 
        # The following are the values in an unordered list:
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
        # SDK operation log details
        self.log_info = log_info
        # SDK Operation Log Details (English Version)
        self.log_info_en = log_info_en
        # SDK operation log statistics details
        self.log_statistics_info = log_statistics_info
        # Whether the authentication passed.
        # 
        # - Y: Passed.
        # - N: Not passed.
        self.passed = passed
        # Sub-result code
        self.sub_code = sub_code
        # Authentication interruption error codes
        # 
        # - 1000: The user completed the face scanning process, and the suggested authentication result is pass
        # - 1001: The user completed the face scanning process, and the suggested authentication result is fail
        # - 1002: System error
        # - 1003: SDK initialization failed, please check if the client time is correct
        # - 1004: Camera permission error
        # - 1005: Network error
        # - 1006: User exited
        # - 1007: Invalid TransactionId
        # - 1009: Client timestamp error
        # - 1011: Incorrect document type submitted
        # - 1012: Missing or format validation failure of key information on the recognized document
        # - 1013: Poor image quality
        # - 1014: Exceeded the upper limit of errors
        # - 1015: Android system version too low
        # - 1016: Camera permission not obtained
        # - 9999: Suspected authentication process interruption
        self.verify_error_code = verify_error_code
        # Authentication status, values:
        # 
        # - 0: finished (authentication completed)
        # - 1: unfinished (authentication interrupted)
        # - 2: notstart (authentication not started)
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

