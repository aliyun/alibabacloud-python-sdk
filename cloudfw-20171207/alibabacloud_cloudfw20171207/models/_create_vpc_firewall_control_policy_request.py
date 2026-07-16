# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
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
        member_uid: str = None,
        new_order: str = None,
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
        # The action that Cloud Firewall performs on the traffic in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **accept**: allows the traffic.
        # - **drop**: denies the traffic.
        # - **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The application type supported by the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **FTP**
        # - **HTTP**
        # - **HTTPS**
        # - **MySQL**
        # - **SMTP**
        # - **SMTPS**
        # - **RDP**
        # - **VNC**
        # - **SSH**
        # - **Redis**
        # - **MQTT**
        # - **MongoDB**
        # - **Memcache**
        # - **SSL**
        # - **ANY**: all application types.
        self.application_name = application_name
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list
        # The description of the virtual private cloud (VPC) firewall access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port of traffic in the virtual private cloud (VPC) firewall access control policy.
        # 
        # > Set this parameter when **DestPortType** is set to `port`.
        self.dest_port = dest_port
        # The name of the destination port address book of traffic in the virtual private cloud (VPC) firewall access control policy.
        # 
        # > Set this parameter when **DestPortType** is set to `group`.
        self.dest_port_group = dest_port_group
        # The type of the destination port of traffic in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **port**: port
        # - **group**: port address book.
        self.dest_port_type = dest_port_type
        # The destination address of traffic in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - If **DestinationType** is set to `net`, the value of **Destination** is a destination CIDR block.
        # 
        # - If **DestinationType** is set to `group`, the value of **Destination** is a destination address book name.
        # 
        # - If **DestinationType** is set to `domain`, the value of **Destination** is a destination domain name.
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # - **group**: destination address book
        # - **domain**: destination domain name.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # * **FQDN**: FQDN-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN-based and DNS-based dynamic resolution.
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The value must be on the hour or on the half hour and must be at least 30 minutes later than the start time.
        # > If RepeatType is set to Permanent, EndTime is empty. If RepeatType is set to None, Daily, Weekly, or Monthly, EndTime must be specified.
        self.end_time = end_time
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English.
        self.lang = lang
        # The UID of a member account of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The priority of the virtual private cloud (VPC) firewall access control policy.
        # 
        # The priority value starts from 1 and increases by increment. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The security protocol type of traffic in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **ANY**: any protocol type. Set this value if the protocol type is uncertain.
        # - **TCP**
        # - **UDP**
        # - **ICMP**.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. The policy is enabled by default after it is created. Valid values:
        # 
        # - **true**: enables the access control policy.
        # - **false**: does not enable the access control policy.
        self.release = release
        # The days of the recurrence for the policy validity period of the access control policy.
        # - If RepeatType is set to `Permanent`, `None`, or `Daily`, RepeatDays is an empty collection.
        #   Example: []
        # - If RepeatType is set to Weekly, RepeatDays cannot be empty.
        #   Example: [0, 6]
        # > If RepeatType is set to Weekly, the values in RepeatDays cannot be repeated.
        # - If RepeatType is set to `Monthly`, RepeatDays cannot be empty.
        #   Example: [1, 31]
        # > If RepeatType is set to Monthly, the values in RepeatDays cannot be repeated.
        self.repeat_days = repeat_days
        # The recurrence end time of the policy validity period for the access control policy. Example: 23:30. The value must be on the hour or on the half hour and must be at least 30 minutes later than the recurrence start time.
        # > If RepeatType is set to Permanent or None, RepeatEndTime is empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatEndTime must be specified. The format is HH:MM (24-hour clock), such as 08:00.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time of the policy validity period for the access control policy. Example: 08:00. The value must be on the hour or on the half hour and must be at least 30 minutes earlier than the recurrence end time.
        # > If RepeatType is set to Permanent or None, RepeatStartTime is empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatStartTime must be specified. The format is HH:MM (24-hour clock), such as 08:00.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the policy validity period for the access control policy. Valid values:
        # - **Permanent** (default): The policy is always valid.
        # - **None**: The policy is valid for a specified single time period.
        # - **Daily**: The policy is valid on a daily basis.
        # - **Weekly**: The policy is valid on a weekly basis.
        # - **Monthly**: The policy is valid on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the virtual private cloud (VPC) firewall access control policy.
        # 
        # - If SourceType is set to `net`, the value of Source is a source CIDR block.
        # - If SourceType is set to `group`, the value of Source is a source address book name.
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the virtual private cloud (VPC) firewall access control policy. Valid values:
        # 
        # - **net**: source CIDR block
        # 
        # - **group**: source address book.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The value must be on the hour or on the half hour and must be at least 30 minutes earlier than the end time.
        # > If RepeatType is set to Permanent, StartTime is empty. If RepeatType is set to None, Daily, Weekly, or Monthly, StartTime must be specified.
        self.start_time = start_time
        # The ID of the virtual private cloud (VPC) firewall access control policy group.
        # - If the VPC firewall protects traffic between two VPCs connected through CEN, the value of this parameter is the CEN instance ID.
        #   
        # - If the VPC firewall protects traffic between two VPCs connected through Express Connect, the value of this parameter is the VPC firewall instance ID.
        # 
        # > You can invoke the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to obtain the ID.
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

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.new_order is not None:
            result['NewOrder'] = self.new_order

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

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')

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

