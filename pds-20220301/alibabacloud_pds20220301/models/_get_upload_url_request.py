# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class GetUploadUrlRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[main_models.GetUploadUrlRequestPartInfoList] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The information about the file parts.
        # 
        # This parameter is required.
        self.part_info_list = part_info_list
        # The share ID.
        self.share_id = share_id
        # The ID of the upload task.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for v1 in self.part_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k1 in self.part_info_list:
                result['part_info_list'].append(k1.to_map() if k1 else None)

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k1 in m.get('part_info_list'):
                temp_model = main_models.GetUploadUrlRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k1))

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        return self

class GetUploadUrlRequestPartInfoList(DaraModel):
    def __init__(
        self,
        content_md_5: str = None,
        content_type: str = None,
        parallel_sha_1ctx: main_models.GetUploadUrlRequestPartInfoListParallelSha1Ctx = None,
        parallel_sha_256ctx: main_models.GetUploadUrlRequestPartInfoListParallelSha256Ctx = None,
        part_number: int = None,
    ):
        self.content_md_5 = content_md_5
        self.content_type = content_type
        # The SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.parallel_sha_1ctx = parallel_sha_1ctx
        self.parallel_sha_256ctx = parallel_sha_256ctx
        # The serial number of a part.
        self.part_number = part_number

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()
        if self.parallel_sha_256ctx:
            self.parallel_sha_256ctx.validate()

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

        if self.parallel_sha_256ctx is not None:
            result['parallel_sha256_ctx'] = self.parallel_sha_256ctx.to_map()

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
            temp_model = main_models.GetUploadUrlRequestPartInfoListParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m.get('parallel_sha1_ctx'))

        if m.get('parallel_sha256_ctx') is not None:
            temp_model = main_models.GetUploadUrlRequestPartInfoListParallelSha256Ctx()
            self.parallel_sha_256ctx = temp_model.from_map(m.get('parallel_sha256_ctx'))

        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')

        return self

class GetUploadUrlRequestPartInfoListParallelSha256Ctx(DaraModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        self.h = h
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

class GetUploadUrlRequestPartInfoListParallelSha1Ctx(DaraModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to fifth 32-bit variables of the SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.h = h
        # The size of the file part. Unit: bytes. The value must be a multiple of 64. This parameter takes effect only if the parallel upload feature is enabled.
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

