# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ValidateDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ValidateDataSourcesResponseBodyResult] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The result returned.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ValidateDataSourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ValidateDataSourcesResponseBodyResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_source: main_models.ValidateDataSourcesResponseBodyResultDataSource = None,
        message: str = None,
    ):
        # The code returned for the request.
        self.code = code
        # The data source.
        self.data_source = data_source
        # The status of the execution.
        self.message = message

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataSource') is not None:
            temp_model = main_models.ValidateDataSourcesResponseBodyResultDataSource()
            self.data_source = temp_model.from_map(m.get('dataSource'))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ValidateDataSourcesResponseBodyResultDataSource(DaraModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        table_name: str = None,
        type: str = None,
    ):
        # The parameters of the data source.
        self.parameters = parameters
        # The name of the table.
        self.table_name = table_name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

