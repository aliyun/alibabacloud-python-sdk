# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreatePhoneNoAReportResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CreatePhoneNoAReportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of denied access.
        self.access_denied_detail = access_denied_detail
        # Request status code.
        self.code = code
        # The struct of the A-number filing result.
        self.data = data
        # Error message for failure.
        self.message = message
        # The returned ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # - true: Succeeded.
        # 
        # - false: Failed.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreatePhoneNoAReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreatePhoneNoAReportResponseBodyData(DaraModel):
    def __init__(
        self,
        create_result: bool = None,
        fail_type: int = None,
    ):
        # Creation result. Valid values:
        # 
        # - true: Succeeded.
        # 
        # - false: Failed.
        self.create_result = create_result
        # Enumeration of creation types. A value of 1 indicates success, and negative values indicate creation failure. Valid values:
        # 
        # - 1: Succeeded.
        # 
        # - -1: The mobile phone number has already been submitted for filing; no need to submit again.
        # 
        # - -2: The mobile phone number has already been successfully filed; no need to file again.
        self.fail_type = fail_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_result is not None:
            result['CreateResult'] = self.create_result

        if self.fail_type is not None:
            result['FailType'] = self.fail_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateResult') is not None:
            self.create_result = m.get('CreateResult')

        if m.get('FailType') is not None:
            self.fail_type = m.get('FailType')

        return self

