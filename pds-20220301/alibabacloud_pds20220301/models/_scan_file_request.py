# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScanFileRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file properties to return.
        # 
        # *   If you want to return all file properties, set this parameter to \\*.
        # *   By default, if you do not specify this parameter, the following properties of a file are returned: - file_id, - drive_id, - parent_file_id, - type, - created_at, - updated_at, - file_extention, - size, - starred, - status, - category, and - permissions.
        # *   You can also specify properties to return. Separate multiple properties with commas (,).
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
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

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        return self

