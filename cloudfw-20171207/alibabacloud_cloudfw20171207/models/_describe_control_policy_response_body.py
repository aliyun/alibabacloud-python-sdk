# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        page_no: str = None,
        page_size: str = None,
        policys: List[main_models.DescribeControlPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The information about the access control policies.
        self.policys = policys
        # The ID of the request.
        self.request_id = request_id
        # The total number of the returned access control policies.
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.policys = []
        if m.get('Policys') is not None:
            for k1 in m.get('Policys'):
                temp_model = main_models.DescribeControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeControlPolicyResponseBodyPolicys(DaraModel):
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
        direction: str = None,
        dns_result: str = None,
        dns_result_time: int = None,
        domain_resolve_type: str = None,
        end_time: int = None,
        hit_last_time: int = None,
        hit_times: int = None,
        ip_version: int = None,
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
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action
        # The UUID of the access control policy.
        self.acl_uuid = acl_uuid
        # The application ID in the access control policy.
        self.application_id = application_id
        # The application type supported by the access control policy. We recommend that you specify ApplicationNameList. Valid values:
        # 
        # *   **FTP**
        # *   **HTTP**
        # *   **HTTPS**
        # *   **Memcache**
        # *   **MongoDB**
        # *   **MQTT**
        # *   **MySQL**
        # *   **RDP**
        # *   **Redis**
        # *   **SMTP**
        # *   **SMTPS**
        # *   **SSH**
        # *   **SSL**
        # *   **VNC**
        # *   **ANY**: all types of applications
        self.application_name = application_name
        # The application names.
        self.application_name_list = application_name_list
        # The time when the access control policy was created.
        self.create_time = create_time
        # The description of the access control policy.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. The value of this parameter varies based on the value of DestinationType.
        # 
        # *   If the value of **DestinationType** is **net**, the value of Destination is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If the value of **DestinationType** is **domain**, the value of Destination is a domain name. Example: aliyuncs.com.
        # *   If the value of **DestinationType** is **group**, the value of Destination is the name of an address book. Example: db_group.
        # *   If the value of **DestinationType** is **location**, the value of Destination is the name of a location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"].
        self.destination = destination
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more IP addresses
        # *   **tag**: an ECS tag-based address book that includes the IP addresses of the ECS instances with one or more specific tags
        # *   **domain**: an address book that includes one or more domain names
        # *   **threat**: an address book that includes one or more malicious IP addresses or domain names
        # *   **backsrc**: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances
        self.destination_group_type = destination_group_type
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: location
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction
        # The DNS resolution results.
        self.dns_result = dns_result
        # The time when the Domain Name System (DNS) resolution was performed. The value is a timestamp. Unit: seconds.
        self.dns_result_time = dns_result_time
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a timestamp. Unit: seconds. The end time must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
        self.end_time = end_time
        # The time when the access control policy was last hit. The value is a timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time
        # The number of hits for the access control policy.
        self.hit_times = hit_times
        # The IP version used in the access control policy. Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The time when the access control policy was modified.
        self.modify_time = modify_time
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.order = order
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **ANY**
        # *   **TCP**
        # *   **UDP**
        # *   **ICMP**
        self.proto = proto
        # The status of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If RepeatType is set to `Permanent`, `None`, or `Daily`, this parameter is left empty. Example: [].
        # *   If RepeatType is set to Weekly, this parameter must be specified. Example: [0, 6].
        # 
        # >  If RepeatType is set to Weekly, the fields in the value of RepeatDays cannot be repeated.
        # 
        # *   If RepeatType is set to `Monthly`, this parameter must be specified. Example: [1, 31].
        # 
        # >  If RepeatType is set to Monthly, the fields in the value of RepeatDays cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_start_time = repeat_start_time
        # The recurrence type based on which the access control policy takes effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If **SourceType** is set to `group`, the value of Source is the name of an address book. Example: db_group.
        # *   If **SourceType** is set to `location`, the value of Source is a location. For more information about location codes, see [AddControlPolicy](https://help.aliyun.com/document_detail/138867.html). Example: ["BJ11", "ZB"].
        self.source = source
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more IP addresses
        # *   **tag**: an Elastic Compute Service (ECS) tag-based address book that includes the IP addresses of the ECS instances with one or more specific tags
        # *   **domain**: an address book that includes one or more domain names
        # *   **threat**: an address book that includes one or more malicious IP addresses or domain names
        # *   **backsrc**: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or Web Application Firewall (WAF) instances
        self.source_group_type = source_group_type
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        self.source_type = source_type
        # The total quota consumed by the returned access control policies, which is the sum of the quota consumed by each policy. The quota that is consumed by an access control policy is calculated by using the following formula: Quota that is consumed by an access control policy = Number of source addresses (number of CIDR blocks or regions) × Number of destination addresses (number of CIDR blocks, regions, or domain names) × Number of port ranges × Number of applications.
        self.spread_cnt = spread_cnt
        # The time when the access control policy starts to take effect. The value is a timestamp. Unit: seconds. The start time must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
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

        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time

        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

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

        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')

        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

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

