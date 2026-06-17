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
        # The action that Cloud Firewall performs on traffic that matches the access control policy.
        # 
        # Valid values:
        # 
        # - **accept**: Allows the traffic.
        # 
        # - **drop**: Drops the traffic.
        # 
        # - **log**: Logs the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The list of applications to which the access control policy applies.
        # 
        # This parameter is required.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port for the traffic. The value of this parameter depends on the `Proto` and `DestPortType` parameters.
        # 
        # - If `Proto` is `ICMP`, leave this parameter empty.
        # 
        # > Access control cannot be configured based on the destination port for ICMP traffic.
        # 
        # - If the destination port type (`DestPortType`) is `group`, leave this parameter empty.
        # 
        # > If `DestPortType` is set to `group`, you do not need to specify a destination port because the required ports are defined in the selected port address book.
        # 
        # - If the protocol is TCP, UDP, or ANY and the destination port type (`DestPortType`) is `port`, specify the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book.
        # 
        # > This parameter is required if `DestPortType` is set to `group`.
        self.dest_port_group = dest_port_group
        # The type of the destination port.
        # 
        # - **port**: Port or port range
        # 
        # - **group**: Port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # The value of this parameter varies based on the value of `DestinationType`:
        # 
        # - If `DestinationType` is `net`, set this parameter to the destination CIDR.
        # 
        #   Example: `1.2.XX.XX/24`
        # 
        # - If `DestinationType` is `group`, set this parameter to the name of the destination address book.
        # 
        #   Example: `db_group`
        # 
        # - If `DestinationType` is `domain`, set this parameter to the destination domain.
        # 
        #   Example: \\*.aliyuncs.com
        # 
        # - If `DestinationType` is `location`, set this parameter to the destination location.
        # 
        #   Example: ["BJ11", "ZB"]
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: Destination CIDR
        # 
        # - **group**: Destination address book
        # 
        # - **domain**: Destination domain
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The traffic direction for the access control policy. Valid values:
        # 
        # - **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method. Valid values:
        # 
        # - **0**: FQDN-based resolution
        # 
        # - **1**: Dynamic DNS-based resolution
        # 
        # - **2**: FQDN-based and dynamic DNS-based resolution
        # 
        # > If the resolution method includes FQDN, you can set the protocol only to TCP. The supported applications are HTTP, HTTPS, SMTP, SMTPS, and SSL.
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy\\"s validity period, specified as a Unix timestamp. The time must be on the hour or half-hour and be at least 30 minutes after the start time.
        # 
        # > This parameter is required if `RepeatType` is `None`, `Daily`, `Weekly`, or `Monthly`. If `RepeatType` is `Permanent`, leave this parameter empty.
        self.end_time = end_time
        # The IP version for the access control policy. Valid values:
        # 
        # - **4** (default): IPv4
        self.ip_version = ip_version
        # The language of the response messages.
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # 
        # - **en**: English
        self.lang = lang
        # The instance ID of the NAT Gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy. Values start from 1. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol for the traffic in the access control policy.
        # 
        # Valid values:
        # 
        # - ANY: all protocols
        # 
        # - TCP
        # 
        # - UDP
        # 
        # - ICMP
        # 
        # > If the destination is a domain, a threat intelligence address book, or a cloud service address book, you can only set this parameter to `TCP`. The supported application types are HTTP, HTTPS, SMTP, SMTPS, and SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether the access control policy is enabled. By default, policies are enabled upon creation. Valid values:
        # 
        # - **true**: Enables the policy.
        # 
        # - **false**: Disables the policy.
        self.release = release
        # The days of the week or month on which the policy recurs.
        # 
        # - If `RepeatType` is set to `Permanent`, `None`, or `Daily`, leave this parameter empty. Example: `[]`
        # 
        # - If `RepeatType` is `Weekly`, this parameter is required. Example: `[0, 6]`
        # 
        # > If `RepeatType` is `Weekly`, the values in `RepeatDays` must be unique.
        # 
        # - If `RepeatType` is `Monthly`, this parameter is required. Example: `[1, 31]`
        # 
        # > If `RepeatType` is `Monthly`, the values in `RepeatDays` must be unique.
        self.repeat_days = repeat_days
        # The end time of the recurrence. The time must be on the hour or half-hour, and must be at least 30 minutes later than the start time.
        # 
        # > This parameter is required if `RepeatType` is set to `Daily`, `Weekly`, or `Monthly`. If `RepeatType` is `Permanent` or `None`, leave this parameter empty.
        # > The time is in the HH:mm format (24-hour). For example, `08:00` or `23:30`.
        self.repeat_end_time = repeat_end_time
        # The start time of the recurrence. The time must be on the hour or half-hour, and must be at least 30 minutes earlier than the end time.
        # 
        # > This parameter is required if `RepeatType` is set to `Daily`, `Weekly`, or `Monthly`. If `RepeatType` is `Permanent` or `None`, leave this parameter empty.
        # > The time is in the HH:mm format (24-hour). For example, `08:00` or `23:30`.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy validity period. Valid values:
        # 
        # - **Permanent** (default): The policy is always active.
        # 
        # - **None**: The policy runs once for a specified duration.
        # 
        # - **Daily**: The policy recurs daily.
        # 
        # - **Weekly**: The policy recurs weekly within a specified time range.
        # 
        # - **Monthly**: The policy recurs monthly within a specified time range.
        self.repeat_type = repeat_type
        # The source address in the access control policy.
        # 
        # The value of this parameter varies based on the value of `SourceType`:
        # 
        # - If **SourceType** is `net`, set this parameter to the source CIDR.
        # 
        #   Example: 10.2.4.0/24
        # 
        # - If **SourceType** is `group`, set this parameter to the name of the source address book.
        # 
        #   Example: db_group
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: Source CIDR
        # 
        # - **group**: Source address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time of the policy\\"s validity period, specified as a Unix timestamp. The time must be on the hour or half-hour and be at least 30 minutes before the end time.
        # 
        # > This parameter is required if `RepeatType` is `None`, `Daily`, `Weekly`, or `Monthly`. If `RepeatType` is `Permanent`, leave this parameter empty.
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

