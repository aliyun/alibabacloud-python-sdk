# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeReportExportRequest(DaraModel):
    def __init__(
        self,
        export_id: int = None,
        lang: str = None,
    ):
        # The ID of the export task.
        # 
        # >  You can call the [ExportCustomizeReport](https://help.aliyun.com/document_detail/2842677.html) operation to query the ID.
        # 
        # This parameter is required.
        self.export_id = export_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

