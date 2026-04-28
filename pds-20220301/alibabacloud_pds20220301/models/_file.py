# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class File(DaraModel):
    def __init__(
        self,
        action_list: List[str] = None,
        auto_delete_left_sec: int = None,
        category: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        dir_size_info: main_models.FileDirSizeInfo = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        id_path: str = None,
        image_media_metadata: main_models.ImageMediaMetadata = None,
        labels: List[str] = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        name_path: str = None,
        parent_file_id: str = None,
        revision_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        thumbnail: str = None,
        thumbnail_urls: Dict[str, str] = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        user_tags: Dict[str, str] = None,
        video_media_metadata: main_models.VideoMediaMetadata = None,
    ):
        # The permissions.
        self.action_list = action_list
        # The remaining time until the file is automatically deleted from the recycle bin (if in it).
        self.auto_delete_left_sec = auto_delete_left_sec
        # The category. Drive and Photo Service (PDS) classifies files based on their extensions and mime-type. The supported categories include doc, image, audio, and video.
        self.category = category
        # The hash value of the content.
        self.content_hash = content_hash
        # The name of the hash algorithm. Set the value to sha1.
        self.content_hash_name = content_hash_name
        # The type of the content.
        self.content_type = content_type
        # crc64
        self.crc_64hash = crc_64hash
        # The time when the file was created.
        self.created_at = created_at
        # The description of the file.
        self.description = description
        # The information about the folder structure. This parameter is returned only if you include the dir_size field in the fields parameter by calling the ListFile or GetFile operation.
        self.dir_size_info = dir_size_info
        # The domain ID.
        self.domain_id = domain_id
        # The download URL. The default validity period of the download URL is 15 minutes. If the URL expires, you can obtain the URL by calling the GetFile operation.
        self.download_url = download_url
        # The drive ID.
        self.drive_id = drive_id
        # The file name extension.
        self.file_extension = file_extension
        # The file ID.
        self.file_id = file_id
        # Specifies whether to hide the file.
        self.hidden = hidden
        # The file ID path.
        self.id_path = id_path
        # The image metadata. This parameter takes effect only if the value-added image processing feature is enabled.
        self.image_media_metadata = image_media_metadata
        # The labels of the file.
        self.labels = labels
        # The time when the local file was created. The time refers to the local time when the file was uploaded. This parameter helps identify the local upload time.
        self.local_created_at = local_created_at
        # The time when the local file was modified. The time refers to the local time when the modified file was uploaded. This parameter helps identify the local update time.
        self.local_modified_at = local_modified_at
        # The file name.
        self.name = name
        # The file path.
        self.name_path = name_path
        # The parent folder ID.
        self.parent_file_id = parent_file_id
        # The version ID. If a file that has the same file ID with an existing one is uploaded, a new version ID is generated for the file.
        self.revision_id = revision_id
        # The file size
        # 
        # or folder size. The folder size is calculated based on all descendant files and folders in the folder. Note: The folder size can be returned only when you call the ListFile or GetFile operation and include the dir_size field in the fields parameter.
        self.size = size
        # Specifies whether to add the file to favorites.
        self.starred = starred
        # The status of the file. Only files and directories in the available state can be accessed. If you call the GetFile operation to obtain a file that is in the uploading state, a response indicating that the file does not exist is returned. If you call the ListFile operation to query files, files in the uploading state are not returned.
        self.status = status
        # The URL of the thumbnail. This parameter is deprecated and we recommend that you use thumbnail_urls.
        self.thumbnail = thumbnail
        # The information about the returned thumbnail. The value corresponds to the key that is specified by thumbnail_processes.
        self.thumbnail_urls = thumbnail_urls
        # The time when the file was put into the recycle bin.
        self.trashed_at = trashed_at
        # The file type.
        # 
        # Valid values:
        # 
        # *   file
        # *   folder
        self.type = type
        # The time when the file was modified.
        self.updated_at = updated_at
        # The upload ID.
        self.upload_id = upload_id
        # The custom tags.
        self.user_tags = user_tags
        # The audio and video information.
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.dir_size_info:
            self.dir_size_info.validate()
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['action_list'] = self.action_list

        if self.auto_delete_left_sec is not None:
            result['auto_delete_left_sec'] = self.auto_delete_left_sec

        if self.category is not None:
            result['category'] = self.category

        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.dir_size_info is not None:
            result['dir_size_info'] = self.dir_size_info.to_map()

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.download_url is not None:
            result['download_url'] = self.download_url

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_extension is not None:
            result['file_extension'] = self.file_extension

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.hidden is not None:
            result['hidden'] = self.hidden

        if self.id_path is not None:
            result['id_path'] = self.id_path

        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()

        if self.labels is not None:
            result['labels'] = self.labels

        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at

        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.name_path is not None:
            result['name_path'] = self.name_path

        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.size is not None:
            result['size'] = self.size

        if self.starred is not None:
            result['starred'] = self.starred

        if self.status is not None:
            result['status'] = self.status

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.thumbnail_urls is not None:
            result['thumbnail_urls'] = self.thumbnail_urls

        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        if self.user_tags is not None:
            result['user_tags'] = self.user_tags

        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')

        if m.get('auto_delete_left_sec') is not None:
            self.auto_delete_left_sec = m.get('auto_delete_left_sec')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('dir_size_info') is not None:
            temp_model = main_models.FileDirSizeInfo()
            self.dir_size_info = temp_model.from_map(m.get('dir_size_info'))

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')

        if m.get('id_path') is not None:
            self.id_path = m.get('id_path')

        if m.get('image_media_metadata') is not None:
            temp_model = main_models.ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m.get('image_media_metadata'))

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')

        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('name_path') is not None:
            self.name_path = m.get('name_path')

        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('starred') is not None:
            self.starred = m.get('starred')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('thumbnail_urls') is not None:
            self.thumbnail_urls = m.get('thumbnail_urls')

        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')

        if m.get('video_media_metadata') is not None:
            temp_model = main_models.VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(m.get('video_media_metadata'))

        return self

class FileDirSizeInfo(DaraModel):
    def __init__(
        self,
        dir_count: int = None,
        file_count: int = None,
    ):
        # The number of all descendant folders in the folder, which is calculated recursively.
        self.dir_count = dir_count
        # The number of all descendant files in the folder, which is calculated recursively.
        self.file_count = file_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dir_count is not None:
            result['dir_count'] = self.dir_count

        if self.file_count is not None:
            result['file_count'] = self.file_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dir_count') is not None:
            self.dir_count = m.get('dir_count')

        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')

        return self

