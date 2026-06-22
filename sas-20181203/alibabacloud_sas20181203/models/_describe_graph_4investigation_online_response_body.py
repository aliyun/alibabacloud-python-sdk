# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGraph4InvestigationOnlineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeGraph4InvestigationOnlineResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Any other value indicates failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The response data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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
            temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGraph4InvestigationOnlineResponseBodyData(DaraModel):
    def __init__(
        self,
        edge_list: List[main_models.DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList] = None,
        entity_type_list: List[main_models.DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList] = None,
        relation_type_list: List[main_models.DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList] = None,
        vertex_list: List[main_models.DescribeGraph4InvestigationOnlineResponseBodyDataVertexList] = None,
    ):
        # The list of edges.
        self.edge_list = edge_list
        # The list of vertex types.
        self.entity_type_list = entity_type_list
        # The list of edge types.
        self.relation_type_list = relation_type_list
        # The list of vertices.
        self.vertex_list = vertex_list

    def validate(self):
        if self.edge_list:
            for v1 in self.edge_list:
                 if v1:
                    v1.validate()
        if self.entity_type_list:
            for v1 in self.entity_type_list:
                 if v1:
                    v1.validate()
        if self.relation_type_list:
            for v1 in self.relation_type_list:
                 if v1:
                    v1.validate()
        if self.vertex_list:
            for v1 in self.vertex_list:
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

        result['EntityTypeList'] = []
        if self.entity_type_list is not None:
            for k1 in self.entity_type_list:
                result['EntityTypeList'].append(k1.to_map() if k1 else None)

        result['RelationTypeList'] = []
        if self.relation_type_list is not None:
            for k1 in self.relation_type_list:
                result['RelationTypeList'].append(k1.to_map() if k1 else None)

        result['VertexList'] = []
        if self.vertex_list is not None:
            for k1 in self.vertex_list:
                result['VertexList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_list = []
        if m.get('EdgeList') is not None:
            for k1 in m.get('EdgeList'):
                temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList()
                self.edge_list.append(temp_model.from_map(k1))

        self.entity_type_list = []
        if m.get('EntityTypeList') is not None:
            for k1 in m.get('EntityTypeList'):
                temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList()
                self.entity_type_list.append(temp_model.from_map(k1))

        self.relation_type_list = []
        if m.get('RelationTypeList') is not None:
            for k1 in m.get('RelationTypeList'):
                temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList()
                self.relation_type_list.append(temp_model.from_map(k1))

        self.vertex_list = []
        if m.get('VertexList') is not None:
            for k1 in m.get('VertexList'):
                temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyDataVertexList()
                self.vertex_list.append(temp_model.from_map(k1))

        return self

class DescribeGraph4InvestigationOnlineResponseBodyDataVertexList(DaraModel):
    def __init__(
        self,
        name: str = None,
        neighbor_list: List[main_models.DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList] = None,
        properties: str = None,
        time: str = None,
        type: str = None,
        uuid: str = None,
    ):
        # The name of the vertex.
        self.name = name
        # The list of vertices adjacent to the current vertex.
        self.neighbor_list = neighbor_list
        # The properties.
        self.properties = properties
        # The time.
        self.time = time
        # The type of the vertex.
        self.type = type
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        if self.neighbor_list:
            for v1 in self.neighbor_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['NeighborList'] = []
        if self.neighbor_list is not None:
            for k1 in self.neighbor_list:
                result['NeighborList'].append(k1.to_map() if k1 else None)

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.neighbor_list = []
        if m.get('NeighborList') is not None:
            for k1 in m.get('NeighborList'):
                temp_model = main_models.DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList()
                self.neighbor_list.append(temp_model.from_map(k1))

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeGraph4InvestigationOnlineResponseBodyDataVertexListNeighborList(DaraModel):
    def __init__(
        self,
        count: int = None,
        has_more: bool = None,
        type: str = None,
    ):
        # The number of adjacent nodes.
        self.count = count
        # Indicates whether more adjacent vertices exist.
        self.has_more = has_more
        # The type of the neighbor node.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeGraph4InvestigationOnlineResponseBodyDataRelationTypeList(DaraModel):
    def __init__(
        self,
        directed: int = None,
        display_color: str = None,
        display_icon: str = None,
        name: str = None,
    ):
        # The direction of the edge. Valid values:
        # - **1**: forward
        # - **0**: reverse.
        self.directed = directed
        # The rendering color of the edge.
        self.display_color = display_color
        # The icon style of the edge.
        self.display_icon = display_icon
        # The name of the edge.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directed is not None:
            result['Directed'] = self.directed

        if self.display_color is not None:
            result['DisplayColor'] = self.display_color

        if self.display_icon is not None:
            result['DisplayIcon'] = self.display_icon

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directed') is not None:
            self.directed = m.get('Directed')

        if m.get('DisplayColor') is not None:
            self.display_color = m.get('DisplayColor')

        if m.get('DisplayIcon') is not None:
            self.display_icon = m.get('DisplayIcon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeGraph4InvestigationOnlineResponseBodyDataEntityTypeList(DaraModel):
    def __init__(
        self,
        display_color: str = None,
        display_icon: str = None,
        display_order: int = None,
        id: str = None,
        name: str = None,
    ):
        # The rendering color of the vertex.
        self.display_color = display_color
        # The icon of the vertex.
        self.display_icon = display_icon
        # The display order.
        self.display_order = display_order
        # The ID of the node type.
        self.id = id
        # The name of the vertex.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_color is not None:
            result['DisplayColor'] = self.display_color

        if self.display_icon is not None:
            result['DisplayIcon'] = self.display_icon

        if self.display_order is not None:
            result['DisplayOrder'] = self.display_order

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayColor') is not None:
            self.display_color = m.get('DisplayColor')

        if m.get('DisplayIcon') is not None:
            self.display_icon = m.get('DisplayIcon')

        if m.get('DisplayOrder') is not None:
            self.display_order = m.get('DisplayOrder')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeGraph4InvestigationOnlineResponseBodyDataEdgeList(DaraModel):
    def __init__(
        self,
        end_id: str = None,
        end_type: str = None,
        name: str = None,
        start_id: str = None,
        start_type: str = None,
        time: str = None,
        type: str = None,
    ):
        # The ID of the end vertex of the edge.
        self.end_id = end_id
        # The type of the end vertex of the edge. Valid values include but are not limited to:
        # - **process**: process
        # - **file**: file
        # - **alert**: alert
        # - **ip**: IP address
        # - **domain**: domain name.
        self.end_type = end_type
        # The name of the edge.
        self.name = name
        # The ID of the start vertex of the edge.
        self.start_id = start_id
        # The type of the start vertex of the edge. Valid values include but are not limited to:
        # - **process**: process
        # - **file**: file
        # - **alert**: alert
        # - **ip**: IP address
        # - **domain**: domain name.
        self.start_type = start_type
        # The time when the edge was created.
        self.time = time
        # The type of the edge.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_id is not None:
            result['EndId'] = self.end_id

        if self.end_type is not None:
            result['EndType'] = self.end_type

        if self.name is not None:
            result['Name'] = self.name

        if self.start_id is not None:
            result['StartId'] = self.start_id

        if self.start_type is not None:
            result['StartType'] = self.start_type

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndId') is not None:
            self.end_id = m.get('EndId')

        if m.get('EndType') is not None:
            self.end_type = m.get('EndType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartId') is not None:
            self.start_id = m.get('StartId')

        if m.get('StartType') is not None:
            self.start_type = m.get('StartType')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

