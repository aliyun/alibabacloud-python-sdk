# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUninstallAegisMachinesRequest(DaraModel):
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
        # The page number of the first page to display in the query results. Default value: **1**, which indicates that the query results are displayed from page 1.
        self.current_page = current_page
        # The operating system.
        # > You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to obtain supported operating systems from the **Values** of the item whose **Name** is **osType**.
        self.os = os
        # The number of entries per page in a paged query. Default value: **5**, which indicates that 5 entries are displayed per page.
        self.page_size = page_size
        # The region where the server resides.
        # 
        # > You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to obtain supported regions from the **Values** of the item whose **Name** is **regionId**.
        self.region_id_str = region_id_str
        # The region where the server resides.
        # 
        # > You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to obtain supported regions from the **Values** of the item whose **Name** is **regionId**.
        self.region_no = region_no
        # The asset information to query. You can set this parameter to the asset name or public IP address.
        self.remark = remark
        # The IP address of the access source.
        self.source_ip = source_ip
        # The server vendor. Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: non-cloud asset
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**: third-party cloud asset
        # - **8**: lightweight asset.
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

