# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetFileMetaContentGet(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        file_create_time: str = None,
        file_dir: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        status: str = None,
        tag_update_time: str = None,
        tags: str = None,
        uri: str = None,
    ):
        # The file comment.
        self.comment = comment
        # The MIME type of the file, which includes the type and subtype.
        self.content_type = content_type
        # The file size in bytes.
        self.data_size = data_size
        # The ID of the dataset file metadata.
        self.dataset_file_meta_id = dataset_file_meta_id
        # The creation time of the file in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # The directory path of the OSS, NAS, or CPFS file.
        self.file_dir = file_dir
        # The fingerprint of the file. This value is used to determine the uniqueness of the file content and changes when the file content is modified. The ETag is used for OSS files, and the MD5 value is used for NAS files.
        self.file_finger_print = file_finger_print
        # The file name.
        self.file_name = file_name
        # The file type. This is the same as the MIME type.
        self.file_type = file_type
        # The last modification time of the file in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        # The specific metadata of the file in JSON string format. This metadata does not support search capabilities.
        self.meta_attributes = meta_attributes
        # The task ID for building the semantic index.
        self.semantic_index_job_id = semantic_index_job_id
        # The time when the semantic index was built.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        # The status of the file metadata. ACTIVE indicates that the metadata is valid, and DELETED indicates that the metadata is deleted.
        self.status = status
        # The last modification time of the tags in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.tag_update_time = tag_update_time
        # The collection of tags for this metadata, including:
        # - Algorithm tag groups:
        #   - ai: A list of tag names summarized from all algorithm tagging tasks for a single metadata entry.
        # - User-defined tag groups:
        #   - user: A list of tag names added by the user for a single metadata entry.
        #   - user-delete-ai-tags: A list of tag names to be deleted by the user from the algorithm tag group for a single metadata entry.
        self.tags = tags
        # The unique URI of the file. This URI records the unique path of the file. File paths in OSS and NAS are supported.
        # <details>
        # <summary>OSS</summary>
        # oss://${bucket}/${path}
        # </details>
        # <details>
        # <summary>NAS</summary>
        # nas://${fileSystemId}/${path}
        # </details>
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

        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id

        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time

        if self.file_dir is not None:
            result['FileDir'] = self.file_dir

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

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_update_time is not None:
            result['TagUpdateTime'] = self.tag_update_time

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

        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')

        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')

        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagUpdateTime') is not None:
            self.tag_update_time = m.get('TagUpdateTime')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

