# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
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
    ):
        # The action that the access control policy performs on the traffic that passes through the firewall. Valid values:
        # - **accept**: allows access.
        # - **drop**: deny access.
        # - **log**: monitors the traffic.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        # 
        # > To modify an access control policy, you must provide the unique ID of the policy. You can call the [DescribeControlPolicy](https://help.aliyun.com/document_detail/138866.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The application type supported by the access control policy. Valid values:
        # 
        # - **ANY**
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
        # 
        # > **ANY** indicates that the policy applies to all types of applications.
        # 
        # > You must specify either ApplicationNameList or ApplicationName. You cannot leave both parameters empty. If you specify both parameters, the value of ApplicationNameList takes precedence.
        self.application_name = application_name
        # The application name list.
        # 
        # > You must specify either ApplicationNameList or ApplicationName. You cannot leave both parameters empty. If you specify both parameters, the value of ApplicationNameList takes precedence.
        self.application_name_list = application_name_list
        # The idempotence token.
        self.client_token = client_token
        # The description of the access control policy.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # - If **DestinationType** is set to net, **Destination** is a destination CIDR block. Example: 1.2.XX.XX/24.
        # - If **DestinationType** is set to group, **Destination** is a destination address book name. Example: db_group.
        # - If **DestinationType** is set to domain, **Destination** is a destination domain name. Example: *.aliyuncs.com.
        # - If **DestinationType** is set to location, **Destination** is a destination area. For specific area positional encoding, see the subsequent sections. Example: ["BJ11", "ZB"\\].
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # - **group**: destination address book
        # - **domain**: destination domain name
        # - **location**: destination region
        self.destination_type = destination_type
        # The traffic direction of the access control policy. Valid values:
        # 
        # - **in**: inbound traffic access control
        # - **out**: outbound traffic access control
        self.direction = direction
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # * **FQDN**: FQDN-based
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run
        # The end time of the Policy Validity Period for the access control policy. The value is a UNIX timestamp in seconds format. The time must be on the hour or half hour and must be at least 30 minutes later than the start time. Settings for the access control policy validity period.
        # > If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter is required.
        self.end_time = end_time
        # The language of the request and response. Valid values:
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The security protocol type in the access control policy. Valid values:
        # 
        # - **ANY**
        # - **TCP**
        # - **UDP**
        # - **ICMP**
        # 
        # > **ANY** indicates that the policy applies to all protocol types.
        # 
        # > If the traffic direction is outbound and the destination address is a threat intelligence address book or cloud service address book of the domain type, you can configure only the TCP or ANY protocol. If you select TCP, the application can be HTTP, HTTPS, SMTP, SMTPS, or SSL. If you select ANY, the application can only be ANY.
        self.proto = proto
        # The enabling status of the access control policy. Valid values:
        # 
        # - true: The policy is enabled.
        # - false: The policy is in shutdown state.
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect. Settings for the Policy Validity Period recurrence days.
        # - If RepeatType is set to `Permanent`, `None`, or `Daily`, RepeatDays is an empty collection.
        #   Example: []
        # - If RepeatType is set to Weekly, RepeatDays cannot be empty.
        #   Example: [0, 6]
        # > If RepeatType is set to Weekly, the values in RepeatDays cannot be repeated.
        # - If RepeatType is set to `Monthly`, RepeatDays cannot be empty.
        #   Example: [1, 31]
        # > If RepeatType is set to Monthly, the values in RepeatDays cannot be repeated.
        self.repeat_days = repeat_days
        # The recurrence end time of the policy validity period. The time is in the HH:mm format and uses a 24-hour clock. Example: 23:00.
        # > If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter is required.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time of the policy validity period. The time is in the HH:mm format and uses a 24-hour clock. Example: 08:00.
        # > If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter is required.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy validity period of the access control policy. Valid values:
        # - **Permanent** (default): always
        # - **None**: one-time
        # - **Daily**: daily
        # - **Weekly**: weekly
        # - **Monthly**: monthly
        self.repeat_type = repeat_type
        # The source address in the access control policy.
        # 
        # - If **SourceType** is set to net, **Source** is a source CIDR block. Example: 1.2.XX.XX/24.
        # - If **SourceType** is set to group, **Source** is a source address book name. Example: db_group.
        # - If **SourceType** is set to location, **Source** is a source area. For specific area positional encoding, see the subsequent sections. Example: ["BJ11", "ZB"\\].
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: source CIDR block
        # - **group**: source address book
        # - **location**: source region
        self.source_type = source_type
        # The start time of the Policy Validity Period for the access control policy. The value is a UNIX timestamp in seconds format. The time must be on the hour or half hour and must be at least 30 minutes earlier than the end time. Settings for the access control policy validity period.
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

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

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

        return self

