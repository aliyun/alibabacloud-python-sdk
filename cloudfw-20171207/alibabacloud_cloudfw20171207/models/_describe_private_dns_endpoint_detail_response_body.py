# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePrivateDnsEndpointDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_instance_name: str = None,
        ali_uid: int = None,
        endpoint_id: str = None,
        firewall_type: List[str] = None,
        gmt_create: int = None,
        ip_protocol: str = None,
        member_uid: int = None,
        port: int = None,
        primary_dns: str = None,
        primary_vswitch_id: str = None,
        primary_vswitch_ip: str = None,
        primary_zone_id: str = None,
        private_dns_type: str = None,
        region_no: str = None,
        request_id: str = None,
        standby_dns: str = None,
        standby_vswitch_id: str = None,
        standby_vswitch_ip: str = None,
        standby_zone_id: str = None,
        status: str = None,
        task_id: str = None,
        vpc_id: str = None,
    ):
        # The instance ID.
        self.access_instance_id = access_instance_id
        # The name of the access instance.
        self.access_instance_name = access_instance_name
        # The UID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The type of the Cloud Firewall. Valid values:
        # 
        # - **internet**
        # 
        # - **vpc**
        # 
        # - **nat**
        self.firewall_type = firewall_type
        # The time when the endpoint was created. This is a UNIX timestamp in seconds.
        self.gmt_create = gmt_create
        # The IP protocol. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        self.ip_protocol = ip_protocol
        # The UID of the member account.
        self.member_uid = member_uid
        # The port number.
        self.port = port
        # The primary DNS server.
        self.primary_dns = primary_dns
        # The ID of the primary vSwitch.
        self.primary_vswitch_id = primary_vswitch_id
        # The IP address of the primary vSwitch.
        self.primary_vswitch_ip = primary_vswitch_ip
        # The zone of the primary vSwitch.
        self.primary_zone_id = primary_zone_id
        # The type of the private DNS. Valid values:
        # 
        # - **PrivateZone**
        # 
        # - **Custom** (Default)
        self.private_dns_type = private_dns_type
        # The ID of the region where the instance is located.
        self.region_no = region_no
        # The ID of the request.
        self.request_id = request_id
        # The standby DNS server.
        self.standby_dns = standby_dns
        # The ID of the standby vSwitch.
        self.standby_vswitch_id = standby_vswitch_id
        # The IP address of the standby vSwitch.
        self.standby_vswitch_ip = standby_vswitch_ip
        # The zone of the standby vSwitch.
        self.standby_zone_id = standby_zone_id
        # The instance status. Valid values:
        # 
        # - **creating**: Creating.
        # 
        # - **deleting**: Deleting.
        # 
        # - **normal**: Normal.
        # 
        # - **updating**: Updating.
        self.status = status
        # The ID of the task.
        self.task_id = task_id
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.access_instance_name is not None:
            result['AccessInstanceName'] = self.access_instance_name

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.port is not None:
            result['Port'] = self.port

        if self.primary_dns is not None:
            result['PrimaryDns'] = self.primary_dns

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_vswitch_ip is not None:
            result['PrimaryVSwitchIp'] = self.primary_vswitch_ip

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.private_dns_type is not None:
            result['PrivateDnsType'] = self.private_dns_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.standby_dns is not None:
            result['StandbyDns'] = self.standby_dns

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_vswitch_ip is not None:
            result['StandbyVSwitchIp'] = self.standby_vswitch_ip

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('AccessInstanceName') is not None:
            self.access_instance_name = m.get('AccessInstanceName')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrimaryDns') is not None:
            self.primary_dns = m.get('PrimaryDns')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryVSwitchIp') is not None:
            self.primary_vswitch_ip = m.get('PrimaryVSwitchIp')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('PrivateDnsType') is not None:
            self.private_dns_type = m.get('PrivateDnsType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StandbyDns') is not None:
            self.standby_dns = m.get('StandbyDns')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyVSwitchIp') is not None:
            self.standby_vswitch_ip = m.get('StandbyVSwitchIp')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

