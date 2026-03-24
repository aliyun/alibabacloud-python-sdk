# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCdnSubTaskRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        report_ids: str = None,
    ):
        # The domain names to be tracked. Separate multiple domain names with commas (,). You can specify up to 500 domain names. If you want to specify more than 500 domain names, [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex).
        # 
        # > If you do not specify a domain name, the custom operations report is created for all domain names that belong to your Alibaba Cloud account.
        self.domain_name = domain_name
        # The IDs of the metrics that you want to include in the report. Separate multiple IDs with commas (,). Valid values:
        # 
        # *   **1**: frequently requested URLs (ranked by the number of requests)
        # *   **3**: frequently requested URLs (ranked by the amount of network traffic)
        # *   **5**: frequently used Referer headers (ranked by the number of requests)
        # *   **7**: frequently used Referer headers (ranked by the amount of network traffic)
        # *   **9**: frequently requested URLs that are redirected to the origin (ranked by the number of requests)
        # *   **11**: frequently requested URLs that are redirected to the origin (ranked by the amount of network traffic)
        # *   **13**: top client IP addresses (ranked by the number of requests)
        # *   **15**: top client IP addresses (ranked by the amount of network traffic)
        # *   **17**: domain names ranked by the amount of network traffic
        # *   **19**: page views and unique visitors
        # *   **21**: regions from which requests are initiated
        # *   **23**: Internet service providers (ISPs)
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

