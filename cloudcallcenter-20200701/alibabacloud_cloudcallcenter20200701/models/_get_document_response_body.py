# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class GetDocumentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDocumentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetDocumentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        document: Dict[str, Any] = None,
        schema: main_models.GetDocumentResponseBodyDataSchema = None,
    ):
        self.document = document
        # scheme
        self.schema = schema

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['Document'] = self.document

        if self.schema is not None:
            result['Schema'] = self.schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Document') is not None:
            self.document = m.get('Document')

        if m.get('Schema') is not None:
            temp_model = main_models.GetDocumentResponseBodyDataSchema()
            self.schema = temp_model.from_map(m.get('Schema'))

        return self

class GetDocumentResponseBodyDataSchema(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        deleted: bool = None,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        properties: Dict[str, main_models.DataSchemaPropertiesValue] = None,
        updated_time: str = None,
    ):
        self.created_time = created_time
        self.deleted = deleted
        self.description = description
        # schame id
        self.id = id
        self.instance_id = instance_id
        self.properties = properties
        self.updated_time = updated_time

    def validate(self):
        if self.properties:
            for v1 in self.properties.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Properties'] = {}
        if self.properties is not None:
            for k1, v1 in self.properties.items():
                result['Properties'][k1] = v1.to_map() if v1 else None

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.properties = {}
        if m.get('Properties') is not None:
            for k1, v1 in m.get('Properties').items():
                temp_model = main_models.DataSchemaPropertiesValue()
                self.properties[k1] = temp_model.from_map(v1)

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

