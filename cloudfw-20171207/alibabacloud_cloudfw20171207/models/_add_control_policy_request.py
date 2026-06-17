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
        # The action to perform on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: monitors the traffic.
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
        # - **Memcache**
        # 
        # - **MongoDB**
        # 
        # - **MQTT**
        # 
        # - **MySQL**
        # 
        # - **RDP**
        # 
        # - **Redis**
        # 
        # - **SMTP**
        # 
        # - **SMTPS**
        # 
        # - **SSH**
        # 
        # - **SSL_No_Cert**
        # 
        # - **SSL**
        # 
        # - **VNC**
        # 
        # - **ANY** (all application types)
        # 
        # > The available application types depend on the protocol type (\\`Proto\\`). If you set \\`Proto\\` to \\`TCP\\`, you can set \\`ApplicationName\\` to any of the listed application types. If you set \\`Proto\\` to \\`UDP\\`, \\`ICMP\\`, or \\`ANY\\`, you can set \\`ApplicationName\\` only to \\`ANY\\`. Specify either \\`ApplicationNameList\\` or \\`ApplicationName\\`.
        self.application_name = application_name
        # The application types that the access control policy supports.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy. Valid values:
        # 
        # - If \\`Proto\\` is \\`ICMP\\`, leave this parameter empty.
        # 
        # > If the protocol type is ICMP, you cannot control access based on the destination port.
        # 
        # - If \\`Proto\\` is \\`TCP\\`, \\`UDP\\`, or \\`ANY\\`, and \\`DestPortType\\` is \\`group\\`, leave this parameter empty.
        # 
        # > If you set \\`DestPortType\\` to \\`group\\` (port address book), you do not need to specify a destination port number. The port address book contains all the destination ports that the policy manages.
        # 
        # - If \\`Proto\\` is \\`TCP\\`, \\`UDP\\`, or \\`ANY\\`, and \\`DestPortType\\` is \\`port\\`, set this parameter to the destination port number.
        self.dest_port = dest_port
        # The name of the destination port address book for the traffic in the access control policy.
        # 
        # > If you set \\`DestPortType\\` to \\`group\\`, you must specify this parameter.
        self.dest_port_group = dest_port_group
        # The type of the destination port for the traffic in the access control policy.
        # 
        # Valid values:
        # 
        # - **port**: port
        # 
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # Valid values:
        # 
        # - If \\`DestinationType\\` is \\`net\\`, set this parameter to the destination CIDR block.
        # 
        #   Example: 1.2.XX.XX/24
        # 
        # - If \\`DestinationType\\` is \\`group\\`, set this parameter to the name of the destination address book.
        # 
        #   Example: db_group
        # 
        # - If \\`DestinationType\\` is \\`domain\\`, set this parameter to the destination domain name.
        # 
        #   Example: \\*.aliyuncs.com
        # 
        # - If \\`DestinationType\\` is \\`location\\`, set this parameter to the destination region.
        # 
        #   Example: ["BJ11", "ZB"]
        # 
        # > For more information about region codes, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        # 
        # - **location**: destination region
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # - **in**: inbound traffic
        # 
        # - **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method for the access control policy. Valid values:
        # 
        # - **FQDN**: based on FQDN
        # 
        # - **DNS**: based on dynamic DNS resolution
        # 
        # - **FQDN_AND_DNS**: based on FQDN and dynamic DNS resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the policy becomes ineffective. This is a UNIX timestamp. The time must be on the hour or half-hour, and at least 30 minutes after the start time.
        # 
        # > If \\`RepeatType\\` is \\`Permanent\\`, leave this parameter empty. This parameter is required if \\`RepeatType\\` is \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`.
        self.end_time = end_time
        # The IP version supported.
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
        # 
        # - **en**: English
        self.lang = lang
        # The priority of the access control policy. The priority starts from 1. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type of the traffic in the access control policy. Valid values:
        # 
        # - **ANY** (any protocol)
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # > If the traffic direction is \\`out\\` and the destination is a domain-based threat intelligence or cloud service address book, you can set the protocol only to \\`TCP\\`. The supported applications are HTTP, HTTPS, SMTP, SMTPS, and SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # The status of the access control policy. By default, the policy is enabled after it is created. Valid values:
        # 
        # - **true**: enables the access control policy
        # 
        # - **false**: disables the access control policy
        self.release = release
        # The days of the week or month when the policy is active.
        # 
        # - If \\`RepeatType\\` is \\`Permanent\\`, \\`None\\`, or \\`Daily\\`, leave this parameter empty.
        #   Example: []
        # 
        # - This parameter is required if \\`RepeatType\\` is \\`Weekly\\`.
        #   Example: [0, 6]
        # 
        # > If you set \\`RepeatType\\` to \\`Weekly\\`, the values in \\`RepeatDays\\` cannot be duplicates.
        # 
        # - This parameter is required if \\`RepeatType\\` is \\`Monthly\\`.
        #   Example: [1, 31]
        # 
        # > If you set \\`RepeatType\\` to \\`Monthly\\`, the values in \\`RepeatDays\\` cannot be duplicates.
        self.repeat_days = repeat_days
        # The end time of the recurrence. Example: 23:30. The time must be on the hour or half-hour, and at least 30 minutes after the start time.
        # 
        # > If \\`RepeatType\\` is \\`Permanent\\` or \\`None\\`, leave this parameter empty. This parameter is required if \\`RepeatType\\` is \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`.
        self.repeat_end_time = repeat_end_time
        # The start time of the recurrence. Example: 08:00. The time must be on the hour or half-hour, and at least 30 minutes before the end time.
        # 
        # > If \\`RepeatType\\` is \\`Permanent\\` or \\`None\\`, leave this parameter empty. This parameter is required if \\`RepeatType\\` is \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy\\"s effective period. Valid values:
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
        # The source address in the access control policy. Valid values:
        # 
        # - If \\`SourceType\\` is \\`net\\`, set this parameter to the source CIDR block.
        # 
        #   Example: 1.1.XX.XX/24
        # 
        # - If \\`SourceType\\` is \\`group\\`, set this parameter to the name of the source address book.
        # 
        #   Example: db_group
        # 
        # - If \\`SourceType\\` is \\`location\\`, set this parameter to the source region.
        # 
        #   Example: ["BJ11", "ZB"]
        # 
        # > For more information about region codes, see [Region codes](https://help.aliyun.com/document_detail/2854161.html).
        # 
        # This parameter is required.
        self.source = source
        # The source IP address of the traffic.
        self.source_ip = source_ip
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: source CIDR block
        # 
        # - **group**: source address book
        # 
        # - **location**: source region
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the policy becomes effective. This is a UNIX timestamp. The time must be on the hour or half-hour, and at least 30 minutes before the end time.
        # 
        # > If \\`RepeatType\\` is \\`Permanent\\`, leave this parameter empty. This parameter is required if \\`RepeatType\\` is \\`None\\`, \\`Daily\\`, \\`Weekly\\`, or \\`Monthly\\`.
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

