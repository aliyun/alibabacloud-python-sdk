# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFacegroupsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
        remarks: str = None,
        return_total_count: bool = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker
        # The filter condition that is used to query groups. The value can be up to 128 characters in length. An exact match is used.
        self.remarks = remarks
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.remarks is not None:
            result['remarks'] = self.remarks

        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')

        return self

