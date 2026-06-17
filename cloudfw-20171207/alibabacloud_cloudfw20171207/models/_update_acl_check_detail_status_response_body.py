# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class UpdateAclCheckDetailStatusResponseBody(DaraModel):
    def __init__(
        self,
        check_record: main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecord = None,
        request_id: str = None,
    ):
        # The ACL check record.
        self.check_record = check_record
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.check_record:
            self.check_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_record is not None:
            result['CheckRecord'] = self.check_record.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRecord') is not None:
            temp_model = main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecord()
            self.check_record = temp_model.from_map(m.get('CheckRecord'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateAclCheckDetailStatusResponseBodyCheckRecord(DaraModel):
    def __init__(
        self,
        acls: List[main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAcls] = None,
        check_name: str = None,
        description: str = None,
        last_check_time: str = None,
        level: str = None,
        policy_total_count: int = None,
        record_assessment_detail: str = None,
        task_id: str = None,
    ):
        # A list of ACL check results.
        self.acls = acls
        # The name of the ACL check. Valid values:
        # 
        # - **PolicyHitCountZero**: The policy has no traffic hits.
        # 
        # - **PolicySourceDestinationSame**: The source and destination are the same, rendering the policy invalid.
        # 
        # - **PolicyDuplicate**: The policy is duplicate or redundant.
        # 
        # - **PolicyConflict**: The policy conflicts with business requirements.
        # 
        # - **DefaultPolicyNotDeny**: The default policy is not a Deny All policy, which is recommended for whitelist mechanisms.
        # 
        # - **PolicyPortHighRisk**: The policy allows traffic on high-risk ports.
        # 
        # - **PolicyTooLoose**: The policy is overly permissive or too broad.
        # 
        # - **AddressBookIpSeparated**: The IP address books contain duplicate, overlapping, or scattered entries.
        # 
        # - **AddressBookPortSeparated**: The port address books contain duplicate, overlapping, or scattered entries.
        # 
        # - **AddressBookDomainValid**: The domain name address book contains invalid entries.
        self.check_name = check_name
        # The description of the rule.
        self.description = description
        # The UNIX timestamp, in seconds, of the last check.
        self.last_check_time = last_check_time
        # The risk level.
        self.level = level
        # The total number of policies.
        self.policy_total_count = policy_total_count
        # The assessment details of the check.
        self.record_assessment_detail = record_assessment_detail
        # The ID of the ACL check task.
        self.task_id = task_id

    def validate(self):
        if self.acls:
            for v1 in self.acls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Acls'] = []
        if self.acls is not None:
            for k1 in self.acls:
                result['Acls'].append(k1.to_map() if k1 else None)

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.description is not None:
            result['Description'] = self.description

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.level is not None:
            result['Level'] = self.level

        if self.policy_total_count is not None:
            result['PolicyTotalCount'] = self.policy_total_count

        if self.record_assessment_detail is not None:
            result['RecordAssessmentDetail'] = self.record_assessment_detail

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k1 in m.get('Acls'):
                temp_model = main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAcls()
                self.acls.append(temp_model.from_map(k1))

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PolicyTotalCount') is not None:
            self.policy_total_count = m.get('PolicyTotalCount')

        if m.get('RecordAssessmentDetail') is not None:
            self.record_assessment_detail = m.get('RecordAssessmentDetail')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class UpdateAclCheckDetailStatusResponseBodyCheckRecordAcls(DaraModel):
    def __init__(
        self,
        acl: main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAcl = None,
        acl_assessment_detail: str = None,
        acl_status: str = None,
    ):
        # The ACL check result.
        self.acl = acl
        # The assessment details of the policy.
        self.acl_assessment_detail = acl_assessment_detail
        # The status of the policy check.
        self.acl_status = acl_status

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()

        if self.acl_assessment_detail is not None:
            result['AclAssessmentDetail'] = self.acl_assessment_detail

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAcl()
            self.acl = temp_model.from_map(m.get('Acl'))

        if m.get('AclAssessmentDetail') is not None:
            self.acl_assessment_detail = m.get('AclAssessmentDetail')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        return self

class UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAcl(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        address_list: List[str] = None,
        address_list_count: int = None,
        application_id: str = None,
        application_name: str = None,
        application_name_list: List[str] = None,
        auto_add_tag_ecs: int = None,
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
        direction: str = None,
        dns_result: str = None,
        dns_result_time: int = None,
        domain_resolve_type: int = None,
        end_time: int = None,
        group_name: str = None,
        group_type: str = None,
        group_uuid: str = None,
        hit_last_time: int = None,
        hit_times: int = None,
        ip_version: int = None,
        modify_time: int = None,
        nat_gateway_id: str = None,
        order: int = None,
        proto: str = None,
        reference_count: int = None,
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
        tag_list: List[main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAclTagList] = None,
        tag_relation: str = None,
        vpc_firewall_id: str = None,
    ):
        # The action performed on traffic that matches the policy. Valid values:
        # 
        # - **accept**: Allows the traffic.
        # 
        # - **drop**: Denies the traffic.
        # 
        # - **log**: Monitors the traffic.
        self.acl_action = acl_action
        # The UUID of the policy.
        self.acl_uuid = acl_uuid
        # A list of addresses in the address book.
        self.address_list = address_list
        # The number of addresses in the address book.
        self.address_list_count = address_list_count
        # The application ID for traffic in the policy.
        self.application_id = application_id
        # The application types supported by the access control policy. Valid values:
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
        # > The available application types depend on the `Proto` value. When `Proto` is `TCP`, all the above application types are supported. If both `ApplicationName` and `ApplicationNameList` are specified, `ApplicationNameList` takes precedence.
        self.application_name = application_name
        # A list of application types that are supported by the policy.
        self.application_name_list = application_name_list
        # Indicates if public IP addresses from new ECS instances with matching tags are automatically added to the address book. This applies to both newly purchased instances and existing instances whose tags are updated to match.
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The time when the policy was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The description of the policy.
        self.description = description
        # The destination port for traffic in the policy.
        self.dest_port = dest_port
        # The type of the destination port for traffic in the policy. Valid values:
        # 
        # - **port**: A single port or a port range.
        # 
        # - **group**: A port address book.
        self.dest_port_group = dest_port_group
        # A list of ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports
        # The type of the destination port in the policy. Valid values:
        # 
        # - **port**: A single port or a port range.
        # 
        # - **group**: A port address book.
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. This parameter supports fuzzy search. The value of this parameter varies based on the value of `DestinationType`.
        # 
        # - If `DestinationType` is set to`net`, the value of this parameter is a CIDR block. Example: 10.0.3.0/24.
        # 
        # - If `DestinationType` is set to`domain`, the value of this parameter is a domain name. Example: aliyun.
        # 
        # - If `DestinationType` is set to`group`, the value of this parameter is the name of an address book. Example: db_group.
        # 
        # - If `DestinationType` is set to`location`, the value of this parameter is a location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"].
        # 
        # > If this parameter is not specified, all types of destination addresses are queried.
        self.destination = destination
        # A list of CIDR blocks in the destination address book of the policy.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the policy. Valid values:
        # 
        # - **ip**: An address book containing IP addresses or CIDR blocks.
        # 
        # - **tag**: An address book containing the IP addresses of ECS instances that match specified tags.
        # 
        # - **domain**: An address book containing one or more domain names.
        # 
        # - **threat**: A threat intelligence address book containing malicious IP addresses or domain names.
        # 
        # - **backsrc**: A back-to-source address book containing the back-to-source addresses of Anti-DDoS or WAF instances.
        self.destination_group_type = destination_group_type
        # The type of the destination address in the policy.
        # 
        # Valid values:
        # 
        # - **net**: A destination CIDR block.
        # 
        # - **group**: A destination address book.
        # 
        # - **domain**: A destination domain name.
        self.destination_type = destination_type
        # The traffic direction for the access control policy.
        # 
        # Valid values:
        # 
        # - **in**: Inbound traffic.
        # 
        # - **out**: Outbound traffic.
        self.direction = direction
        # The result of the DNS resolution.
        self.dns_result = dns_result
        # The UNIX timestamp, in seconds, of the DNS resolution.
        self.dns_result_time = dns_result_time
        # The domain name resolution method of the policy. Valid values:
        # 
        # - **FQDN**: FQDN-based resolution.
        # 
        # - **DNS**: Dynamic DNS-based resolution.
        # 
        # - **FQDN_AND_DNS**: A combination of FQDN and dynamic DNS-based resolution.
        self.domain_resolve_type = domain_resolve_type
        # The end time of the query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The name of the address book.
        self.group_name = group_name
        # The type of the address book. Valid values:
        # 
        # - **ip**: An IP address book.
        # 
        # - **domain**: A domain address book.
        # 
        # - **port**: A port address book.
        # 
        # - **tag**: An ECS tag-based address book.
        # 
        # - **allCloud**: A cloud service address book.
        # 
        # - **threat**: A threat intelligence address book.
        self.group_type = group_type
        # The UUID of the address book.
        # 
        # > For more information, see [DescribeAddressBook](~~DescribeAddressBook~~).
        self.group_uuid = group_uuid
        # The UNIX timestamp, in seconds, of the last policy hit.
        self.hit_last_time = hit_last_time
        # The hit count of the policy.
        self.hit_times = hit_times
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # - **4**: IPv4 (default).
        # 
        # - **6**: IPv6.
        self.ip_version = ip_version
        # The time when the policy was last modified. The value is a UNIX timestamp. Unit: seconds.
        self.modify_time = modify_time
        # The ID of the NAT Gateway.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller value indicates a higher priority.
        self.order = order
        # The protocol type of traffic in the access control policy. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # - **ANY**: All protocol types.
        # 
        # > If this parameter is not specified, all protocol types are queried.
        self.proto = proto
        # The number of times the address book is referenced.
        self.reference_count = reference_count
        # Indicates whether the policy is enabled. Valid values:
        # 
        # - **true**: The policy is enabled.
        # 
        # - **false**: The policy is disabled.
        self.release = release
        # An array of the days of a week or month on which the policy recurs.
        # 
        # - If `RepeatType` is set to`Permanent`,`None`, or`Daily`, `RepeatDays` is an empty array.
        #   Example: []
        # 
        # - If `RepeatType` is set to `Weekly`, `RepeatDays` cannot be empty.
        #   Example: [0, 6]
        # 
        # > If `RepeatType` is set to `Weekly`, `RepeatDays` cannot contain duplicate values.
        # 
        # - If `RepeatType` is set to`Monthly`, `RepeatDays` cannot be empty.
        #   Example: [1, 31]
        # 
        # > If `RepeatType` is set to `Monthly`, `RepeatDays` cannot contain duplicate values.
        self.repeat_days = repeat_days
        # The recurrence end time in HH:mm format. The time must be on the hour or half-hour and at least 30 minutes after the start time.
        # 
        # > This parameter is returned only if `RepeatType` is `Daily`, `Weekly`, or `Monthly`.
        self.repeat_end_time = repeat_end_time
        # The recurrence start time in HH:mm format. The time must be on the hour or half-hour and at least 30 minutes before the end time.
        # 
        # > This parameter is returned only if `RepeatType` is `Daily`, `Weekly`, or `Monthly`.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the validity period of the policy. Valid values:
        # 
        # - **Permanent**: Always.
        # 
        # - **None**: A single occurrence.
        # 
        # - **Daily**: Daily.
        # 
        # - **Weekly**: Weekly.
        # 
        # - **Monthly**: Monthly.
        self.repeat_type = repeat_type
        # The source address in the policy.
        # 
        # Valid values:
        # 
        # - If **SourceType** is set to`net`, the value of `Source` is a source CIDR block.
        # 
        #   Example: 10.2.4.0/24
        # 
        # - If **SourceType** is set to`group`, the value of `Source` is the name of a source address book.
        # 
        #   Example: db_group
        self.source = source
        # A list of CIDR blocks in the source address book of the policy.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the policy. Valid values:
        # 
        # - **ip**: An address book containing IP addresses or CIDR blocks.
        # 
        # - **tag**: An address book containing the IP addresses of ECS instances that match specified tags.
        # 
        # - **domain**: An address book containing one or more domain names.
        # 
        # - **threat**: A threat intelligence address book containing malicious IP addresses or domain names.
        # 
        # - **backsrc**: A back-to-source address book containing the back-to-source addresses of Anti-DDoS or WAF instances.
        self.source_group_type = source_group_type
        # The type of the source address in the policy. Valid values:
        # 
        # - **net**: A source CIDR block.
        # 
        # - **group**: A source address book.
        # 
        # - **location**: A source region.
        self.source_type = source_type
        # The number of rule entries that the policy consumes. The number of entries that a single policy consumes is calculated by using the following formula: Number of source CIDR blocks × Number of destination addresses (CIDR blocks, locations, or domain names) × Number of applications × Number of port ranges.
        self.spread_cnt = spread_cnt
        # The start time of the query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # A list of ECS tags.
        self.tag_list = tag_list
        # The logical relationship among multiple ECS tags.
        self.tag_relation = tag_relation
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.address_list is not None:
            result['AddressList'] = self.address_list

        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list

        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs

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

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dns_result is not None:
            result['DnsResult'] = self.dns_result

        if self.dns_result_time is not None:
            result['DnsResultTime'] = self.dns_result_time

        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time

        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.order is not None:
            result['Order'] = self.order

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count

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

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AddressListCount') is not None:
            self.address_list_count = m.get('AddressListCount')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')

        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')

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

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DnsResult') is not None:
            self.dns_result = m.get('DnsResult')

        if m.get('DnsResultTime') is not None:
            self.dns_result_time = m.get('DnsResultTime')

        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')

        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')

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

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAclTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

class UpdateAclCheckDetailStatusResponseBodyCheckRecordAclsAclTagList(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the ECS tag.
        self.tag_key = tag_key
        # The value of the ECS tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

