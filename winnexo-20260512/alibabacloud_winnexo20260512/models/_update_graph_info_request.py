# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGraphInfoRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        business_profile: str = None,
        display_name: str = None,
        graph_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
    ):
        # The application token issued by the console. If you specify this parameter, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The business description of the graph. If this parameter is not specified, the value is an empty string.
        self.business_profile = business_profile
        # The display name.
        self.display_name = display_name
        # The name of the graph.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The code of the proxy user, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The ID of the proxy user, which is the user ID on the WINNEXO platform. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The tenant ID.
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

        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

