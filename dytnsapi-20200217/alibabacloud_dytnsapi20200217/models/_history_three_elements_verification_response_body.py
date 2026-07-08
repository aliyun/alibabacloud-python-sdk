# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class HistoryThreeElementsVerificationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.HistoryThreeElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Details about why access is denied.
        # 
        # > This parameter is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The status code of the request.
        # 
        # - A value of `OK` indicates the request was successful.
        # 
        # - For other values, see the Error Codes section.
        self.code = code
        # The query results.
        self.data = data
        # The description of the status code.
        self.message = message
        # The request ID.
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
            temp_model = main_models.HistoryThreeElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class HistoryThreeElementsVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        is_consistent: int = None,
        request_carrier: str = None,
    ):
        # The consistency of the verification result. Valid values:
        # 
        # - `0`: No record found.
        # 
        # - `1`: The phone number, ID number, and name match the carrier\\"s records.
        # 
        # - `2`: The phone number and ID number match the carrier\\"s records, but the name does not.
        # 
        # - `3`: The phone number and name match the carrier\\"s records, but the ID number does not.
        # 
        # - `4`: The phone number matches the carrier\\"s records, but the name and ID number do not.
        self.is_consistent = is_consistent
        # The carrier to which the request was routed.
        self.request_carrier = request_carrier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent

        if self.request_carrier is not None:
            result['RequestCarrier'] = self.request_carrier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')

        if m.get('RequestCarrier') is not None:
            self.request_carrier = m.get('RequestCarrier')

        return self

