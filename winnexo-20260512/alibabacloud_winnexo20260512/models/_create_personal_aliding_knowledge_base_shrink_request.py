# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseShrinkRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        kb_name: str = None,
        kb_url: str = None,
        object_bindings_shrink: str = None,
        operating_object_name: str = None,
        sync_config_shrink: str = None,
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
        self.object_bindings_shrink = object_bindings_shrink
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
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

        if self.sync_config_shrink is not None:
            result['syncConfig'] = self.sync_config_shrink

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

        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('syncConfig') is not None:
            self.sync_config_shrink = m.get('syncConfig')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

