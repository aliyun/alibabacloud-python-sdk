# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomBlockInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_list: List[main_models.DescribeCustomBlockInstancesResponseBodyInstanceList] = None,
        page_info: main_models.DescribeCustomBlockInstancesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The server ID.
        self.instance_list = instance_list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.DescribeCustomBlockInstancesResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCustomBlockInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomBlockInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # The total number of servers to which the defense rule is applied.
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

class DescribeCustomBlockInstancesResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        ali_net_online: bool = None,
        block_type: str = None,
        error_code: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        status: int = None,
        success_info: str = None,
        uuid: str = None,
    ):
        # The status of the host network extension. Valid values:
        # 
        # *   **true**: online
        # *   **false**: offline
        self.ali_net_online = ali_net_online
        # The blocking type. Valid values:
        # 
        # *   **group**: security group
        # *   **alinet**: host network extension
        self.block_type = block_type
        # The error code returned.
        self.error_code = error_code
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # Indicates whether the rule is enabled for the server.
        # 
        # *   **2**: enabling failed
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status
        # The information that is returned after brute-force attacks are blocked.
        self.success_info = success_info
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_net_online is not None:
            result['AliNetOnline'] = self.ali_net_online

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.success_info is not None:
            result['SuccessInfo'] = self.success_info

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliNetOnline') is not None:
            self.ali_net_online = m.get('AliNetOnline')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessInfo') is not None:
            self.success_info = m.get('SuccessInfo')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

