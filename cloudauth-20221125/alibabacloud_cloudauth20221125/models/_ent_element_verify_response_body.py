# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20221125 import models as main_models
from darabonba.model import DaraModel

class EntElementVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EntElementVerifyResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Error message
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Result
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
            temp_model = main_models.EntElementVerifyResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self



class EntElementVerifyResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        open_time: str = None,
        reason_code: str = None,
        reason_detail: str = None,
        status: str = None,
    ):
        # Verification result code.
        # - 1: Verification consistent
        # - 2: Verification inconsistent
        # - 3: Not found
        self.biz_code = biz_code
        # Operating period: start and end time of operations.
        # - Format: yyyy-MM-dd/yyyy-MM-dd.
        # - Example: 2018-09-25/9999-09-09.
        self.open_time = open_time
        # ReasonCode explanation:
        # 
        # - 100: Verification consistent
        # 
        # - 201: Inconsistent between person and enterprise
        # 
        # - 202: Inconsistent in two elements of the enterprise
        # 
        # - 301: No enterprise found, unable to verify
        # 
        # - 302: Legal representative does not exist in the database
        # >Warning: This field will be discontinued on June 15, 2023. Existing customers are not affected.
        self.reason_code = reason_code
        # Details of inconsistencies, multiple inconsistencies will be separated by commas.
        # - LegalPersonNameFlag: Inconsistent legal representative name
        # - LegalPersonCertNoFlag: Inconsistent legal representative ID number
        # - EntNameFlag: Inconsistent enterprise name
        # - LicenseNoFlag: Inconsistent business license number
        self.reason_detail = reason_detail
        # Enterprise operating status.
        # - 1: In operation (open)
        # - 2: Relocated
        # - 3: Deregistered
        # - 4: Revoked
        # - 5: Canceled
        # - 6: Suspended
        # - 0: Other
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_detail is not None:
            result['ReasonDetail'] = self.reason_detail

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonDetail') is not None:
            self.reason_detail = m.get('ReasonDetail')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

