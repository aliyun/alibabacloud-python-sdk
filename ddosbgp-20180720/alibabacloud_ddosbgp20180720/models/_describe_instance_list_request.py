# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceListRequest(DaraModel):
    def __init__(
        self,
        instance_id_list: str = None,
        instance_type: str = None,
        instance_type_list: List[str] = None,
        ip: str = None,
        ip_version: str = None,
        orderby: str = None,
        orderdire: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeInstanceListRequestTag] = None,
    ):
        # The IDs of the Anti-DDoS Origin instances to query. Specify the value in the `["<Instance ID 1>","<Instance ID 2>",……]` format.
        self.instance_id_list = instance_id_list
        # The mitigation plan type of the Anti-DDoS Origin instance to query. Valid values:
        # 
        # - **0**: Professional.
        # - **1**: Enterprise.
        self.instance_type = instance_type
        # The mitigation plan types of the Anti-DDoS Origin instances to query.
        self.instance_type_list = instance_type_list
        # The protected IP address of the Anti-DDoS Origin instance to query.
        self.ip = ip
        # The protocol type of the IP assets protected by the Anti-DDoS Origin instance to query. Valid values:
        # 
        # - **IPv4**: IPv4 protocol.
        # - **IPv6**: IPv6 protocol.
        self.ip_version = ip_version
        # The sort field for the Anti-DDoS Origin instance list. The value is fixed as **expireTime**, which indicates sorting by instance expiration time.
        # 
        # You can use the **Orderdire** parameter to specify the sort order.
        self.orderby = orderby
        # The sort order. Valid values:
        # 
        # - **desc** (default): descending order by expiration time.
        # - **asc**: ascending order by expiration time.
        self.orderdire = orderdire
        # The page number of the current page in a paging query. Settings the current page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of instances on each page in a paging query. Settings the number of instances per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of the Anti-DDoS Origin instance to query.
        # 
        # > You can call [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) to query all region IDs supported by Anti-DDoS Origin.
        # >-
        # >Notice: This parameter is required. If it is not specified, the API returns DDosBgp.CheckError.InvalidRegion(400).</notice>
        self.region_id = region_id
        # The remark of the Anti-DDoS Origin instance to query. Fuzzy match is supported.
        self.remark = remark
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the default resource group is used.
        self.resource_group_id = resource_group_id
        # The tags bound to the Anti-DDoS Origin instances to query.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_list is not None:
            result['InstanceTypeList'] = self.instance_type_list

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.orderby is not None:
            result['Orderby'] = self.orderby

        if self.orderdire is not None:
            result['Orderdire'] = self.orderdire

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeList') is not None:
            self.instance_type_list = m.get('InstanceTypeList')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')

        if m.get('Orderdire') is not None:
            self.orderdire = m.get('Orderdire')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstanceListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag bound to the Anti-DDoS Origin instance to query.
        self.key = key
        # The value of the tag bound to the Anti-DDoS Origin instance to query.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

