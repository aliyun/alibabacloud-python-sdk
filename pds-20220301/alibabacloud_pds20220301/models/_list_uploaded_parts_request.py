# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUploadedPartsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        limit: int = None,
        part_number_marker: int = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # The drive ID. This parameter is required if the file is not uploaded by using the share URL of the file.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.part_number_marker = part_number_marker
        # The share ID. This parameter is required if the file is uploaded by using the share URL of the file.
        self.share_id = share_id
        # The ID of the upload task.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker

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

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('part_number_marker') is not None:
            self.part_number_marker = m.get('part_number_marker')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        return self

