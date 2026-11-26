# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperatingObjectFavoritesRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        graph_name: str = None,
        next_token: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is executed as the user identified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The name of the graph. You can call the listGraphs operation to obtain the graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The pagination cursor.
        self.next_token = next_token
        # The object type, such as customer. This parameter has a value when type is set to mention.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The name of the digital worker, which is the name of the operating object. This parameter is optional.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the effective tenant.
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

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

