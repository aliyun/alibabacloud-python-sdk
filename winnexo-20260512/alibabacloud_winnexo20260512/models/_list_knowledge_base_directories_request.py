# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBaseDirectoriesRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If this parameter is passed, the request is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The directory ID.
        self.directory_id = directory_id
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The field by which the returned results are sorted. Valid values:
        # 
        # - event_time: the event creation time
        # - event_execute_start_time: the event execution time
        # - event_execute_finish_time: the event completion time
        self.sort_field = sort_field
        # The sort order. This parameter takes effect only when sortBy is specified. Valid values: ASC and DESC. The values are case-insensitive.
        self.sort_order = sort_order
        # The tenant ID. This is a common parameter. For winnexo-cli, this parameter is explicitly passed by using --tenant-id.
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

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

