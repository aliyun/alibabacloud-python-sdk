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
        # The information about the access control policies of the virtual private cloud (VPC) firewall.
        self.policys = policys
        # The request ID.
        self.request_id = request_id
        # The total number of access control policies for the virtual private cloud (VPC) firewall.
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
        # The action (settings) that Cloud Firewall performs on the traffic in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.acl_action = acl_action
        # The unique identity ID of the access control policy of the virtual private cloud (VPC) firewall.
        self.acl_uuid = acl_uuid
        # The ID of the application with traffic settings in the access control policy of the virtual private cloud (VPC) firewall.
        self.application_id = application_id
        # The application type supported by the access control policy of the virtual private cloud (VPC) firewall. Use ApplicationNameList instead. Valid values:
        self.application_name = application_name
        # The list of application names.
        self.application_name_list = application_name_list
        # The time when the policy was created. The value is a UNIX timestamp in seconds.
        self.create_time = create_time
        # The description of the access control policy of the virtual private cloud (VPC) firewall.
        self.description = description
        # The destination port of the traffic in the access control policy of the virtual private cloud (VPC) firewall.
        self.dest_port = dest_port
        # The name of the destination port address book for the traffic in the access control policy of the virtual private cloud (VPC) firewall.
        self.dest_port_group = dest_port_group
        # The details of the destination port address book in the access control policy of the virtual private cloud (VPC) firewall.
        self.dest_port_group_ports = dest_port_group_ports
        # The destination port type for the traffic in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.destination = destination
        # The CIDR block information in the destination address book of the access control policy of the virtual private cloud (VPC) firewall.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the access control policy. Valid values:
        self.destination_group_type = destination_group_type
        # The destination address type in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.destination_type = destination_type
        # The domain name resolution method of the access control policy. Valid values:
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The time must be on the hour or half hour and must be at least 30 minutes later than the start time.
        self.end_time = end_time
        # The most recent time of hits. The value is a UNIX timestamp in seconds format.
        self.hit_last_time = hit_last_time
        # The number of hits for the access control policy of the virtual private cloud (VPC) firewall.
        self.hit_times = hit_times
        # The UID of a member account of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The time when the policy was modified. The value is a UNIX timestamp in seconds.
        self.modify_time = modify_time
        # The priority of the access control policy of the virtual private cloud (VPC) firewall.
        self.order = order
        # The protocol type of the traffic in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.proto = proto
        # The enabled status of the access control policy. The policy is enabled by default after creation. Valid values:
        self.release = release
        # The collection of recurrence days for the policy validity period of the access control policy.
        self.repeat_days = repeat_days
        # The recurrence end time of the policy validity period. The value is in the HH:mm format using a 24-hour clock, such as 23:00.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time of the policy validity period. The value is in the HH:mm format using a 24-hour clock, such as 08:00.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the policy validity period for the access control policy. Valid values:
        self.repeat_type = repeat_type
        # The source address in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.source = source
        # The details of the source address book in the access control policy of the virtual private cloud (VPC) firewall.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the access control policy. The only valid value is **ip**, which indicates an IP address book that contains one or more CIDR blocks.
        self.source_group_type = source_group_type
        # The source address type in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.source_type = source_type
        # The number of access control policy specifications consumed, which is the cumulative number of specifications consumed by each policy.
        self.spread_cnt = spread_cnt
        # The start time of the policy validity period for the access control policy. The value is a UNIX timestamp in seconds. The time must be on the hour or half hour and must be at least 30 minutes earlier than the end time.
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

