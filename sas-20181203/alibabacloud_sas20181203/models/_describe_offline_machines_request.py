# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOfflineMachinesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        os: str = None,
        page_size: int = None,
        region_id_str: str = None,
        region_no: str = None,
        remark: str = None,
        source_ip: str = None,
        vendor: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The operating system of the server.
        # 
        # >  The value of this parameter is the value of the Values parameter that is returned by calling the [DescribeCriteria](~~DescribeCriteria~~) operation. If the value of the **Name** parameter in the response is **osType**, the value of the **Values** parameter indicates an operating system.
        self.os = os
        # The number of entries to return on each page. Default value: **5**.
        self.page_size = page_size
        # The region in which the server resides.
        # 
        # >  The value of this parameter is the value of the Values parameter that is returned by calling the [DescribeCriteria](~~DescribeCriteria~~) operation. If the value of the **Name** parameter in the response is **regionId**, the value of the **Values** parameter indicates a region ID.
        self.region_id_str = region_id_str
        # The region in which the server resides.
        # 
        # >  The value of this parameter is the value of the Values parameter that is returned by calling the [DescribeCriteria](~~DescribeCriteria~~) operation. If the value of the **Name** parameter in the response is **regionId**, the value of the **Values** parameter indicates a region ID.
        self.region_no = region_no
        # The information about the server that you want to query. The value can be the name or the public IP address of the server.
        self.remark = remark
        # The source IP address of the request.
        self.source_ip = source_ip
        # The source of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: a third-party cloud server
        # *   **2**: a server in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.os is not None:
            result['Os'] = self.os

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id_str is not None:
            result['RegionIdStr'] = self.region_id_str

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIdStr') is not None:
            self.region_id_str = m.get('RegionIdStr')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

