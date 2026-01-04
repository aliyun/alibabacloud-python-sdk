# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIpsecServerLogsRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        ipsec_server_id: str = None,
        minute_period: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        to: int = None,
    ):
        # The beginning of the time range to query. The value must be a UNIX timestamp. For example, 1671003744 specifies 15:42:24 (UTC+8) on December 14, 2022.
        # 
        # >  If you specify **From**, you must also specify **To** or **MinutePeriod**.
        self.from_ = from_
        # The ID of the IPsec server.
        # 
        # This parameter is required.
        self.ipsec_server_id = ipsec_server_id
        # The interval at which log data is queried. Valid values: **1** to **10**. Unit: minutes.
        # 
        # >  If both **From** and **To** are not specified, you must specify **MinutePeriod**.
        self.minute_period = minute_period
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the IPsec server is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The end of the time range to query. The value must be a unix timestamp. For example, 1671004344 specifies 15:52:24 (UTC+8) on December 14, 2022.
        # 
        # >  If you specify **To**, you must also specify **From** or **MinutePeriod**.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.ipsec_server_id is not None:
            result['IpsecServerId'] = self.ipsec_server_id

        if self.minute_period is not None:
            result['MinutePeriod'] = self.minute_period

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IpsecServerId') is not None:
            self.ipsec_server_id = m.get('IpsecServerId')

        if m.get('MinutePeriod') is not None:
            self.minute_period = m.get('MinutePeriod')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

