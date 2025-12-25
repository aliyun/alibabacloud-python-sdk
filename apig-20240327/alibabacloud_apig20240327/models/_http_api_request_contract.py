# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiRequestContract(DaraModel):
    def __init__(
        self,
        body: main_models.HttpApiRequestContractBody = None,
        header_parameters: List[main_models.HttpApiParameter] = None,
        path_parameters: List[main_models.HttpApiParameter] = None,
        query_parameters: List[main_models.HttpApiParameter] = None,
    ):
        self.body = body
        self.header_parameters = header_parameters
        self.path_parameters = path_parameters
        self.query_parameters = query_parameters

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header_parameters:
            for v1 in self.header_parameters:
                 if v1:
                    v1.validate()
        if self.path_parameters:
            for v1 in self.path_parameters:
                 if v1:
                    v1.validate()
        if self.query_parameters:
            for v1 in self.query_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        result['headerParameters'] = []
        if self.header_parameters is not None:
            for k1 in self.header_parameters:
                result['headerParameters'].append(k1.to_map() if k1 else None)

        result['pathParameters'] = []
        if self.path_parameters is not None:
            for k1 in self.path_parameters:
                result['pathParameters'].append(k1.to_map() if k1 else None)

        result['queryParameters'] = []
        if self.query_parameters is not None:
            for k1 in self.query_parameters:
                result['queryParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.HttpApiRequestContractBody()
            self.body = temp_model.from_map(m.get('body'))

        self.header_parameters = []
        if m.get('headerParameters') is not None:
            for k1 in m.get('headerParameters'):
                temp_model = main_models.HttpApiParameter()
                self.header_parameters.append(temp_model.from_map(k1))

        self.path_parameters = []
        if m.get('pathParameters') is not None:
            for k1 in m.get('pathParameters'):
                temp_model = main_models.HttpApiParameter()
                self.path_parameters.append(temp_model.from_map(k1))

        self.query_parameters = []
        if m.get('queryParameters') is not None:
            for k1 in m.get('queryParameters'):
                temp_model = main_models.HttpApiParameter()
                self.query_parameters.append(temp_model.from_map(k1))

        return self

class HttpApiRequestContractBody(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.content_type = content_type
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.description is not None:
            result['description'] = self.description

        if self.example is not None:
            result['example'] = self.example

        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('example') is not None:
            self.example = m.get('example')

        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')

        return self

