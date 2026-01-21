# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitoringAgentHostsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hosts: main_models.DescribeMonitoringAgentHostsResponseBodyHosts = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        page_total: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the call is successful.
        self.code = code
        # The information about the hosts.
        self.hosts = hosts
        # The error message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned pages.
        self.page_total = page_total
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.hosts:
            self.hosts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hosts is not None:
            result['Hosts'] = self.hosts.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_total is not None:
            result['PageTotal'] = self.page_total

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Hosts') is not None:
            temp_model = main_models.DescribeMonitoringAgentHostsResponseBodyHosts()
            self.hosts = temp_model.from_map(m.get('Hosts'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMonitoringAgentHostsResponseBodyHosts(DaraModel):
    def __init__(
        self,
        host: List[main_models.DescribeMonitoringAgentHostsResponseBodyHostsHost] = None,
    ):
        self.host = host

    def validate(self):
        if self.host:
            for v1 in self.host:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Host'] = []
        if self.host is not None:
            for k1 in self.host:
                result['Host'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host = []
        if m.get('Host') is not None:
            for k1 in m.get('Host'):
                temp_model = main_models.DescribeMonitoringAgentHostsResponseBodyHostsHost()
                self.host.append(temp_model.from_map(k1))

        return self

class DescribeMonitoringAgentHostsResponseBodyHostsHost(DaraModel):
    def __init__(
        self,
        agent_version: str = None,
        ali_uid: int = None,
        eip_address: str = None,
        eip_id: str = None,
        host_name: str = None,
        instance_id: str = None,
        instance_type_family: str = None,
        ip_group: str = None,
        nat_ip: str = None,
        network_type: str = None,
        operating_system: str = None,
        region: str = None,
        serial_number: str = None,
        is_aliyun_host: bool = None,
    ):
        # The version of the CloudMonitor agent.
        self.agent_version = agent_version
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The elastic IP address (EIP) of the host.
        self.eip_address = eip_address
        # The ID of the EIP.
        self.eip_id = eip_id
        # The name of the host.
        self.host_name = host_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the ECS instance.
        self.instance_type_family = instance_type_family
        # The IP address of the host.
        # 
        # > Multiple IP addresses are separated with commas (,).
        self.ip_group = ip_group
        # The IP address of the Network Address Translation (NAT) gateway.
        self.nat_ip = nat_ip
        # The network type.
        self.network_type = network_type
        # The operating system.
        self.operating_system = operating_system
        # The ID of the region.
        self.region = region
        # The serial number of the host. A host that is not provided by Alibaba Cloud has a serial number instead of an instance ID.
        # 
        # > This parameter can be used to accurately search for a monitored host.
        self.serial_number = serial_number
        # Indicates whether the host is provided by Alibaba Cloud. Valid values:
        # 
        # *   true: The host is provided by Alibaba Cloud.
        # *   false: The host is not provided by Alibaba Cloud.
        self.is_aliyun_host = is_aliyun_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.ip_group is not None:
            result['IpGroup'] = self.ip_group

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system

        if self.region is not None:
            result['Region'] = self.region

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.is_aliyun_host is not None:
            result['isAliyunHost'] = self.is_aliyun_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('IpGroup') is not None:
            self.ip_group = m.get('IpGroup')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('isAliyunHost') is not None:
            self.is_aliyun_host = m.get('isAliyunHost')

        return self

