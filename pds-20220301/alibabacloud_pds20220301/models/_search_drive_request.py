# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDriveRequest(DaraModel):
    def __init__(
        self,
        drive_name: str = None,
        limit: int = None,
        marker: str = None,
        owner: str = None,
        owner_type: str = None,
    ):
        # The drive name.
        self.drive_name = drive_name
        # The maximum number of asynchronous tasks to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The owner of the drive.
        self.owner = owner
        # The type of the owner. Valid values:
        # 
        # user group
        self.owner_type = owner_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.owner is not None:
            result['owner'] = self.owner

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        return self

