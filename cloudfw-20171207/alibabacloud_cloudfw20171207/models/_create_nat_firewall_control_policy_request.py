# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNatFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        application_name_list: List[str] = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        domain_resolve_type: int = None,
        end_time: int = None,
        ip_version: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
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
    ):
        # The action that Cloud Firewall performs on traffic in the access control policy. Valid values:
        # 
        # - **accept**: allows the traffic
        # - **drop**: denies the traffic
        # - **log**: monitors the traffic
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The list of application types supported by the access control policy.
        # 
        # This parameter is required.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy. Valid values:
        # 
        # - If the protocol is ICMP, leave this parameter empty.
        #    
        # > Access control based on destination ports is not supported when the protocol is ICMP.
        # 
        # - If the protocol is TCP, UDP, or ANY and the destination Protocol Type (DestPortType) is group, leave this parameter empty.
        # 
        # > If you set DestPortType to group, you do not need to specify a destination port. All ports managed by this policy are included in the destination port address book.
        # 
        # - If the protocol is TCP, UDP, or ANY and the destination Protocol Type (DestPortType) is port, set this parameter to the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        # 
        # > If you set DestPortType to group, you must specify the name of the destination port address book.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: a port
        # - **group**: a port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. Valid values:
        # 
        # - If DestinationType is set to net, set Destination to the destination CIDR block.
        #   
        #   Example: 1.2.XX.XX/24
        # 
        # - If DestinationType is set to group, set Destination to the name of the destination address book.
        # 
        #   Example: db_group
        # 
        # - If DestinationType is set to domain, set Destination to the destination domain name.
        # 
        #   Example: *.aliyuncs.com
        # 
        # - If DestinationType is set to location, set Destination to the destination region.
        # 
        #   Example: ["BJ11", "ZB"\\]
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: a destination CIDR block
        # - **group**: a destination address book
        # - **domain**: a destination domain name
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The traffic direction of the access control policy. Valid values:
        # 
        # - **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name parse method of the access control policy. Valid values:
        # 
        # - **0**: FQDN-based parse
        # - **1**: DNS-based dynamic parse
        # - **2**: FQDN-based and DNS-based dynamic parse
        # 
        # > If the domain name identification mode includes FQDN, you can only configure the TCP protocol. The supported applications are HTTP, HTTPS, SMTP, SMTPS, SSL, IMAPS, and POPS.
        self.domain_resolve_type = domain_resolve_type
        # The end time for the Policy Validity Period of the access control policy. The value is in the format of a UNIX timestamp in seconds. The time must be on the hour or half hour, and must be at least 30 minutes later than the start time.
        # > If RepeatType is set to Permanent, leave EndTime empty. If RepeatType is set to None, Daily, Weekly, or Monthly, EndTime must have a value, and you must specify the Settings for the end time.
        self.end_time = end_time
        # The IP address version. Valid values:
        # 
        # - **4**: IPv4 (default)
        self.ip_version = ip_version
        # The language of the response message. Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang
        # The instance ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy. The priority value starts from 1 and increases sequentially. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type of the traffic in the access control policy. Valid values:
        # 
        # - ANY: all protocols
        # - TCP
        # - UDP
        # - ICMP
        # 
        # > If the destination address is a threat intelligence address book or a cloud service address book of the domain name type, you can only configure the TCP protocol. The supported applications are HTTP, HTTPS, SMTP, SMTPS, and SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, the policy is enabled after it is created. Valid values:
        # 
        # - **true**: enables the access control policy
        # - **false**: does not enable the access control policy
        self.release = release
        # The set of recurrence days for the Policy Validity Period of the access control policy.
        # 
        # - If RepeatType is set to `Permanent`, `None`, or `Daily`, leave RepeatDays empty.
        #   Example: []
        # - If RepeatType is set to Weekly, RepeatDays cannot be empty.
        #   Example: [0, 6]
        # > When the RepeatType Settings are Weekly, the values in RepeatDays cannot be duplicate.
        # - If RepeatType is set to `Monthly`, RepeatDays cannot be empty.
        #   Example: [1, 31]
        # > When the RepeatType Settings are Monthly, the values in RepeatDays cannot be duplicate.
        self.repeat_days = repeat_days
        # The recurrence end time for the Policy Validity Period of the access control policy. Example: 23:30. The time must be on the hour or half hour, and must be at least 30 minutes later than the recurrence start time.
        # > If RepeatType is set to Permanent or None, leave RepeatEndTime empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatEndTime must have a value, and you must specify the Settings for the recurrence end time.
        # > The time format is HH:mm (24-hour clock), such as 08:00 and 23:30.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time for the Policy Validity Period of the access control policy. Example: 08:00. The time must be on the hour or half hour, and must be at least 30 minutes earlier than the recurrence end time.
        # > If RepeatType is set to Permanent or None, leave RepeatStartTime empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatStartTime must have a value, and you must specify the Settings for the recurrence start time.
        # > The time format is HH:mm (24-hour clock), such as 08:00 and 23:30.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the Policy Validity Period for the access control policy. Valid values:
        # 
        # - **Permanent**: always (default)
        # - **None**: a specific single time
        # - **Daily**: every day
        # - **Weekly**: every week
        # - **Monthly**: every month
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # - If **SourceType** is set to `net`, set Source to the source CIDR block.
        # 
        #   Example: 10.2.4.0/24
        # 
        # - If **SourceType** is set to `group`, set Source to the name of the source address book.
        # 
        #   Example: db_group
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: a source CIDR block
        # - **group**: a source address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time for the Policy Validity Period of the access control policy. The value is in the format of a UNIX timestamp in seconds. The time must be on the hour or half hour, and must be at least 30 minutes earlier than the end time.
        # > If RepeatType is set to Permanent, leave StartTime empty. If RepeatType is set to None, Daily, Weekly, or Monthly, StartTime must have a value, and you must specify the Settings for the start time.
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

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

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

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

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

        return self

