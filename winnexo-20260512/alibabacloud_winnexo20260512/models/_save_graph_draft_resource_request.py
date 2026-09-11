# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveGraphDraftResourceRequest(DaraModel):
    def __init__(
        self,
        element_type: str = None,
        graph_name: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tenant_id: str = None,
        yaml_edit: str = None,
    ):
        # 资源小类：resourceType=object 时固定 object_type；resourceType=element 时为 indicator / logic / process / rule / analysis 之一
        # 
        # This parameter is required.
        self.element_type = element_type
        # 图谱名称，须已存在（active 记录）
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 资源名（创建后不可改名，底层校验）
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # 资源大类：object（对象）/ element（业务元素）
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 单资源 YAML 文本
        # 
        # This parameter is required.
        self.yaml_edit = yaml_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element_type is not None:
            result['elementType'] = self.element_type

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.yaml_edit is not None:
            result['yamlEdit'] = self.yaml_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elementType') is not None:
            self.element_type = m.get('elementType')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self

