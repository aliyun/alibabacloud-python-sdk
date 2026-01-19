# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class UploadFileCheckResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.UploadFileCheckResponseBodyResultObject = None,
    ):
        # ID of the request
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.UploadFileCheckResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class UploadFileCheckResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        effective_number: int = None,
        result_list: List[str] = None,
        total_number: int = None,
    ):
        # Number of effective rows
        self.effective_number = effective_number
        # Valid sample data
        self.result_list = result_list
        # Total number of rows
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_number is not None:
            result['effectiveNumber'] = self.effective_number

        if self.result_list is not None:
            result['resultList'] = self.result_list

        if self.total_number is not None:
            result['totalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectiveNumber') is not None:
            self.effective_number = m.get('effectiveNumber')

        if m.get('resultList') is not None:
            self.result_list = m.get('resultList')

        if m.get('totalNumber') is not None:
            self.total_number = m.get('totalNumber')

        return self

