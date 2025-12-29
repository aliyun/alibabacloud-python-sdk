# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class GetInventorySchemaResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        schemas: List[main_models.GetInventorySchemaResponseBodySchemas] = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that was used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The detailed configurations of the configuration list.
        self.schemas = schemas

    def validate(self):
        if self.schemas:
            for v1 in self.schemas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Schemas'] = []
        if self.schemas is not None:
            for k1 in self.schemas:
                result['Schemas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.schemas = []
        if m.get('Schemas') is not None:
            for k1 in m.get('Schemas'):
                temp_model = main_models.GetInventorySchemaResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k1))

        return self

class GetInventorySchemaResponseBodySchemas(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.GetInventorySchemaResponseBodySchemasAttributes] = None,
        type_name: str = None,
        version: str = None,
    ):
        # The properties of the configuration list.
        self.attributes = attributes
        # The name of the configuration list.
        self.type_name = type_name
        # The version of the configuration list.
        self.version = version

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.GetInventorySchemaResponseBodySchemasAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetInventorySchemaResponseBodySchemasAttributes(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        name: str = None,
    ):
        # The data type of the property.
        self.data_type = data_type
        # The name of the property.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

