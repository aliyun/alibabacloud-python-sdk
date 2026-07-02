# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetListRecordRequest(DaraModel):
    def __init__(
        self,
        analysis_id: str = None,
        current: int = None,
        custom_id: int = None,
        page_size: int = None,
        region: str = None,
    ):
        self.analysis_id = analysis_id
        # The current page number.
        self.current = current
        self.custom_id = custom_id
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id

        if self.current is not None:
            result['current'] = self.current

        if self.custom_id is not None:
            result['customId'] = self.custom_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('customId') is not None:
            self.custom_id = m.get('customId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

