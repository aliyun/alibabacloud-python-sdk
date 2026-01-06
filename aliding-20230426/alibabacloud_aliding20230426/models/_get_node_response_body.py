# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetNodeResponseBody(DaraModel):
    def __init__(
        self,
        node: main_models.GetNodeResponseBodyNode = None,
        request_id: str = None,
    ):
        self.node = node
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node is not None:
            result['node'] = self.node.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node') is not None:
            temp_model = main_models.GetNodeResponseBodyNode()
            self.node = temp_model.from_map(m.get('node'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetNodeResponseBodyNode(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        creator_id: str = None,
        extension: str = None,
        has_children: bool = None,
        modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        node_id: str = None,
        permission_role: str = None,
        size: int = None,
        statistical_info: main_models.GetNodeResponseBodyNodeStatisticalInfo = None,
        type: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.category = category
        self.create_time = create_time
        self.creator_id = creator_id
        self.extension = extension
        self.has_children = has_children
        self.modified_time = modified_time
        self.modifier_id = modifier_id
        self.name = name
        self.node_id = node_id
        self.permission_role = permission_role
        self.size = size
        self.statistical_info = statistical_info
        self.type = type
        self.url = url
        self.workspace_id = workspace_id

    def validate(self):
        if self.statistical_info:
            self.statistical_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.has_children is not None:
            result['HasChildren'] = self.has_children

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.permission_role is not None:
            result['PermissionRole'] = self.permission_role

        if self.size is not None:
            result['Size'] = self.size

        if self.statistical_info is not None:
            result['StatisticalInfo'] = self.statistical_info.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('HasChildren') is not None:
            self.has_children = m.get('HasChildren')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PermissionRole') is not None:
            self.permission_role = m.get('PermissionRole')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StatisticalInfo') is not None:
            temp_model = main_models.GetNodeResponseBodyNodeStatisticalInfo()
            self.statistical_info = temp_model.from_map(m.get('StatisticalInfo'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetNodeResponseBodyNodeStatisticalInfo(DaraModel):
    def __init__(
        self,
        word_count: int = None,
    ):
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.word_count is not None:
            result['WordCount'] = self.word_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        return self

