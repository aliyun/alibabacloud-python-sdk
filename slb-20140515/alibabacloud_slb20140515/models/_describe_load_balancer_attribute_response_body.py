# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        address_type: str = None,
        auto_release_time: int = None,
        backend_servers: main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers = None,
        bandwidth: int = None,
        create_time: str = None,
        create_time_stamp: int = None,
        delete_protection: str = None,
        end_time: str = None,
        end_time_stamp: int = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        listener_ports: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPorts = None,
        listener_ports_and_protocal: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal = None,
        listener_ports_and_protocol: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        master_zone_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        region_id_alias: str = None,
        renewal_cyc_unit: str = None,
        renewal_duration: int = None,
        renewal_status: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        slave_zone_id: str = None,
        tags: main_models.DescribeLoadBalancerAttributeResponseBodyTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The service IP address of the CLB instance.
        self.address = address
        # The version of the IP address. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The address type of the CLB instance.
        self.address_type = address_type
        # The timestamp generated when the CLB instance is released.
        self.auto_release_time = auto_release_time
        # The backend servers of the CLB instance.
        self.backend_servers = backend_servers
        # The maximum bandwidth of the Internet-facing CLB instance that is billed on a pay-by-bandwidth basis.
        self.bandwidth = bandwidth
        # The time when the CLB instance was created. The time is in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The timestamp generated when the CA certificate is uploaded.
        self.create_time_stamp = create_time_stamp
        # Indicates whether deletion protection is enabled for the CLB instance.
        # 
        # Valid values: **on** and **off**.
        self.delete_protection = delete_protection
        # The time when the CLB instance expires.
        self.end_time = end_time
        # The timestamp that indicates the expiration time of the CLB instance.
        self.end_time_stamp = end_time_stamp
        # The metering method of the CLB instance. Valid values:
        # 
        # *   **PayBySpec** (default)
        # *   **PayByCLCU**
        # 
        # > This parameter is available only on the China site and takes effect only when **PayType** is set to **PayOnDemand**.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Internet-facing CLB instance. Valid values:
        # 
        # *   **paybytraffic**
        # *   **paybybandwidth**
        self.internet_charge_type = internet_charge_type
        # The frontend port used by the CLB instance.
        self.listener_ports = listener_ports
        # The ports or protocols of the listeners.
        self.listener_ports_and_protocal = listener_ports_and_protocal
        # The ports or protocols of the listeners.
        self.listener_ports_and_protocol = listener_ports_and_protocol
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The name of the CLB instance.
        self.load_balancer_name = load_balancer_name
        # The specification of the CLB instance.
        # 
        # >  Pay-as-you-go CLB instances are not subject to specifications. By default, **slb.lcu.elastic** is returned.
        self.load_balancer_spec = load_balancer_spec
        # The status of the CLB instance. Valid values:
        # 
        # *   **inactive**: The CLB instance is disabled. CLB instances in the inactive state do not forward traffic.
        # *   **active**: The CLB instance is running as expected. Newly created CLB instances are in the **active** state by default.
        # *   **locked**: The CLB instance is locked. CLB instances may be locked due to overdue payments or other reasons.
        self.load_balancer_status = load_balancer_status
        # The ID of the primary zone to which the CLB instance belongs.
        self.master_zone_id = master_zone_id
        # The reason why the configuration read-only mode is enabled. The value is 1 to 80 characters in length. It starts with a letter and can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  This parameter is valid only when **ModificationProtectionStatus** is set to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason
        # Indicates whether the configuration read-only mode is enabled. Valid values:
        # 
        # *   **NonProtection**: The configuration read-only mode is disabled. After you disable the configuration read-only mode, the value of **ModificationProtectionReason** is cleared.
        # *   **ConsoleProtection**: The configuration read-only mode is enabled.
        # 
        # >  If this parameter is set to **ConsoleProtection**, you cannot modify instance configurations in the CLB console. However, you can modify instance configurations by calling API operations.
        self.modification_protection_status = modification_protection_status
        # The network type of the CLB instance.
        self.network_type = network_type
        # The billing method of the CLB instance. Valid values:
        # 
        # *   Only **PayOnDemand** may be returned, which indicates the pay-as-you-go billing method.
        self.pay_type = pay_type
        # The region ID of the CLB instance.
        self.region_id = region_id
        # The alias of the region to which the CLB instance belongs.
        self.region_id_alias = region_id_alias
        # The auto-renewal cycle. Valid values: **Year** and **Month**. Default value: Month.
        # 
        # >  This parameter is valid only if you create a subscription CLB instance on the Alibaba Cloud China site. In this case, **PayType** must be set to **PrePay** and **RenewalStatus** must be set to **AutoRenewal**.
        self.renewal_cyc_unit = renewal_cyc_unit
        # The auto-renewal duration. This parameter is valid only if **RenewalStatus** is set to **AutoRenewal**.
        # 
        # *   Valid values when **PeriodUnit** is set to **Year**: **1**~**5**.
        # 
        # *   Valid values when **PeriodUnit** is set to **Month**: **1**~ **9**.
        # 
        # > This parameter is valid only when you create a subscription CLB instance on the Alibaba Cloud China site. In this case, the **PayType** parameter must be set to **PrePay**.
        self.renewal_duration = renewal_duration
        # Indicates whether auto-renewal is enabled. Valid values:
        # 
        # *   **AutoRenewal**: Auto-renewal is enabled.
        # 
        # *   **Normal**: Auto-renewal is disabled. You must manually renew the CLB instance.
        # 
        # *   **NotRenewal**: The CLB instance will not be renewed upon expiration. If this value is returned, the system does not send notifications until three days before the expiration date.
        # 
        #     **
        # 
        #     **Note** This parameter is valid only when you create a subscription CLB instance on the Alibaba Cloud China site. In this case, **PayType** must be set to **PrePay**.
        self.renewal_status = renewal_status
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the secondary zone to which the CLB instance belongs.
        self.slave_zone_id = slave_zone_id
        # The tags.
        self.tags = tags
        # The ID of the vSwitch to which the internal-facing CLB instance belongs.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) where the internal-facing CLB instance is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()
        if self.listener_ports:
            self.listener_ports.validate()
        if self.listener_ports_and_protocal:
            self.listener_ports_and_protocal.validate()
        if self.listener_ports_and_protocol:
            self.listener_ports_and_protocol.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.listener_ports is not None:
            result['ListenerPorts'] = self.listener_ports.to_map()

        if self.listener_ports_and_protocal is not None:
            result['ListenerPortsAndProtocal'] = self.listener_ports_and_protocal.to_map()

        if self.listener_ports_and_protocol is not None:
            result['ListenerPortsAndProtocol'] = self.listener_ports_and_protocol.to_map()

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_id_alias is not None:
            result['RegionIdAlias'] = self.region_id_alias

        if self.renewal_cyc_unit is not None:
            result['RenewalCycUnit'] = self.renewal_cyc_unit

        if self.renewal_duration is not None:
            result['RenewalDuration'] = self.renewal_duration

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('BackendServers') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('ListenerPorts') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPorts()
            self.listener_ports = temp_model.from_map(m.get('ListenerPorts'))

        if m.get('ListenerPortsAndProtocal') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal()
            self.listener_ports_and_protocal = temp_model.from_map(m.get('ListenerPortsAndProtocal'))

        if m.get('ListenerPortsAndProtocol') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol()
            self.listener_ports_and_protocol = temp_model.from_map(m.get('ListenerPortsAndProtocol'))

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIdAlias') is not None:
            self.region_id_alias = m.get('RegionIdAlias')

        if m.get('RenewalCycUnit') is not None:
            self.renewal_cyc_unit = m.get('RenewalCycUnit')

        if m.get('RenewalDuration') is not None:
            self.renewal_duration = m.get('RenewalDuration')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeLoadBalancerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLoadBalancerAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key. Valid values of N: **1** to **20**. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 64 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.tag_key = tag_key
        # The tag value. Valid values of N: **1** to **20**. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol(DaraModel):
    def __init__(
        self,
        listener_port_and_protocol: List[main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol] = None,
    ):
        self.listener_port_and_protocol = listener_port_and_protocol

    def validate(self):
        if self.listener_port_and_protocol:
            for v1 in self.listener_port_and_protocol:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListenerPortAndProtocol'] = []
        if self.listener_port_and_protocol is not None:
            for k1 in self.listener_port_and_protocol:
                result['ListenerPortAndProtocol'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocol = []
        if m.get('ListenerPortAndProtocol') is not None:
            for k1 in m.get('ListenerPortAndProtocol'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol()
                self.listener_port_and_protocol.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol(DaraModel):
    def __init__(
        self,
        description: str = None,
        forward_port: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
    ):
        # Indicates whether the listener is enabled.
        self.description = description
        # The destination listening port to which requests are forwarded. The port must be open and use HTTPS.
        self.forward_port = forward_port
        # Indicates whether the listener is enabled.
        self.listener_forward = listener_forward
        # The frontend port that is used by the CLB instance.
        self.listener_port = listener_port
        # The frontend protocol that is used by the CLB instance.
        self.listener_protocol = listener_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal(DaraModel):
    def __init__(
        self,
        listener_port_and_protocal: List[main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal] = None,
    ):
        self.listener_port_and_protocal = listener_port_and_protocal

    def validate(self):
        if self.listener_port_and_protocal:
            for v1 in self.listener_port_and_protocal:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListenerPortAndProtocal'] = []
        if self.listener_port_and_protocal is not None:
            for k1 in self.listener_port_and_protocal:
                result['ListenerPortAndProtocal'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocal = []
        if m.get('ListenerPortAndProtocal') is not None:
            for k1 in m.get('ListenerPortAndProtocal'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal()
                self.listener_port_and_protocal.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal(DaraModel):
    def __init__(
        self,
        listener_port: int = None,
        listener_protocal: str = None,
    ):
        # The frontend port that is used by the CLB instance.
        self.listener_port = listener_port
        # The frontend protocol that is used by the CLB instance.
        self.listener_protocal = listener_protocal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocal is not None:
            result['ListenerProtocal'] = self.listener_protocal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocal') is not None:
            self.listener_protocal = m.get('ListenerProtocal')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPorts(DaraModel):
    def __init__(
        self,
        listener_port: List[int] = None,
    ):
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        return self

class DescribeLoadBalancerAttributeResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for v1 in self.backend_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k1 in self.backend_server:
                result['BackendServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k1 in m.get('BackendServer'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        description: str = None,
        server_id: str = None,
        server_ip: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The description of the backend server.
        # 
        # > This parameter is not returned if Description is not set.
        self.description = description
        # The backend server ID.
        self.server_id = server_id
        # The ID of the elastic network interface (ENI) or elastic container instance.
        self.server_ip = server_ip
        # The type of the backend server.
        self.type = type
        # The weight of the backend server.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

