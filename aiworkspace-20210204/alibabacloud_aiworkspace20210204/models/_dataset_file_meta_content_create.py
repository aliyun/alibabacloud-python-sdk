# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetFileMetaContentCreate(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        tags: str = None,
        uri: str = None,
    ):
        # The comment on the file.
        self.comment = comment
        # The MIME type of the file. It includes a type and a subtype.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The size of the file in bytes.
        self.data_size = data_size
        # The time when the file was created. The time is in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # The fingerprint of the file. This value ensures the uniqueness of the file content and changes if the content is modified. For OSS files, this is the ETag. For NAS files, this is the MD5 value.
        # 
        # This parameter is required.
        self.file_finger_print = file_finger_print
        # The name of the file.
        self.file_name = file_name
        # The type of the file. This is the same as the Multipurpose Internet Mail Extensions (MIME) type.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The time when the file was last modified. The time is in ISO 8601 format.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        # The specific metadata of the file. This metadata cannot be used for retrieval. The value must be a JSON string.
        self.meta_attributes = meta_attributes
        # The tags that are manually added by users. The \\`add\\` operation is used to add tags to a tag group. The value must be a JSON string.
        # The following tag group is available:
        # 
        # - user: A list of tag names added to a single piece of metadata.
        # 
        # ```
        # {
        #     "user":{
        #         "add":["Lane line","Sunny day"]
        #     }
        # }
        # ```
        self.tags = tags
        # The unique URI of the file. This URI records the unique path of the file. The path can be an OSS or NAS path.
        # 
        # <details>
        # 
        # <summary>
        # 
        # OSS
        # 
        # </summary>
        # 
        # oss\\://${bucket}/${path}
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # NAS
        # 
        # </summary>
        # 
        # nas\\://${fileSystemId}/${path}
        # 
        # </details>
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time

        if self.file_finger_print is not None:
            result['FileFingerPrint'] = self.file_finger_print

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time

        if self.meta_attributes is not None:
            result['MetaAttributes'] = self.meta_attributes

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')

        if m.get('FileFingerPrint') is not None:
            self.file_finger_print = m.get('FileFingerPrint')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')

        if m.get('MetaAttributes') is not None:
            self.meta_attributes = m.get('MetaAttributes')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

