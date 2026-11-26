# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveGraphDraftResourceRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        element_type: str = None,
        graph_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tenant_id: str = None,
        yaml_edit: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The element type. Currently, only text is supported.
        # 
        # This parameter is required.
        self.element_type = element_type
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The resource name.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The resource type.
        # 
        # This parameter is set to **instance**, which indicates that the resource type is instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tenant ID.
        self.tenant_id = tenant_id
        # The original YAML text of the graph schema trimmed by READ permissions, with $ref references within the authorized subgraph retained.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.element_type is not None:
            result['elementType'] = self.element_type

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('elementType') is not None:
            self.element_type = m.get('elementType')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self

