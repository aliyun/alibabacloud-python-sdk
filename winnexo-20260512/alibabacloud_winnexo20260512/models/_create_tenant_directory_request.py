# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateTenantDirectoryRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        change_record_enabled: bool = None,
        description: str = None,
        name: str = None,
        oo_visibility_mode: str = None,
        operating_object_names: List[str] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        parent_id: int = None,
        path: str = None,
        tenant_id: str = None,
    ):
        # The platform application credential. Pass this parameter when you use the application proxy mode, and specify the operator by using opsUserId or opsUserCode based on the application configuration. Do not use real credentials in logs or public examples.
        self.app_token = app_token
        # Specifies whether to generate AI version summaries for subsequent content updates. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # If this parameter is omitted or set to null, the configuration is not changed. Disabling this feature does not delete existing summaries. This parameter is supported only for standard enterprise knowledge base root directories.
        self.change_record_enabled = change_record_enabled
        # The purpose or content description of the directory. If this parameter is omitted, the value is empty.
        self.description = description
        # The name of the directory. The name must be 1 to 256 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The digital employee association mode. ALL indicates that the directory is visible to all digital employees, and operatingObjectNames must be omitted, set to null, or set to an empty array. SPECIFIED indicates association by list, and operatingObjectNames must be explicitly provided. An empty array indicates that no employees are associated. If this parameter is omitted or set to null, the association configuration is not changed. This parameter is supported only for standard enterprise knowledge base root directories.
        self.oo_visibility_mode = oo_visibility_mode
        # The list of internal names of the specified associated digital employees. This parameter must be used together with ooVisibilityMode. This parameter is required when ooVisibilityMode is set to SPECIFIED. An empty array indicates that all associations are cleared. When ooVisibilityMode is set to ALL, this parameter must be omitted, set to null, or set to an empty array. You can specify up to 100 items. Each item must be 1 to 256 characters in length after leading and trailing spaces are removed. The server verifies that the employees exist and are available in the current tenant, and fully replaces the associations after deduplication.
        self.operating_object_names = operating_object_names
        # The unique code of the proxied user in the tenant. This parameter is used only when the identity mapping mode of the application credential is source_uid. You cannot use this parameter to bypass tenant or knowledge base permission verification.
        self.ops_user_code = ops_user_code
        # The ID of the proxied WINNEXO platform user. This parameter is used only when the identity mapping mode of the application credential is winnexo_uid. You cannot use this parameter to bypass tenant or knowledge base permission verification.
        self.ops_user_id = ops_user_id
        # The internal primary key of the parent directory. If this parameter is omitted or set to null, an enterprise knowledge base root directory is created. If this parameter is specified, a subdirectory is created. This parameter must be omitted or set to null when digital employee association or version summary configurations are included.
        self.parent_id = parent_id
        # The path of the directory. If this parameter is omitted or set to null, the server calculates the path based on the parent directory and the name.
        self.path = path
        # The ID of the target tenant. This parameter is used for tenant routing in public requests. The server authentication chain verifies access permissions based on this parameter. You cannot use this parameter to access unauthorized tenants.
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

        if self.change_record_enabled is not None:
            result['changeRecordEnabled'] = self.change_record_enabled

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.oo_visibility_mode is not None:
            result['ooVisibilityMode'] = self.oo_visibility_mode

        if self.operating_object_names is not None:
            result['operatingObjectNames'] = self.operating_object_names

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.path is not None:
            result['path'] = self.path

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('changeRecordEnabled') is not None:
            self.change_record_enabled = m.get('changeRecordEnabled')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ooVisibilityMode') is not None:
            self.oo_visibility_mode = m.get('ooVisibilityMode')

        if m.get('operatingObjectNames') is not None:
            self.operating_object_names = m.get('operatingObjectNames')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

