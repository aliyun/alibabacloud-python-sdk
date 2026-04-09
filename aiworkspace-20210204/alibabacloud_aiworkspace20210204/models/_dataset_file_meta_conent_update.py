# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetFileMetaConentUpdate(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        tags: str = None,
    ):
        # The file comment.
        self.comment = comment
        # The MIME type of the file. The value consists of a type and a subtype.
        # 
        # Valid values:
        # 
        # *   image/png
        # *   image/svg+xml
        # *   image/jpeg
        # *   image/tiff
        # *   image/gif
        # *   image/bmp
        # *   image/x-icon
        # *   image/heic
        # *   image/webp
        self.content_type = content_type
        # The file size. Unit: byte.
        self.data_size = data_size
        # The metadata ID of the dataset file.
        # 
        # This parameter is required.
        self.dataset_file_meta_id = dataset_file_meta_id
        # The time when the file is created. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # The fingerprint information of the file.
        self.file_finger_print = file_finger_print
        # The file name.
        self.file_name = file_name
        # The file type, which is the same as Multipurpose Internet Mail Extensions (MIME) type.
        # 
        # Valid values:
        # 
        # *   image
        # *   application
        # *   audio
        # *   video
        # *   text
        self.file_type = file_type
        # The time when the file is last modified. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        # The specific metadata of the file, such as the width and height of an image and the bitrate and resolution of a video file. You cannot retrieve the metadata. The value is a JSON string.
        self.meta_attributes = meta_attributes
        # The ID of the semantic index-based job.
        self.semantic_index_job_id = semantic_index_job_id
        # The time when the semantic index is created.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        # The tags to be updated.
        # 
        # *   Update an algorithm tag group (a valid TagJobId must be set):
        # 
        # <!---->
        # 
        #     {
        #        "ai":["Lane line", "Water horse", "Sunny day"]
        #     }
        # 
        # *   Update a user-defined tag group (add or remove indicates that tags are added or deleted): Tag groups that can be updated:
        # 
        #     *   user: a list of user-defined tags that can be added to or deleted from a single piece of metadata.
        #     *   user-delete-ai-tags: a list of tags that you want to delete from an algorithm tag group.
        # 
        # <!---->
        # 
        #     {
        #         "user":{
        #             "add":["Lane line","Sunny day"],
        #             "remove":["Water horse"]    },
        #         "user-delete-ai-tags":{
        #             "add": ["Ground shadow"],
        #             "remove": []
        #         }
        #     }
        self.tags = tags

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

        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id

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

        if self.semantic_index_job_id is not None:
            result['SemanticIndexJobId'] = self.semantic_index_job_id

        if self.semantic_index_update_time is not None:
            result['SemanticIndexUpdateTime'] = self.semantic_index_update_time

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')

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

        if m.get('SemanticIndexJobId') is not None:
            self.semantic_index_job_id = m.get('SemanticIndexJobId')

        if m.get('SemanticIndexUpdateTime') is not None:
            self.semantic_index_update_time = m.get('SemanticIndexUpdateTime')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

