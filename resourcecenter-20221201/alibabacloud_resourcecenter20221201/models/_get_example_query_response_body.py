# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetExampleQueryResponseBody(DaraModel):
    def __init__(
        self,
        example_query: main_models.GetExampleQueryResponseBodyExampleQuery = None,
        request_id: str = None,
    ):
        # The information about the sample query template.
        self.example_query = example_query
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.example_query:
            self.example_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_query is not None:
            result['ExampleQuery'] = self.example_query.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleQuery') is not None:
            temp_model = main_models.GetExampleQueryResponseBodyExampleQuery()
            self.example_query = temp_model.from_map(m.get('ExampleQuery'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetExampleQueryResponseBodyExampleQuery(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        self.description = description
        # The query statement in the template.
        self.expression = expression
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.name is not None:
            result['Name'] = self.name

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        return self

