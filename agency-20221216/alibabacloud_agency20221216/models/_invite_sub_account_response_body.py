# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class InviteSubAccountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        results: main_models.InviteSubAccountResponseBodyResults = None,
        success: bool = None,
    ):
        # Error Code: </br>
        # • 200 OK</br>
        # • 1109 System Error</br>
        self.code = code
        # Message</br>
        self.message = message
        # Request ID, Alibaba Cloud will track errors with this ID.
        self.request_id = request_id
        # List of invitation sending results
        self.results = results
        # Candidate Values: True/False, this value states if the current API calling action is successful. It does not guarantee the success of subsequent business operations.
        self.success = success

    def validate(self):
        if self.results:
            self.results.validate()

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

        if self.results is not None:
            result['Results'] = self.results.to_map()

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

        if m.get('Results') is not None:
            temp_model = main_models.InviteSubAccountResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InviteSubAccountResponseBodyResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.InviteSubAccountResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.InviteSubAccountResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class InviteSubAccountResponseBodyResultsResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: main_models.InviteSubAccountResponseBodyResultsResultResult = None,
        success: bool = None,
    ):
        # Error Code, 200 OK
        self.code = code
        # Message, Notes of Code
        self.message = message
        # Returning Message of Invitation Results
        self.result = result
        # Always true.
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
            temp_model = main_models.InviteSubAccountResponseBodyResultsResultResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InviteSubAccountResponseBodyResultsResultResult(DaraModel):
    def __init__(
        self,
        days: int = None,
        invite_id: int = None,
        reg_url: str = None,
    ):
        # Valid days of registration URL, count on daily basis.
        self.days = days
        # Invitation ID, The invitation status tracking code.
        self.invite_id = invite_id
        # URL for Partner Customer Registration.
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

