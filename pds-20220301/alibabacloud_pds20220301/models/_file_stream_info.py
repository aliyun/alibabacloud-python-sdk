# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FileStreamInfo(DaraModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_md_5: str = None,
        part_info_list: List[main_models.UploadPartInfo] = None,
        pre_hash: str = None,
        proof_code: str = None,
        proof_version: str = None,
        size: int = None,
    ):
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_md_5 = content_md_5
        self.part_info_list = part_info_list
        self.pre_hash = pre_hash
        self.proof_code = proof_code
        self.proof_version = proof_version
        self.size = size

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
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5

        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k1 in self.part_info_list:
                result['part_info_list'].append(k1.to_map() if k1 else None)

        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash

        if self.proof_code is not None:
            result['proof_code'] = self.proof_code

        if self.proof_version is not None:
            result['proof_version'] = self.proof_version

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')

        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k1 in m.get('part_info_list'):
                temp_model = main_models.UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k1))

        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')

        if m.get('proof_code') is not None:
            self.proof_code = m.get('proof_code')

        if m.get('proof_version') is not None:
            self.proof_version = m.get('proof_version')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

