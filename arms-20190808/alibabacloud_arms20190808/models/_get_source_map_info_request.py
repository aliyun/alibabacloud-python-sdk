# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceMapInfoRequest(DaraModel):
    def __init__(
        self,
        ascending_sequence: bool = None,
        edition: str = None,
        id: str = None,
        keyword: str = None,
        order_field: str = None,
        region_id: str = None,
    ):
        # The order in which the files are sorted. Valid values:
        # 
        # *   true: ascending order
        # *   false: descending order
        self.ascending_sequence = ascending_sequence
        # The version of the SourceMap file.
        self.edition = edition
        # The ID of the SourceMap file.
        # 
        # This parameter is required.
        self.id = id
        # The keyword in the file name. The files are searched by keyword.
        self.keyword = keyword
        # The criterion by which the files are sorted. Valid values:
        # 
        # *   version: The files are sorted by version.
        # *   uploadTime: The files are sorted by upload time.
        self.order_field = order_field
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascending_sequence is not None:
            result['AscendingSequence'] = self.ascending_sequence

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.id is not None:
            result['ID'] = self.id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AscendingSequence') is not None:
            self.ascending_sequence = m.get('AscendingSequence')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

