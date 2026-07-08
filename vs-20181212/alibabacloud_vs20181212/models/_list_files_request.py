# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFilesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        file_id: str = None,
        file_name: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # This parameter filters data by time range. It must conform to the ISO 8601 standard and use UTC time in the format yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # File ID. Each ID corresponds to a unique active file.
        self.file_id = file_id
        # File name.
        self.file_name = file_name
        # The page number to retrieve. Page numbering starts at 1.Default value: 1.
        self.page_number = page_number
        # The number of rows per page for a paged query. The value must be in the range of 1 to 100. The default is 10.
        self.page_size = page_size
        # Start time of the time range filter. Specify in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

