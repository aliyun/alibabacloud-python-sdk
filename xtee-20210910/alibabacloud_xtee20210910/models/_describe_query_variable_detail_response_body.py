# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeQueryVariableDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeQueryVariableDetailResponseBodyResultObject = None,
    ):
        # Request ID.
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
            temp_model = main_models.DescribeQueryVariableDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeQueryVariableDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        data_source_code: int = None,
        data_source_name: str = None,
        description: str = None,
        event_code: str = None,
        expression: str = None,
        expression_title: str = None,
        expression_variable: str = None,
        id: int = None,
        outlier: str = None,
        outputs: str = None,
        title: str = None,
    ):
        # Data source code.
        self.data_source_code = data_source_code
        # Data source name
        self.data_source_name = data_source_name
        # Description.
        self.description = description
        # Event code
        self.event_code = event_code
        # Expression.
        self.expression = expression
        # Expression title.
        self.expression_title = expression_title
        # Expression variable.
        self.expression_variable = expression_variable
        # Variable ID
        self.id = id
        # Outlier
        self.outlier = outlier
        # Output results.
        self.outputs = outputs
        # Title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_code is not None:
            result['dataSourceCode'] = self.data_source_code

        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name

        if self.description is not None:
            result['description'] = self.description

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.expression is not None:
            result['expression'] = self.expression

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.expression_variable is not None:
            result['expressionVariable'] = self.expression_variable

        if self.id is not None:
            result['id'] = self.id

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceCode') is not None:
            self.data_source_code = m.get('dataSourceCode')

        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('expressionVariable') is not None:
            self.expression_variable = m.get('expressionVariable')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

