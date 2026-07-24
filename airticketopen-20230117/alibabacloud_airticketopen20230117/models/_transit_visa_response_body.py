# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TransitVisaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[main_models.TransitVisaResponseBodyData] = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with an error response.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful HTTP requests.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.TransitVisaResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class TransitVisaResponseBodyData(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        visa_type: int = None,
    ):
        # The three-letter IATA code of the stopover or transfer city.
        self.city_code = city_code
        # The transit visa type. Valid values:
        # - 0: no transit visa required.
        # - 1: transit visa required.
        self.visa_type = visa_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.visa_type is not None:
            result['visa_type'] = self.visa_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('visa_type') is not None:
            self.visa_type = m.get('visa_type')

        return self

