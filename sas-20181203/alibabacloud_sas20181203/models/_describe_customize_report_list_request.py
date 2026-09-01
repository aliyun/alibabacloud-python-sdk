# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomizeReportListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        pinned: bool = None,
        report_status: int = None,
        report_type: int = None,
        report_version: str = None,
        resource_directory_account_id: int = None,
        title: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to pin the report. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.pinned = pinned
        # The state of the report. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.report_status = report_status
        # The type of the report. Valid values:
        # 
        # *   **0**: daily report
        # *   **1**: weekly report
        # *   **2**: monthly report
        # *   **3**: report whose statistics are collected in a custom time range
        self.report_type = report_type
        # The report version. Valid values:
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        self.report_version = report_version
        self.resource_directory_account_id = resource_directory_account_id
        # The name of the report.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.pinned is not None:
            result['Pinned'] = self.pinned

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_version is not None:
            result['ReportVersion'] = self.report_version

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportVersion') is not None:
            self.report_version = m.get('ReportVersion')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

