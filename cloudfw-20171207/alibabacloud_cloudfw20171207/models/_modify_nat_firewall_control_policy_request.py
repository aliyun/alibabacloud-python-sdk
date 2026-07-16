# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyNatFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        application_name_list: List[str] = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        domain_resolve_type: str = None,
        end_time: int = None,
        lang: str = None,
        nat_gateway_id: str = None,
        proto: str = None,
        release: str = None,
        repeat_days: List[int] = None,
        repeat_end_time: str = None,
        repeat_start_time: str = None,
        repeat_type: str = None,
        source: str = None,
        source_type: str = None,
        start_time: int = None,
    ):
        # The action that you want to perform on traffic. Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: monitors the traffic.
        self.acl_action = acl_action
        # The UUID of the access control policy.
        # 
        # To modify an access control policy, you must provide the UUID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The application names.
        self.application_name_list = application_name_list
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        self.description = description
        # The destination port in the access control policy.
        # 
        # > This parameter is required when you set **DestPortType** to `port`.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # 
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # - If **DestinationType** is `net`, specify a destination CIDR block. Example: `1.2.3.4/24`.
        # 
        # - If **DestinationType** is `group`, specify a destination address book. Example: `db_group`.
        # 
        # - If **DestinationType** is `domain`, specify a destination domain name. Example: `*.aliyuncs.com`.
        # 
        # - If **DestinationType** is `location`, specify a destination location. For more information about location codes, see AddIpamPoolCidr. Example: `["BJ11", "ZB"]`.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        # 
        # - **location**: destination location
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # - **out**: outbound traffic
        self.direction = direction
        # The DNS resolution method of the domain name. Valid values:
        # 
        # - **0**: FQDN
        # 
        # - **1**: dynamic DNS
        # 
        # - **2**: FQDN and dynamic DNS
        # 
        # > If the domain name is resolved in FQDN mode, you can select only the TCP protocol. The supported applications are HTTP, HTTPS, SMTP, SMTPS, SSL, IMAPS, and POPS.
        self.domain_resolve_type = domain_resolve_type
        # The end time of the effective period for the access control policy. The time is a Unix timestamp. The time must be on the hour or half-hour and be at least 30 minutes after the start time.
        # 
        # > If `RepeatType` is Permanent, `EndTime` is empty. If `RepeatType` is None, Daily, Weekly, or Monthly, `EndTime` is required.
        self.end_time = end_time
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The protocol type in the access control policy. Valid values:
        # 
        # - **ANY**
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # > **ANY** indicates that the policy applies to all protocol types.
        # 
        # > If the destination is a domain name-based address book that contains a threat intelligence address book or a cloud service address book, you can select TCP. If you select TCP, you can select HTTP, HTTPS, SMTP, SMTPS, or SSL.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.release = release
        # The days of a week or a month on which the policy recurs.
        # 
        # - If you set **RepeatType** to `Permanent`, `None`, or `Daily`, leave this parameter empty. Example: [].
        # 
        # - If you set **RepeatType** to `Weekly`, this parameter is required. Example: [0, 6].
        # 
        # > When RepeatType is set to Weekly, RepeatDays does not allow duplicates.
        # 
        # - When RepeatType is `Monthly`, RepeatDays cannot be empty. For example: [1, 31]
        # 
        # > When RepeatType is set to Monthly, RepeatDays cannot contain duplicate values.
        self.repeat_days = repeat_days
        # The end time of the policy\\"s recurrence period. The time must be in the 24-hour HH:mm format, such as 23:30, be on the hour or half-hour, and be at least half an hour later than the recurrence start time.
        # 
        # > When RepeatType is Permanent or None, RepeatEndTime is empty. When RepeatType is Daily, Weekly, or Monthly, you must set RepeatEndTime to specify the end time for the repetition.
        self.repeat_end_time = repeat_end_time
        # The start time of the repeat cycle. Use the 24-hour HH:mm format, such as 08:00. The time must be on the hour or half-hour and at least 30 minutes before the repeat end time.
        # 
        # > This parameter is not used if `RepeatType` is set to `Permanent` or `None`. This parameter is required if `RepeatType` is set to `Daily`, `Weekly`, or `Monthly`.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy to take effect. Valid values:
        # 
        # - **Permanent** (default): The policy is always in effect.
        # 
        # - **None**: The policy takes effect for a specified period of time.
        # 
        # - **Daily**: The policy takes effect daily.
        # 
        # - **Weekly**: The policy takes effect weekly.
        # 
        # - **Monthly**: The policy takes effect monthly.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # - When **SourceType** is `net`, Source is the source CIDR address, for example, 10.2.XX.XX/24.
        # 
        # - If **SourceType** is `group`, specify a source address book. Example: `db_group`.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: source CIDR block
        # 
        # - **group**: source address book
        self.source_type = source_type
        # The start time of the effective period for the access control policy is specified in the Unix timestamp format. It must be on the hour or half-hour and at least half an hour earlier than the end time.
        # 
        # > When RepeatType is Permanent, StartTime is empty. When RepeatType is None, Daily, Weekly, or Monthly, StartTime is required.
        self.start_time = start_time

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

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

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

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

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

        return self

