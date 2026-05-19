# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class InviteSubResellerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        results: List[main_models.InviteSubResellerResponseBodyResults] = None,
        success: bool = None,
    ):
        # Result code.
        self.code = code
        # Message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # 邀请结果信息
        self.results = results
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

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

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.InviteSubResellerResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InviteSubResellerResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: main_models.InviteSubResellerResponseBodyResultsResult = None,
        success: bool = None,
    ):
        # Error code, 200 OK
        self.code = code
        # Prompt message, explanation of the code
        self.message = message
        # Returned invitation result information
        self.result = result
        # Always true
        self.success = success

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            temp_model = main_models.InviteSubResellerResponseBodyResultsResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InviteSubResellerResponseBodyResultsResult(DaraModel):
    def __init__(
        self,
        days: int = None,
        invite_id: int = None,
        reg_url: str = None,
    ):
        # Validity period of the registration URL, in days
        self.days = days
        # Invitation ID, used for querying the invitation status
        self.invite_id = invite_id
        # T2 Reseller registration URL
        self.reg_url = reg_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.invite_id is not None:
            result['InviteId'] = self.invite_id

        if self.reg_url is not None:
            result['RegUrl'] = self.reg_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')

        if m.get('RegUrl') is not None:
            self.reg_url = m.get('RegUrl')

        return self

