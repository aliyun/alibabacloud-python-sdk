# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policys: List[main_models.DescribeVpcFirewallControlPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The VPC firewall access control policies.
        self.policys = policys
        # The request ID.
        self.request_id = request_id
        # The total number of VPC firewall access control policies.
        self.total_count = total_count

    def validate(self):
        if self.policys:
            for v1 in self.policys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policys'] = []
        if self.policys is not None:
            for k1 in self.policys:
                result['Policys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k1 in m.get('Policys'):
                temp_model = main_models.DescribeVpcFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallControlPolicyResponseBodyPolicys(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        application_id: str = None,
        application_name: str = None,
        application_name_list: List[str] = None,
        create_time: int = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_group_ports: List[str] = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_group_cidrs: List[str] = None,
        destination_group_type: str = None,
        destination_type: str = None,
        domain_resolve_type: str = None,
        end_time: int = None,
        hit_last_time: int = None,
        hit_times: int = None,
        member_uid: str = None,
        modify_time: int = None,
        order: int = None,
        proto: str = None,
        release: str = None,
        repeat_days: List[int] = None,
        repeat_end_time: str = None,
        repeat_start_time: str = None,
        repeat_type: str = None,
        source: str = None,
        source_group_cidrs: List[str] = None,
        source_group_type: str = None,
        source_type: str = None,
        spread_cnt: int = None,
        start_time: int = None,
    ):
        # The action to perform on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: logs the traffic.
        self.acl_action = acl_action
        # The unique identifier of the access control policy.
        self.acl_uuid = acl_uuid
        # The ID of the application.
        self.application_id = application_id
        # The application type. We recommend that you use `ApplicationNameList` instead. Valid values:
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
        # The list of application names.
        self.application_name_list = application_name_list
        # The UNIX timestamp, in seconds, of when the policy was created.
        self.create_time = create_time
        # The policy description.
        self.description = description
        # The destination port.
        self.dest_port = dest_port
        # The name of the destination port address book.
        self.dest_port_group = dest_port_group
        # The ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports
        # The type of the destination port. Valid values:
        # 
        # - **port**: a single port
        # 
        # - **group**: a port address book
        self.dest_port_type = dest_port_type
        # The destination address for the access control policy. The value depends on `DestinationType`.
        # 
        # - If `DestinationType` is `net`, the value is a destination CIDR block.
        # 
        # - If `DestinationType` is `domain`, the value is a destination domain name.
        # 
        # - If `DestinationType` is `group`, the value is the name of a destination address book.
        self.destination = destination
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book. Valid values:
        # 
        # - **ip**: an address book of IP addresses or CIDR blocks.
        # 
        # - **domain**: an address book of domain names.
        self.destination_group_type = destination_group_type
        # The type of the destination address. Valid values:
        # 
        # - **net**: a destination CIDR block
        # 
        # - **group**: a destination address book
        # 
        # - **domain**: a destination domain name
        self.destination_type = destination_type
        # The domain name resolution mode. Valid values:
        # 
        # - **FQDN**: FQDN-based resolution
        # 
        # - **DNS**: DNS-based dynamic resolution
        # 
        # - **FQDN_AND_DNS**: FQDN-based and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The UNIX timestamp, in seconds, for the end of the policy\\"s effective period. The time must be on the hour or half-hour and at least 30 minutes after the start time.
        # 
        # > This parameter is not used if `RepeatType` is `Permanent`. It is required for `None`, `Daily`, `Weekly`, or `Monthly` recurrence.
        self.end_time = end_time
        # The UNIX timestamp, in seconds, of the last policy hit.
        self.hit_last_time = hit_last_time
        # The number of policy hits.
        self.hit_times = hit_times
        # The UID of the member account.
        self.member_uid = member_uid
        # The UNIX timestamp, in seconds, of when the policy was last modified.
        self.modify_time = modify_time
        # The priority of the access control policy, starting from 1. A smaller value indicates a higher priority.
        self.order = order
        # The protocol type. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # - **ANY** (all protocol types)
        self.proto = proto
        # The enabled status of the access control policy. A policy is enabled by default after it is created. Valid values:
        # 
        # - **true**: The policy is enabled.
        # 
        # - **false**: The policy is disabled.
        self.release = release
        # The days of the week or month on which the policy recurs.
        # 
        # - If `RepeatType` is set to `Permanent`, `None`, or `Daily`, this parameter is empty. Example: `[]`
        # 
        # - If `RepeatType` is set to `Weekly`, this parameter is required. Example: `[0, 6]`
        # 
        # > If `RepeatType` is set to `Weekly`, do not specify duplicate values for this parameter.
        # 
        # - If `RepeatType` is set to `Monthly`, this parameter is required. Example: `[1, 31]`
        # 
        # > If `RepeatType` is set to `Monthly`, do not specify duplicate values for this parameter.
        self.repeat_days = repeat_days
        # The recurrence end time. The time is in the `HH:mm` 24-hour format, such as `23:30`.
        # 
        # > This parameter is not used if `RepeatType` is `Permanent` or `None`. It is required for `Daily`, `Weekly`, or `Monthly` recurrence.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time. The time is in the `HH:mm` 24-hour format, such as `08:00`.
        # 
        # > This parameter is not used if `RepeatType` is `Permanent` or `None`. It is required for `Daily`, `Weekly`, or `Monthly` recurrence.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the policy\\"s effective period. Valid values:
        # 
        # - **Permanent** (default): The policy is always active.
        # 
        # - **None**: The policy applies only once.
        # 
        # - **Daily**: The policy recurs daily.
        # 
        # - **Weekly**: The policy recurs weekly.
        # 
        # - **Monthly**: The policy recurs monthly.
        self.repeat_type = repeat_type
        # The source address for the access control policy. The value depends on `SourceType`.
        # 
        # - If `SourceType` is `net`, the value is a source CIDR block.
        # 
        # - If `SourceType` is `group`, the value is the name of a source address book.
        self.source = source
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book. The value is always **ip**, which indicates an address book that contains IP addresses or CIDR blocks.
        self.source_group_type = source_group_type
        # The type of the source address. Valid values:
        # 
        # - **net**: a source CIDR block
        # 
        # - **group**: a source address book
        self.source_type = source_type
        # The number of rule capacity units that the access control policy consumes. This is calculated as: Number of source addresses × Number of destination addresses × Number of applications × Number of port ranges.
        self.spread_cnt = spread_cnt
        # The UNIX timestamp, in seconds, for the start of the policy\\"s effective period. The time must be on the hour or half-hour and at least 30 minutes before the end time.
        # 
        # > This parameter is not used if `RepeatType` is `Permanent`. It is required for `None`, `Daily`, `Weekly`, or `Monthly` recurrence.
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

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_port is not None:
            result['DestPort'] = self.dest_port

        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group

        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports

        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs

        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time

        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.order is not None:
            result['Order'] = self.order

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

        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs

        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.spread_cnt is not None:
            result['SpreadCnt'] = self.spread_cnt

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')

        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')

        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')

        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')

        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')

        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

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

        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')

        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpreadCnt') is not None:
            self.spread_cnt = m.get('SpreadCnt')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

