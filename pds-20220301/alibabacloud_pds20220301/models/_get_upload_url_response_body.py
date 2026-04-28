# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class GetUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        create_at: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[main_models.UploadPartInfo] = None,
        upload_id: str = None,
    ):
        # The time when the upload task was created.
        self.create_at = create_at
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # The information about the file parts.
        self.part_info_list = part_info_list
        # The ID of the upload task.
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
        if self.create_at is not None:
            result['create_at'] = self.create_at

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k1 in self.part_info_list:
                result['part_info_list'].append(k1.to_map() if k1 else None)

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create_at') is not None:
            self.create_at = m.get('create_at')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k1 in m.get('part_info_list'):
                temp_model = main_models.UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k1))

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        return self

