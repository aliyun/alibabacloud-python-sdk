# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class UploadPartInfo(DaraModel):
    def __init__(
        self,
        etag: str = None,
        internal_upload_url: str = None,
        parallel_sha_1ctx: main_models.UploadPartInfoParallelSha1Ctx = None,
        parallel_sha_256ctx: main_models.UploadPartInfoParallelSha256Ctx = None,
        part_number: int = None,
        part_size: int = None,
        upload_url: str = None,
    ):
        # This parameter is discontinued.
        self.etag = etag
        # The internal upload URL that is used for internal access over a virtual private cloud (VPC). If the intelligent domain name feature is enabled, this parameter is not required. This parameter is returned in the upload_url parameter based on the request. If you want to use this parameter, contact Photo and Drive Service (PDS) technical support.
        self.internal_upload_url = internal_upload_url
        # The Secure Hash Algorithm 1 (SHA-1) context of the previous part. This parameter takes effect only if the parallel upload feature is enabled.
        self.parallel_sha_1ctx = parallel_sha_1ctx
        # The SHA-256 context of the previous part.
        self.parallel_sha_256ctx = parallel_sha_256ctx
        # The serial number of the file part.
        # 
        # This parameter is required.
        self.part_number = part_number
        # This parameter is discontinued.
        self.part_size = part_size
        # The upload URL. By default, the validity period of the URL is 15 minutes. If the URL expires, you must call the GetUploadUrl operation to obtain another URL. If the intelligent domain name feature is enabled, the internal_upload_url value is returned within the parameter based on the request.
        # 
        # This parameter is required.
        self.upload_url = upload_url

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
        if self.etag is not None:
            result['etag'] = self.etag

        if self.internal_upload_url is not None:
            result['internal_upload_url'] = self.internal_upload_url

        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()

        if self.parallel_sha_256ctx is not None:
            result['parallel_sha256_ctx'] = self.parallel_sha_256ctx.to_map()

        if self.part_number is not None:
            result['part_number'] = self.part_number

        if self.part_size is not None:
            result['part_size'] = self.part_size

        if self.upload_url is not None:
            result['upload_url'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')

        if m.get('internal_upload_url') is not None:
            self.internal_upload_url = m.get('internal_upload_url')

        if m.get('parallel_sha1_ctx') is not None:
            temp_model = main_models.UploadPartInfoParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m.get('parallel_sha1_ctx'))

        if m.get('parallel_sha256_ctx') is not None:
            temp_model = main_models.UploadPartInfoParallelSha256Ctx()
            self.parallel_sha_256ctx = temp_model.from_map(m.get('parallel_sha256_ctx'))

        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')

        if m.get('part_size') is not None:
            self.part_size = m.get('part_size')

        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')

        return self

class UploadPartInfoParallelSha256Ctx(DaraModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to eighth 32-bit variables in the SHA-256 context of the previous part.
        self.h = h
        # The total size of all the previous parts. Unit: bytes. The value must be a multiple of 64.
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

class UploadPartInfoParallelSha1Ctx(DaraModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to fifth 32-bit variables in the SHA-1 context of the previous part. This parameter takes effect only if the parallel upload feature is enabled.
        self.h = h
        # The total size of all the previous parts. Unit: bytes. The value must be a multiple of 64. This parameter takes effect only if the parallel upload feature is enabled.
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

