# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeObjectShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_shrink: str = None,
        description: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        type: str = None,
        upload_id: str = None,
    ):
        # The idempotency token for the creation request. Keep the original request unchanged when retrying.
        self.client_token = client_token
        # Only Content.Document is supported. It includes Text and ContentFormat (MARKDOWN or TEXT).
        self.content_shrink = content_shrink
        # The document description.
        self.description = description
        # The ID of the target knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The document name. Existing objects are not overwritten based on the name.
        # 
        # This parameter is required.
        self.name = name
        # The type of the object. For this operation, the value is fixed to DOCUMENT.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the completed PUT upload session for this knowledge base. This parameter is mutually exclusive with Content.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        return self

