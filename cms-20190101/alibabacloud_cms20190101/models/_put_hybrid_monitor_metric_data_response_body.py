# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutHybridMonitorMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_detail: List[main_models.PutHybridMonitorMetricDataResponseBodyErrorDetail] = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The details of invalid parameters.
        # 
        # If a request parameter is invalid, the details of the invalid parameter are returned.
        self.error_detail = error_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.error_detail:
            for v1 in self.error_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['ErrorDetail'] = []
        if self.error_detail is not None:
            for k1 in self.error_detail:
                result['ErrorDetail'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.error_detail = []
        if m.get('ErrorDetail') is not None:
            for k1 in m.get('ErrorDetail'):
                temp_model = main_models.PutHybridMonitorMetricDataResponseBodyErrorDetail()
                self.error_detail.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PutHybridMonitorMetricDataResponseBodyErrorDetail(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        index: int = None,
    ):
        # The error message of the invalid parameter.
        self.error_message = error_message
        # The position of the error message in the array.
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

