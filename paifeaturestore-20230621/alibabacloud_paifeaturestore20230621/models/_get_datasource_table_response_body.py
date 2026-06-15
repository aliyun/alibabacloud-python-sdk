# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class GetDatasourceTableResponseBody(DaraModel):
    def __init__(
        self,
        fields: List[main_models.GetDatasourceTableResponseBodyFields] = None,
        request_id: str = None,
        table_name: str = None,
    ):
        # The list of fields.
        self.fields = fields
        # The request ID.
        self.request_id = request_id
        # The name of the data table.
        self.table_name = table_name

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetDatasourceTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetDatasourceTableResponseBodyFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        # The attributes of the field. Valid values:
        # 
        # ● Partition: indicates that the field is a partition field.
        # 
        # ● EventTime: indicates that the field is an event time field.
        # 
        # ● PrimaryKey: indicates that the field is a primary key field.
        self.attributes = attributes
        # The name of the field.
        self.name = name
        # The data type of the field. Valid values:
        # 
        # ● INT32
        # 
        # ● INT64
        # 
        # ● FLOAT
        # 
        # ● DOUBLE
        # 
        # ● STRING
        # 
        # ● BOOLEAN
        # 
        # ● TIMESTAMP
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

