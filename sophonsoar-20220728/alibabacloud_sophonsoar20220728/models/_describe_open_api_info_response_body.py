# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenApiInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeOpenApiInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenApiInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenApiInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        input_params: str = None,
        output_params: str = None,
        response_demo: str = None,
        summary: str = None,
        title: str = None,
    ):
        # The description of the API operation.
        self.description = description
        # The input parameters of the API operation.
        self.input_params = input_params
        # The output parameters of the API operation.
        self.output_params = output_params
        # The sample response parameters.
        self.response_demo = response_demo
        # The summary of the API operation.
        self.summary = summary
        # The title of the API operation.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.input_params is not None:
            result['InputParams'] = self.input_params

        if self.output_params is not None:
            result['OutputParams'] = self.output_params

        if self.response_demo is not None:
            result['ResponseDemo'] = self.response_demo

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')

        if m.get('ResponseDemo') is not None:
            self.response_demo = m.get('ResponseDemo')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

