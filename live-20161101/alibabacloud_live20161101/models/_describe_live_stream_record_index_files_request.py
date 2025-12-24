# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamRecordIndexFilesRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        order: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        security_token: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # System-defined parameter. Value: **DescribeLiveStreamRecordIndexFiles**.
        # 
        # This parameter is required.
        self.app_name = app_name
        # ## [](#)Usage notes
        # 
        # *   ApsaraVideo Live stores the information about an M3U8 index file for six months. You can query only the information of index files created in the previous six months.
        # *   M3U8 index files are stored in Object Storage Service (OSS) buckets. The retention period is determined by the storage configuration of the OSS buckets.
        # 
        # ## [](#qps-)QPS limit
        # 
        # You can call this operation up to 15 times per second per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/343507.html).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the live stream.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The order in which the entries are sorted based on creation time. Valid values:
        # 
        # *   **asc** (default): ascending order
        # *   **desc**: descending order
        self.order = order
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_num = page_num
        # The number of entries per page. Valid values: **5 to 30**. Default value: **10**.
        self.page_size = page_size
        self.security_token = security_token
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The main streaming domain.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

