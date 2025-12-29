# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class CompanyThreeElementsVerificationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CompanyThreeElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CompanyThreeElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CompanyThreeElementsVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_info: main_models.CompanyThreeElementsVerificationResponseBodyDataDetailInfo = None,
        inconsistent_data: List[str] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        # The information about the enterprise.
        self.detail_info = detail_info
        # The fields to be verified.
        self.inconsistent_data = inconsistent_data
        # The code of the verification result. Valid values:
        # 
        # *   0: The three elements belong to the same enterprise.
        # *   1: The three elements belong to the same enterprise, and the business status of the enterprise is abnormal.
        # *   2: The legal representative information cannot match the enterprise information.
        # *   3: The three elements do not belong to the same enterprise.
        # *   4: No information about the enterprise is found.
        # *   5: No information about the legal representative is found.
        self.reason_code = reason_code
        # The verification result. Valid values:
        # 
        # *   true: The three elements belong to the same enterprise and the business status of the enterprise is Active.
        # *   false: The three elements do not belong to the same enterprise.
        self.verify_result = verify_result

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()

        if self.inconsistent_data is not None:
            result['InconsistentData'] = self.inconsistent_data

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = main_models.CompanyThreeElementsVerificationResponseBodyDataDetailInfo()
            self.detail_info = temp_model.from_map(m.get('DetailInfo'))

        if m.get('InconsistentData') is not None:
            self.inconsistent_data = m.get('InconsistentData')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

class CompanyThreeElementsVerificationResponseBodyDataDetailInfo(DaraModel):
    def __init__(
        self,
        enterprise_status: str = None,
        open_time: str = None,
    ):
        # The business status of the enterprise.
        self.enterprise_status = enterprise_status
        # The business term of the enterprise.
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_status is not None:
            result['EnterpriseStatus'] = self.enterprise_status

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseStatus') is not None:
            self.enterprise_status = m.get('EnterpriseStatus')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        return self

