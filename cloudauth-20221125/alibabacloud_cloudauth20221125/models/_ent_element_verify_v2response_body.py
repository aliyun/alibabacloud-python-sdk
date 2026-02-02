# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20221125 import models as main_models
from darabonba.model import DaraModel

class EntElementVerifyV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EntElementVerifyV2ResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Error message
        self.message = message
        # Id of the request
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
            temp_model = main_models.EntElementVerifyV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class EntElementVerifyV2ResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        open_time: str = None,
        reason_detail: str = None,
        status: str = None,
    ):
        # Verification result code.
        # - 1: Verification consistent
        # - 2: Verification inconsistent
        # - 3: Not found
        self.biz_code = biz_code
        # Business term: start and end time of operations.
        # - Format: yyyy-MM-dd/yyyy-MM-dd.
        # - Example: 2018-09-25/9999-09-09.
        self.open_time = open_time
        # Details of inconsistencies, multiple inconsistencies will be separated by commas.
        # - LegalPersonNameFlag: Legal person\\"s name does not match
        # - LegalPersonCertNoFlag: Legal person\\"s ID number does not match
        # - EntNameFlag: Enterprise name does not match
        # - LicenseNoFlag: Business license number does not match
        self.reason_detail = reason_detail
        # Business operation status.
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

        if m.get('ReasonDetail') is not None:
            self.reason_detail = m.get('ReasonDetail')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

