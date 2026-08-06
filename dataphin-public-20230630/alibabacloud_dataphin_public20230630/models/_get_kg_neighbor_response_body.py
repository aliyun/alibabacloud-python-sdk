# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetKgNeighborResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKgNeighborResponseBodyData = None,
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
            temp_model = main_models.GetKgNeighborResponseBodyData()
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

class GetKgNeighborResponseBodyData(DaraModel):
    def __init__(
        self,
        edge_list: List[main_models.GetKgNeighborResponseBodyDataEdgeList] = None,
        node_list: List[main_models.GetKgNeighborResponseBodyDataNodeList] = None,
    ):
        # The edge list.
        self.edge_list = edge_list
        # The node list.
        self.node_list = node_list

    def validate(self):
        if self.edge_list:
            for v1 in self.edge_list:
                 if v1:
                    v1.validate()
        if self.node_list:
            for v1 in self.node_list:
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

        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_list = []
        if m.get('EdgeList') is not None:
            for k1 in m.get('EdgeList'):
                temp_model = main_models.GetKgNeighborResponseBodyDataEdgeList()
                self.edge_list.append(temp_model.from_map(k1))

        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.GetKgNeighborResponseBodyDataNodeList()
                self.node_list.append(temp_model.from_map(k1))

        return self

class GetKgNeighborResponseBodyDataNodeList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        property_list: List[main_models.GetKgNeighborResponseBodyDataNodeListPropertyList] = None,
    ):
        # The entity record ID.
        self.entity_id = entity_id
        # The entity type code.
        self.entity_type = entity_type
        # The entity record property list.
        self.property_list = property_list

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.GetKgNeighborResponseBodyDataNodeListPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        return self

class GetKgNeighborResponseBodyDataNodeListPropertyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_type: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property data type. Valid values: STRING (string), INTEGER (integer), FLOAT (float), BOOLEAN (Boolean), DATE (date), LIST (list), and others.
        self.data_type = data_type
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

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetKgNeighborResponseBodyDataEdgeList(DaraModel):
    def __init__(
        self,
        property_list: List[main_models.GetKgNeighborResponseBodyDataEdgeListPropertyList] = None,
        relation_id: str = None,
        relation_type: str = None,
        source_entity_id: str = None,
        target_entity_id: str = None,
    ):
        # The relation record property list.
        self.property_list = property_list
        # The relation record ID.
        self.relation_id = relation_id
        # The relation type code.
        self.relation_type = relation_type
        # The source entity ID.
        self.source_entity_id = source_entity_id
        # The target entity ID.
        self.target_entity_id = target_entity_id

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_entity_id is not None:
            result['SourceEntityId'] = self.source_entity_id

        if self.target_entity_id is not None:
            result['TargetEntityId'] = self.target_entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.GetKgNeighborResponseBodyDataEdgeListPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceEntityId') is not None:
            self.source_entity_id = m.get('SourceEntityId')

        if m.get('TargetEntityId') is not None:
            self.target_entity_id = m.get('TargetEntityId')

        return self

class GetKgNeighborResponseBodyDataEdgeListPropertyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_type: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property data type. Valid values: STRING (string), INTEGER (integer), FLOAT (float), BOOLEAN (Boolean), DATE (date), LIST (list), and others.
        self.data_type = data_type
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

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

