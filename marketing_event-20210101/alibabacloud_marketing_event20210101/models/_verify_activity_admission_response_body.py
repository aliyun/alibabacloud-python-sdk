# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class VerifyActivityAdmissionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VerifyActivityAdmissionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.VerifyActivityAdmissionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class VerifyActivityAdmissionResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        activity_name: str = None,
        address: str = None,
        admission_date: str = None,
        allowed_dates: List[str] = None,
        decision: str = None,
        end_time: str = None,
        masked_id_card_no: str = None,
        name: str = None,
        registration_status: int = None,
        signed_in: bool = None,
        signin_time: str = None,
        start_time: str = None,
    ):
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.address = address
        self.admission_date = admission_date
        self.allowed_dates = allowed_dates
        self.decision = decision
        self.end_time = end_time
        self.masked_id_card_no = masked_id_card_no
        self.name = name
        self.registration_status = registration_status
        self.signed_in = signed_in
        self.signin_time = signin_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.address is not None:
            result['Address'] = self.address

        if self.admission_date is not None:
            result['AdmissionDate'] = self.admission_date

        if self.allowed_dates is not None:
            result['AllowedDates'] = self.allowed_dates

        if self.decision is not None:
            result['Decision'] = self.decision

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.masked_id_card_no is not None:
            result['MaskedIdCardNo'] = self.masked_id_card_no

        if self.name is not None:
            result['Name'] = self.name

        if self.registration_status is not None:
            result['RegistrationStatus'] = self.registration_status

        if self.signed_in is not None:
            result['SignedIn'] = self.signed_in

        if self.signin_time is not None:
            result['SigninTime'] = self.signin_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AdmissionDate') is not None:
            self.admission_date = m.get('AdmissionDate')

        if m.get('AllowedDates') is not None:
            self.allowed_dates = m.get('AllowedDates')

        if m.get('Decision') is not None:
            self.decision = m.get('Decision')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaskedIdCardNo') is not None:
            self.masked_id_card_no = m.get('MaskedIdCardNo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegistrationStatus') is not None:
            self.registration_status = m.get('RegistrationStatus')

        if m.get('SignedIn') is not None:
            self.signed_in = m.get('SignedIn')

        if m.get('SigninTime') is not None:
            self.signin_time = m.get('SigninTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

