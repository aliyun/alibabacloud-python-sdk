# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        instance_list: List[main_models.DescribeInstanceListResponseBodyInstanceList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The details of the Anti-DDoS Origin instances.
        self.instance_list = instance_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of Anti-DDoS Origin instances returned.
        self.total = total

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.DescribeInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstanceListResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        auto_protect_condition: main_models.DescribeInstanceListResponseBodyInstanceListAutoProtectCondition = None,
        auto_renewal: bool = None,
        blackholding_count: str = None,
        commodity_type: str = None,
        coverage_type: int = None,
        debt_status: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        instance_type: str = None,
        ip_type: str = None,
        log_ext: str = None,
        product: str = None,
        remark: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # The automatic binding condition.
        self.auto_protect_condition = auto_protect_condition
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.auto_renewal = auto_renewal
        # The number of IP addresses that are in blackhole filtering status among the assets that are assigned public IP addresses protected by the instance.
        # 
        # > You can invoke [DeleteBlackhole](https://help.aliyun.com/document_detail/118692.html) to deactivate blackhole filtering for a single protected IP address.
        self.blackholding_count = blackholding_count
        # The commodity type of the instance.
        # 
        # - **ddos_ddosorigin_public_cn**: Anti-DDoS Origin 2.0 (Pay-as-you-go) China site.
        # - **ddos_ddosorigin_public_intl**: Anti-DDoS Origin 2.0 (Pay-as-you-go) International site.
        self.commodity_type = commodity_type
        # The asset overwrite type of the instance.
        # 
        # - **1**: Supports assets that are assigned public IP addresses in multiple regions globally.
        # - **2**: Supports assets that are assigned public IP addresses in multiple regions in the Chinese mainland.
        # - **3**: Supports assets that are assigned public IP addresses in multiple regions outside the Chinese mainland.
        # - **4**: Supports assets that are assigned public IP addresses in a single region globally.
        self.coverage_type = coverage_type
        # The overdue payment status. Valid values:
        # 
        # - **0**: No overdue payment.
        # - **1**: Overdue payment.
        self.debt_status = debt_status
        # The expiration time of the instance. The value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The purchase time of the instance. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The instance ID.
        self.instance_id = instance_id
        # The mitigation plan type of the instance. Valid values:
        # 
        # - **0**: Professional.
        # - **1**: Enterprise.
        self.instance_type = instance_type
        # The protocol type of the IP assets protected by the instance. Valid values:
        # 
        # - **IPv4**: IPv4 protocol.
        # - **IPv6**: IPv6 protocol.
        self.ip_type = ip_type
        # The full logs property.
        self.log_ext = log_ext
        # The type of the cloud service associated with the instance. This parameter is not returned by default. It is returned only when the Anti-DDoS Origin instance is created by another cloud service, with the corresponding cloud service code.
        # 
        # Valid values:
        # 
        # - **gamebox**: The Anti-DDoS Origin instance is created by Game Security Box.
        # - **eip**: The Anti-DDoS Origin instance is created by an EIP with Anti-DDoS (Enhanced) enabled.
        self.product = product
        # The remark of the instance.
        self.remark = remark
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the instance. Valid values:
        # 
        # - **1**: Normal.
        # - **2**: Expired.
        # - **3**: Released.
        self.status = status

    def validate(self):
        if self.auto_protect_condition:
            self.auto_protect_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_protect_condition is not None:
            result['AutoProtectCondition'] = self.auto_protect_condition.to_map()

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.blackholding_count is not None:
            result['BlackholdingCount'] = self.blackholding_count

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.coverage_type is not None:
            result['CoverageType'] = self.coverage_type

        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.log_ext is not None:
            result['LogExt'] = self.log_ext

        if self.product is not None:
            result['Product'] = self.product

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProtectCondition') is not None:
            temp_model = main_models.DescribeInstanceListResponseBodyInstanceListAutoProtectCondition()
            self.auto_protect_condition = temp_model.from_map(m.get('AutoProtectCondition'))

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BlackholdingCount') is not None:
            self.blackholding_count = m.get('BlackholdingCount')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('CoverageType') is not None:
            self.coverage_type = m.get('CoverageType')

        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('LogExt') is not None:
            self.log_ext = m.get('LogExt')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeInstanceListResponseBodyInstanceListAutoProtectCondition(DaraModel):
    def __init__(
        self,
        events: List[str] = None,
    ):
        # The events on which automatic binding is based.
        self.events = events

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.events is not None:
            result['Events'] = self.events

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')

        return self

