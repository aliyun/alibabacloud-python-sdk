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
        client_token: str = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        domain_resolve_type: str = None,
        dry_run: bool = None,
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
        # The action that Cloud Firewall performs on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: allows the traffic.
        # - **drop**: blocks the traffic.
        # - **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The Protocol Type supported by the access control policy. Valid values:
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
        # - **ANY**: all Protocol Types.
        # 
        # > The valid values of ApplicationName depend on the value of Proto. If Proto is set to TCP, ApplicationName can be set to any of the preceding Protocol Types. If Proto is set to UDP, ICMP, or ANY, ApplicationName can only be set to ANY. You must specify ApplicationNameList or ApplicationName. You cannot leave both parameters empty.
        self.application_name = application_name
        # The list of application types supported by the access control policy.
        self.application_name_list = application_name_list
        # The client token that is used to ensure idempotence.
        self.client_token = client_token
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port for traffic in the access control policy. Valid values:
        # 
        # - When the Protocol Type is ICMP, leave DestPort empty.
        #    
        # > When the protocol type is ICMP, access control on destination ports is not supported.
        # 
        # - When the Protocol Type is TCP, UDP, or ANY, and DestPortType is set to group, leave DestPort empty.
        # 
        # > When you select group (destination port address book) for the destination port type of the access control policy, you do not need to configure the Settings for specific destination port numbers. All ports that you want to manage by using this access control policy are included in the destination port address book.
        # 
        # - When the Protocol Type is TCP, UDP, or ANY, and DestPortType is set to port, set DestPort to the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        # 
        # 
        # > If DestPortType is set to group, you must specify the name of the destination port address book.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy.
        # 
        # Valid values:
        # 
        # - **port**: port
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # Valid values:
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
        # > For more information about destination regions, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # - **group**: destination address book
        # - **domain**: destination domain name
        # - **location**: destination area
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The traffic direction of the access control policy. Valid values:
        # 
        # - **in**: inbound traffic
        # - **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution mode of the access control policy. Valid values:
        # 
        # * **FQDN**: FQDN-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN- and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run
        # The end time of the Policy Validity Period for the access control policy. It is expressed in the format of a UNIX timestamp accurate to seconds. The time must be on the hour or half hour, and must be at least 30 minutes later than the start time.
        # > If RepeatType is set to Permanent, leave EndTime empty. If RepeatType is set to None, Daily, Weekly, or Monthly, EndTime is required, and you must configure the Settings for the end time.
        self.end_time = end_time
        # The IP address version.
        # 
        # Valid values:
        # 
        # - **4**: IPv4
        # 
        # - **6**: IPv6
        self.ip_version = ip_version
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The priority of the access control policy. The priority value starts from 1 and increases sequentially. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type of traffic in the access control policy. Valid values:
        # 
        # - **ANY**: all protocols
        # - **TCP**
        # - **UDP**
        # - **ICMP**
        # 
        # > If the traffic direction is outbound and the destination address is a threat intelligence address book or a cloud service address book of the domain name type, you can only set Proto to TCP. In this case, you can set the application type to HTTP, HTTPS, SMTP, SMTPS, or SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, the policy is enabled after it is created. Valid values:
        # - **true**: enables the access control policy.
        # 
        # - **false**: does not enable the access control policy.
        self.release = release
        # The set of recurrence days for the Policy Validity Period of the access control policy.
        # - If RepeatType is set to `Permanent`, `None`, or `Daily`, leave RepeatDays empty.
        #   Example: []
        # - If RepeatType is set to Weekly, RepeatDays cannot be empty.
        #   Example: [0, 6]
        # > When the RepeatType Settings is Weekly, the values in RepeatDays cannot be duplicate.
        # - If RepeatType is set to `Monthly`, RepeatDays cannot be empty.
        #   Example: [1, 31]
        # > When the RepeatType Settings is Monthly, the values in RepeatDays cannot be duplicate.
        self.repeat_days = repeat_days
        # The recurrence end time of the Policy Validity Period for the access control policy. Example: 23:30. The time must be on the hour or half hour, and must be at least 30 minutes later than the recurrence start time.
        # > If RepeatType is set to Permanent or None, leave RepeatEndTime empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatEndTime is required, and you must configure the Settings for the recurrence end time.
        # > The time is in the HH:mm format (24-hour clock). Example: 08:00 or 23:30.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time of the Policy Validity Period for the access control policy. Example: 08:00. The time must be on the hour or half hour, and must be at least 30 minutes earlier than the recurrence end time.
        # > If RepeatType is set to Permanent or None, leave RepeatStartTime empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatStartTime is required, and you must configure the Settings for the recurrence start time.
        # > The time is in the HH:mm format (24-hour clock). Example: 08:00 or 23:30.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the Policy Validity Period for the access control policy. Valid values:
        # - **Permanent** (default): always
        # - **None**: specified single time
        # - **Daily**: every day
        # - **Weekly**: every week
        # - **Monthly**: every month
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # - If SourceType is set to net, set Source to the source CIDR block.
        # 
        #   Example: 1.1.XX.XX/24
        # 
        # - If SourceType is set to group, set Source to the name of the source address book.
        # 
        #   Example: db_group
        # 
        # - If SourceType is set to location, set Source to the source region.
        # 
        #   Example: ["BJ11", "ZB"\\]
        # 
        # > For more information about source regions, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.source = source
        # The source IP address of the requester.
        self.source_ip = source_ip
        # The source address type in the access control policy. Valid values:
        # - **net**: source CIDR block
        # - **group**: source address book
        # - **location**: source location
        # 
        # This parameter is required.
        self.source_type = source_type
        # The start time of the Policy Validity Period for the access control policy. It is expressed in the format of a UNIX timestamp accurate to seconds. The time must be on the hour or half hour, and must be at least 30 minutes earlier than the end time.
        # > If RepeatType is set to Permanent, leave StartTime empty. If RepeatType is set to None, Daily, Weekly, or Monthly, StartTime is required, and you must configure the Settings for the start time.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

