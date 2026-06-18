# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class AddOrganizationMemberResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddOrganizationMemberResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is empty if the request is successful.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. This parameter is empty if the request is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddOrganizationMemberResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class AddOrganizationMemberResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        seat_assigned: bool = None,
    ):
        # The account ID.
        self.account_id = account_id
        # Indicates whether the seat was successfully assigned.
        self.seat_assigned = seat_assigned

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.seat_assigned is not None:
            result['SeatAssigned'] = self.seat_assigned

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('SeatAssigned') is not None:
            self.seat_assigned = m.get('SeatAssigned')

        return self

