# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        application_name: str = None,
        application_name_list: List[str] = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        domain_resolve_type: str = None,
        end_time: int = None,
        lang: str = None,
        proto: str = None,
        release: str = None,
        repeat_days: List[int] = None,
        repeat_end_time: str = None,
        repeat_start_time: str = None,
        repeat_type: str = None,
        source: str = None,
        source_type: str = None,
        start_time: int = None,
        vpc_firewall_id: str = None,
    ):
        # The action that is performed on traffic that hits the access control policy.
        # 
        # Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: monitors the traffic.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        # 
        # To modify an access control policy, you must provide the unique ID of the policy. You can call the [DescribeVpcFirewallControlPolicy](https://help.aliyun.com/document_detail/159758.html) operation to query the ID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The application type supported by the access control policy.
        # 
        # Valid values:
        # 
        # - ANY (all application types)
        # 
        # - FTP
        # 
        # - HTTP
        # 
        # - HTTPS
        # 
        # - MySQL
        # 
        # - SMTP
        # 
        # - SMTPS
        # 
        # - RDP
        # 
        # - VNC
        # 
        # - SSH
        # 
        # - Redis
        # 
        # - MQTT
        # 
        # - MongoDB
        # 
        # - Memcache
        # 
        # - SSL
        self.application_name = application_name
        # The list of application names.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book for the traffic to which the access control policy applies.
        self.dest_port_group = dest_port_group
        # The type of the destination port for the traffic to which the access control policy applies.
        # 
        # - **port**: port
        # 
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # - If **DestinationType** is set to `net`, specify a destination CIDR block.
        # 
        #   Example: 10.2.3.0/24
        # 
        # - If **DestinationType** is set to `group`, specify the name of a destination address book.
        # 
        #   Example: db_group
        # 
        # - If **DestinationType** is set to `domain`, specify a destination domain name.
        # 
        #   Example: \\*.aliyuncs.com
        self.destination = destination
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        self.destination_type = destination_type
        # The domain name resolution method for the access control policy. Valid values:
        # 
        # - **FQDN**: based on Fully Qualified Domain Name (FQDN)
        # 
        # - **DNS**: based on dynamic DNS resolution
        # 
        # - **FQDN_AND_DNS**: based on FQDN and dynamic DNS resolution
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period. The value is a UNIX timestamp. The time is on the hour or on the half hour, and is at least 30 minutes later than the start time.
        # 
        # > If RepeatType is set to \\`Permanent\\`, this parameter is empty. If RepeatType is set to \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, you must specify this parameter.
        self.end_time = end_time
        # The language of the response message.
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # 
        # - **en**: English
        self.lang = lang
        # The protocol type for the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # - ANY (all protocol types)
        # 
        # - TCP
        # 
        # - UDP
        # 
        # - ICMP
        self.proto = proto
        # The status of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # - **true**: enables the access control policy.
        # 
        # - **false**: disables the access control policy.
        self.release = release
        # The days of a week or month on which the policy takes effect.
        # 
        # - If RepeatType is set to \\`Permanent\\`, \\`None\\`, or \\`Daily\\`, this parameter is empty.
        #   Example: []
        # 
        # - If RepeatType is set to \\`Weekly\\`, this parameter cannot be empty.
        #   Example: [0, 6]
        # 
        # > If RepeatType is set to \\`Weekly\\`, the elements in the array cannot be repeated.
        # 
        # - If RepeatType is set to \\`Monthly\\`, this parameter cannot be empty.
        #   Example: [1, 31]
        # 
        # > If RepeatType is set to \\`Monthly\\`, the elements in the array cannot be repeated.
        self.repeat_days = repeat_days
        # The end time of the recurrence. The time is in the HH:mm format. The time is on the hour or on the half hour, and is at least 30 minutes later than the start time. Example: 23:30.
        # 
        # > If RepeatType is set to \\`Permanent\\` or \\`None\\`, this parameter is empty. If RepeatType is set to \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, you must specify this parameter.
        self.repeat_end_time = repeat_end_time
        # The start time of the recurrence. The time is in the HH:mm format. The time is on the hour or on the half hour, and is at least 30 minutes earlier than the end time. Example: 08:00.
        # 
        # > If RepeatType is set to \\`Permanent\\` or \\`None\\`, this parameter is empty. If RepeatType is set to \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, you must specify this parameter.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy to take effect. Valid values:
        # 
        # - **Permanent** (default): The policy is always in effect.
        # 
        # - **None**: The policy takes effect for a specific period of time.
        # 
        # - **Daily**: The policy takes effect daily.
        # 
        # - **Weekly**: The policy takes effect weekly.
        # 
        # - **Monthly**: The policy takes effect monthly.
        self.repeat_type = repeat_type
        # The source address in the access control policy.
        # 
        # Valid values:
        # 
        # - If **SourceType** is set to `net`, specify a source CIDR block.
        # 
        #   Example: 10.2.4.0/24
        # 
        # - If **SourceType** is set to `group`, specify the name of a source address book.
        # 
        #   Example: db_group
        self.source = source
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: source CIDR block
        # 
        # - **group**: source address book
        self.source_type = source_type
        # The start time of the policy validity period. The value is a UNIX timestamp. The time is on the hour or on the half hour, and is at least 30 minutes earlier than the end time.
        # 
        # > If RepeatType is set to \\`Permanent\\`, this parameter is empty. If RepeatType is set to \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, you must specify this parameter.
        self.start_time = start_time
        # The ID of the VPC firewall instance. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # - If the VPC firewall protects a CEN instance, the value of this parameter is the ID of the CEN instance.
        # 
        #   Example: cen-ervw0g12b5jbw\\*\\*\\*\\*
        # 
        # - If the VPC firewall protects an Express Connect circuit, the value of this parameter is the ID of the VPC firewall instance.
        # 
        #   Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_port is not None:
            result['DestPort'] = self.dest_port

        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group

        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.release is not None:
            result['Release'] = self.release

        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days

        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time

        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')

        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')

        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')

        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')

        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

