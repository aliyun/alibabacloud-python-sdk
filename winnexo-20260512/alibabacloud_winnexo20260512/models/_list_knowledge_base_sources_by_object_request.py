# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBaseSourcesByObjectRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        graph_name: str = None,
        object_id: str = None,
        object_type: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # token
        self.app_token = app_token
        # The graph name. You can call listGraphs to obtain it.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The ID of the associated variable.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The object type, such as customer. This parameter has a value when type is set to mention.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The code of the operator.
        self.ops_user_code = ops_user_code
        # The ID of the operator.
        self.ops_user_id = ops_user_id
        # The current page number.
        self.page = page
        # The page size.
        self.page_size = page_size
        # The tenant ID. This is a common parameter. In winnexo-cli, it is explicitly passed by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

