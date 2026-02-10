# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridProxyClusterListResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: List[main_models.DescribeHybridProxyClusterListResponseBodyClusterList] = None,
        page_info: main_models.DescribeHybridProxyClusterListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The proxy clusters.
        self.cluster_list = cluster_list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_list:
            for v1 in self.cluster_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterList'] = []
        if self.cluster_list is not None:
            for k1 in self.cluster_list:
                result['ClusterList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_list = []
        if m.get('ClusterList') is not None:
            for k1 in m.get('ClusterList'):
                temp_model = main_models.DescribeHybridProxyClusterListResponseBodyClusterList()
                self.cluster_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeHybridProxyClusterListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridProxyClusterListResponseBodyPageInfo(DaraModel):
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

class DescribeHybridProxyClusterListResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_key_secret: str = None,
        client_count: int = None,
        cluster_name: str = None,
        install_command: str = None,
        ip: str = None,
        last_heart_time: int = None,
        proxy_count: int = None,
        remark: str = None,
        status: str = None,
    ):
        # The ID of the credential that is used for cluster authentication.
        self.auth_key = auth_key
        # The key of the credential that is used for cluster authentication.
        self.auth_key_secret = auth_key_secret
        # The number of servers that are connected to the proxy cluster.
        self.client_count = client_count
        # The name of the proxy cluster.
        self.cluster_name = cluster_name
        # The installation command for the node of the proxy cluster.
        self.install_command = install_command
        # The endpoint of the cluster. An IP address or a domain name is specified.
        self.ip = ip
        # The timestamp when the cluster last sent a heartbeat message. Unit: milliseconds.
        self.last_heart_time = last_heart_time
        # The number of proxy nodes.
        self.proxy_count = proxy_count
        # The description of the proxy cluster.
        self.remark = remark
        # The status of the cluster.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_key_secret is not None:
            result['AuthKeySecret'] = self.auth_key_secret

        if self.client_count is not None:
            result['ClientCount'] = self.client_count

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.install_command is not None:
            result['InstallCommand'] = self.install_command

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.last_heart_time is not None:
            result['LastHeartTime'] = self.last_heart_time

        if self.proxy_count is not None:
            result['ProxyCount'] = self.proxy_count

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthKeySecret') is not None:
            self.auth_key_secret = m.get('AuthKeySecret')

        if m.get('ClientCount') is not None:
            self.client_count = m.get('ClientCount')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('InstallCommand') is not None:
            self.install_command = m.get('InstallCommand')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('LastHeartTime') is not None:
            self.last_heart_time = m.get('LastHeartTime')

        if m.get('ProxyCount') is not None:
            self.proxy_count = m.get('ProxyCount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

