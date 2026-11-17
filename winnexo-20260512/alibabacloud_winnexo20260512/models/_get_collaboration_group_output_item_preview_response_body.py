# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCollaborationGroupOutputItemPreviewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        degraded: bool = None,
        download_url: str = None,
        file_ext: str = None,
        file_name: str = None,
        item_id: str = None,
        message: str = None,
        preview_type: str = None,
        preview_url: str = None,
        request_id: str = None,
    ):
        # The common business status code.
        self.code = code
        # The text content or preview prompt. This field can be empty.
        self.content = content
        # Indicates whether the preview is downgraded to a download preview.
        self.degraded = degraded
        # The short-term signed download URL. This field can be empty. If the URL expires, call this operation again.
        self.download_url = download_url
        # The file name extension. This field can be empty.
        self.file_ext = file_ext
        # The file name. This field can be empty.
        self.file_name = file_name
        # The output detail ID.
        self.item_id = item_id
        # The common error description.
        self.message = message
        # The preview type.
        self.preview_type = preview_type
        # The short-term preview URL. This field can be empty.
        self.preview_url = preview_url
        # The request tracking ID.
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

        if self.degraded is not None:
            result['degraded'] = self.degraded

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.file_ext is not None:
            result['fileExt'] = self.file_ext

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.message is not None:
            result['message'] = self.message

        if self.preview_type is not None:
            result['previewType'] = self.preview_type

        if self.preview_url is not None:
            result['previewUrl'] = self.preview_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('degraded') is not None:
            self.degraded = m.get('degraded')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('fileExt') is not None:
            self.file_ext = m.get('fileExt')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')

        if m.get('previewUrl') is not None:
            self.preview_url = m.get('previewUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

