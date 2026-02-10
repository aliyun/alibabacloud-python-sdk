# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class FindContainerNetworkConnectResponseBody(DaraModel):
    def __init__(
        self,
        connects: List[main_models.FindContainerNetworkConnectResponseBodyConnects] = None,
        page_info: main_models.FindContainerNetworkConnectResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the network connections.
        self.connects = connects
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.connects:
            for v1 in self.connects:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connects'] = []
        if self.connects is not None:
            for k1 in self.connects:
                result['Connects'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connects = []
        if m.get('Connects') is not None:
            for k1 in m.get('Connects'):
                temp_model = main_models.FindContainerNetworkConnectResponseBodyConnects()
                self.connects.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.FindContainerNetworkConnectResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class FindContainerNetworkConnectResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class FindContainerNetworkConnectResponseBodyConnects(DaraModel):
    def __init__(
        self,
        dst_container: main_models.FindContainerNetworkConnectResponseBodyConnectsDstContainer = None,
        dst_ip: str = None,
        dst_port: str = None,
        first_time: int = None,
        id: int = None,
        last_time: int = None,
        src_container: main_models.FindContainerNetworkConnectResponseBodyConnectsSrcContainer = None,
        src_ip: str = None,
        src_port: str = None,
    ):
        # The information about the destination container.
        # 
        # > This parameter is not supported.
        self.dst_container = dst_container
        # The destination IP address.
        self.dst_ip = dst_ip
        # The destination port.
        self.dst_port = dst_port
        # The timestamp when the connection was first established.
        self.first_time = first_time
        # The ID of the network connection.
        self.id = id
        # The timestamp when the connection was last established.
        self.last_time = last_time
        # The information about the source container.
        # 
        # > This parameter is not supported.
        self.src_container = src_container
        # The source IP address.
        self.src_ip = src_ip
        # The source port.
        self.src_port = src_port

    def validate(self):
        if self.dst_container:
            self.dst_container.validate()
        if self.src_container:
            self.src_container.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_container is not None:
            result['DstContainer'] = self.dst_container.to_map()

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.id is not None:
            result['Id'] = self.id

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.src_container is not None:
            result['SrcContainer'] = self.src_container.to_map()

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstContainer') is not None:
            temp_model = main_models.FindContainerNetworkConnectResponseBodyConnectsDstContainer()
            self.dst_container = temp_model.from_map(m.get('DstContainer'))

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('SrcContainer') is not None:
            temp_model = main_models.FindContainerNetworkConnectResponseBodyConnectsSrcContainer()
            self.src_container = temp_model.from_map(m.get('SrcContainer'))

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        return self

class FindContainerNetworkConnectResponseBodyConnectsSrcContainer(DaraModel):
    def __init__(
        self,
        container_id: str = None,
    ):
        # The ID of the source container.
        self.container_id = container_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        return self

class FindContainerNetworkConnectResponseBodyConnectsDstContainer(DaraModel):
    def __init__(
        self,
        container_id: str = None,
    ):
        # The ID of the destination container.
        self.container_id = container_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        return self

