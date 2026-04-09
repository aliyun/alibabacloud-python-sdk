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
        # The file comment.
        self.comment = comment
        # The MIME type of the file. It contains Type and SubType.
        # 
        # Valid values:
        # 
        # *   image/png: PNG.
        # *   image/jpeg: JPEG.
        # *   image/tiff: TIFF.
        # *   image/bmp: BMP.
        # *   image/gif: GIF.
        # *   image/x-icon: ICON.
        # *   image/svg+xml: SVG.
        # *   image/webp: WEBP.
        # *   image/heic: HEIC
        # 
        # This parameter is required.
        self.content_type = content_type
        # The file size. Unit: bytes.
        self.data_size = data_size
        # The time when the file was created. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # The file fingerprint. Used to check the uniqueness of the file. This value changes after the file content is modified. OSS files use ETags, and NAS files use MD5 values.
        # 
        # This parameter is required.
        self.file_finger_print = file_finger_print
        # The file name.
        self.file_name = file_name
        # The file type. The same as MIME type.
        # 
        # Valid values:
        # 
        # *   image
        # *   application
        # *   audio
        # *   video
        # *   text
        # 
        # This parameter is required.
        self.file_type = file_type
        # The time when the file was last modified. The time follows the ISO 8601 standard.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        # The specific metadata of the file. You cannot retrieve the metadata. The value is a JSON string.
        self.meta_attributes = meta_attributes
        # The tags manually added. The value is a JSON string. Operable tag group:
        # 
        # *   user: the list of tags to add to a metadata entry.
        # 
        # <!---->
        # 
        #     {
        #         "user":{
        #             "add":["lane line","sunny"]
        #         }
        #     }
        self.tags = tags
        # The URI of the file. Used to record the unique path of the file. File paths in Object Storage Service (OSS) and File Storage NAS (NAS) are supported.
        # 
        # **OSS**
        # 
        # oss://${bucket}/${path}
        # 
        # **NAS**
        # 
        # nas://${fileSystemId}/${path}
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

