# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProgramsRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        page_no: str = None,
        page_size: str = None,
        program_name: str = None,
        sort_by: str = None,
    ):
        # The name of the channel.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size
        # The name of the program.
        self.program_name = program_name
        # The sorting order. By default, the query results are sorted by creation time in descending order. Valid values:
        # 
        # *   asc: ascending order.
        # *   desc: descending order.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

