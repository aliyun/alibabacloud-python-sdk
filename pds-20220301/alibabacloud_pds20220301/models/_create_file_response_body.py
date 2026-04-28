# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CreateFileResponseBody(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        exist: bool = None,
        file_id: str = None,
        file_name: str = None,
        parent_file_id: str = None,
        part_info_list: List[main_models.UploadPartInfo] = None,
        rapid_upload: bool = None,
        status: str = None,
        type: str = None,
        upload_id: str = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # Indicates whether the file exists.
        self.exist = exist
        # The file ID.
        self.file_id = file_id
        # The file name.
        self.file_name = file_name
        # The ID of the parent directory.
        self.parent_file_id = parent_file_id
        # The information about the file parts.
        self.part_info_list = part_info_list
        # Indicates whether the file is instantly uploaded.
        self.rapid_upload = rapid_upload
        # The state of the file.
        self.status = status
        # The type of the file.
        self.type = type
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
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.exist is not None:
            result['exist'] = self.exist

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id

        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k1 in self.part_info_list:
                result['part_info_list'].append(k1.to_map() if k1 else None)

        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('exist') is not None:
            self.exist = m.get('exist')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')

        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k1 in m.get('part_info_list'):
                temp_model = main_models.UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k1))

        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        return self

