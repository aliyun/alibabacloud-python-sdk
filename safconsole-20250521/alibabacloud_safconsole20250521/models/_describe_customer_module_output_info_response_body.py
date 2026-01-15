# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomerModuleOutputInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeCustomerModuleOutputInfoResponseBodyResultObject = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeCustomerModuleOutputInfoResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomerModuleOutputInfoResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        final_score_format: str = None,
        process_expression: str = None,
        test_file: str = None,
    ):
        self.final_score_format = final_score_format
        self.process_expression = process_expression
        self.test_file = test_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_score_format is not None:
            result['FinalScoreFormat'] = self.final_score_format

        if self.process_expression is not None:
            result['ProcessExpression'] = self.process_expression

        if self.test_file is not None:
            result['TestFile'] = self.test_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalScoreFormat') is not None:
            self.final_score_format = m.get('FinalScoreFormat')

        if m.get('ProcessExpression') is not None:
            self.process_expression = m.get('ProcessExpression')

        if m.get('TestFile') is not None:
            self.test_file = m.get('TestFile')

        return self

