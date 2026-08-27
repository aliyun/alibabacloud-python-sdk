# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewKnowledgeBaseSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        file_ext: str = None,
        file_name: str = None,
        message: str = None,
        preview_type: str = None,
        preview_url: str = None,
        public_url: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The text content. This is used for the CONTENT type.
        self.content = content
        # The file name extension. This is used for the OSS_IMM type.
        self.file_ext = file_ext
        # The file name. This is used for the OSS_IMM type.
        self.file_name = file_name
        # The description of the status code.
        self.message = message
        # The preview type. Valid values: OSS_IMM, IMAGE, AUDIO, VIDEO, HTML, DING_TALK, VOICE_MEETING, CONTENT.
        self.preview_type = preview_type
        # The preview URL. This is used for the OSS_IMM, DING_TALK, and VOICE_MEETING types.
        self.preview_url = preview_url
        # The public download URL of the file.
        self.public_url = public_url
        # The request trace ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.file_ext is not None:
            result['fileExt'] = self.file_ext

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.message is not None:
            result['message'] = self.message

        if self.preview_type is not None:
            result['previewType'] = self.preview_type

        if self.preview_url is not None:
            result['previewUrl'] = self.preview_url

        if self.public_url is not None:
            result['publicUrl'] = self.public_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('fileExt') is not None:
            self.file_ext = m.get('fileExt')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')

        if m.get('previewUrl') is not None:
            self.preview_url = m.get('previewUrl')

        if m.get('publicUrl') is not None:
            self.public_url = m.get('publicUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

