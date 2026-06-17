# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAclCheckResponseBody(DaraModel):
    def __init__(
        self,
        check_record: main_models.DescribeAclCheckResponseBodyCheckRecord = None,
        request_id: str = None,
    ):
        # The check record.
        self.check_record = check_record
        # The request ID.
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
            temp_model = main_models.DescribeAclCheckResponseBodyCheckRecord()
            self.check_record = temp_model.from_map(m.get('CheckRecord'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAclCheckResponseBodyCheckRecord(DaraModel):
    def __init__(
        self,
        acl_total_count: int = None,
        acls: List[main_models.DescribeAclCheckResponseBodyCheckRecordAcls] = None,
        check_name: str = None,
        description: str = None,
        last_check_time: str = None,
        level: str = None,
        record_assessment_detail: str = None,
        task_id: str = None,
    ):
        # The total number of access control policies at the time of the check.
        self.acl_total_count = acl_total_count
        # The ACL check results.
        self.acls = acls
        # The name of the ACL check.
        self.check_name = check_name
        # The description of the ACL check item.
        self.description = description
        # The time of the last check, provided as a UNIX timestamp in seconds.
        self.last_check_time = last_check_time
        # The risk level.
        self.level = level
        # The assessment details of the ACL check.
        self.record_assessment_detail = record_assessment_detail
        # The task ID.
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
        if self.acl_total_count is not None:
            result['AclTotalCount'] = self.acl_total_count

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

        if self.record_assessment_detail is not None:
            result['RecordAssessmentDetail'] = self.record_assessment_detail

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclTotalCount') is not None:
            self.acl_total_count = m.get('AclTotalCount')

        self.acls = []
        if m.get('Acls') is not None:
            for k1 in m.get('Acls'):
                temp_model = main_models.DescribeAclCheckResponseBodyCheckRecordAcls()
                self.acls.append(temp_model.from_map(k1))

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('RecordAssessmentDetail') is not None:
            self.record_assessment_detail = m.get('RecordAssessmentDetail')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeAclCheckResponseBodyCheckRecordAcls(DaraModel):
    def __init__(
        self,
        acl: main_models.DescribeAclCheckResponseBodyCheckRecordAclsAcl = None,
        acl_assessment_detail: str = None,
        acl_status: str = None,
    ):
        # The ACL check result.
        self.acl = acl
        # The assessment details of the access control policy.
        self.acl_assessment_detail = acl_assessment_detail
        # The status of the ACL check.
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
            temp_model = main_models.DescribeAclCheckResponseBodyCheckRecordAclsAcl()
            self.acl = temp_model.from_map(m.get('Acl'))

        if m.get('AclAssessmentDetail') is not None:
            self.acl_assessment_detail = m.get('AclAssessmentDetail')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        return self

class DescribeAclCheckResponseBodyCheckRecordAclsAcl(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        address_list: List[str] = None,
        address_list_count: int = None,
        addresses: List[main_models.DescribeAclCheckResponseBodyCheckRecordAclsAclAddresses] = None,
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
        tag_list: List[main_models.DescribeAclCheckResponseBodyCheckRecordAclsAclTagList] = None,
        tag_relation: str = None,
        vpc_firewall_id: str = None,
    ):
        # The action performed on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: allow
        # 
        # - **drop**: deny
        # 
        # - **log**: monitor
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The addresses in the address book.
        self.address_list = address_list
        # The number of addresses in the address book.
        self.address_list_count = address_list_count
        # The addresses and their remarks.
        self.addresses = addresses
        # The ID of the application that is used in the access control policy.
        self.application_id = application_id
        # The application type supported by the access control policy for the VPC firewall. We recommend that you use the ApplicationNameList parameter instead. Valid values:
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
        # - **ANY**: All application types.
        self.application_name = application_name
        # The application types that are supported by the access control policy. Valid values:
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
        # - **SSL**
        # 
        # - **VNC**
        # 
        # - **ANY** (indicates all application types)
        self.application_name_list = application_name_list
        # Indicates whether to automatically add the public IP addresses of new ECS instances that match the tags to the address book. New ECS instances include newly purchased instances with the specified tags and existing instances whose tags are modified to match.
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The time when the policy was created, provided as a UNIX timestamp in seconds.
        self.create_time = create_time
        # The description of the access control policy.
        self.description = description
        # The destination port that is used in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book.
        # 
        # - **port**: Port
        # 
        # - **group**: Port address book
        self.dest_port_group = dest_port_group
        # The ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # 
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. The value of this parameter varies based on the value of DestinationType.
        # 
        # - If the value of DestinationType is`net`, the value of this parameter is a CIDR block. Example: 10.0.3.0/24.
        # 
        # - If the value of DestinationType is`domain`, the value of this parameter is a domain name. Example: aliyun.
        # 
        # - If the value of DestinationType is`group`, the value of this parameter is the name of an address book. Example: db_group.
        # 
        # - If the value of DestinationType is`location`, the value of this parameter is a location. For more information about the location codes, see AddControlPolicy. Example: ["BJ11", "ZB"].
        # 
        # > If this parameter is omitted, all types of destination addresses are retrieved.
        self.destination = destination
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # - **ip**: an IP address book, which contains one or more CIDR blocks.
        # 
        # - **tag**: an ECS tag-based address book, which contains the public IP addresses of ECS instances that have specific tags.
        # 
        # - **domain**: a domain name address book, which contains one or more domain names.
        # 
        # - **threat**: a threat intelligence address book, which contains one or more malicious IP addresses or domain names.
        # 
        # - **backsrc**: a back-to-source address book, which contains the back-to-source IP addresses of one or more Anti-DDoS or WAF instances.
        self.destination_group_type = destination_group_type
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        # 
        # - **location**: destination region
        self.destination_type = destination_type
        # The direction of internet traffic. Valid values:
        # 
        # - **in**: inbound traffic
        # 
        # - **out**: outbound traffic
        self.direction = direction
        # The result of the DNS resolution.
        self.dns_result = dns_result
        # The time of the DNS resolution, provided as a UNIX timestamp in seconds.
        self.dns_result_time = dns_result_time
        # The DNS resolution method of the domain name in the access control policy. Valid values:
        # 
        # - **0**: FQDN-based resolution
        # 
        # - **1**: DNS-based dynamic resolution
        # 
        # - **2**: FQDN-based and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The end time of the policy validity period. This is a UNIX timestamp, accurate to the second. The time must be on the hour or half-hour and must be at least 30 minutes later than the start time.
        # 
        # > This parameter is empty if RepeatType is set to Permanent. It is required if RepeatType is set to None, Daily, Weekly, or Monthly.
        self.end_time = end_time
        # The name of the address book.
        self.group_name = group_name
        # The type of the address book. Valid values:
        # 
        # - **ip**: IP address book
        # 
        # - **domain**: domain address book
        # 
        # - **port**: port address book
        # 
        # - **tag**: ECS tag-based address book
        # 
        # - **allCloud**: cloud service address book
        # 
        # - **threat**: threat intelligence address book
        self.group_type = group_type
        # The unique ID of the address book.
        # 
        # This ID is required for other operations, such as deleting the address book. You can obtain the ID by calling the [DescribeAddressBook](https://help.aliyun.com/document_detail/138869.html) operation.
        self.group_uuid = group_uuid
        # The time when the policy was last hit, provided as a UNIX timestamp in seconds.
        self.hit_last_time = hit_last_time
        # The hit count of the access control policy.
        self.hit_times = hit_times
        # The IP version. Valid values:
        # 
        # - **4**: IPv4
        # 
        # - **6**: IPv6
        self.ip_version = ip_version
        # The time when the policy was last modified, provided as a UNIX timestamp in seconds.
        self.modify_time = modify_time
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy.
        # 
        # The priority starts from 1. A smaller value indicates a higher priority.
        self.order = order
        # The protocol type of the traffic in the access control policy. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # - **ANY**: All protocol types
        # 
        # >
        self.proto = proto
        # The number of policies that reference this address book.
        self.reference_count = reference_count
        # The status of the access control policy. Valid values:
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.release = release
        # The days of a week or month on which the policy recurs.
        # 
        # > If RepeatType is set to Weekly, the valid values are 0 to 6. The week starts on Sunday.
        # > If RepeatType is set to Monthly, the valid values are 1 to 31.
        self.repeat_days = repeat_days
        # The time when the policy stops to take effect. Example: 23:30. The time must be on the hour or half-hour and must be at least 30 minutes later than the recurrence start time.
        # 
        # > This parameter is returned empty if RepeatType is set to Permanent or None. This parameter is required if RepeatType is set to Daily, Weekly, or Monthly. The time is in the HH:mm format. Examples: 08:00 and 23:30.
        self.repeat_end_time = repeat_end_time
        # The time when the policy starts to take effect. Example: 08:00. The time must be on the hour or half-hour and must be at least 30 minutes earlier than the recurrence end time.
        # 
        # > This parameter is returned empty if RepeatType is set to Permanent or None. This parameter is required if RepeatType is set to Daily, Weekly, or Monthly. The time is in the HH:mm format. Examples: 08:00 and 23:30.
        self.repeat_start_time = repeat_start_time
        # The recurrence type of the policy. Valid values:
        # 
        # - **Permanent** (default): The policy is always valid.
        # 
        # - **None**: The policy is valid only once.
        # 
        # - **Daily**: The policy recurs daily.
        # 
        # - **Weekly**: The policy recurs weekly.
        # 
        # - **Monthly**: The policy recurs monthly.
        self.repeat_type = repeat_type
        # The source address in the access control policy. The value of this parameter varies based on the value of SourceType.
        # 
        # - If **SourceType** is set to`net`, the value of this parameter is a CIDR block. Example: 192.0.XX.XX/24.
        # 
        # - If **SourceType** is set to`group`, the value of this parameter is the name of a source address book. Example: db_group.
        # 
        # - If **SourceType** is set to`location`, the value of this parameter is a location. For more information, see [AddControlPolicy](https://help.aliyun.com/document_detail/138867.html). Example: ["BJ11", "ZB"].
        self.source = source
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the access control policy. Valid values:
        # 
        # - **ip**: An address book that contains one or more IP addresses or CIDR blocks.
        # 
        # - **tag**: An address book that contains the public IP addresses of ECS instances with specific tags.
        # 
        # - **domain**: A domain name address book, which contains one or more domain names.
        # 
        # - **threat**: a threat intelligence address book, which contains one or more malicious IP addresses or domain names.
        # 
        # - **backsrc**: a back-to-source address book, which contains the back-to-source IP addresses of one or more Anti-DDoS or WAF instances.
        self.source_group_type = source_group_type
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: a source CIDR block
        # 
        # - **group**: a source address book
        # 
        # - **location**: a source region
        self.source_type = source_type
        # The number of specification units that the policy consumes. The value is calculated by using the following formula: Number of source addresses × Number of destination addresses × Number of port ranges × Number of applications.
        self.spread_cnt = spread_cnt
        # The start of the policy\\"s validity period, provided as a UNIX timestamp in seconds.
        self.start_time = start_time
        # The ECS tags.
        self.tag_list = tag_list
        # The logical relationship among multiple ECS tags. Valid values:
        # 
        # - **and**: An ECS instance must have all the specified tags.
        # 
        # - **or**: An ECS instance must have one of the specified tags.
        self.tag_relation = tag_relation
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
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

        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

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

        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.DescribeAclCheckResponseBodyCheckRecordAclsAclAddresses()
                self.addresses.append(temp_model.from_map(k1))

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
                temp_model = main_models.DescribeAclCheckResponseBodyCheckRecordAclsAclTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

class DescribeAclCheckResponseBodyCheckRecordAclsAclTagList(DaraModel):
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

class DescribeAclCheckResponseBodyCheckRecordAclsAclAddresses(DaraModel):
    def __init__(
        self,
        address: str = None,
        note: str = None,
    ):
        # The address in the address book.
        self.address = address
        # The remarks.
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.note is not None:
            result['Note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        return self

