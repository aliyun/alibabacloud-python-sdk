# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridProxyListResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeHybridProxyListResponseBodyPageInfo = None,
        proxy_list: List[main_models.DescribeHybridProxyListResponseBodyProxyList] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The information about the proxy clusters.
        self.proxy_list = proxy_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.proxy_list:
            for v1 in self.proxy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ProxyList'] = []
        if self.proxy_list is not None:
            for k1 in self.proxy_list:
                result['ProxyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeHybridProxyListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.proxy_list = []
        if m.get('ProxyList') is not None:
            for k1 in m.get('ProxyList'):
                temp_model = main_models.DescribeHybridProxyListResponseBodyProxyList()
                self.proxy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridProxyListResponseBodyProxyList(DaraModel):
    def __init__(
        self,
        client_count: int = None,
        current_version: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        proxy_uuid: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The number of servers that are connected to the proxy instance.
        self.client_count = client_count
        # The version of the proxy instance.
        self.current_version = current_version
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The UUID of the proxy node.
        self.proxy_uuid = proxy_uuid
        # The status of the proxy server. Valid values:
        # 
        # *   **online**
        # *   **offline**
        self.status = status
        # The UUID of the server that is connected to the proxy instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_count is not None:
            result['ClientCount'] = self.client_count

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.proxy_uuid is not None:
            result['ProxyUuid'] = self.proxy_uuid

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCount') is not None:
            self.client_count = m.get('ClientCount')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('ProxyUuid') is not None:
            self.proxy_uuid = m.get('ProxyUuid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeHybridProxyListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
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

