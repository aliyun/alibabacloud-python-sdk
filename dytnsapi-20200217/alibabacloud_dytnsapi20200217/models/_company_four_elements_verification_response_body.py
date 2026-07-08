# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class CompanyFourElementsVerificationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CompanyFourElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The request status code.
        self.code = code
        # The structure.
        self.data = data
        # The description of the returned status code.
        self.message = message
        # The common parameter. The ID returned for each request is unique and can be used to troubleshoot and locate issues.
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
            temp_model = main_models.CompanyFourElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CompanyFourElementsVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_info: main_models.CompanyFourElementsVerificationResponseBodyDataDetailInfo = None,
        inconsistent_data: List[str] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        # The enterprise details.
        self.detail_info = detail_info
        # The fields that failed verification.
        self.inconsistent_data = inconsistent_data
        # The verification result code. Valid values:
        # 
        # - 0: Verification passed.
        # - 1: Verification passed, but the enterprise is not operating normally.
        # - 2: The legal person and enterprise information are inconsistent.
        # - 3: The enterprise four-element verification failed.
        # - 4: The enterprise was not found.
        # - 5: The legal person was not found in the database.
        self.reason_code = reason_code
        # The verification result. Valid values:
        # -   true: The information is consistent and the enterprise is operating normally.
        # -   false: Verification failed.
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
            temp_model = main_models.CompanyFourElementsVerificationResponseBodyDataDetailInfo()
            self.detail_info = temp_model.from_map(m.get('DetailInfo'))

        if m.get('InconsistentData') is not None:
            self.inconsistent_data = m.get('InconsistentData')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

class CompanyFourElementsVerificationResponseBodyDataDetailInfo(DaraModel):
    def __init__(
        self,
        enterprise_status: str = None,
        open_time: str = None,
    ):
        # The operating status of the enterprise.
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

