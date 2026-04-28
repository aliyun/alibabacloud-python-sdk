# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRevisionRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        limit: int = None,
        marker: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # Specifies the returned fields.
        # 
        # By default, this parameter is left empty. If you set this parameter to \\*, all fields are returned. If you leave this parameter empty, the creator of the file is not returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # Default value: 50.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.
        # 
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        return self

