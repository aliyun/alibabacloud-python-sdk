# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class TranscribeChatVoiceAdvanceRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        file_content_base_64: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        tenant_id: str = None,
    ):
        # The content type of the file. Valid values:
        # - **image**: Image.
        # - **document**: General document.
        # - **alidoc**: AliDoc.
        # - **text**: Text.
        # - **video**: Video.
        # - **audio**: Audio.
        # - **archive**: Archive.
        # - **app**: Application.
        # - **link**: Shortcut.
        # - **other**: Other.
        self.content_type = content_type
        # The standard Base64-encoded audio content, excluding the data URI prefix. This parameter and FileUrl are mutually exclusive.
        self.file_content_base_64 = file_content_base_64
        # The full path and name of the file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The publicly accessible URL of the attachment.
        self.file_url_object = file_url_object
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.file_content_base_64 is not None:
            result['fileContentBase64'] = self.file_content_base_64

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('fileContentBase64') is not None:
            self.file_content_base_64 = m.get('fileContentBase64')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

