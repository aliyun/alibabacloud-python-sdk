# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddControlPolicyRequest(DaraModel):
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
        direction: str = None,
        domain_resolve_type: str = None,
        end_time: int = None,
        ip_version: str = None,
        lang: str = None,
        new_order: str = None,
        proto: str = None,
        release: str = None,
        repeat_days: List[int] = None,
        repeat_end_time: str = None,
        repeat_start_time: str = None,
        repeat_type: str = None,
        source: str = None,
        source_ip: str = None,
        source_type: str = None,
        start_time: int = None,
    ):
        # The action that is set in the access control policy. Settings the method in which traffic passes through Cloud Firewall. Valid values:
        # 
        # - **accept**: allows the access.
        # - **drop**: deny the access.
        # - **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The application type supported by the access control policy. Valid values:
        # - **FTP**
        # - **HTTP**
        # - **HTTPS**
        # - **Memcache**
        # - **MongoDB**
        # - **MQTT**
        # - **MySQL**
        # - **RDP**
        # - **Redis**
        # - **SMTP**
        # - **SMTPS**
        # - **SSH**
        # - **SSL_No_Cert**
        # - **SSL**
        # - **VNC**
        # - **ANY**: all application types
        # 
        # > The valid values of ApplicationName depend on the value of the protocol type (Proto). If Proto is set to TCP, ApplicationName can be set to any of the preceding application types. If Proto is set to UDP, ICMP, or ANY, ApplicationName can be set only to ANY. You must specify either ApplicationNameList or ApplicationName. You cannot leave both of them empty.
        self.application_name = application_name
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy. Valid values:
        # 
        # - If the protocol type is ICMP, the value of DestPort is empty.
        #    
        # > If the protocol type is ICMP, access control on the destination port is not supported.
        # 
        # - If the protocol type is TCP, UDP, or ANY, and the destination port type (DestPortType) is group, the value of DestPort is empty.
        # 
        # > If the destination port type of the access control policy is set to group (port address book), you do not need to specify a destination port number. All ports that the access control policy manages are included in the port address book.
        # 
        # - If the protocol type is TCP, UDP, or ANY, and the destination port type (DestPortType) is port, the value of DestPort is the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        # 
        # 
        # > If DestPortType is set to group, you must specify the destination port address book name.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy.
        # 
        # Valid values:
        # 
        # - **port**: port
        # - **group**: port address book.
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # Valid values:
        # - If DestinationType is set to net, the value of Destination is a destination CIDR block.
        #   
        #   Example: 1.2.XX.XX/24
        # 
        # - If DestinationType is set to group, the value of Destination is a destination address book name.
        # 
        #   Example: db_group
        # 
        # - If DestinationType is set to domain, the value of Destination is a destination domain name.
        # 
        #   Example: *.aliyuncs.com
        # 
        # - If DestinationType is set to location, the value of Destination is a destination region.
        # 
        #   Example: ["BJ11", "ZB"\\]
        # 
        # > If Destination is set to a destination region, for more information, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # - **group**: destination address book
        # - **domain**: destination domain name
        # - **location**: destination region.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The traffic direction of the access control policy. Valid values:
        # 
        # - **in**: inbound traffic
        # - **out**: outbound traffic.
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # * **FQDN**: FQDN-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN-based and DNS-based dynamic resolution.
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # > If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter is required.
        self.end_time = end_time
        # The IP address version supported.
        # 
        # Valid values:
        # 
        # - **4**: IPv4
        # 
        # - **6**: IPv6.
        self.ip_version = ip_version
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English.
        self.lang = lang
        # The priority of the access control policy. The priority value starts from 1. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type in the access control policy. Valid values:
        # 
        # - **ANY**: any protocol
        # - **TCP**
        # - **UDP**
        # - **ICMP**
        # 
        # > If the traffic direction is outbound and the destination address is a threat intelligence address book or cloud service address book of the domain name type, only TCP is supported. The application type can be set to HTTP, HTTPS, SMTP, SMTPS, or SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. The policy is enabled by default after it is created. Valid values:
        # - **true**: enables the access control policy.
        # 
        # - **false**: disables the access control policy.
        self.release = release
        # The days of the recurrence for the policy validity period of the access control policy.
        # - If RepeatType is set to `Permanent`, `None`, or `Daily`, the value of RepeatDays is an empty array.
        #   Example: []
        # - If RepeatType is set to Weekly, the value of RepeatDays must not be empty.
        #   Example: [0, 6]
        # > If RepeatType is set to Weekly, the values in RepeatDays cannot be repeated.
        # - If RepeatType is set to `Monthly`, the value of RepeatDays must not be empty.
        #   Example: [1, 31]
        # > If RepeatType is set to Monthly, the values in RepeatDays cannot be repeated.
        self.repeat_days = repeat_days
        # The recurrence end time of the policy validity period for the access control policy. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the recurrence start time.
        # > If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter is required.
        # > The time is in the HH:mm format (24-hour clock). Example: 08:00 or 23:30.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time of the policy validity period for the access control policy. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the recurrence end time.
        # > If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter is required.
        # > The time is in the HH:mm format (24-hour clock). Example: 08:00 or 23:30.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the policy validity period for the access control policy. Valid values:
        # - **Permanent** (default): The policy is always valid.
        # - **None**: The policy is valid for a specified single time period.
        # - **Daily**: The policy is valid on a daily basis.
        # - **Weekly**: The policy is valid on a weekly basis.
        # - **Monthly**: The policy is valid on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # - If SourceType is set to net, the value of Source is a source CIDR block.
        # 
        #   Example: 1.1.XX.XX/24
        # 
        # - If SourceType is set to group, the value of Source is a source address book name.
        # 
        #   Example: db_group
        # 
        # - If SourceType is set to location, the value of Source is a source region.
        # 
        #   Example: ["BJ11", "ZB"\\]
        # 
        # > If Source is set to a source region, for more information, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.source = source
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the source address in the access control policy. Valid values:
        # - **net**: source CIDR block
        # - **group**: source address book
        # - **location**: source region.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # > If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter is required.
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

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

