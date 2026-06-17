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
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # - **accept**: Allows the traffic.
        # 
        # - **drop**: Denies the traffic.
        # 
        # - **log**: Monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The application type that the access control policy supports. Valid values:
        # 
        # - **FTP**
        # 
        # - **HTTP**
        # 
        # - **HTTPS**
        # 
        # - **MySQL**
        # 
        # - **SMTP**
        # 
        # - **SMTPS**
        # 
        # - **RDP**
        # 
        # - **VNC**
        # 
        # - **SSH**
        # 
        # - **Redis**
        # 
        # - **MQTT**
        # 
        # - **MongoDB**
        # 
        # - **Memcache**
        # 
        # - **SSL**
        # 
        # - **ANY** (all application types)
        self.application_name = application_name
        # The list of application types that the access control policy supports.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy.
        # 
        # > Set this parameter when **DestPortType** is set to `port`.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        # 
        # > Set this parameter when **DestPortType** is set to `group`.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # 
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. Valid values:
        # 
        # - If **DestinationType** is `net`, set this parameter to a destination CIDR block.
        # 
        # - If **DestinationType** is `group`, set this parameter to the name of a destination address book.
        # 
        # - If **DestinationType** is `domain`, set this parameter to a destination domain name.
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # 
        # - **group**: address book
        # 
        # - **domain**: domain name
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The domain name resolution method for the access control policy. Valid values:
        # 
        # - **FQDN**: FQDN-based
        # 
        # - **DNS**: DNS-based dynamic resolution
        # 
        # - **FQDN_AND_DNS**: FQDN-based and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period. This value is a UNIX timestamp. The time must be on the hour or half-hour and must be at least 30 minutes later than the start time.
        # 
        # > If RepeatType is \\`Permanent\\`, leave this parameter empty. If RepeatType is \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, set this parameter.
        self.end_time = end_time
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The UID of the member account.
        self.member_uid = member_uid
        # The priority of the access control policy.
        # 
        # The priority starts from 1. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type in the access control policy. Valid values:
        # 
        # - **ANY** (Set this value if you are unsure of the protocol type.)
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # This parameter is required.
        self.proto = proto
        # The status of the access control policy. The policy is enabled by default after it is created. Valid values:
        # 
        # - **true**: Enables the access control policy.
        # 
        # - **false**: Disables the access control policy.
        self.release = release
        # The days of the week or month on which the policy is recurrently active.
        # 
        # - If RepeatType is `Permanent`, `None`, or `Daily`, leave this parameter empty. Example: \\`[]\\`
        # 
        # - If RepeatType is \\`Weekly\\`, set this parameter. Example: \\`[0, 6]\\`
        # 
        # > If RepeatType is set to \\`Weekly\\`, the values in RepeatDays cannot be duplicates.
        # 
        # - If **RepeatType** is \\`Monthly\\`, set this parameter. Example: \\`[1, 31]\\`
        # 
        # > If RepeatType is set to \\`Monthly\\`, the values in RepeatDays cannot be duplicates.
        self.repeat_days = repeat_days
        # The recurring end time of the policy validity period. For example: \\`23:30\\`. The time must be on the hour or half-hour and must be at least 30 minutes later than the recurring start time.
        # 
        # > If RepeatType is \\`Permanent\\` or \\`None\\`, leave this parameter empty. If RepeatType is \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, set this parameter.
        self.repeat_end_time = repeat_end_time
        # The recurring start time of the policy validity period. For example: \\`08:00\\`. The time must be on the hour or half-hour and must be at least 30 minutes earlier than the recurring end time.
        # 
        # > If RepeatType is \\`Permanent\\` or \\`None\\`, leave this parameter empty. If RepeatType is \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, set this parameter.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy validity period. Valid values:
        # 
        # - **Permanent** (default): always
        # 
        # - **None**: one-time
        # 
        # - **Daily**: daily
        # 
        # - **Weekly**: weekly
        # 
        # - **Monthly**: monthly
        self.repeat_type = repeat_type
        # The source address in the access control policy.
        # 
        # - If SourceType is `net`, set this parameter to a source CIDR block.
        # 
        # - If SourceType is `group`, set this parameter to the name of a source address book.
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # 
        # - **group**: address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time of the policy validity period. This value is a UNIX timestamp. The time must be on the hour or half-hour and must be at least 30 minutes earlier than the end time.
        # 
        # > If RepeatType is \\`Permanent\\`, leave this parameter empty. If RepeatType is \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`, set this parameter.
        self.start_time = start_time
        # The ID of the policy group for the VPC border firewall.
        # 
        # - If the VPC border firewall protects traffic between two VPCs that are connected using a CEN instance, set this parameter to the ID of the CEN instance.
        # 
        # - If the VPC border firewall protects traffic between two VPCs that are connected using an Express Connect circuit, set this parameter to the ID of the VPC border firewall instance.
        # 
        # > Call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to get this ID.
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

