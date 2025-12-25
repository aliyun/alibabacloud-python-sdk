# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCreateRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        record_list_shrink: str = None,
        site_id: int = None,
    ):
        # The list of DNS records to be created.
        # 
        # This parameter is required.
        self.record_list_shrink = record_list_shrink
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_list_shrink is not None:
            result['RecordList'] = self.record_list_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordList') is not None:
            self.record_list_shrink = m.get('RecordList')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

