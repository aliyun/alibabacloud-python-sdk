# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListUploadedPartsResponseBody(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        next_part_number_marker: str = None,
        parallel_upload: bool = None,
        upload_id: str = None,
        uploaded_parts: List[main_models.UploadPartInfo] = None,
    ):
        # The file ID.
        self.file_id = file_id
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_part_number_marker = next_part_number_marker
        # Indicates whether the parallel upload feature is enabled.
        self.parallel_upload = parallel_upload
        # The ID of the upload task.
        self.upload_id = upload_id
        # The information about the file parts.
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.uploaded_parts:
            for v1 in self.uploaded_parts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.next_part_number_marker is not None:
            result['next_part_number_marker'] = self.next_part_number_marker

        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k1 in self.uploaded_parts:
                result['uploaded_parts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('next_part_number_marker') is not None:
            self.next_part_number_marker = m.get('next_part_number_marker')

        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        self.uploaded_parts = []
        if m.get('uploaded_parts') is not None:
            for k1 in m.get('uploaded_parts'):
                temp_model = main_models.UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k1))

        return self

