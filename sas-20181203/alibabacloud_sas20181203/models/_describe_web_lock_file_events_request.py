# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebLockFileEventsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        page_size: int = None,
        process_name: str = None,
        remark: str = None,
        ts_begin: int = None,
        ts_end: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether the event on web tamper proofing is handled. Valid values:
        # 
        # *   **n**: The event on web tamper proofing is handled.
        # *   **y**: The event on web tamper proofing is not handled.
        self.dealed = dealed
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The name of the process.
        self.process_name = process_name
        # The name of the asset.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the names of assets.
        self.remark = remark
        # The beginning of the time range to query. The value is a UNIX timestamp.
        self.ts_begin = ts_begin
        # The end of the time range to query. The value is a UNIX timestamp.
        self.ts_end = ts_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.ts_begin is not None:
            result['TsBegin'] = self.ts_begin

        if self.ts_end is not None:
            result['TsEnd'] = self.ts_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TsBegin') is not None:
            self.ts_begin = m.get('TsBegin')

        if m.get('TsEnd') is not None:
            self.ts_end = m.get('TsEnd')

        return self

