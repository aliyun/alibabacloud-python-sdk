# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth: int = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: main_models.DescribeAcceleratorResponseBodyBasicBandwidthPackage = None,
        cen_id: str = None,
        create_time: int = None,
        cross_border_mode: str = None,
        cross_border_status: bool = None,
        cross_domain_bandwidth_package: main_models.DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage = None,
        cross_private_state: str = None,
        ddos_config_list: List[main_models.DescribeAcceleratorResponseBodyDdosConfigList] = None,
        ddos_id: str = None,
        description: str = None,
        dns_name: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        ip_set_config: main_models.DescribeAcceleratorResponseBodyIpSetConfig = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        second_dns_name: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeAcceleratorResponseBodyServiceManagedInfos] = None,
        spec: str = None,
        state: str = None,
        tags: List[main_models.DescribeAcceleratorResponseBodyTags] = None,
        upgradable_status: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        self.bandwidth = bandwidth
        # The bandwidth metering method. Valid values:
        # 
        # *   **BandwidthPackage:** billed based on bandwidth plans.
        # *   **CDT**: billed based on data transfer.
        self.bandwidth_billing_type = bandwidth_billing_type
        # The details about the basic bandwidth plan that is associated with the GA instance.
        self.basic_bandwidth_package = basic_bandwidth_package
        # The ID of the Cloud Enterprise Network (CEN) instance with which the GA instance is associated.
        self.cen_id = cen_id
        # The timestamp that indicates when the GA instance is created.
        self.create_time = create_time
        # The type of cross-border acceleration. This parameter is returned for GA instances whose bandwidth metering method is pay-by-data-transfer (CDT).
        # 
        # Only **bpgPro** may be returned, which indicates BGP (Multi-ISP) Pro lines.
        self.cross_border_mode = cross_border_mode
        # Indicates whether cross-border acceleration is enabled.
        # - **true**: yes
        # - **false**: no
        self.cross_border_status = cross_border_status
        # The details about the cross-border acceleration bandwidth plan that is associated with the GA instance.
        # 
        # This array is returned only for GA instances that are created on the international site (alibabacloud.com).
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        # Indicates whether cross-border acceleration is enabled.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.cross_private_state = cross_private_state
        self.ddos_config_list = ddos_config_list
        # The ID of the Anti-DDoS Pro/Premium instance that is associated with the GA instance.
        self.ddos_id = ddos_id
        # The description of the GA instance.
        self.description = description
        # The canonical name (CNAME) that is assigned to the GA instance.
        self.dns_name = dns_name
        # The timestamp that indicates when the GA instance expires.
        self.expired_time = expired_time
        # The billing method of the GA instance.
        self.instance_charge_type = instance_charge_type
        # The configurations of the acceleration area.
        self.ip_set_config = ip_set_config
        # The name of the GA instance.
        self.name = name
        # The region ID of the GA instance.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The CNAME that is used to integrate the GA instance with the Anti-DDoS service.
        self.second_dns_name = second_dns_name
        # The ID of the service that manages the GA instance.
        # 
        # >  This parameter is returned only if the value of **ServiceManaged** is **true**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_managed = service_managed
        # The actions that users can perform on the managed instance.
        # 
        # > 
        # 
        # *   This parameter is returned only if the value of **ServiceManaged** is **true**.
        # 
        # *   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The specification of the GA instance. Valid values:
        # 
        # *   **1**: Small Ⅰ
        # *   **2**: Small Ⅱ
        # *   **3**: Small Ⅲ
        # *   **5**: Medium Ⅰ
        # *   **8**: Medium Ⅱ
        # *   **10**: Medium Ⅲ
        # *   **20**: Large Ⅰ
        # *   **30**: Large Ⅱ
        # *   **40**: Large Ⅲ
        # *   **50**: Large Ⅳ
        # *   **60**: Large Ⅴ
        # *   **70**: Large Ⅵ
        # *   **80**: Large VⅡ
        # *   **90**: Large VⅢ
        # *   **100**: Super Large Ⅰ
        # *   **200**: Super Large Ⅱ
        # 
        # >  The Large Ⅲ specification and higher specifications are available only to users that are added to the whitelist. To use these specifications, contact your Alibaba Cloud account manager.
        # 
        # Different specifications provide different capabilities. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/153127.html).
        self.spec = spec
        # The status of the GA instance. Valid values:
        # 
        # *   **init**: The GA instance is being initialized.
        # *   **active**: The GA instance is available.
        # *   **configuring**: The GA instance is being configured.
        # *   **binding**: The GA instance is being associated.
        # *   **unbinding**: The GA instance is being disassociated.
        # *   **deleting**: The GA instance is being deleted.
        # *   **finacialLocked**: The GA instance is locked due to overdue payments.
        self.state = state
        # The tags of the GA instance.
        self.tags = tags
        # Indicates whether the GA instance can be upgraded. Valid values:
        # 
        # *   **notUpgradable:** The GA instance does not need to be upgraded.
        # *   **upgradable:** The GA instance can be upgraded to the latest version.
        # *   **upgradeFailed:** The GA instance failed to be upgraded.
        self.upgradable_status = upgradable_status

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.ddos_config_list:
            for v1 in self.ddos_config_list:
                 if v1:
                    v1.validate()
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.service_managed_infos:
            for v1 in self.service_managed_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type

        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_border_mode is not None:
            result['CrossBorderMode'] = self.cross_border_mode

        if self.cross_border_status is not None:
            result['CrossBorderStatus'] = self.cross_border_status

        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()

        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state

        result['DdosConfigList'] = []
        if self.ddos_config_list is not None:
            for k1 in self.ddos_config_list:
                result['DdosConfigList'].append(k1.to_map() if k1 else None)

        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dns_name is not None:
            result['DnsName'] = self.dns_name

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.state is not None:
            result['State'] = self.state

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.upgradable_status is not None:
            result['UpgradableStatus'] = self.upgradable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')

        if m.get('BasicBandwidthPackage') is not None:
            temp_model = main_models.DescribeAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m.get('BasicBandwidthPackage'))

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossBorderMode') is not None:
            self.cross_border_mode = m.get('CrossBorderMode')

        if m.get('CrossBorderStatus') is not None:
            self.cross_border_status = m.get('CrossBorderStatus')

        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = main_models.DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m.get('CrossDomainBandwidthPackage'))

        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')

        self.ddos_config_list = []
        if m.get('DdosConfigList') is not None:
            for k1 in m.get('DdosConfigList'):
                temp_model = main_models.DescribeAcceleratorResponseBodyDdosConfigList()
                self.ddos_config_list.append(temp_model.from_map(k1))

        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('IpSetConfig') is not None:
            temp_model = main_models.DescribeAcceleratorResponseBodyIpSetConfig()
            self.ip_set_config = temp_model.from_map(m.get('IpSetConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeAcceleratorResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpgradableStatus') is not None:
            self.upgradable_status = m.get('UpgradableStatus')

        return self

class DescribeAcceleratorResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is added to the GA instance.
        self.key = key
        # The value of tag N that is added to the GA instance.
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

class DescribeAcceleratorResponseBodyServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action performed on the managed instance. Valid values:
        # 
        # *   **Create**
        # *   **Update**
        # *   **Delete**
        # *   **Associate**
        # *   **UserUnmanaged**
        # *   **CreateChild**
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # *   **Listener**: a listener.
        # *   **IpSet**: an acceleration region.
        # *   **EndpointGroup**: an endpoint group.
        # *   **ForwardingRule**: a forwarding rule.
        # *   **Endpoint**: an endpoint.
        # *   **EndpointGroupDestination**: a protocol mapping of an endpoint group associated with a custom routing listener.
        # *   **EndpointPolicy**: a traffic policy of an endpoint associated with a custom routing listener.
        # 
        # >  This parameter is returned only if the value of **Action** is **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed. Valid values:
        # 
        # *   **true**: The specified actions are managed, and you cannot perform the specified actions on the managed instance.
        # *   **false**: The specified actions are not managed, and you can perform the specified actions on the managed instance.
        self.is_managed = is_managed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.child_type is not None:
            result['ChildType'] = self.child_type

        if self.is_managed is not None:
            result['IsManaged'] = self.is_managed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ChildType') is not None:
            self.child_type = m.get('ChildType')

        if m.get('IsManaged') is not None:
            self.is_managed = m.get('IsManaged')

        return self

class DescribeAcceleratorResponseBodyIpSetConfig(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
    ):
        # The access mode of the acceleration area. Valid values:
        # 
        # *   **UserDefine**: custom nearby access mode. You can select acceleration areas and regions based on your business requirements. GA allocates a separate elastic IP address (EIP) to each acceleration region.
        # *   **Anycast**: automatic nearby access mode. You do not need to specify an acceleration area. GA allocates an Anycast EIP to multiple regions across the globe. Users can connect to the nearest access point of the Alibaba Cloud global transmission network by sending requests to the Anycast EIP.
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        return self

class DescribeAcceleratorResponseBodyDdosConfigList(DaraModel):
    def __init__(
        self,
        ddos_id: str = None,
        ddos_region_id: str = None,
    ):
        self.ddos_id = ddos_id
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        return self

class DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        # The bandwidth that is provided by the cross-border acceleration bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The ID of the cross-border acceleration bandwidth plan.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class DescribeAcceleratorResponseBodyBasicBandwidthPackage(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        # The bandwidth value of the basic bandwidth plan. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The type of the bandwidth that is provided by the basic bandwidth plan. Valid values:
        # 
        # *   **Basic**: basic
        # *   **Enhanced**: enhanced
        # *   **Advanced**: premium
        self.bandwidth_type = bandwidth_type
        # The ID of the basic bandwidth plan.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

