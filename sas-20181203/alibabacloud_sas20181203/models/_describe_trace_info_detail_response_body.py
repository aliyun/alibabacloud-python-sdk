# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeTraceInfoDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        trace_info_detail: main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetail = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The details of the tracing diagram.
        self.trace_info_detail = trace_info_detail

    def validate(self):
        if self.trace_info_detail:
            self.trace_info_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_info_detail is not None:
            result['TraceInfoDetail'] = self.trace_info_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceInfoDetail') is not None:
            temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetail()
            self.trace_info_detail = temp_model.from_map(m.get('TraceInfoDetail'))

        return self

class DescribeTraceInfoDetailResponseBodyTraceInfoDetail(DaraModel):
    def __init__(
        self,
        edge_list: List[main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailEdgeList] = None,
        entity_type_list: List[main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailEntityTypeList] = None,
        relation_type_list: List[main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailRelationTypeList] = None,
        vertex_list: List[main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexList] = None,
    ):
        # An array that consists of the edges of the tracing diagram.
        self.edge_list = edge_list
        # An array that consists of the metadata configurations of the vertex type.
        self.entity_type_list = entity_type_list
        # An array that consists of the metadata configurations of the edge type.
        self.relation_type_list = relation_type_list
        # An array that consists of all vertexes of the tracing diagram.
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
                temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailEdgeList()
                self.edge_list.append(temp_model.from_map(k1))

        self.entity_type_list = []
        if m.get('EntityTypeList') is not None:
            for k1 in m.get('EntityTypeList'):
                temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailEntityTypeList()
                self.entity_type_list.append(temp_model.from_map(k1))

        self.relation_type_list = []
        if m.get('RelationTypeList') is not None:
            for k1 in m.get('RelationTypeList'):
                temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailRelationTypeList()
                self.relation_type_list.append(temp_model.from_map(k1))

        self.vertex_list = []
        if m.get('VertexList') is not None:
            for k1 in m.get('VertexList'):
                temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexList()
                self.vertex_list.append(temp_model.from_map(k1))

        return self

class DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexList(DaraModel):
    def __init__(
        self,
        count: int = None,
        id: str = None,
        name: str = None,
        neighbor_list: List[main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexListNeighborList] = None,
        time: str = None,
        type: str = None,
    ):
        # The number of times.
        self.count = count
        # The ID of the vertex.
        self.id = id
        # The name of the entity represented by the vertex.
        self.name = name
        # An array that consists of the neighbor nodes.
        self.neighbor_list = neighbor_list
        # The point in time.
        self.time = time
        # The type of the entity represented by the vertex.
        self.type = type

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
        if self.count is not None:
            result['Count'] = self.count

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['NeighborList'] = []
        if self.neighbor_list is not None:
            for k1 in self.neighbor_list:
                result['NeighborList'].append(k1.to_map() if k1 else None)

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.neighbor_list = []
        if m.get('NeighborList') is not None:
            for k1 in m.get('NeighborList'):
                temp_model = main_models.DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexListNeighborList()
                self.neighbor_list.append(temp_model.from_map(k1))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeTraceInfoDetailResponseBodyTraceInfoDetailVertexListNeighborList(DaraModel):
    def __init__(
        self,
        count: int = None,
        has_more: bool = None,
        type: str = None,
    ):
        # The number of neighbor nodes.
        self.count = count
        # Indicates whether one more page is returned.
        self.has_more = has_more
        # The type of the neighbor node. The value is fixed as **alert**.
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

class DescribeTraceInfoDetailResponseBodyTraceInfoDetailRelationTypeList(DaraModel):
    def __init__(
        self,
        directed: int = None,
        display_color: str = None,
        name: str = None,
        relation_type_id: str = None,
        show_type: str = None,
    ):
        # Indicates whether the edge is a directional edge. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.directed = directed
        # The rendering color of the edge.
        self.display_color = display_color
        # The name of the edge type.
        self.name = name
        # The ID of the edge type.
        self.relation_type_id = relation_type_id
        # This parameter is deprecated.
        self.show_type = show_type

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

        if self.name is not None:
            result['Name'] = self.name

        if self.relation_type_id is not None:
            result['RelationTypeId'] = self.relation_type_id

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directed') is not None:
            self.directed = m.get('Directed')

        if m.get('DisplayColor') is not None:
            self.display_color = m.get('DisplayColor')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelationTypeId') is not None:
            self.relation_type_id = m.get('RelationTypeId')

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        return self

class DescribeTraceInfoDetailResponseBodyTraceInfoDetailEntityTypeList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        display_color: str = None,
        display_icon: str = None,
        display_template: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        limit: int = None,
        name: str = None,
        namespace: str = None,
        offset: int = None,
    ):
        # This parameter is deprecated.
        self.db_id = db_id
        # The rendering color of the vertex.
        self.display_color = display_color
        # The icon style of the vertex.
        self.display_icon = display_icon
        # This parameter is deprecated.
        self.display_template = display_template
        # The timestamp when the vertex was created.
        self.gmt_create = gmt_create
        # The time when the vertex was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the vertex type.
        self.id = id
        # This parameter is deprecated.
        self.limit = limit
        # The name of the vertex type.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # This parameter is deprecated.
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.display_color is not None:
            result['DisplayColor'] = self.display_color

        if self.display_icon is not None:
            result['DisplayIcon'] = self.display_icon

        if self.display_template is not None:
            result['DisplayTemplate'] = self.display_template

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.offset is not None:
            result['Offset'] = self.offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DisplayColor') is not None:
            self.display_color = m.get('DisplayColor')

        if m.get('DisplayIcon') is not None:
            self.display_icon = m.get('DisplayIcon')

        if m.get('DisplayTemplate') is not None:
            self.display_template = m.get('DisplayTemplate')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        return self

class DescribeTraceInfoDetailResponseBodyTraceInfoDetailEdgeList(DaraModel):
    def __init__(
        self,
        count: int = None,
        end_id: str = None,
        start_id: str = None,
        time: str = None,
        type: str = None,
    ):
        # The number of times.
        self.count = count
        # The ending vertex ID of the edge of the tracing diagram.
        self.end_id = end_id
        # The starting vertex ID of the edge of the tracing diagram.
        self.start_id = start_id
        # The point in time.
        self.time = time
        # The type of the edge of the tracing diagram.
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

        if self.end_id is not None:
            result['EndId'] = self.end_id

        if self.start_id is not None:
            result['StartId'] = self.start_id

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EndId') is not None:
            self.end_id = m.get('EndId')

        if m.get('StartId') is not None:
            self.start_id = m.get('StartId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

