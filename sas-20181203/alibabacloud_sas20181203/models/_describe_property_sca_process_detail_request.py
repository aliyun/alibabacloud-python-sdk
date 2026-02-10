# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyScaProcessDetailRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        cmdline: str = None,
        current_page: int = None,
        page_size: int = None,
        pid: str = None,
        remark: str = None,
        uuid: str = None,
    ):
        # The type of the application process. Default value: **java**. Valid values:
        # 
        # *   **java**: Java process.
        # *   **php**: PHP process.
        self.biz_type = biz_type
        # The startup parameter.
        # 
        # >  This parameter supports only prefix queries. Fuzzy match is not supported.
        self.cmdline = cmdline
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The number of entries per page. Default value: 10. If you leave this parameter empty, 10 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The process ID.
        # 
        # >  Only exact match is supported.
        self.pid = pid
        # The information about the server that you want to query. The value can be the public IP address, private IP address, or name of the server. Fuzzy match is supported.
        self.remark = remark
        # The UUID of the server.
        # 
        # > 
        # 
        # *   You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        # 
        # *   Only exact match is supported.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

