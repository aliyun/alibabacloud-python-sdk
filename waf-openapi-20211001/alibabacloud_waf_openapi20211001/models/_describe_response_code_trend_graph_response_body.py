# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeResponseCodeTrendGraphResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response_codes: List[main_models.DescribeResponseCodeTrendGraphResponseBodyResponseCodes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the statistics of the error codes.
        self.response_codes = response_codes

    def validate(self):
        if self.response_codes:
            for v1 in self.response_codes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResponseCodes'] = []
        if self.response_codes is not None:
            for k1 in self.response_codes:
                result['ResponseCodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.response_codes = []
        if m.get('ResponseCodes') is not None:
            for k1 in m.get('ResponseCodes'):
                temp_model = main_models.DescribeResponseCodeTrendGraphResponseBodyResponseCodes()
                self.response_codes.append(temp_model.from_map(k1))

        return self

class DescribeResponseCodeTrendGraphResponseBodyResponseCodes(DaraModel):
    def __init__(
        self,
        code_302pv: int = None,
        code_405pv: int = None,
        code_444pv: int = None,
        code_499pv: int = None,
        code_5xx_pv: int = None,
        index: int = None,
    ):
        # The number of 302 error codes that are returned.
        self.code_302pv = code_302pv
        # The number of 405 error codes that are returned.
        self.code_405pv = code_405pv
        # The number of 444 error codes that are returned.
        self.code_444pv = code_444pv
        # The number of 499 error codes that are returned.
        self.code_499pv = code_499pv
        # The number of 5xx error codes that are returned.
        self.code_5xx_pv = code_5xx_pv
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_302pv is not None:
            result['302Pv'] = self.code_302pv

        if self.code_405pv is not None:
            result['405Pv'] = self.code_405pv

        if self.code_444pv is not None:
            result['444Pv'] = self.code_444pv

        if self.code_499pv is not None:
            result['499Pv'] = self.code_499pv

        if self.code_5xx_pv is not None:
            result['5xxPv'] = self.code_5xx_pv

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('302Pv') is not None:
            self.code_302pv = m.get('302Pv')

        if m.get('405Pv') is not None:
            self.code_405pv = m.get('405Pv')

        if m.get('444Pv') is not None:
            self.code_444pv = m.get('444Pv')

        if m.get('499Pv') is not None:
            self.code_499pv = m.get('499Pv')

        if m.get('5xxPv') is not None:
            self.code_5xx_pv = m.get('5xxPv')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

