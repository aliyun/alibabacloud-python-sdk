# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractExtractResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RunContractExtractResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.RunContractExtractResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class RunContractExtractResponseBodyData(DaraModel):
    def __init__(
        self,
        contract_text: str = None,
        extract_result: List[main_models.RunContractExtractResponseBodyDataExtractResult] = None,
    ):
        self.contract_text = contract_text
        self.extract_result = extract_result

    def validate(self):
        if self.extract_result:
            for v1 in self.extract_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contract_text is not None:
            result['contractText'] = self.contract_text

        result['extractResult'] = []
        if self.extract_result is not None:
            for k1 in self.extract_result:
                result['extractResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contractText') is not None:
            self.contract_text = m.get('contractText')

        self.extract_result = []
        if m.get('extractResult') is not None:
            for k1 in m.get('extractResult'):
                temp_model = main_models.RunContractExtractResponseBodyDataExtractResult()
                self.extract_result.append(temp_model.from_map(k1))

        return self

class RunContractExtractResponseBodyDataExtractResult(DaraModel):
    def __init__(
        self,
        desc: str = None,
        extract_item: str = None,
        option: str = None,
        value: List[main_models.RunContractExtractResponseBodyDataExtractResultValue] = None,
    ):
        self.desc = desc
        self.extract_item = extract_item
        self.option = option
        self.value = value

    def validate(self):
        if self.value:
            for v1 in self.value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.extract_item is not None:
            result['extractItem'] = self.extract_item

        if self.option is not None:
            result['option'] = self.option

        result['value'] = []
        if self.value is not None:
            for k1 in self.value:
                result['value'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('extractItem') is not None:
            self.extract_item = m.get('extractItem')

        if m.get('option') is not None:
            self.option = m.get('option')

        self.value = []
        if m.get('value') is not None:
            for k1 in m.get('value'):
                temp_model = main_models.RunContractExtractResponseBodyDataExtractResultValue()
                self.value.append(temp_model.from_map(k1))

        return self

class RunContractExtractResponseBodyDataExtractResultValue(DaraModel):
    def __init__(
        self,
        data: str = None,
        original_text: str = None,
    ):
        self.data = data
        self.original_text = original_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.original_text is not None:
            result['originalText'] = self.original_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('originalText') is not None:
            self.original_text = m.get('originalText')

        return self

