# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetFileMeta(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        download_url: str = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        score: float = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        status: str = None,
        tags: str = None,
        thumbnail_url: str = None,
        uri: str = None,
    ):
        # The MIME type of the file. The value contains the type and subtype.
        self.content_type = content_type
        # The file size, in bytes.
        self.data_size = data_size
        # The dataset file metadata ID.
        self.dataset_file_meta_id = dataset_file_meta_id
        # The download URL of the file.
        self.download_url = download_url
        # The file creation time. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # The file fingerprint value. This parameter is used to determine the uniqueness of the file content. The value changes when the file content is modified. The ETag is used for OSS files, and the MD5 value is used for NAS files.
        self.file_finger_print = file_finger_print
        # The file name.
        self.file_name = file_name
        # The file type. The value is the same as the MIME type.
        self.file_type = file_type
        # The last modification time of the file. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        # The specific metadata of the file. For example, image width and height, or video bitrate and resolution. Search is not supported for this field. The value is in JSON string format.
        self.meta_attributes = meta_attributes
        # The similarity score.
        self.score = score
        # The task ID of the last semantic index build.
        self.semantic_index_job_id = semantic_index_job_id
        # The last update time of the semantic index. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        # The current status of the metadata. Valid values:
        # * ACTIVE: active.
        # * DELETED: deleted.
        self.status = status
        # The collection of labels for the metadata, in JSON string format. The following label groups are included:
        # - Algorithm label group:
        #   - ai: the list of label names aggregated from all algorithm labeling tasks for a single metadata entry.
        # - User-defined label group:
        #   - user: the list of label names manually added by the user for a single metadata entry.
        #   - user-delete-ai-tags: the list of label names in the algorithm label group that the user wants to delete for a single metadata entry.
        self.tags = tags
        # The thumbnail URL.
        self.thumbnail_url = thumbnail_url
        # The unique URI of the file. This parameter is used to record the unique path of the file. File paths in OSS and NAS are supported.
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
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

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

        if self.score is not None:
            result['Score'] = self.score

        if self.semantic_index_job_id is not None:
            result['SemanticIndexJobId'] = self.semantic_index_job_id

        if self.semantic_index_update_time is not None:
            result['SemanticIndexUpdateTime'] = self.semantic_index_update_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

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

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SemanticIndexJobId') is not None:
            self.semantic_index_job_id = m.get('SemanticIndexJobId')

        if m.get('SemanticIndexUpdateTime') is not None:
            self.semantic_index_update_time = m.get('SemanticIndexUpdateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

