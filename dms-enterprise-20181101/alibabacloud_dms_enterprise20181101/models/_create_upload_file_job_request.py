# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadFileJobRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_source: str = None,
        tid: int = None,
        upload_url: str = None,
    ):
        # The name of the attachment file.
        # 
        # >  The file name must end with .txt or .sql. For example, the file name can be test.txt or test.sql.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The purpose of the attachment file. Valid values:
        # 
        # *   **datacorrect**: The file is uploaded to change data.
        # *   **order_info_attachment**: The file is uploaded as an attachment in a ticket.
        # *   **big-file**: The file is uploaded to import multiple data records at a time.
        # *   **sqlreview**: The file is uploaded for SQL review.
        # 
        # This parameter is required.
        self.file_source = file_source
        # The ID of the tenant.
        # 
        # >  You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid
        # The URL of the attachment file. The URL must be an HTTP URL or an HTTPS URL.
        # 
        # >  You can upload the attachment file to an Object Storage Service (OSS) bucket and obtain the URL of the file in the OSS console. For more information, see [Share objects](https://help.aliyun.com/document_detail/195674.html).
        # 
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_source is not None:
            result['FileSource'] = self.file_source

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')

        return self

