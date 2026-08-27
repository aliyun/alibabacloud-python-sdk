# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceUploadSignatureResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content_type: str = None,
        expires_in: int = None,
        file_public_url: str = None,
        file_record_id: str = None,
        file_url: str = None,
        message: str = None,
        method: str = None,
        object_name: str = None,
        request_id: str = None,
        upload_signature_url: str = None,
    ):
        # The response status code.
        self.code = code
        # The content type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The validity period of the task, in seconds.
        self.expires_in = expires_in
        # The publicly accessible URL of the DingTalk online document.
        self.file_public_url = file_public_url
        # The file record ID. This parameter is optional and corresponds to settings.file_record_id.
        self.file_record_id = file_record_id
        # The Yida attachment URL.
        self.file_url = file_url
        # The prompt message.
        self.message = message
        # The method.
        self.method = method
        # The object name.
        self.object_name = object_name
        # The request ID.
        self.request_id = request_id
        # The signed URL.
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

        if self.expires_in is not None:
            result['expiresIn'] = self.expires_in

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.message is not None:
            result['message'] = self.message

        if self.method is not None:
            result['method'] = self.method

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

        if m.get('expiresIn') is not None:
            self.expires_in = m.get('expiresIn')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('uploadSignatureUrl') is not None:
            self.upload_signature_url = m.get('uploadSignatureUrl')

        return self

