# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20221125 import models as main_models
from darabonba.model import DaraModel

class EntVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EntVerifyResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Error message
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Result
        self.result = result

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.EntVerifyResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class EntVerifyResponseBodyResult(DaraModel):
    def __init__(
        self,
        risk_verify_result: main_models.EntVerifyResponseBodyResultRiskVerifyResult = None,
    ):
        # Enterprise risk verification result
        self.risk_verify_result = risk_verify_result

    def validate(self):
        if self.risk_verify_result:
            self.risk_verify_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_verify_result is not None:
            result['RiskVerifyResult'] = self.risk_verify_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskVerifyResult') is not None:
            temp_model = main_models.EntVerifyResponseBodyResultRiskVerifyResult()
            self.risk_verify_result = temp_model.from_map(m.get('RiskVerifyResult'))

        return self

class EntVerifyResponseBodyResultRiskVerifyResult(DaraModel):
    def __init__(
        self,
        found: bool = None,
        model_results: List[main_models.EntVerifyResponseBodyResultRiskVerifyResultModelResults] = None,
    ):
        # Whether found
        self.found = found
        # List of enterprise risk verification model results
        self.model_results = model_results

    def validate(self):
        if self.model_results:
            for v1 in self.model_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.found is not None:
            result['Found'] = self.found

        result['ModelResults'] = []
        if self.model_results is not None:
            for k1 in self.model_results:
                result['ModelResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Found') is not None:
            self.found = m.get('Found')

        self.model_results = []
        if m.get('ModelResults') is not None:
            for k1 in m.get('ModelResults'):
                temp_model = main_models.EntVerifyResponseBodyResultRiskVerifyResultModelResults()
                self.model_results.append(temp_model.from_map(k1))

        return self

class EntVerifyResponseBodyResultRiskVerifyResultModelResults(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        result: str = None,
    ):
        # Model name
        self.model_name = model_name
        # Model result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

