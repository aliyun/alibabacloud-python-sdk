# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListTransferFilesResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListTransferFilesResponseBodyFiles] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The files.
        self.files = files
        # The number of entries to return on each page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The returned value of `NextToken` is a pagination token, which can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListTransferFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTransferFilesResponseBodyFiles(DaraModel):
    def __init__(
        self,
        icon_url: str = None,
        id: str = None,
        name: str = None,
        oss_file_name: str = None,
        oss_file_path: str = None,
        size: str = None,
        status: str = None,
        type: str = None,
    ):
        # The URL of the file icon.
        # 
        # > 
        # 
        # *   For image file types (.png, .jpg, .jpeg, .gif, .webp, and .svg), the URL of the specific image is returned.
        # 
        # *   For other file types, the URL of the default image is returned.
        self.icon_url = icon_url
        # The file ID.
        self.id = id
        # The file name.
        self.name = name
        # The name of the object stored in OSS.
        # 
        # > 
        # 
        # *   A value is returned for this parameter only when the object is stored in a custom OSS bucket.
        self.oss_file_name = oss_file_name
        # The path of the object in the OSS bucket.
        # 
        # > 
        # 
        # *   A value is returned for this parameter only when the object is stored in a custom OSS bucket.
        self.oss_file_path = oss_file_path
        # The file size.
        self.size = size
        # The file status.
        # 
        # Valid values:
        # 
        # *   DELETING
        # *   DELETED
        # *   UPLOADED
        self.status = status
        # The file type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name

        if self.oss_file_path is not None:
            result['OssFilePath'] = self.oss_file_path

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')

        if m.get('OssFilePath') is not None:
            self.oss_file_path = m.get('OssFilePath')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

