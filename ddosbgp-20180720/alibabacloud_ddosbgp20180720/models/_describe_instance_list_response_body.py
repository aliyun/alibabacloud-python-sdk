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
        # The details about the Anti-DDoS Origin instances.
        self.instance_list = instance_list
        # The details about the Anti-DDoS Origin instance.
        self.request_id = request_id
        # The details about the Anti-DDoS Origin instances.
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
        product: str = None,
        remark: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # The event that triggers automatic association. Valid values:
        # 
        # *   **any**: The instance is automatically associated with an object based on traffic scrubbing events or blackhole filtering events.
        # *   **clean**: The instance is automatically associated with an object based on traffic scrubbing events.
        # *   **blackhole**: The instance is automatically associated with an object based on blackhole filtering events.
        self.auto_protect_condition = auto_protect_condition
        # The time when the instance expires. The value is a UNIX timestamp. Unit: milliseconds.
        self.auto_renewal = auto_renewal
        # The type of the instance.
        # 
        # *   **ddos_ddosorigin_public_cn**: Anti-DDoS Origin 2.0 (Pay-as-you-go) on the China site (aliyun.com).
        # *   **ddos_ddosorigin_public_intl**: Anti-DDoS Origin 2.0 (Pay-as-you-go) on the International site (alibabacloud.com).
        self.blackholding_count = blackholding_count
        # The condition that triggers automatic association of the instance with an object.
        self.commodity_type = commodity_type
        # Indicates whether overdue payments exist. Valid values:
        # 
        # *   **0**: Overdue payments do not exist.
        # *   **1**: Overdue payments exist.
        self.coverage_type = coverage_type
        # The events that trigger automatic association.
        self.debt_status = debt_status
        # The time when the instance was purchased. The value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **0**: the Professional mitigation plan
        # *   **1**: the Enterprise mitigation plan
        self.gmt_create = gmt_create
        # The number of protected public IP addresses for which blackhole filtering is triggered.
        # 
        # >  You can call the [DeleteBlackhole](https://help.aliyun.com/document_detail/118692.html) operation to deactivate blackhole filtering for a protected IP address.
        self.instance_id = instance_id
        # The application scope of the instance.
        # 
        # *   **1**: The instance supports public IP addresses in all regions.
        # *   **2**: The instance supports public IP addresses in regions in the Chinese mainland.
        # *   **3**: The instance supports public IP addresses in regions outside the Chinese mainland.
        # *   **4**: The instance supports public IP addresses in a region in or outside the Chinese mainland.
        self.instance_type = instance_type
        # The description of the instance.
        self.ip_type = ip_type
        # The ID of the instance.
        self.product = product
        # The type of the cloud service that is associated with the Anti-DDoS Origin instance By default, this parameter is not returned. If the Anti-DDoS Origin instance is created by using a different cloud service, the code of the cloud service is returned.
        # 
        # Valid values:
        # 
        # *   **gamebox**: The Anti-DDoS Origin instance is created by using Game Security Box.
        # *   **eip**: The Anti-DDoS Origin instance is created by using an elastic IP address (EIP) for which Anti-DDoS (Enhanced Edition) is enabled.
        self.remark = remark
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
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
        # Events which result in auto binding.
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

