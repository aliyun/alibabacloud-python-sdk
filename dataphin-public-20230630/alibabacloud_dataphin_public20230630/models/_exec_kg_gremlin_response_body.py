# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecKgGremlinResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExecKgGremlinResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The query result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ExecKgGremlinResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecKgGremlinResponseBodyData(DaraModel):
    def __init__(
        self,
        edge_list: List[main_models.ExecKgGremlinResponseBodyDataEdgeList] = None,
        exec_query: str = None,
        node_list: List[main_models.ExecKgGremlinResponseBodyDataNodeList] = None,
        row_list: List[main_models.ExecKgGremlinResponseBodyDataRowList] = None,
    ):
        # The list of edges.
        self.edge_list = edge_list
        # The transformed execution statement.
        self.exec_query = exec_query
        # The list of nodes.
        self.node_list = node_list
        # The list of rows.
        self.row_list = row_list

    def validate(self):
        if self.edge_list:
            for v1 in self.edge_list:
                 if v1:
                    v1.validate()
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()
        if self.row_list:
            for v1 in self.row_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EdgeList'] = []
        if self.edge_list is not None:
            for k1 in self.edge_list:
                result['EdgeList'].append(k1.to_map() if k1 else None)

        if self.exec_query is not None:
            result['ExecQuery'] = self.exec_query

        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        result['RowList'] = []
        if self.row_list is not None:
            for k1 in self.row_list:
                result['RowList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_list = []
        if m.get('EdgeList') is not None:
            for k1 in m.get('EdgeList'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataEdgeList()
                self.edge_list.append(temp_model.from_map(k1))

        if m.get('ExecQuery') is not None:
            self.exec_query = m.get('ExecQuery')

        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataNodeList()
                self.node_list.append(temp_model.from_map(k1))

        self.row_list = []
        if m.get('RowList') is not None:
            for k1 in m.get('RowList'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataRowList()
                self.row_list.append(temp_model.from_map(k1))

        return self

class ExecKgGremlinResponseBodyDataRowList(DaraModel):
    def __init__(
        self,
        columns: List[main_models.ExecKgGremlinResponseBodyDataRowListColumns] = None,
    ):
        # The list of columns in the row.
        self.columns = columns

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataRowListColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class ExecKgGremlinResponseBodyDataRowListColumns(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ExecKgGremlinResponseBodyDataNodeList(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        entity_type: str = None,
        properties: List[main_models.ExecKgGremlinResponseBodyDataNodeListProperties] = None,
    ):
        # The data ID of the entity record.
        self.data_id = data_id
        # The entity type.
        self.entity_type = entity_type
        # The list of entity record properties.
        self.properties = properties

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataNodeListProperties()
                self.properties.append(temp_model.from_map(k1))

        return self

class ExecKgGremlinResponseBodyDataNodeListProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ExecKgGremlinResponseBodyDataEdgeList(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        properties: List[main_models.ExecKgGremlinResponseBodyDataEdgeListProperties] = None,
        relation_type: str = None,
        source_entity_data_id: str = None,
        source_entity_type: str = None,
        target_entity_data_id: str = None,
        target_entity_type: str = None,
    ):
        # The data ID of the relationship record.
        self.data_id = data_id
        # The list of relationship record properties.
        self.properties = properties
        # The relationship type.
        self.relation_type = relation_type
        # The data ID of the source entity record.
        self.source_entity_data_id = source_entity_data_id
        # The source entity type.
        self.source_entity_type = source_entity_type
        # The data ID of the target entity record.
        self.target_entity_data_id = target_entity_data_id
        # The target entity type.
        self.target_entity_type = target_entity_type

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_entity_data_id is not None:
            result['SourceEntityDataId'] = self.source_entity_data_id

        if self.source_entity_type is not None:
            result['SourceEntityType'] = self.source_entity_type

        if self.target_entity_data_id is not None:
            result['TargetEntityDataId'] = self.target_entity_data_id

        if self.target_entity_type is not None:
            result['TargetEntityType'] = self.target_entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.ExecKgGremlinResponseBodyDataEdgeListProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceEntityDataId') is not None:
            self.source_entity_data_id = m.get('SourceEntityDataId')

        if m.get('SourceEntityType') is not None:
            self.source_entity_type = m.get('SourceEntityType')

        if m.get('TargetEntityDataId') is not None:
            self.target_entity_data_id = m.get('TargetEntityDataId')

        if m.get('TargetEntityType') is not None:
            self.target_entity_type = m.get('TargetEntityType')

        return self

class ExecKgGremlinResponseBodyDataEdgeListProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

