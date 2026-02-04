# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDcdnSubTaskRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        report_ids: str = None,
    ):
        # The domain names to be tracked. Separate multiple domain names with commas (,). You can specify up to 500 domain names. If you want to specify more than 500 domain names, [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex).
        # 
        # > If you do not specify a domain name, the tracking task is created for all domain names that belong to your Alibaba Cloud account.
        self.domain_name = domain_name
        # The IDs of the metrics that you want to include in the report. Separate multiple IDs with commas (,). Valid values:
        # 
        # *   **2**: Popular URLs by Request
        # *   **4**: Popular URLs by Traffic
        # *   **6**: Popular Referer by Request
        # *   **8**: Popular Referer by Traffic
        # *   **10**: Popular Back-to-origin URLs by Request
        # *   **12**: Popular Back-to-origin URLs by Traffic
        # *   **14**: Top Client IPs by Request
        # *   **16**: Top Client IPs by Traffic
        # *   **18**: Popular Domain Names by Traffic
        # *   **20**: PV/UV
        # *   **22**: Visit Distribution by Region
        # *   **24**: Distribution of ISPs
        # *   **26**: Peak IPv4/IPv6 Bandwidth
        # *   **27**: Back-to-origin bandwidth
        # 
        # This parameter is required.
        self.report_ids = report_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')

        return self

