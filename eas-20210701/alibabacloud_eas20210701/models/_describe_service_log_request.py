# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceLogRequest(DaraModel):
    def __init__(
        self,
        container_name: str = None,
        end_time: str = None,
        instance_name: str = None,
        ip: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        previous: bool = None,
        start_time: str = None,
    ):
        # The name of the container that runs the service.
        self.container_name = container_name
        # The end of the time range to query. The time must be in UTC.
        self.end_time = end_time
        # The name of the instance that runs the service. For more information about how to query the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_name = instance_name
        # The IP address of the instance whose logs you want to query. For more information about how to query the IP address of an instance, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.ip = ip
        # The keyword that you use to query the logs of the service.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 500.
        self.page_size = page_size
        # Specifies whether to query the logs that are generated before the instance last restarts. This parameter is available only if the instance restarts.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.previous = previous
        # The beginning of the time range to query. The time must be in Coordinated Universal Time (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.previous is not None:
            result['Previous'] = self.previous

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Previous') is not None:
            self.previous = m.get('Previous')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

