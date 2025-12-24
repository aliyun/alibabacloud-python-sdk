# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListCdsFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        file_models: List[main_models.ListCdsFilesResponseBodyFileModels] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response parameters. If the request was successful, `success` is returned. If the request failed, an error message is returned.
        self.code = code
        # The total number of file list entries.
        self.count = count
        # The files.
        self.file_models = file_models
        # Error message. This parameter is not returned if the value of Code is `success`.
        self.message = message
        # The token used to start the next query. If the `NextToken` is empty, the next query does not exist.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        # 
        # Valid value:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.file_models:
            for v1 in self.file_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['FileModels'] = []
        if self.file_models is not None:
            for k1 in self.file_models:
                result['FileModels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.file_models = []
        if m.get('FileModels') is not None:
            for k1 in m.get('FileModels'):
                temp_model = main_models.ListCdsFilesResponseBodyFileModels()
                self.file_models.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCdsFilesResponseBodyFileModels(DaraModel):
    def __init__(
        self,
        category: str = None,
        content_type: str = None,
        create_time: str = None,
        creator: str = None,
        description: str = None,
        download_url: str = None,
        file_extension: str = None,
        file_id: str = None,
        file_path: str = None,
        file_type: str = None,
        md_5: str = None,
        modified_time: str = None,
        modifier: str = None,
        name: str = None,
        open_time: str = None,
        open_time_stamp: int = None,
        parent_id: str = None,
        region_id: str = None,
        sha_1: str = None,
        size: int = None,
        thumbnail: str = None,
    ):
        # File type classification. The network disk will classify files according to their suffix and MIME Type. The main categories are `doc`, `image`, `audio` and `video`.
        self.category = category
        # The content type of the file.
        self.content_type = content_type
        # The time when the file was created.
        self.create_time = create_time
        # The file creator.
        self.creator = creator
        # The file description.
        self.description = description
        # The download link. The default validity period is 15 minutes.
        self.download_url = download_url
        # The filename extension.
        self.file_extension = file_extension
        # The file ID.
        self.file_id = file_id
        # The file path.
        self.file_path = file_path
        # The file type.
        # 
        # Valid value:
        # 
        # *   file
        # *   folder
        self.file_type = file_type
        # The MD5 hash of the object.
        self.md_5 = md_5
        # The time when the file was last modified.
        self.modified_time = modified_time
        # Modifier.
        self.modifier = modifier
        # The name of the file.
        self.name = name
        # The time when the file was last opened.
        self.open_time = open_time
        # The timestamp that indicates the time when the file was last opened.
        self.open_time_stamp = open_time_stamp
        # The ID of the parent folder.
        self.parent_id = parent_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to obtain the list of regions supported by cloud computers.
        self.region_id = region_id
        # The SHA1 hash of the data file.
        self.sha_1 = sha_1
        # The size of the file. Unit: bytes.
        self.size = size
        # The URL of the thumbnail.
        self.thumbnail = thumbnail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.name is not None:
            result['Name'] = self.name

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        if self.open_time_stamp is not None:
            result['OpenTimeStamp'] = self.open_time_stamp

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sha_1 is not None:
            result['Sha1'] = self.sha_1

        if self.size is not None:
            result['Size'] = self.size

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        if m.get('OpenTimeStamp') is not None:
            self.open_time_stamp = m.get('OpenTimeStamp')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sha1') is not None:
            self.sha_1 = m.get('Sha1')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        return self

