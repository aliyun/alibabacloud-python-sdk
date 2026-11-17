# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeObjectUploadRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_md_5: str = None,
        content_sha_256: str = None,
        content_type: str = None,
        file_name: str = None,
        knowledge_base_id: str = None,
        size_bytes: int = None,
    ):
        # The idempotency key for the upload request.
        self.client_token = client_token
        # The Base64-encoded MD5 hash value of the original file.
        # 
        # This parameter is required.
        self.content_md_5 = content_md_5
        # The SHA-256 checksum of the original file.
        self.content_sha_256 = content_sha_256
        # The HTTP media type for the upload.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The original file name, which is not used as the object ID.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The target knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The size of the original file in bytes. This parameter reuses the existing maximum size limit for single-file uploads, which defaults to 100 MiB. If the size exceeds the limit, the InputTooLarge error is returned.
        # 
        # This parameter is required.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5

        if self.content_sha_256 is not None:
            result['ContentSha256'] = self.content_sha_256

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')

        if m.get('ContentSha256') is not None:
            self.content_sha_256 = m.get('ContentSha256')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')

        return self

