# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecExamplesResponseBody(DaraModel):
    def __init__(
        self,
        examples: List[main_models.DescribeApisecExamplesResponseBodyExamples] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.examples = examples
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.examples:
            for v1 in self.examples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Examples'] = []
        if self.examples is not None:
            for k1 in self.examples:
                result['Examples'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.examples = []
        if m.get('Examples') is not None:
            for k1 in m.get('Examples'):
                temp_model = main_models.DescribeApisecExamplesResponseBodyExamples()
                self.examples.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecExamplesResponseBodyExamples(DaraModel):
    def __init__(
        self,
        api_url: str = None,
        poc_payload: str = None,
        protocol: str = None,
        request: str = None,
        request_sensitive_data: List[main_models.DescribeApisecExamplesResponseBodyExamplesRequestSensitiveData] = None,
        response: str = None,
        response_sensitive_data: List[main_models.DescribeApisecExamplesResponseBodyExamplesResponseSensitiveData] = None,
    ):
        self.api_url = api_url
        self.poc_payload = poc_payload
        self.protocol = protocol
        self.request = request
        self.request_sensitive_data = request_sensitive_data
        self.response = response
        self.response_sensitive_data = response_sensitive_data

    def validate(self):
        if self.request_sensitive_data:
            for v1 in self.request_sensitive_data:
                 if v1:
                    v1.validate()
        if self.response_sensitive_data:
            for v1 in self.response_sensitive_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_url is not None:
            result['ApiUrl'] = self.api_url

        if self.poc_payload is not None:
            result['PocPayload'] = self.poc_payload

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request is not None:
            result['Request'] = self.request

        result['RequestSensitiveData'] = []
        if self.request_sensitive_data is not None:
            for k1 in self.request_sensitive_data:
                result['RequestSensitiveData'].append(k1.to_map() if k1 else None)

        if self.response is not None:
            result['Response'] = self.response

        result['ResponseSensitiveData'] = []
        if self.response_sensitive_data is not None:
            for k1 in self.response_sensitive_data:
                result['ResponseSensitiveData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUrl') is not None:
            self.api_url = m.get('ApiUrl')

        if m.get('PocPayload') is not None:
            self.poc_payload = m.get('PocPayload')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Request') is not None:
            self.request = m.get('Request')

        self.request_sensitive_data = []
        if m.get('RequestSensitiveData') is not None:
            for k1 in m.get('RequestSensitiveData'):
                temp_model = main_models.DescribeApisecExamplesResponseBodyExamplesRequestSensitiveData()
                self.request_sensitive_data.append(temp_model.from_map(k1))

        if m.get('Response') is not None:
            self.response = m.get('Response')

        self.response_sensitive_data = []
        if m.get('ResponseSensitiveData') is not None:
            for k1 in m.get('ResponseSensitiveData'):
                temp_model = main_models.DescribeApisecExamplesResponseBodyExamplesResponseSensitiveData()
                self.response_sensitive_data.append(temp_model.from_map(k1))

        return self

class DescribeApisecExamplesResponseBodyExamplesResponseSensitiveData(DaraModel):
    def __init__(
        self,
        sensitive_code: str = None,
        sensitive_data_list: List[str] = None,
    ):
        self.sensitive_code = sensitive_code
        self.sensitive_data_list = sensitive_data_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_data_list is not None:
            result['SensitiveDataList'] = self.sensitive_data_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveDataList') is not None:
            self.sensitive_data_list = m.get('SensitiveDataList')

        return self

class DescribeApisecExamplesResponseBodyExamplesRequestSensitiveData(DaraModel):
    def __init__(
        self,
        sensitive_code: str = None,
        sensitive_data_list: List[str] = None,
    ):
        self.sensitive_code = sensitive_code
        self.sensitive_data_list = sensitive_data_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_data_list is not None:
            result['SensitiveDataList'] = self.sensitive_data_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveDataList') is not None:
            self.sensitive_data_list = m.get('SensitiveDataList')

        return self

