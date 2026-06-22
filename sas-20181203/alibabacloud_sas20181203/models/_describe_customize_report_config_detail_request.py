# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomizeReportConfigDetailRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        report_id: int = None,
        source_ip: str = None,
    ):
        # The language type. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The report ID.\\
        # The ReportId returned by calling the [DescribeCustomizeReportList](https://help.aliyun.com/document_detail/271655.html) operation.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

