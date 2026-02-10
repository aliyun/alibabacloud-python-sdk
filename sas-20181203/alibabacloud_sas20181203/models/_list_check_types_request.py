# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCheckTypesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_id: int = None,
        show_checks: bool = None,
        source: str = None,
        uuid: str = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The ID of the baseline.
        # 
        # >  You can call the [DescribeCheckWarningSummary](https://help.aliyun.com/document_detail/116179.html) operation to query the IDs of baselines.
        self.risk_id = risk_id
        # Whether to query the check item list. The default value is false. Valid values:
        # 
        # - **false**: Not Query
        # - **true**: Query
        self.show_checks = show_checks
        # The data source. Default value: **default**. Valid values:
        # 
        # *   **agentless**: The check items of baselines for agentless detection.
        # *   **default**: The check items of baselines for hosts.
        self.source = source
        # The UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.show_checks is not None:
            result['ShowChecks'] = self.show_checks

        if self.source is not None:
            result['Source'] = self.source

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('ShowChecks') is not None:
            self.show_checks = m.get('ShowChecks')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

