# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadChatFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content_type: str = None,
        file_name: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        file_url: str = None,
        message: str = None,
        object_name: str = None,
        request_id: str = None,
        upload_signature_url: str = None,
    ):
        # The status code.
        self.code = code
        # The content type of the file. Valid values:
        # 
        # - **image**: Image.
        # - **document**: General document.
        # - **alidoc**: Alibaba document.
        # - **text**: Text.
        # - **video**: Video.
        # - **audio**: Audio.
        # - **archive**: Archive.
        # - **app**: Application.
        # - **link**: Shortcut.
        # - **other**: Other.
        self.content_type = content_type
        # The full path name of the file.
        self.file_name = file_name
        # The publicly accessible URL of the AliDing online document.
        self.file_public_url = file_public_url
        # The file record ID. This parameter is optional and corresponds to settings.file_record_id.
        self.file_record_id = file_record_id
        # The Yida attachment address.
        self.file_url = file_url
        # The description of the status code.
        self.message = message
        # The object name.
        self.object_name = object_name
        # The request ID.
        self.request_id = request_id
        # The signature URL.
        self.upload_signature_url = upload_signature_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.message is not None:
            result['message'] = self.message

        if self.object_name is not None:
            result['objectName'] = self.object_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.upload_signature_url is not None:
            result['uploadSignatureUrl'] = self.upload_signature_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('uploadSignatureUrl') is not None:
            self.upload_signature_url = m.get('uploadSignatureUrl')

        return self

