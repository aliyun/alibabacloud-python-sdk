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
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The application types supported by the access control policy.
        # 
        # This parameter is required.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy. Valid values:
        # 
        # *   If Proto is set to ICMP, DestPort is automatically left empty.
        # 
        # > If Proto is set to ICMP, access control does not take effect on the destination port.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to group, DestPort is empty.
        # 
        # > If DestPortType is set to group, you do not need to specify the destination port number. All ports on which the access control policy takes effect are included in the destination port address book.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to port, the value of DestPort is the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        # 
        # > If DestPortType is set to group, you must specify the name of the destination port address book.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If DestinationType is set to net, the value of this parameter is a CIDR block.
        # 
        #     Example: 1.2.XX.XX/24
        # 
        # *   If DestinationType is set to group, the value of this parameter is an address book.
        # 
        #     Example: db_group
        # 
        # *   If DestinationType is set to domain, the value of this parameter is a domain name.
        # 
        #     Example: \\*.aliyuncs.com
        # 
        # *   If DestinationType is set to location, the value of this parameter is a location.
        # 
        #     Example: ["BJ11", "ZB"]
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid value:
        # 
        # *   **out**: outbound.
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # *   **0**: fully qualified domain name (FQDN)-based resolution
        # *   **1**: Domain Name System (DNS)-based dynamic resolution
        # *   **2**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of StartTime.
        # 
        # >  If RepeatType is set to Permanent, EndTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
        self.end_time = end_time
        # The IP version supported by the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        self.ip_version = ip_version
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type in the access control policy.
        # 
        # Valid values:
        # 
        # *   ANY: all types of protocols.
        # *   TCP
        # *   UDP
        # *   ICMP
        # 
        # >  If the destination address is a threat intelligence address book of the domain name type or a cloud service address book, you can set Proto only to TCP and set ApplicationNameList to HTTP, HTTPS, SMTP, SMTPS, or SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If RepeatType is set to `Permanent`, `None`, or `Daily`, RepeatDays is left empty. Example: [].
        # *   If RepeatType is set to Weekly, RepeatDays must be specified. Example: [0, 6].
        # 
        # >  If RepeatType is set to Weekly, the fields in the value of RepeatDays cannot be repeated.
        # 
        # *   If RepeatType is set to `Monthly`, RepeatDays must be specified. Example: [1, 31].
        # 
        # >  If RepeatType is set to Monthly, the fields in the value of RepeatDays cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of RepeatStartTime.
        # 
        # >  If RepeatType is set to Permanent or None, RepeatEndTime is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of RepeatEndTime.
        # 
        # >  If RepeatType is set to Permanent or None, RepeatStartTime is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block.
        # 
        #     Example: 10.2.4.0/24
        # 
        # *   If **SourceType** is set to `group`, the value of this parameter must be an address book name.
        # 
        #     Example: db_group
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: source CIDR block
        # *   **group**: source address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of EndTime.
        # 
        # >  If RepeatType is set to Permanent, StartTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
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

