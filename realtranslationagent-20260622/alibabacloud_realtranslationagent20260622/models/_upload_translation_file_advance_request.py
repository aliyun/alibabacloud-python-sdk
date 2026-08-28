# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class UploadTranslationFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        file_object: BinaryIO = None,
        file_name: str = None,
    ):
        # The API key that identifies the identity of the member accounts. You can obtain it from the RuiYiBao console.
        self.apikey = apikey
        # The file. The SDK supports direct upload and temporary authorized upload.
        # - **Direct upload**: Use UploadTranslationFileAdvance in the SDK for direct upload. The Java field type is InputStream, and the Python type is BinaryIO.
        # - **Temporary authorized upload**: Use AuthorizeFileUpload and UploadTranslationFile in the SDK for temporary authorized upload.
        #   - Step 1: Call AuthorizeFileUpload to obtain a temporary OSS upload credential, then upload the file to obtain the complete file URL.
        #   - Step 2: Call UploadTranslationFile and pass the URL to the File field.
        # 
        # > Notes on temporary authorized upload
        # > - You need to additionally import OpenPlatform(2019-12-19) - AuthorizeFileUpload to obtain a temporary OssPolicy. For information about how to upload files, refer to [Upload objects directly from clients to OSS](https://www.alibabacloud.com/help/en/oss/user-guide/uploading-objects-to-oss-directly-from-clients/).
        # 
        # > File size limit
        # > - The maximum file size is 500 MB.
        # 
        # This parameter is required.
        self.file_object = file_object
        # The name of the uploaded file.
        # 
        # <notice>Make sure the correct file name (including the extension) is provided. Otherwise, file parsing will fail.</notice>
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.file_object is not None:
            result['File'] = self.file_object

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('File') is not None:
            self.file_object = m.get('File')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

