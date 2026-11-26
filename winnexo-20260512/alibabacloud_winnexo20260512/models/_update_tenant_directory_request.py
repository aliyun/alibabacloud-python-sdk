# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateTenantDirectoryRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        change_record_enabled: bool = None,
        description: str = None,
        directory_id: str = None,
        name: str = None,
        oo_visibility_mode: str = None,
        operating_object_names: List[str] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        parent_id: int = None,
        path: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 后续内容更新的AI版本摘要开关；false关闭，未传/null保持既有语义，不删除既有摘要
        self.change_record_enabled = change_record_enabled
        # The new directory description. If this parameter is omitted or set to null, the original value is retained.
        self.description = description
        # The business ID of the enterprise knowledge base directory for the current tenant, which is not the internal primary key. When digital employee associations or version summary configurations are included, the target must be the root directory of a standard enterprise knowledge base.
        self.directory_id = directory_id
        # The new directory name. It can be up to 256 characters in length. If this parameter is omitted or set to null, the original value is retained.
        self.name = name
        # 数字员工关联模式；仅普通企业知识库根可设置。未传/null保持既有语义；SPECIFIED须显式提供名单，ALL仅允许省略或空名单
        self.oo_visibility_mode = oo_visibility_mode
        # 数字员工内部名称列表，最多100项，每项非空且最多256字符；SPECIFIED空数组表示不关联任何员工，非空名单按去重后全量替换
        self.operating_object_names = operating_object_names
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The internal primary key of the new parent folder. If this parameter is omitted or set to null, the original parent folder is retained. If a non-null value is passed, knowledge base management permissions for the target parent folder are required. This parameter cannot be committed at the same time as the digital employee associate or version summary configurations.
        self.parent_id = parent_id
        # The new directory path. If this parameter is omitted or set to null, a new path is not explicitly specified and is processed by the directory service.
        self.path = path
        # The ID of the target tenant. It is used for tenant routing in public requests. The server-side authentication chain verifies access permissions. You cannot use this parameter to access unauthorized tenants.
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

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

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

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

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

