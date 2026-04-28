# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsEipAddressesResponseBody(DaraModel):
    def __init__(
        self,
        eip_addresses: main_models.DescribeEnsEipAddressesResponseBodyEipAddresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the EIPs.
        self.eip_addresses = eip_addresses
        # The page number. Valid values: an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Valid values: **10** to **100**.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddresses') is not None:
            temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m.get('EipAddresses'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEnsEipAddressesResponseBodyEipAddresses(DaraModel):
    def __init__(
        self,
        eip_address: List[main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for v1 in self.eip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k1 in self.eip_address:
                result['EipAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k1 in m.get('EipAddress'):
                temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k1))

        return self

class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        allocation_time: str = None,
        bandwidth: int = None,
        bandwidth_package_bandwidth: int = None,
        bandwidth_package_id: str = None,
        charge_type: str = None,
        description: str = None,
        ens_region_id: str = None,
        icmp_reply_enabled: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        ip_status: str = None,
        isp: str = None,
        name: str = None,
        operation_locks: main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocks = None,
        standby: bool = None,
        status: str = None,
        tags: main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTags = None,
    ):
        # EIP的实例ID。
        self.allocation_id = allocation_id
        # EIP的创建时间
        self.allocation_time = allocation_time
        # EIP的带宽峰值，默认值为5。取值范围：**5**~**10000**，单位：Mbps。
        self.bandwidth = bandwidth
        self.bandwidth_package_bandwidth = bandwidth_package_bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        # EIP的计费模式。
        # 
        # - **PrePaid**：包年包月。
        # 
        # - **PostPaid**：按量计费。
        self.charge_type = charge_type
        # EIP的描述信息。
        self.description = description
        # ENS节点ID。
        self.ens_region_id = ens_region_id
        self.icmp_reply_enabled = icmp_reply_enabled
        # 当前绑定的实例的ID。
        self.instance_id = instance_id
        # 要绑定的云产品实例的类型，取值： 
        # 
        # - **EnsInstance**：VPC类型的ENS实例。
        # 
        # - **SlbInstance**：负载均衡实例。
        self.instance_type = instance_type
        # EIP的计费方式。
        # 
        # - **95BandwidthByMonth**：月95峰值带宽。
        # 
        # - **PayByBandwidth**：固定带宽计费。
        self.internet_charge_type = internet_charge_type
        # EIP的IP地址。
        self.ip_address = ip_address
        # 如果该弹性IP是备用EIP时，表示当前EIP的运行状态。
        # - **Stopped**：已停止。
        # - **Running**：运行中。
        # - **Starting**：启动中。
        # - **Stopping**：停止中。
        self.ip_status = ip_status
        # 运营商，取值：
        # 
        # - **cmcc**：中国移动。
        # - **unicom**：中国联通。
        # - **telecom**：中国电信。
        self.isp = isp
        # EIP实例名称。
        self.name = name
        self.operation_locks = operation_locks
        # 该EIP是否是备用。
        self.standby = standby
        # EIP的状态。
        # 
        # - **Associating**：绑定中。
        # 
        # - **Unassociating**：解绑中。   
        # 
        # - **InUse**：已分配。   
        # 
        # - **Available**：可用。
        self.status = status
        # 标签集合。
        self.tags = tags

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.allocation_time is not None:
            result['AllocationTime'] = self.allocation_time

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_bandwidth is not None:
            result['BandwidthPackageBandwidth'] = self.bandwidth_package_bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.icmp_reply_enabled is not None:
            result['IcmpReplyEnabled'] = self.icmp_reply_enabled

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.ip_status is not None:
            result['IpStatus'] = self.ip_status

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.standby is not None:
            result['Standby'] = self.standby

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('AllocationTime') is not None:
            self.allocation_time = m.get('AllocationTime')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageBandwidth') is not None:
            self.bandwidth_package_bandwidth = m.get('BandwidthPackageBandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('IcmpReplyEnabled') is not None:
            self.icmp_reply_enabled = m.get('IcmpReplyEnabled')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IpStatus') is not None:
            self.ip_status = m.get('IpStatus')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('Standby') is not None:
            self.standby = m.get('Standby')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签键。
        self.tag_key = tag_key
        # 标签值。
        self.tag_value = tag_value
        # 标签值。
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

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocks(DaraModel):
    def __init__(
        self,
        lock: List[main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLock] = None,
    ):
        self.lock = lock

    def validate(self):
        if self.lock:
            for v1 in self.lock:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Lock'] = []
        if self.lock is not None:
            for k1 in self.lock:
                result['Lock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock = []
        if m.get('Lock') is not None:
            for k1 in m.get('Lock'):
                temp_model = main_models.DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLock()
                self.lock.append(temp_model.from_map(k1))

        return self

class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddressOperationLocksLock(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

