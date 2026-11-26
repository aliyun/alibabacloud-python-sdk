# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        kb_name: str = None,
        kb_url: str = None,
        object_bindings: List[main_models.CreatePersonalAlidingKnowledgeBaseRequestObjectBindings] = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_tags: str = None,
        sync_config: main_models.CreatePersonalAlidingKnowledgeBaseRequestSyncConfig = None,
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
        self.object_bindings = object_bindings
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The list of resource tag JSON strings applied to all child sources created during knowledge base synchronization.
        self.source_tags = source_tags
        # The synchronization settings.
        self.sync_config = sync_config
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.object_bindings:
            for v1 in self.object_bindings:
                 if v1:
                    v1.validate()
        if self.sync_config:
            self.sync_config.validate()

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

        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.sync_config is not None:
            result['syncConfig'] = self.sync_config.to_map()

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

        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.CreatePersonalAlidingKnowledgeBaseRequestObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('syncConfig') is not None:
            temp_model = main_models.CreatePersonalAlidingKnowledgeBaseRequestSyncConfig()
            self.sync_config = temp_model.from_map(m.get('syncConfig'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class CreatePersonalAlidingKnowledgeBaseRequestSyncConfig(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
    ):
        # The cron expression for the timed scheduling node.
        self.cron = cron
        # Specifies whether to enable synchronization.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class CreatePersonalAlidingKnowledgeBaseRequestObjectBindings(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        object_type: str = None,
    ):
        # The ID of the recommended item, which can be a **feedId** or a micro-application ID.
        self.object_id = object_id
        # The advanced field type.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

