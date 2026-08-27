# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseAliDingDocRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        file_public_url: str = None,
        knowledge_id: str = None,
        name: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # The description of the alias.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The publicly accessible URL of the AliDing online document.
        # 
        # This parameter is required.
        self.file_public_url = file_public_url
        # Not supported. This parameter is ignored.
        self.knowledge_id = knowledge_id
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The resource tags (optional, a JSON string list, such as ["tagA","tagB"]).
        self.source_tags = source_tags
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.knowledge_id is not None:
            result['knowledgeId'] = self.knowledge_id

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('knowledgeId') is not None:
            self.knowledge_id = m.get('knowledgeId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

