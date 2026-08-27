# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        kb_name: str = None,
        kb_url: str = None,
        object_bindings: List[main_models.CreatePersonalAlidingKnowledgeBaseRequestObjectBindings] = None,
        operating_object_name: str = None,
        sync_config: main_models.CreatePersonalAlidingKnowledgeBaseRequestSyncConfig = None,
        tenant_id: str = None,
    ):
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

        if self.sync_config is not None:
            result['syncConfig'] = self.sync_config.to_map()

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # The cron expression for timed scheduling.
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

