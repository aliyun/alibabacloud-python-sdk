# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ComponentLayout(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_selector: main_models.ComponentLayoutNodeSelector = None,
    ):
        # 应用名称。
        self.application_name = application_name
        # 组件名称。
        self.component_name = component_name
        # 节点选择器。
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('NodeSelector') is not None:
            temp_model = main_models.ComponentLayoutNodeSelector()
            self.node_selector = temp_model.from_map(m.get('NodeSelector'))

        return self

class ComponentLayoutNodeSelector(DaraModel):
    def __init__(
        self,
        node_end_index: int = None,
        node_group_id: str = None,
        node_group_index: int = None,
        node_group_name: str = None,
        node_group_types: List[str] = None,
        node_names: List[str] = None,
        node_select_type: str = None,
        node_start_index: int = None,
    ):
        # 节点结束编号，包含结束编号。
        self.node_end_index = node_end_index
        # 节点组ID。
        self.node_group_id = node_group_id
        # 机器组下标编号。
        self.node_group_index = node_group_index
        # 机器组名。
        self.node_group_name = node_group_name
        # SelectType = NODE_GROUP 且 nodeGroupId 不存在时使用
        self.node_group_types = node_group_types
        # 节点名称列表。
        self.node_names = node_names
        # 节点选择类型。
        # 
        # This parameter is required.
        self.node_select_type = node_select_type
        # 节点开始编号，包含开始编号。
        self.node_start_index = node_start_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_end_index is not None:
            result['NodeEndIndex'] = self.node_end_index

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_index is not None:
            result['NodeGroupIndex'] = self.node_group_index

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type

        if self.node_start_index is not None:
            result['NodeStartIndex'] = self.node_start_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeEndIndex') is not None:
            self.node_end_index = m.get('NodeEndIndex')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupIndex') is not None:
            self.node_group_index = m.get('NodeGroupIndex')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')

        if m.get('NodeStartIndex') is not None:
            self.node_start_index = m.get('NodeStartIndex')

        return self

