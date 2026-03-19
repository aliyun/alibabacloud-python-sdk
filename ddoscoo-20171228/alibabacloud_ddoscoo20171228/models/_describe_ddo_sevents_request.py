# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSEventsRequest(DaraModel):
    def __init__(
        self,
        eip: str = None,
        end_time: int = None,
        offset: int = None,
        page_size: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.eip = eip
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip is not None:
            result['Eip'] = self.eip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

