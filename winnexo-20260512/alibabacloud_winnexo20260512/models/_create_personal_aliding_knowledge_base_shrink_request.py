# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        kb_name: str = None,
        kb_url: str = None,
        object_bindings_shrink: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_tags: str = None,
        sync_config_shrink: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The directory ID.
        self.directory_id = directory_id
        # The display name of the knowledge base. If not provided, the name is populated from the root node name pulled from the remote source.
        self.kb_name = kb_name
        # The publicly accessible URL of the AliDing knowledge base.
        # 
        # This parameter is required.
        self.kb_url = kb_url
        # The object bindings.
        self.object_bindings_shrink = object_bindings_shrink
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The list of resource tag JSON strings applied to all child sources created during knowledge base synchronization.
        self.source_tags = source_tags
        # The synchronization settings.
        self.sync_config_shrink = sync_config_shrink
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

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.kb_name is not None:
            result['kbName'] = self.kb_name

        if self.kb_url is not None:
            result['kbUrl'] = self.kb_url

        if self.object_bindings_shrink is not None:
            result['objectBindings'] = self.object_bindings_shrink

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.sync_config_shrink is not None:
            result['syncConfig'] = self.sync_config_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('kbName') is not None:
            self.kb_name = m.get('kbName')

        if m.get('kbUrl') is not None:
            self.kb_url = m.get('kbUrl')

        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('syncConfig') is not None:
            self.sync_config_shrink = m.get('syncConfig')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

