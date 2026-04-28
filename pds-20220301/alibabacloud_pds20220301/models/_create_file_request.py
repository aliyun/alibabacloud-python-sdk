# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CreateFileRequest(DaraModel):
    def __init__(
        self,
        check_name_mode: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        description: str = None,
        drive_id: str = None,
        file_id: str = None,
        hidden: bool = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        parallel_upload: bool = None,
        parent_file_id: str = None,
        part_info_list: List[main_models.CreateFileRequestPartInfoList] = None,
        pre_hash: str = None,
        share_id: str = None,
        size: int = None,
        type: str = None,
        user_tags: List[main_models.UserTag] = None,
    ):
        # The processing method that is used if the file that you want to create has the same name as an existing file in the cloud. Valid values:
        # 
        # ignore: allows you to create the file by using the same name as an existing file in the cloud.
        # 
        # auto_rename: automatically renames the file that you want to create. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not create the file that you want to create but returns the information about the file that has the same name in the cloud.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The hash value of the file content. The value is calculated based on the algorithm specified by content_hash_name.
        self.content_hash = content_hash
        # The name of the algorithm that is used to calculate the hash value of the file content. Only SHA1 is supported.
        self.content_hash_name = content_hash_name
        # The type of the file content. Default value: application/oct-stream.
        self.content_type = content_type
        # The description of the file. The description can be up to 1,024 characters in length. By default, this parameter is left empty.
        self.description = description
        # The drive ID. This parameter is required if the file is not uploaded by using the share URL of the file.
        self.drive_id = drive_id
        # The file ID. This parameter is required if check_name_mode is set to ignore.
        self.file_id = file_id
        # Specifies whether to hide the file or folder. By default, the file or folder is not hidden.
        self.hidden = hidden
        # The time when the local file was created. By default, this parameter is left empty. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_created_at = local_created_at
        # The time when the local file was modified. By default, this parameter is left empty. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_modified_at = local_modified_at
        # The name of the file. The name can be up to 1,024 bytes in length based on the UTF-8 encoding rule and cannot contain forward slash (/).
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to enable the parallel upload feature.
        self.parallel_upload = parallel_upload
        # The ID of the parent directory. If you want to create a file or folder in the root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.parent_file_id = parent_file_id
        # The information about the file parts. You can specify up to 10,000 parts. By default, if you do not specify this parameter, only one part is returned.
        self.part_info_list = part_info_list
        # The SHA-1 hash value of the first 1 KB data of the file. This parameter is required if you perform instant file upload by using the pre-hashing feature. If the SHA-1 hash value is not matched on the cloud, the client does not need to calculate the SHA-1 hash value of the entire file.
        self.pre_hash = pre_hash
        # The share ID. This parameter is required if the file is uploaded by using the share URL of the file.
        self.share_id = share_id
        # The size of the file. Unit: bytes.
        self.size = size
        # The type of the file. Valid values:
        # 
        # file folder
        # 
        # This parameter is required.
        self.type = type
        # The custom tags. You can specify up to 1,000 tags.
        self.user_tags = user_tags

    def validate(self):
        if self.part_info_list:
            for v1 in self.part_info_list:
                 if v1:
                    v1.validate()
        if self.user_tags:
            for v1 in self.user_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode

        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.description is not None:
            result['description'] = self.description

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.hidden is not None:
            result['hidden'] = self.hidden

        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at

        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload

        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id

        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k1 in self.part_info_list:
                result['part_info_list'].append(k1.to_map() if k1 else None)

        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.size is not None:
            result['size'] = self.size

        if self.type is not None:
            result['type'] = self.type

        result['user_tags'] = []
        if self.user_tags is not None:
            for k1 in self.user_tags:
                result['user_tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')

        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')

        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')

        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')

        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')

        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k1 in m.get('part_info_list'):
                temp_model = main_models.CreateFileRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k1))

        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('type') is not None:
            self.type = m.get('type')

        self.user_tags = []
        if m.get('user_tags') is not None:
            for k1 in m.get('user_tags'):
                temp_model = main_models.UserTag()
                self.user_tags.append(temp_model.from_map(k1))

        return self

class CreateFileRequestPartInfoList(DaraModel):
    def __init__(
        self,
        content_md_5: str = None,
        content_type: str = None,
        parallel_sha_1ctx: main_models.CreateFileRequestPartInfoListParallelSha1Ctx = None,
        part_number: int = None,
    ):
        # The MD5 hash value of the file part. This parameter is required when the MD5 hash value of the file part needs to be verified during part upload.
        self.content_md_5 = content_md_5
        self.content_type = content_type
        # The SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.parallel_sha_1ctx = parallel_sha_1ctx
        # The serial number of a file part. The number starts from 1.
        self.part_number = part_number

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()

        if self.part_number is not None:
            result['part_number'] = self.part_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('parallel_sha1_ctx') is not None:
            temp_model = main_models.CreateFileRequestPartInfoListParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m.get('parallel_sha1_ctx'))

        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')

        return self

class CreateFileRequestPartInfoListParallelSha1Ctx(DaraModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to fifth 32-bit variables of the SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.h = h
        # The size of the file content before the file part. Unit: bytes. The value must be a multiple of 64. This parameter takes effect only if the parallel upload feature is enabled.
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['h'] = self.h

        if self.part_offset is not None:
            result['part_offset'] = self.part_offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')

        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')

        return self

