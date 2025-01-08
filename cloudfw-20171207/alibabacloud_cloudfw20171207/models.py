# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddAddressBookRequestTagList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AddAddressBookRequest(TeaModel):
    def __init__(
        self,
        address_list: str = None,
        auto_add_tag_ecs: str = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        lang: str = None,
        source_ip: str = None,
        tag_list: List[AddAddressBookRequestTagList] = None,
        tag_relation: str = None,
    ):
        # The addresses that you want to add to the address book. Separate multiple addresses with commas (,).
        # 
        # >  If you set GroupType to `ip`, `port` or `domain`, you must specify AddressList.
        # 
        # *   If you set GroupType to `ip`, you must add IP addresses to the address book. Example: 192.0.XX.XX/32,192.0.XX.XX/24.
        # *   If you set GroupType to `port`, you must add port numbers or port ranges to the address book. Example: 80,100/200.
        # *   If you set GroupType to `domain`, you must add domain names to the address book. Example: example.com,aliyundoc.com.
        self.address_list = address_list
        # Specifies whether to automatically add public IP addresses of ECS instances to the address book if the instances match the specified tags. Valid values:
        # 
        # *   **1**: yes
        # *   **0** (default): no
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        # 
        # This parameter is required.
        self.description = description
        # The name of the address book.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the address book. Valid values:
        # 
        # *   **ip**: IP address book
        # *   **domain**: domain address book
        # *   **port**: port address book
        # *   **tag**: ECS tag-based address book
        # 
        # This parameter is required.
        self.group_type = group_type
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ECS tags that you want to match.
        self.tag_list = tag_list
        # The logical relation among the ECS tags that you want to match. Valid values:
        # 
        # *   **and** (default): Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # *   **or**: The public IP addresses of ECS instances that match one of the specified tags can be added to the address book.
        self.tag_relation = tag_relation

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = AddAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class AddAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        group_uuid: str = None,
        request_id: str = None,
    ):
        # The UUID of the returned address book.
        self.group_uuid = group_uuid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddControlPolicyRequest(TeaModel):
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
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The application type supported by the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # *   **ANY**\
        # 
        # > The value of this parameter is based on the value of Proto. If Proto is set to TCP, you can set ApplicationName to any valid value. If Proto is set to UDP, ICMP, or ANY, you can set ApplicationName only to ANY. You must specify at least one of the ApplicationNameList and ApplicationName parameters.
        self.application_name = application_name
        # The application types supported by the access control policy.
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
        # The type of the destination port in the access control policy.
        # 
        # Valid values:
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
        # *   If DestinationType is set to group, the value of this parameter is an address book name.
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
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: location
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.end_time = end_time
        # The IP version supported by the access control policy.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The priority of the access control policy. The priority value starts from 1. A smaller priority value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The protocol type supported by the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: enables the access control policy.
        # *   **false**: disables the access control policy.
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If you set RepeatType to `Permanent`, `None`, or `Daily`, leave this parameter empty. Example: [].
        # *   If you set RepeatType to Weekly, you must specify this parameter. Example: [0, 6].
        # 
        # >  If you set RepeatType to Weekly, the fields in the value of this parameter cannot be repeated.
        # 
        # *   If you set RepeatType to `Monthly`, you must specify this parameter. Example: [1, 31].
        # 
        # >  If you set RepeatType to Monthly, the fields in the value of this parameter cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The end time must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The start time must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # *   If SourceType is set to net, the value of this parameter is a CIDR block.
        # 
        #     Example: 1.1.XX.XX/24
        # 
        # *   If SourceType is set to group, the value of this parameter is an address book name.
        # 
        #     Example: db_group
        # 
        # *   If SourceType is set to location, the value of this parameter is a location.
        # 
        #     Example: ["BJ11", "ZB"]
        # 
        # This parameter is required.
        self.source = source
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AddControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        # The ID of the access control policy that is created on the Internet firewall.
        self.acl_uuid = acl_uuid
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddInstanceMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_desc: str = None,
        member_uid: int = None,
    ):
        # The remarks of the member. The value must be 1 to 256 characters in length.
        self.member_desc = member_desc
        # The UID of the member. You can add up to 20 members to Cloud Firewall at a time.
        # 
        # This parameter is required.
        self.member_uid = member_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class AddInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[AddInstanceMembersRequestMembers] = None,
    ):
        # The members.
        # 
        # This parameter is required.
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddInstanceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class AddInstanceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddInstanceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCopyVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        source_vpc_firewall_id: str = None,
        target_vpc_firewall_id: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the policy group of the source VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the IDs of policy groups.
        # 
        # This parameter is required.
        self.source_vpc_firewall_id = source_vpc_firewall_id
        # The ID of the policy group of the destination VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a VBR, or a CCN instance.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the IDs of policy groups.
        # 
        # This parameter is required.
        self.target_vpc_firewall_id = target_vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_vpc_firewall_id is not None:
            result['SourceVpcFirewallId'] = self.source_vpc_firewall_id
        if self.target_vpc_firewall_id is not None:
            result['TargetVpcFirewallId'] = self.target_vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceVpcFirewallId') is not None:
            self.source_vpc_firewall_id = m.get('SourceVpcFirewallId')
        if m.get('TargetVpcFirewallId') is not None:
            self.target_vpc_firewall_id = m.get('TargetVpcFirewallId')
        return self


class BatchCopyVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchCopyVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCopyVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCopyVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_uuid_list: List[str] = None,
        vpc_firewall_id: str = None,
    ):
        # The UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid_list = acl_uuid_list
        # The instance ID of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid_list is not None:
            result['AclUuidList'] = self.acl_uuid_list
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuidList') is not None:
            self.acl_uuid_list = m.get('AclUuidList')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class BatchDeleteVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDownloadTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        task_data: str = None,
        task_type: str = None,
        time_zone: str = None,
    ):
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The query condition of the download task.
        self.task_data = task_data
        # The type of the task. For more information about task types, see the descriptions in the "DescribeDownloadTaskType" topic.
        self.task_type = task_type
        # The time zone of the time information in the downloaded file. The value must be an identifier of a time zone in the Internet Assigned Numbers Authority (IANA) database. The default value is Asia/Shanghai, which indicates UTC+8.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_data is not None:
            result['TaskData'] = self.task_data
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskData') is not None:
            self.task_data = m.get('TaskData')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreateDownloadTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_id: int = None,
        task_name: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the task. Valid values:
        # 
        # finish: The task finished. You can query the task to obtain the download link of the file.
        # 
        # start: The task start.
        # 
        # error: An error occurred.
        # 
        # expire: The task file is invalid and cannot be downloaded.
        self.status = status
        # The unique ID of the task.
        self.task_id = task_id
        # The name of the file download task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateDownloadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDownloadTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDownloadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNatFirewallControlPolicyRequest(TeaModel):
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
        # *   **true**\
        # *   **false**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        # The unique ID of the access control policy.
        # 
        # >  To modify an access control policy, you must specify the unique ID of the policy. You can call the DescribeNatFirewallControlPolicy operation to obtain the ID.
        self.acl_uuid = acl_uuid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNatFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNatFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityProxyRequestNatRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the default route.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The next hop of the original NAT gateway.
        # 
        # This parameter is required.
        self.next_hop_id = next_hop_id
        # The network type of the next hop. Set the value to NatGateway.
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        # The route table to which the default route of the NAT gateway belongs.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class CreateSecurityProxyRequest(TeaModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        nat_route_entry_list: List[CreateSecurityProxyRequestNatRouteEntryList] = None,
        proxy_name: str = None,
        region_no: str = None,
        strict_mode: int = None,
        vpc_id: str = None,
        vswitch_auto: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
    ):
        # The status of the NAT firewall. Valid values:
        # 
        # *   **open**: enabled
        # *   **close**: disabled
        self.firewall_switch = firewall_switch
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The routes to be switched to the NAT gateway.
        # 
        # This parameter is required.
        self.nat_route_entry_list = nat_route_entry_list
        # The name of the NAT firewall. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). However, it cannot start with an underscore.
        # 
        # This parameter is required.
        self.proxy_name = proxy_name
        # The region ID of the virtual private cloud (VPC).
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.region_no = region_no
        # Specifies whether to enable the strict mode. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.strict_mode = strict_mode
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The mode of the vSwitch that you want to use. Valid values:
        # 
        # *   **true**: automatic
        # *   **false**: manual
        self.vswitch_auto = vswitch_auto
        # The CIDR block of the vSwitch.
        self.vswitch_cidr = vswitch_cidr
        # The ID of the vSwitch. This parameter is required if you set the VswitchAuto parameter to true.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.nat_route_entry_list:
            for k in self.nat_route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k.to_map() if k else None)
        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_auto is not None:
            result['VswitchAuto'] = self.vswitch_auto
        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k in m.get('NatRouteEntryList'):
                temp_model = CreateSecurityProxyRequestNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k))
        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchAuto') is not None:
            self.vswitch_auto = m.get('VswitchAuto')
        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateSecurityProxyResponseBody(TeaModel):
    def __init__(
        self,
        proxy_id: str = None,
        request_id: str = None,
    ):
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSecurityProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecurityProxyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecurityProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlsLogDispatchRequest(TeaModel):
    def __init__(
        self,
        sls_region_id: str = None,
        ttl: int = None,
    ):
        # The region ID of the Simple Log Service project.
        self.sls_region_id = sls_region_id
        # The log retention period. Unit: days.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class CreateSlsLogDispatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSlsLogDispatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSlsLogDispatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSlsLogDispatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrFirewallV2Request(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_description: str = None,
        firewall_name: str = None,
        firewall_subnet_cidr: str = None,
        firewall_vpc_cidr: str = None,
        firewall_vpc_id: str = None,
        firewall_vswitch_id: str = None,
        lang: str = None,
        region_no: str = None,
        route_mode: str = None,
        tr_attachment_master_cidr: str = None,
        tr_attachment_master_zone: str = None,
        tr_attachment_slave_cidr: str = None,
        tr_attachment_slave_zone: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The description of the firewall.
        self.firewall_description = firewall_description
        # The name of the firewall.
        self.firewall_name = firewall_name
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The ID of the VPC in which the ENI associated with the VPC firewall is created in manual mode.
        self.firewall_vpc_id = firewall_vpc_id
        # The ID of the vSwitch that is used to create the ENI in manual mode.
        self.firewall_vswitch_id = firewall_vswitch_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The region ID of the route router.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The primary zone for the vSwitch.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The secondary zone for the vSwitch.
        self.tr_attachment_slave_zone = tr_attachment_slave_zone
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr
        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr
        if self.firewall_vpc_id is not None:
            result['FirewallVpcId'] = self.firewall_vpc_id
        if self.firewall_vswitch_id is not None:
            result['FirewallVswitchId'] = self.firewall_vswitch_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr
        if self.tr_attachment_master_zone is not None:
            result['TrAttachmentMasterZone'] = self.tr_attachment_master_zone
        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr
        if self.tr_attachment_slave_zone is not None:
            result['TrAttachmentSlaveZone'] = self.tr_attachment_slave_zone
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')
        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')
        if m.get('FirewallVpcId') is not None:
            self.firewall_vpc_id = m.get('FirewallVpcId')
        if m.get('FirewallVswitchId') is not None:
            self.firewall_vswitch_id = m.get('FirewallVswitchId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')
        if m.get('TrAttachmentMasterZone') is not None:
            self.tr_attachment_master_zone = m.get('TrAttachmentMasterZone')
        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')
        if m.get('TrAttachmentSlaveZone') is not None:
            self.tr_attachment_slave_zone = m.get('TrAttachmentSlaveZone')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateTrFirewallV2ResponseBody(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        request_id: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTrFirewallV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrFirewallV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrFirewallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrFirewallV2RoutePolicyRequestDestCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class CreateTrFirewallV2RoutePolicyRequestSrcCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class CreateTrFirewallV2RoutePolicyRequest(TeaModel):
    def __init__(
        self,
        dest_candidate_list: List[CreateTrFirewallV2RoutePolicyRequestDestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        src_candidate_list: List[CreateTrFirewallV2RoutePolicyRequestSrcCandidateList] = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The description of the traffic redirection instance.
        self.policy_description = policy_description
        # The name of the traffic redirection instance.
        self.policy_name = policy_name
        # The type of the traffic redirection scenario of the VPC firewall. Valid values:
        # 
        # *   **fullmesh**: interconnected instances
        # *   **one_to_one**: instance to instance
        # *   **end_to_end**: instance to instances
        self.policy_type = policy_type
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = CreateTrFirewallV2RoutePolicyRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = CreateTrFirewallV2RoutePolicyRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        return self


class CreateTrFirewallV2RoutePolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        dest_candidate_list_shrink: str = None,
        firewall_id: str = None,
        lang: str = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        src_candidate_list_shrink: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list_shrink = dest_candidate_list_shrink
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The description of the traffic redirection instance.
        self.policy_description = policy_description
        # The name of the traffic redirection instance.
        self.policy_name = policy_name
        # The type of the traffic redirection scenario of the VPC firewall. Valid values:
        # 
        # *   **fullmesh**: interconnected instances
        # *   **one_to_one**: instance to instance
        # *   **end_to_end**: instance to instances
        self.policy_type = policy_type
        # The primary traffic redirection instances.
        self.src_candidate_list_shrink = src_candidate_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_candidate_list_shrink is not None:
            result['DestCandidateList'] = self.dest_candidate_list_shrink
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')
        return self


class CreateTrFirewallV2RoutePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class CreateTrFirewallV2RoutePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrFirewallV2RoutePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrFirewallV2RoutePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_switch: str = None,
        firewall_vswitch_cidr_block: str = None,
        firewall_vpc_cidr_block: str = None,
        firewall_vpc_zone_id: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_id: str = None,
        v_switch_id: str = None,
        vpc_firewall_name: str = None,
        vpc_region: str = None,
    ):
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the VPC firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the VPC firewall is disabled. You can call the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to manually enable the VPC firewall.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The CIDR block of the vSwitch that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VSWITCH VPC that is automatically created for the VPC firewall for traffic redirection. The CIDR block does not conflict with your network plan. The subnet mask of the CIDR block must be less than or equal to 29 bits in length. The CIDR block of the vSwitch must be within the network segment of the VPC.
        # 
        # If you do not specify a value, the CIDR block 10.219.219.216/29 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The CIDR block of the VPC that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VPC VPC that is automatically created for the VPC firewall for traffic redirection. The subnet mask of the CIDR block must be less than or equal to 28 bits in length.
        # 
        # If you do not specify a value, the CIDR block 10.0.0.0/8 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The ID of the zone to which the vSwitch belongs. If your service is latency-sensitive, you can specify the same zone for the vSwitch of the firewall and the vSwitch of your business VPC to minimize latency.
        # 
        # If you do not specify a value, a zone is automatically assigned for the vSwitch.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region. For more information about zones that are supported by each region, see [Query zones](https://help.aliyun.com/document_detail/36064.html).
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the VPC for which you want to create the VPC firewall.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The ID of the vSwitch that is used to associate with the elastic network interface (ENI) required by the VPC firewall.
        self.v_switch_id = v_switch_id
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The ID of the region to which the VPC belongs.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.vpc_region = vpc_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.firewall_vswitch_cidr_block is not None:
            result['FirewallVSwitchCidrBlock'] = self.firewall_vswitch_cidr_block
        if self.firewall_vpc_cidr_block is not None:
            result['FirewallVpcCidrBlock'] = self.firewall_vpc_cidr_block
        if self.firewall_vpc_zone_id is not None:
            result['FirewallVpcZoneId'] = self.firewall_vpc_zone_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        if self.vpc_region is not None:
            result['VpcRegion'] = self.vpc_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('FirewallVSwitchCidrBlock') is not None:
            self.firewall_vswitch_cidr_block = m.get('FirewallVSwitchCidrBlock')
        if m.get('FirewallVpcCidrBlock') is not None:
            self.firewall_vpc_cidr_block = m.get('FirewallVpcCidrBlock')
        if m.get('FirewallVpcZoneId') is not None:
            self.firewall_vpc_zone_id = m.get('FirewallVpcZoneId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        if m.get('VpcRegion') is not None:
            self.vpc_region = m.get('VpcRegion')
        return self


class CreateVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_firewall_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVpcFirewallCenConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallConfigureRequest(TeaModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        local_vpc_cidr_table_list: str = None,
        local_vpc_id: str = None,
        local_vpc_region: str = None,
        member_uid: str = None,
        peer_vpc_cidr_table_list: str = None,
        peer_vpc_id: str = None,
        peer_vpc_region: str = None,
        vpc_firewall_name: str = None,
    ):
        # The status of the VPC firewall after you create the firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the VPC firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the VPC firewall is disabled. To enable the firewall, you can call the [ModifyVpcFirewallSwitchStatus](https://help.aliyun.com/document_detail/342935.html) operation.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English.
        self.lang = lang
        # The CIDR blocks of the local VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the local VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the local VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the local VPC.
        # 
        # This parameter is required.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        # The ID of the local VPC.
        # 
        # This parameter is required.
        self.local_vpc_id = local_vpc_id
        # The region ID of the local VPC.
        # 
        # >  For more information about the regions in which Cloud Firewall is available, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.local_vpc_region = local_vpc_region
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The CIDR blocks of the peer VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the peer VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the peer VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the peer VPC.
        # 
        # This parameter is required.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        # The ID of the peer VPC.
        # 
        # This parameter is required.
        self.peer_vpc_id = peer_vpc_id
        # The region ID of the peer VPC.
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.peer_vpc_region = peer_vpc_region
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list
        if self.local_vpc_id is not None:
            result['LocalVpcId'] = self.local_vpc_id
        if self.local_vpc_region is not None:
            result['LocalVpcRegion'] = self.local_vpc_region
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list
        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id
        if self.peer_vpc_region is not None:
            result['PeerVpcRegion'] = self.peer_vpc_region
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')
        if m.get('LocalVpcId') is not None:
            self.local_vpc_id = m.get('LocalVpcId')
        if m.get('LocalVpcRegion') is not None:
            self.local_vpc_region = m.get('LocalVpcRegion')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')
        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')
        if m.get('PeerVpcRegion') is not None:
            self.peer_vpc_region = m.get('PeerVpcRegion')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class CreateVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_firewall_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVpcFirewallConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallControlPolicyRequest(TeaModel):
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
        domain_resolve_type: str = None,
        end_time: int = None,
        lang: str = None,
        member_uid: str = None,
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
        vpc_firewall_id: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # - **accept**: allows the traffic.
        # - **drop**: blocks the traffic.
        # - **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The type of the applications that the access control policy supports. Valid values:
        # 
        # - **FTP**\
        # - **HTTP**\
        # - **HTTPS**\
        # - **MySQL**\
        # - **SMTP**\
        # - **SMTPS**\
        # - **RDP**\
        # - **VNC**\
        # - **SSH**\
        # - **Redis**\
        # - **MQTT**\
        # - **MongoDB**\
        # - **Memcache**\
        # - **SSL**\
        # - **ANY**: all types of applications
        self.application_name = application_name
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy. 
        # 
        # >  If **DestPortType** is set to `port`, you must specify this parameter.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy. 
        # 
        # >  If **DestPortType** is set to `group`, you must specify this parameter.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # - **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. Valid values:
        # 
        # - If **DestinationType** is set to `net`, the value of **Destination** must be a CIDR block.
        # - If **DestinationType** is set to `group`, the value of **Destination** must be an address book.
        # - If **DestinationType** is set to `domain`, the value of **Destination** must be a domain name.
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # - **group**: address book
        # - **domain**: domain name
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.end_time = end_time
        # The language of the content within the request and response. Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The priority of the access control policy. 
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The type of the protocol in the access control policy. Valid values:
        # 
        # - **ANY** (If you are not sure about the protocol type, you can set this parameter to ANY.)
        # - **TCP**\
        # - **UDP**\
        # - **ICMP**\
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values: 
        # 
        # - **true**: enables the access control policy.
        # - **false**: disables the access control policy.
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If you set RepeatType to `Permanent`, `None`, or `Daily`, leave this parameter empty. Example: [].
        # *   If you set RepeatType to Weekly, you must specify this parameter. Example: [0, 6].
        # 
        # >  If you set RepeatType to Weekly, the fields in the value of this parameter cannot be repeated.
        # 
        # *   If you set RepeatType to `Monthly`, you must specify this parameter. Example: [1, 31].
        # 
        # >  If you set RepeatType to Monthly, the fields in the value of this parameter cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
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
        # - If SourceType is set to `net`, the value of Source must be a CIDR block.
        # - If SourceType is set to `group`, the value of Source must be an address book.
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # - **group**: address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.start_time = start_time
        # The ID of the policy group in which you want to create the access control policy. 
        # 
        # - If a VPC firewall protects the traffic between two VPCs that are connected by using a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # - If a VPC firewall protects the traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](https://www.alibabacloud.com/help/en/cloud-firewall/latest/describevpcfirewallaclgrouplist) operation to query the IDs.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
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
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
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
        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
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
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        # The ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAddressBookRequest(TeaModel):
    def __init__(
        self,
        group_uuid: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The ID of the address book.
        # 
        # To delete the address book, you must provide the ID of the address book. You can call the DescribeAddressBook operation to query the ID.
        # 
        # This parameter is required.
        self.group_uuid = group_uuid
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        direction: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The UUID of the access control policy.
        # 
        # To delete an access control policy, you must specify the UUID of the policy. You can call the [DescribeControlPolicy](https://help.aliyun.com/document_detail/138866.html) operation to query the UUID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound.
        # *   **out**: outbound.
        self.direction = direction
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The source IP address of the traffic.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyTemplateRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        template_id: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the access control policy template.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteControlPolicyTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteControlPolicyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteControlPolicyTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteControlPolicyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDownloadTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        task_id: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the file download task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteDownloadTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDownloadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDownloadTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDownloadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFirewallV2RoutePoliciesRequest(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DeleteFirewallV2RoutePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFirewallV2RoutePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFirewallV2RoutePoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFirewallV2RoutePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        member_uids: List[int] = None,
    ):
        # The UIDs of the members.
        # 
        # This parameter is required.
        self.member_uids = member_uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uids is not None:
            result['MemberUids'] = self.member_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUids') is not None:
            self.member_uids = m.get('MemberUids')
        return self


class DeleteInstanceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNatFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
    ):
        # The UUID of the access control policy.
        # 
        # To delete an access control policy, you must provide the ID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DeleteNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNatFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNatFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNatFirewallControlPolicyBatchRequest(TeaModel):
    def __init__(
        self,
        acl_uuid_list: List[str] = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
    ):
        # The UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid_list = acl_uuid_list
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid_list is not None:
            result['AclUuidList'] = self.acl_uuid_list
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuidList') is not None:
            self.acl_uuid_list = m.get('AclUuidList')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DeleteNatFirewallControlPolicyBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNatFirewallControlPolicyBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNatFirewallControlPolicyBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNatFirewallControlPolicyBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityProxyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        proxy_id: str = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        return self


class DeleteSecurityProxyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecurityProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecurityProxyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSecurityProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrFirewallV2Request(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteTrFirewallV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrFirewallV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrFirewallV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrFirewallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id_list: List[str] = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id_list = vpc_firewall_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')
        return self


class DeleteVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVpcFirewallCenConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id_list: List[str] = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id_list = vpc_firewall_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')
        return self


class DeleteVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcFirewallConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVpcFirewallConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
        vpc_firewall_id: str = None,
    ):
        # The ID of the access control policy. 
        # 
        # To delete an access control policy, you must provide the ID of the policy. You can call the **DescribeVpcFirewallControlPolicy** operation to query the ID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The natural language of the request and response. Valid values: 
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The ID of the group to which the access control policy belongs. You can call the **DescribeVpcFirewallAclGroupList** operation to query the ID.  
        # 
        # Valid values:
        # 
        # - If the VPC firewall is used to protect a CEN instance, the value of this parameter is the ID of the CEN instance.  
        # 
        # Example: cen-ervw0g12b5jbw****\
        # - If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall.  
        # 
        # Example: vfw-a42bbb7b887148c9****\
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DeleteVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeACLProtectTrendRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        lang: str = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp that is accurate to seconds.
        self.end_time = end_time
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The beginning of the time range to query. The value is a UNIX timestamp that is accurate to seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeACLProtectTrendResponseBodyTrendList(TeaModel):
    def __init__(
        self,
        protect_cnt: int = None,
        time: int = None,
    ):
        # The number of requests that are blocked by ACL on the current day.
        self.protect_cnt = protect_cnt
        # The UNIX timestamp at midnight (00:00:00) of each day, which indicates the date of the current day. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_cnt is not None:
            result['ProtectCnt'] = self.protect_cnt
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectCnt') is not None:
            self.protect_cnt = m.get('ProtectCnt')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeACLProtectTrendResponseBody(TeaModel):
    def __init__(
        self,
        in_protect_cnt: int = None,
        inter_vpcprotect_cnt: int = None,
        interval: int = None,
        out_protect_cnt: int = None,
        request_id: str = None,
        total_protect_cnt: int = None,
        trend_list: List[DescribeACLProtectTrendResponseBodyTrendList] = None,
    ):
        # The number of internal requests that are blocked by the ACL feature.
        self.in_protect_cnt = in_protect_cnt
        # This parameter is deprecated.
        self.inter_vpcprotect_cnt = inter_vpcprotect_cnt
        # The interval for returning data. Unit: seconds.
        self.interval = interval
        # The number of external requests that are blocked by the ACL feature.
        self.out_protect_cnt = out_protect_cnt
        # The request ID.
        self.request_id = request_id
        # The total number of requests that are blocked by the ACL feature.
        self.total_protect_cnt = total_protect_cnt
        # The statistics on the requests that are blocked by the ACL feature.
        self.trend_list = trend_list

    def validate(self):
        if self.trend_list:
            for k in self.trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_protect_cnt is not None:
            result['InProtectCnt'] = self.in_protect_cnt
        if self.inter_vpcprotect_cnt is not None:
            result['InterVPCProtectCnt'] = self.inter_vpcprotect_cnt
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.out_protect_cnt is not None:
            result['OutProtectCnt'] = self.out_protect_cnt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_protect_cnt is not None:
            result['TotalProtectCnt'] = self.total_protect_cnt
        result['TrendList'] = []
        if self.trend_list is not None:
            for k in self.trend_list:
                result['TrendList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InProtectCnt') is not None:
            self.in_protect_cnt = m.get('InProtectCnt')
        if m.get('InterVPCProtectCnt') is not None:
            self.inter_vpcprotect_cnt = m.get('InterVPCProtectCnt')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OutProtectCnt') is not None:
            self.out_protect_cnt = m.get('OutProtectCnt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalProtectCnt') is not None:
            self.total_protect_cnt = m.get('TotalProtectCnt')
        self.trend_list = []
        if m.get('TrendList') is not None:
            for k in m.get('TrendList'):
                temp_model = DescribeACLProtectTrendResponseBodyTrendList()
                self.trend_list.append(temp_model.from_map(k))
        return self


class DescribeACLProtectTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeACLProtectTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeACLProtectTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressBookRequest(TeaModel):
    def __init__(
        self,
        contain_port: str = None,
        current_page: str = None,
        group_type: str = None,
        lang: str = None,
        page_size: str = None,
        query: str = None,
    ):
        # The port that is included in the address book. This parameter takes effect only when the **GroupType** parameter is set to **port**.
        self.contain_port = contain_port
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The type of the address book. Valid values:
        # 
        # *   **ip**: IP address book
        # *   **domain**: domain address book
        # *   **port**: port address book
        # *   **tag**: Elastic Compute Service (ECS) tag-based address book
        # *   **allCloud**: cloud service address book
        # *   **threat**: threat intelligence address book
        # *   **ipv6**: IPv6 address book
        # >  If you do not specify a type, the domain address books and ECS tag-based address books are queried.
        self.group_type = group_type
        # The language of the content within the request. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The query condition that is used to search for the address book.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_port is not None:
            result['ContainPort'] = self.contain_port
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainPort') is not None:
            self.contain_port = m.get('ContainPort')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class DescribeAddressBookResponseBodyAclsAddresses(TeaModel):
    def __init__(
        self,
        address: str = None,
        note: str = None,
    ):
        self.address = address
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAddressBookResponseBodyAclsTagList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAddressBookResponseBodyAcls(TeaModel):
    def __init__(
        self,
        address_list: List[str] = None,
        address_list_count: int = None,
        addresses: List[DescribeAddressBookResponseBodyAclsAddresses] = None,
        auto_add_tag_ecs: int = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        group_uuid: str = None,
        reference_count: int = None,
        tag_list: List[DescribeAddressBookResponseBodyAclsTagList] = None,
        tag_relation: str = None,
    ):
        # The addresses in the address book.
        self.address_list = address_list
        # The number of addresses in the address book.
        self.address_list_count = address_list_count
        self.addresses = addresses
        # Indicates whether the public IP addresses of ECS instances are automatically added to the address book if the instances match the specified tags. The setting takes effect on both newly purchased ECS instances whose tag settings are complete and ECS instances whose tag settings are modified. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        self.description = description
        # The name of the address book.
        self.group_name = group_name
        # The type of the address book. Valid values:
        # 
        # *   **ip**: IP address book
        # *   **domain**: domain address book
        # *   **port**: port address book
        # *   **tag**: ECS tag-based address book
        # *   **allCloud**: cloud service address book
        # *   **threat**: threat intelligence address book
        self.group_type = group_type
        # The UUID of the address book.
        self.group_uuid = group_uuid
        # The number of times that the address book is referenced.
        self.reference_count = reference_count
        # The details about the ECS tags that can be automatically added to the address book.
        self.tag_list = tag_list
        # The logical relationship among ECS tags. Valid values:
        # 
        # *   **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # *   **or**: The public IP addresses of ECS instances that match any of the specified tags can be added to the address book.
        self.tag_relation = tag_relation

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AddressListCount') is not None:
            self.address_list_count = m.get('AddressListCount')
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = DescribeAddressBookResponseBodyAclsAddresses()
                self.addresses.append(temp_model.from_map(k))
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeAddressBookResponseBodyAclsTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class DescribeAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        acls: List[DescribeAddressBookResponseBodyAcls] = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the address book.
        self.acls = acls
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of the returned address books.
        self.total_count = total_count

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = DescribeAddressBookResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        ip_version: str = None,
        lang: str = None,
        member_uid: int = None,
        new_resource_tag: str = None,
        out_statistic: str = None,
        page_size: str = None,
        region_no: str = None,
        resource_type: str = None,
        search_item: str = None,
        sensitive_status: str = None,
        sg_status: str = None,
        status: str = None,
        type: str = None,
        user_type: str = None,
    ):
        # The page number. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is added to Cloud Firewall.
        self.member_uid = member_uid
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag
        # Whether to query external traffic information.
        self.out_statistic = out_statistic
        # The number of entries per page. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of your Cloud Firewall.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance or a Classic Load Balancer (CLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance or a CLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type
        # The instance ID or IP address of the asset.
        self.search_item = search_item
        # Data leakage detection activation status.
        self.sensitive_status = sensitive_status
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: delivered
        # *   **block**: undelivered
        # *   **unsupport**: unsupported
        # 
        # > If you do not specify this parameter, the assets on which security group policies in all states take effect are queried.
        self.sg_status = sg_status
        # The status of the firewall. Valid values:
        # 
        # *   **open**: The firewall is enabled.
        # *   **opening**: The firewall is being enabled.
        # *   **closed**: The firewall is disabled.
        # *   **closing**: The firewall is being disabled.
        # 
        # > If you do not specify this parameter, the assets that are configured for firewalls in all states are queried.
        self.status = status
        # This parameter is deprecated.
        self.type = type
        # The edition of Cloud Firewall. Valid values:
        # 
        # *   **buy**: a paid edition (default)
        # *   **free**: Free Edition
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag
        if self.out_statistic is not None:
            result['OutStatistic'] = self.out_statistic
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
        if self.sensitive_status is not None:
            result['SensitiveStatus'] = self.sensitive_status
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')
        if m.get('OutStatistic') is not None:
            self.out_statistic = m.get('OutStatistic')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
        if m.get('SensitiveStatus') is not None:
            self.sensitive_status = m.get('SensitiveStatus')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeAssetListResponseBodyAssets(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        bind_instance_id: str = None,
        bind_instance_name: str = None,
        create_time_stamp: str = None,
        internet_address: str = None,
        intranet_address: str = None,
        ip_version: int = None,
        last_7day_out_traffic_bytes: int = None,
        member_uid: int = None,
        name: str = None,
        new_resource_tag: str = None,
        note: str = None,
        protect_status: str = None,
        region_id: str = None,
        region_status: str = None,
        resource_instance_id: str = None,
        resource_type: str = None,
        risk_level: str = None,
        sensitive_data_status: str = None,
        sg_status: str = None,
        sg_status_time: int = None,
        sync_status: str = None,
        type: str = None,
    ):
        # The UID of the Alibaba Cloud account.
        # 
        # >  The value of this parameter indicates the management account to which the member is added.
        self.ali_uid = ali_uid
        # The ID of the cloud resource with which the asset is associated.
        self.bind_instance_id = bind_instance_id
        # The instance name of the asset.
        self.bind_instance_name = bind_instance_name
        # The timestamp when the asset is added to Cloud Firewall.
        self.create_time_stamp = create_time_stamp
        # The public IP address of the server.
        self.internet_address = internet_address
        # The internal IP address of the server.
        self.intranet_address = intranet_address
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # Outbound traffic in the last 7 days.
        self.last_7day_out_traffic_bytes = last_7day_out_traffic_bytes
        # The UID of the member.
        self.member_uid = member_uid
        # The instance name of the asset that is protected by Cloud Firewall.
        self.name = name
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag
        # The remarks of the asset. Valid values:
        # 
        # *   **REGION_NOT_SUPPORT**: The region is not supported.
        # *   **NETWORK_NOT_SUPPORT**: The network is not supported.
        self.note = note
        # The status of the firewall. Valid values:
        # 
        # *   **open**: enabled.
        # *   **opening**: being enabled.
        # *   **closed**: disabled.
        # *   **closing**: being disabled.
        self.protect_status = protect_status
        # The ID of the region in which the asset resides.
        self.region_id = region_id
        # Indicates whether the firewall is supported in the region in which the asset resides. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The instance ID of the asset.
        self.resource_instance_id = resource_instance_id
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type
        # The risk level of the asset. Valid values:
        # 
        # *   **low**: low
        # *   **middle**: medium
        # *   **hight**: high
        # 
        # >  The value of this parameter is returned only when the UserType parameter is set to free.
        self.risk_level = risk_level
        # Data leakage detection enabled status.
        self.sensitive_data_status = sensitive_data_status
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: applied
        # *   **block**: not applied
        # *   **unsupport**: unsupported
        self.sg_status = sg_status
        # The time when the status of the security group was last checked. The value is a UNIX timestamp. Unit: seconds.
        self.sg_status_time = sg_status_time
        # Indicates whether traffic redirection is supported for the asset. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.sync_status = sync_status
        # This parameter is deprecated.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_name is not None:
            result['BindInstanceName'] = self.bind_instance_name
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.last_7day_out_traffic_bytes is not None:
            result['Last7DayOutTrafficBytes'] = self.last_7day_out_traffic_bytes
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag
        if self.note is not None:
            result['Note'] = self.note
        if self.protect_status is not None:
            result['ProtectStatus'] = self.protect_status
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.sensitive_data_status is not None:
            result['SensitiveDataStatus'] = self.sensitive_data_status
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.sg_status_time is not None:
            result['SgStatusTime'] = self.sg_status_time
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceName') is not None:
            self.bind_instance_name = m.get('BindInstanceName')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Last7DayOutTrafficBytes') is not None:
            self.last_7day_out_traffic_bytes = m.get('Last7DayOutTrafficBytes')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ProtectStatus') is not None:
            self.protect_status = m.get('ProtectStatus')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SensitiveDataStatus') is not None:
            self.sensitive_data_status = m.get('SensitiveDataStatus')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('SgStatusTime') is not None:
            self.sg_status_time = m.get('SgStatusTime')
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetListResponseBody(TeaModel):
    def __init__(
        self,
        assets: List[DescribeAssetListResponseBodyAssets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The assets that are protected by Cloud Firewall.
        self.assets = assets
        # The ID of the request.
        self.request_id = request_id
        # The total number of the assets that are protected by Cloud Firewall.
        self.total_count = total_count

    def validate(self):
        if self.assets:
            for k in self.assets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Assets'] = []
        if self.assets is not None:
            for k in self.assets:
                result['Assets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k in m.get('Assets'):
                temp_model = DescribeAssetListResponseBodyAssets()
                self.assets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAssetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAssetListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAssetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetRiskListRequest(TeaModel):
    def __init__(
        self,
        ip_addr_list: List[str] = None,
        ip_version: int = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The IP addresses to query. Separate the IP addresses with commas (,). You can specify up to 20 IP addresses at a time.
        # 
        # > 
        # 
        # *   Example IPv4 address: 47.97.XX.XX.
        # 
        # *   Example IPv6 address: 2001:db8:ffff:ffff:ffff:XXXX:ffff.
        self.ip_addr_list = ip_addr_list
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4** (default): IPv4
        # *   **6**: IPv6
        # 
        # This parameter is required.
        self.ip_version = ip_version
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_addr_list is not None:
            result['IpAddrList'] = self.ip_addr_list
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddrList') is not None:
            self.ip_addr_list = m.get('IpAddrList')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAssetRiskListResponseBodyAssetList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        ip_version: int = None,
        reason: str = None,
        risk_level: str = None,
    ):
        # The IP address of the server.
        self.ip = ip
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The reason for the risk.
        self.reason = reason
        # The risk level. Valid values:
        # 
        # *   **low**\
        # *   **middle**\
        # *   **high**\
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeAssetRiskListResponseBody(TeaModel):
    def __init__(
        self,
        asset_list: List[DescribeAssetRiskListResponseBodyAssetList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the assets.
        self.asset_list = asset_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.asset_list:
            for k in self.asset_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetList'] = []
        if self.asset_list is not None:
            for k in self.asset_list:
                result['AssetList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_list = []
        if m.get('AssetList') is not None:
            for k in m.get('AssetList'):
                temp_model = DescribeAssetRiskListResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAssetRiskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAssetRiskListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAssetRiskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetStatisticRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        # The language of the content within the request. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAssetStatisticResponseBodyResourceSpecStatistic(TeaModel):
    def __init__(
        self,
        ip_num_spec: int = None,
        ip_num_used: int = None,
        sensitive_data_ip_num_spec: int = None,
        sensitive_data_ip_num_used: int = None,
    ):
        # The number of public IP addresses that can be protected.
        self.ip_num_spec = ip_num_spec
        # The number of public IP addresses that are protected.
        self.ip_num_used = ip_num_used
        # The number of public IP addresses that can enable data leakage detection.
        self.sensitive_data_ip_num_spec = sensitive_data_ip_num_spec
        # The number of public IP addresses that enabled data leakage detection.
        self.sensitive_data_ip_num_used = sensitive_data_ip_num_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_num_spec is not None:
            result['IpNumSpec'] = self.ip_num_spec
        if self.ip_num_used is not None:
            result['IpNumUsed'] = self.ip_num_used
        if self.sensitive_data_ip_num_spec is not None:
            result['SensitiveDataIpNumSpec'] = self.sensitive_data_ip_num_spec
        if self.sensitive_data_ip_num_used is not None:
            result['SensitiveDataIpNumUsed'] = self.sensitive_data_ip_num_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpNumSpec') is not None:
            self.ip_num_spec = m.get('IpNumSpec')
        if m.get('IpNumUsed') is not None:
            self.ip_num_used = m.get('IpNumUsed')
        if m.get('SensitiveDataIpNumSpec') is not None:
            self.sensitive_data_ip_num_spec = m.get('SensitiveDataIpNumSpec')
        if m.get('SensitiveDataIpNumUsed') is not None:
            self.sensitive_data_ip_num_used = m.get('SensitiveDataIpNumUsed')
        return self


class DescribeAssetStatisticResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_spec_statistic: DescribeAssetStatisticResponseBodyResourceSpecStatistic = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics on specifications.
        self.resource_spec_statistic = resource_spec_statistic

    def validate(self):
        if self.resource_spec_statistic:
            self.resource_spec_statistic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_spec_statistic is not None:
            result['ResourceSpecStatistic'] = self.resource_spec_statistic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceSpecStatistic') is not None:
            temp_model = DescribeAssetStatisticResponseBodyResourceSpecStatistic()
            self.resource_spec_statistic = temp_model.from_map(m['ResourceSpecStatistic'])
        return self


class DescribeAssetStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAssetStatisticResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAssetStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCfwRiskLevelSummaryRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        # The instance type.
        self.instance_type = instance_type
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The region ID of your Cloud Firewall.
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCfwRiskLevelSummaryResponseBodyRiskList(TeaModel):
    def __init__(
        self,
        level: str = None,
        num: str = None,
        type: str = None,
    ):
        # The risk levels. Valid values:
        # 
        # *   **medium**\
        self.level = level
        # The number of at-risk Elastic Compute Service (ECS) instances.
        self.num = num
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.num is not None:
            result['Num'] = self.num
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCfwRiskLevelSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risk_list: List[DescribeCfwRiskLevelSummaryResponseBodyRiskList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of risks.
        self.risk_list = risk_list

    def validate(self):
        if self.risk_list:
            for k in self.risk_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskList'] = []
        if self.risk_list is not None:
            for k in self.risk_list:
                result['RiskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_list = []
        if m.get('RiskList') is not None:
            for k in m.get('RiskList'):
                temp_model = DescribeCfwRiskLevelSummaryResponseBodyRiskList()
                self.risk_list.append(temp_model.from_map(k))
        return self


class DescribeCfwRiskLevelSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCfwRiskLevelSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCfwRiskLevelSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # >  If you do not specify this parameter, access control policies of all action types are queried.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The number of the page to return.
        # 
        # Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # >  If you do not specify this parameter, access control policies that have descriptions are queried.
        self.description = description
        # The destination address in the access control policy. Fuzzy match is supported. The value of this parameter varies based on the value of the DestinationType parameter.
        # 
        # *   If you set DestinationType to `net`, the value of Destination is a CIDR block. Example: 10.0.3.0/24.
        # *   If you set DestinationType to `domain`, the value of Destination is a domain name. Example: aliyun.
        # *   If you set DestinationType to `group`, the value of Destination is the name of an address book. Example: db_group.
        # *   If you set DestinationType to `location`, the value of Destination is the name of a location. For more information about location codes, see AddControlPolicy. Example: ["BJ11", "ZB"].
        # 
        # >  If you do not specify this parameter, access control policies of all destination address types are queried.
        self.destination = destination
        # The direction of the traffic to which the access control policies apply. Valid values:
        # 
        # *   **in**: inbound.
        # *   **out**: outbound.
        self.direction = direction
        # The IP version of the address in the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the protocol in the access control policy. Valid values:
        # 
        # * **TCP**\
        # * **UDP**\
        # * **ICMP**\
        # * **ANY**: all types of protocols
        # 
        # >  If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto
        # Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**: The access control policy is enabled.
        # *   **false**: The access control policy is disabled.
        self.release = release
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy match is supported. The value of this parameter depends on the value of the SourceType parameter.
        # 
        # *   If SourceType is set to `net`, the value of Source must be a CIDR block. Example: 192.0.XX.XX/24.
        # *   If SourceType is set to `group`, the value of Source must be the name of an address book. Example: db_group. If the db_group address book does not contain addresses, all source addresses are queried.
        # *   If SourceType is set to `location`, the value of Source must be a location. Example: beijing.
        # 
        # >  If you do not specify this parameter, access control policies of all source address types are queried.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeControlPolicyResponseBodyPolicys(TeaModel):
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
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL**\
        # *   **VNC**\
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
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        page_no: str = None,
        page_size: str = None,
        policys: List[DescribeControlPolicyResponseBodyPolicys] = None,
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
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
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
            for k in m.get('Policys'):
                temp_model = DescribeControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefaultIPSConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDefaultIPSConfigResponseBody(TeaModel):
    def __init__(
        self,
        basic_rules: int = None,
        cti_rules: int = None,
        free_trail_status: str = None,
        max_sdl: int = None,
        patch_rules: int = None,
        request_id: str = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether threat intelligence is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.cti_rules = cti_rules
        self.free_trail_status = free_trail_status
        self.max_sdl = max_sdl
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.patch_rules = patch_rules
        # The request ID.
        self.request_id = request_id
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.cti_rules is not None:
            result['CtiRules'] = self.cti_rules
        if self.free_trail_status is not None:
            result['FreeTrailStatus'] = self.free_trail_status
        if self.max_sdl is not None:
            result['MaxSdl'] = self.max_sdl
        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('CtiRules') is not None:
            self.cti_rules = m.get('CtiRules')
        if m.get('FreeTrailStatus') is not None:
            self.free_trail_status = m.get('FreeTrailStatus')
        if m.get('MaxSdl') is not None:
            self.max_sdl = m.get('MaxSdl')
        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeDefaultIPSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDefaultIPSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolveRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ip_version: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The domain name whose DNS record you want to query.
        # 
        # This parameter is required.
        self.domain = domain
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainResolveResponseBodyResolveResult(TeaModel):
    def __init__(
        self,
        ip_addrs: str = None,
        update_time: int = None,
    ):
        # The IP address to which the domain name is resolved. Multiple IP addresses are separated by commas (,).
        self.ip_addrs = ip_addrs
        # The time when the domain name was resolved. The value of this parameter is a timestamp. Unit: seconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_addrs is not None:
            result['IpAddrs'] = self.ip_addrs
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddrs') is not None:
            self.ip_addrs = m.get('IpAddrs')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDomainResolveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resolve_result: DescribeDomainResolveResponseBodyResolveResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details about the DNS record of the domain name.
        self.resolve_result = resolve_result

    def validate(self):
        if self.resolve_result:
            self.resolve_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolve_result is not None:
            result['ResolveResult'] = self.resolve_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolveResult') is not None:
            temp_model = DescribeDomainResolveResponseBodyResolveResult()
            self.resolve_result = temp_model.from_map(m['ResolveResult'])
        return self


class DescribeDomainResolveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainResolveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainResolveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadTaskRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        lang: str = None,
        page_size: str = None,
        task_type: str = None,
    ):
        # The page number.
        self.current_page = current_page
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The type of the task. For more information about task types, see the descriptions in the "DescribeDownloadTaskType" topic. If you do not specify this parameter, all files are queried by default.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeDownloadTaskResponseBodyTasks(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        expire_time: int = None,
        file_size: str = None,
        file_url: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the task expires. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # The size of the file.
        self.file_size = file_size
        # The URL of the OSS file.
        self.file_url = file_url
        # The status of the task. Valid values:
        # 
        # *   **finish**\
        # *   **start**\
        # *   **error**\
        # *   **expire**: The task file is invalid and cannot be downloaded.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeDownloadTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[DescribeDownloadTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeDownloadTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDownloadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDownloadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadTaskTypeRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        lang: str = None,
        page_size: str = None,
        task_type: str = None,
    ):
        # The page number. Pages start from page 1. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeDownloadTaskTypeResponseBodyTaskTypeArray(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        task_type: str = None,
    ):
        # The name of the task type.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeDownloadTaskTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_type_array: List[DescribeDownloadTaskTypeResponseBodyTaskTypeArray] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The task types.
        self.task_type_array = task_type_array
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_type_array:
            for k in self.task_type_array:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskTypeArray'] = []
        if self.task_type_array is not None:
            for k in self.task_type_array:
                result['TaskTypeArray'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_type_array = []
        if m.get('TaskTypeArray') is not None:
            for k in m.get('TaskTypeArray'):
                temp_model = DescribeDownloadTaskTypeResponseBodyTaskTypeArray()
                self.task_type_array.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDownloadTaskTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadTaskTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDownloadTaskTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        member_desc: str = None,
        member_display_name: str = None,
        member_uid: str = None,
        page_size: str = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The remarks of the member. The remarks must be 1 to 256 characters in length.
        self.member_desc = member_desc
        # The name of the member.
        self.member_display_name = member_display_name
        # The UID of the member.
        self.member_uid = member_uid
        # The number of entries per page.
        # 
        # Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        member_desc: str = None,
        member_display_name: str = None,
        member_status: str = None,
        member_uid: int = None,
        modify_time: int = None,
    ):
        # The time when the member was added to Cloud Firewall. The value is a timestamp. Unit: seconds.
        self.create_time = create_time
        # The remarks of the member.
        self.member_desc = member_desc
        # The name of the member.
        self.member_display_name = member_display_name
        # The status of the member. Valid values:
        # 
        # *   **normal**\
        # *   **deleting**\
        self.member_status = member_status
        # The UID of the member.
        self.member_uid = member_uid
        # The time when the member was last modified. The value is a timestamp. Unit: seconds.
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeInstanceMembersResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of the members.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[DescribeInstanceMembersResponseBodyMembers] = None,
        page_info: DescribeInstanceMembersResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the member.
        self.members = members
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeInstanceMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeInstanceMembersResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRiskLevelsRequestInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        internet_ip: List[str] = None,
        intranet_ip: str = None,
        uuid: str = None,
    ):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The public IP addresses of instances.
        self.internet_ip = internet_ip
        # The private IP address of the instance.
        self.intranet_ip = intranet_ip
        # The UUID of the instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeInstanceRiskLevelsRequest(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstanceRiskLevelsRequestInstances] = None,
        lang: str = None,
    ):
        # The information about the instances.
        self.instances = instances
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstanceRiskLevelsRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails(TeaModel):
    def __init__(
        self,
        ip: str = None,
        level: str = None,
        type: str = None,
    ):
        # The IP addresses of servers.
        self.ip = ip
        # The risk levels. Valid values:
        # 
        # *   **medium**\
        self.level = level
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.level is not None:
            result['Level'] = self.level
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeInstanceRiskLevelsResponseBodyInstanceRisks(TeaModel):
    def __init__(
        self,
        details: List[DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails] = None,
        instance_id: str = None,
        level: str = None,
    ):
        # The risk levels of the Elastic Compute Service (ECS) instance.
        self.details = details
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The risk levels. Valid values:
        # 
        # *   **medium**\
        self.level = level

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeInstanceRiskLevelsResponseBody(TeaModel):
    def __init__(
        self,
        instance_risks: List[DescribeInstanceRiskLevelsResponseBodyInstanceRisks] = None,
        request_id: str = None,
    ):
        # The information about the instances.
        self.instance_risks = instance_risks
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_risks:
            for k in self.instance_risks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceRisks'] = []
        if self.instance_risks is not None:
            for k in self.instance_risks:
                result['InstanceRisks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_risks = []
        if m.get('InstanceRisks') is not None:
            for k in m.get('InstanceRisks'):
                temp_model = DescribeInstanceRiskLevelsResponseBodyInstanceRisks()
                self.instance_risks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceRiskLevelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceRiskLevelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceRiskLevelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInternetOpenIpRequest(TeaModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        assets_type: str = None,
        current_page: str = None,
        end_time: str = None,
        lang: str = None,
        page_size: str = None,
        port: str = None,
        public_ip: str = None,
        region_no: str = None,
        risk_level: str = None,
        service_name: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.assets_instance_id = assets_instance_id
        # The instance name.
        self.assets_instance_name = assets_instance_name
        # The asset type of the instance.
        self.assets_type = assets_type
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The port number.
        self.port = port
        # The public IP address of the instance.
        self.public_ip = public_ip
        # The region ID of the instance.
        self.region_no = region_no
        # The risk level. If you leave this parameter empty, all risk levels are queried. Valid values:
        # 
        # *   **3**: high risk
        # *   **2**: medium risk
        # *   **1**: low risk
        # *   **0**: no risk
        self.risk_level = risk_level
        # The application.
        self.service_name = service_name
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInternetOpenIpResponseBodyDataList(TeaModel):
    def __init__(
        self,
        acl_recommend_detail: str = None,
        assets_instance_id: str = None,
        assets_name: str = None,
        assets_type: str = None,
        detail_num: int = None,
        has_acl_recommend: bool = None,
        port_list: List[str] = None,
        public_ip: str = None,
        region_no: str = None,
        risk_level: int = None,
        risk_reason: str = None,
        service_name_list: List[str] = None,
        src_ip_cnt: int = None,
        total_reply_bytes: int = None,
        traffic_percent_1day: str = None,
        traffic_percent_30day: str = None,
        traffic_percent_7day: str = None,
    ):
        # The reason why recommended intelligent policies are unavailable. Valid values:
        # 
        # *   No recommended intelligent policies are available.
        # *   This feature is available only to some users.
        # *   The policy configuration has been modified. No recommended intelligent policies are available.
        # *   The recommended intelligent policies have been configured. No new recommended intelligent policies are available.
        self.acl_recommend_detail = acl_recommend_detail
        # The instance ID.
        self.assets_instance_id = assets_instance_id
        # The instance name.
        self.assets_name = assets_name
        # The asset type of the instance.
        self.assets_type = assets_type
        # The total number of ports.
        self.detail_num = detail_num
        # Specifies whether an access control policy is recommended. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.has_acl_recommend = has_acl_recommend
        # The list of ports.
        self.port_list = port_list
        # The public IP address of the instance.
        self.public_ip = public_ip
        # The region ID of the instance.
        self.region_no = region_no
        # The risk level. Valid values:
        # 
        # *   **3**: high risk
        # *   **2**: medium risk
        # *   **1**: low risk
        # *   **0**: no risk
        self.risk_level = risk_level
        # The reason for the risk.
        self.risk_reason = risk_reason
        # The list of applications.
        self.service_name_list = service_name_list
        # Number of source IPs.
        self.src_ip_cnt = src_ip_cnt
        # Outbound traffic in the last 7 days.
        self.total_reply_bytes = total_reply_bytes
        # The percentage of traffic of a day. Unit: percent (%).
        self.traffic_percent_1day = traffic_percent_1day
        # The percentage of traffic of 30 days. Unit: percent (%).
        self.traffic_percent_30day = traffic_percent_30day
        # The percentage of traffic of seven days. Unit: percent (%).
        self.traffic_percent_7day = traffic_percent_7day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_name is not None:
            result['AssetsName'] = self.assets_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.detail_num is not None:
            result['DetailNum'] = self.detail_num
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.port_list is not None:
            result['PortList'] = self.port_list
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_reason is not None:
            result['RiskReason'] = self.risk_reason
        if self.service_name_list is not None:
            result['ServiceNameList'] = self.service_name_list
        if self.src_ip_cnt is not None:
            result['SrcIpCnt'] = self.src_ip_cnt
        if self.total_reply_bytes is not None:
            result['TotalReplyBytes'] = self.total_reply_bytes
        if self.traffic_percent_1day is not None:
            result['TrafficPercent1Day'] = self.traffic_percent_1day
        if self.traffic_percent_30day is not None:
            result['TrafficPercent30Day'] = self.traffic_percent_30day
        if self.traffic_percent_7day is not None:
            result['TrafficPercent7Day'] = self.traffic_percent_7day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsName') is not None:
            self.assets_name = m.get('AssetsName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('DetailNum') is not None:
            self.detail_num = m.get('DetailNum')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('PortList') is not None:
            self.port_list = m.get('PortList')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskReason') is not None:
            self.risk_reason = m.get('RiskReason')
        if m.get('ServiceNameList') is not None:
            self.service_name_list = m.get('ServiceNameList')
        if m.get('SrcIpCnt') is not None:
            self.src_ip_cnt = m.get('SrcIpCnt')
        if m.get('TotalReplyBytes') is not None:
            self.total_reply_bytes = m.get('TotalReplyBytes')
        if m.get('TrafficPercent1Day') is not None:
            self.traffic_percent_1day = m.get('TrafficPercent1Day')
        if m.get('TrafficPercent30Day') is not None:
            self.traffic_percent_30day = m.get('TrafficPercent30Day')
        if m.get('TrafficPercent7Day') is not None:
            self.traffic_percent_7day = m.get('TrafficPercent7Day')
        return self


class DescribeInternetOpenIpResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInternetOpenIpResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeInternetOpenIpResponseBodyDataList] = None,
        page_info: DescribeInternetOpenIpResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data_list = data_list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeInternetOpenIpResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeInternetOpenIpResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInternetOpenIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInternetOpenIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInternetOpenIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInternetTrafficTrendRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        end_time: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_private_ip: str = None,
        src_public_ip: str = None,
        start_time: str = None,
        traffic_type: str = None,
    ):
        # The direction of the internet traffic.
        # 
        # Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content in the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source code.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The IP address of the access source.
        self.source_ip = source_ip
        # The private IP address of the source.
        self.src_private_ip = src_private_ip
        # The public IP address of the source.
        self.src_public_ip = src_public_ip
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the traffic that is captured. Valid values:
        # 
        # *   **max** (default): peak traffic
        # *   **avg**: average traffic
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip
        if self.src_public_ip is not None:
            result['SrcPublicIP'] = self.src_public_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')
        if m.get('SrcPublicIP') is not None:
            self.src_public_ip = m.get('SrcPublicIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')
        return self


class DescribeInternetTrafficTrendResponseBodyDataList(TeaModel):
    def __init__(
        self,
        in_bps: int = None,
        in_bytes: int = None,
        in_pps: int = None,
        new_conn: int = None,
        out_bps: int = None,
        out_bytes: int = None,
        out_pps: int = None,
        session_count: int = None,
        time: int = None,
        total_bps: int = None,
    ):
        # The inbound network throughput, which indicates the number of bits that are sent inbound per second. Unit: bit/s.
        self.in_bps = in_bps
        # The inbound network throughput, which indicates the total number of bytes that are sent inbound. Unit: bytes.
        self.in_bytes = in_bytes
        # The inbound network throughput, which indicates the number of packets that are sent inbound per second. Unit: packets per second (pps).
        self.in_pps = in_pps
        # The number of new connections.
        self.new_conn = new_conn
        # The outbound network throughput, which indicates the number of bits that are sent outbound per second. Unit: bit/s.
        self.out_bps = out_bps
        # The outbound network throughput, which indicates the total number of bytes that are sent outbound. Unit: bytes.
        self.out_bytes = out_bytes
        # The outbound network throughput, which indicates the number of packets that are sent outbound per second. Unit: pps.
        self.out_pps = out_pps
        # The number of requests.
        self.session_count = session_count
        # The time when traffic is generated. The value is a UNIX timestamp. Unit: seconds.
        # 
        # If processing is not complete at this point in time, -1 is returned for all other fields.
        self.time = time
        # The total outbound and inbound network throughput, which indicates the total number of bits that are sent inbound and outbound per second. Unit: bit/s.
        self.total_bps = total_bps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.new_conn is not None:
            result['NewConn'] = self.new_conn
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.time is not None:
            result['Time'] = self.time
        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')
        return self


class DescribeInternetTrafficTrendResponseBody(TeaModel):
    def __init__(
        self,
        avg_in_bps: int = None,
        avg_out_bps: int = None,
        avg_session: int = None,
        avg_total_bps: int = None,
        data_list: List[DescribeInternetTrafficTrendResponseBodyDataList] = None,
        max_bandwidth_time: int = None,
        max_day_exceed_bytes: int = None,
        max_in_bps: int = None,
        max_out_bps: int = None,
        max_session: int = None,
        max_total_bps: int = None,
        request_id: str = None,
        total_bytes: int = None,
        total_exceed_bytes: int = None,
        total_in_bytes: int = None,
        total_out_bytes: int = None,
        total_session: int = None,
    ):
        # The average inbound network throughput, which indicates the average number of bits that are sent inbound per second. Unit: bit/s.
        self.avg_in_bps = avg_in_bps
        # The average outbound network throughput, which indicates the average number of bits that are sent outbound per second. Unit: bit/s.
        self.avg_out_bps = avg_out_bps
        # The average number of requests.
        self.avg_session = avg_session
        # The total average inbound and outbound network throughput, which indicates the average number of bits that are sent inbound and outbound per second. Unit: bit/s.
        self.avg_total_bps = avg_total_bps
        # The statistics on traffic.
        self.data_list = data_list
        # The timestamp generated when the bandwidth reaches the peak value. The value is a UNIX timestamp. Unit: seconds.
        self.max_bandwidth_time = max_bandwidth_time
        # The maximum volume of excess traffic allowed per day.
        self.max_day_exceed_bytes = max_day_exceed_bytes
        # The maximum inbound network throughput, which indicates the maximum number of bits that are sent inbound per second. Unit: bit/s.
        self.max_in_bps = max_in_bps
        # The maximum outbound network throughput, which indicates the maximum number of bits that are sent outbound per second. Unit: bit/s.
        self.max_out_bps = max_out_bps
        # The number of requests during the peak hour of the network throughout.
        self.max_session = max_session
        # The total maximum inbound and outbound network throughput, which indicates the maximum number of bits that are sent inbound and outbound per second. Unit: bit/s.
        self.max_total_bps = max_total_bps
        # The request ID.
        self.request_id = request_id
        # The total inbound and outbound network throughput, which indicates the total number of bytes that are sent inbound and outbound. Unit: bytes.
        self.total_bytes = total_bytes
        # The total volume of excess traffic.
        self.total_exceed_bytes = total_exceed_bytes
        # The inbound network throughput, which indicates the total number of bytes that are sent inbound. Unit: bytes.
        self.total_in_bytes = total_in_bytes
        # The outbound network throughput, which indicates the total number of bytes that are sent outbound. Unit: bytes.
        self.total_out_bytes = total_out_bytes
        # The total number of requests.
        self.total_session = total_session

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_in_bps is not None:
            result['AvgInBps'] = self.avg_in_bps
        if self.avg_out_bps is not None:
            result['AvgOutBps'] = self.avg_out_bps
        if self.avg_session is not None:
            result['AvgSession'] = self.avg_session
        if self.avg_total_bps is not None:
            result['AvgTotalBps'] = self.avg_total_bps
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.max_bandwidth_time is not None:
            result['MaxBandwidthTime'] = self.max_bandwidth_time
        if self.max_day_exceed_bytes is not None:
            result['MaxDayExceedBytes'] = self.max_day_exceed_bytes
        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps
        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps
        if self.max_session is not None:
            result['MaxSession'] = self.max_session
        if self.max_total_bps is not None:
            result['MaxTotalBps'] = self.max_total_bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_exceed_bytes is not None:
            result['TotalExceedBytes'] = self.total_exceed_bytes
        if self.total_in_bytes is not None:
            result['TotalInBytes'] = self.total_in_bytes
        if self.total_out_bytes is not None:
            result['TotalOutBytes'] = self.total_out_bytes
        if self.total_session is not None:
            result['TotalSession'] = self.total_session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')
        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')
        if m.get('AvgSession') is not None:
            self.avg_session = m.get('AvgSession')
        if m.get('AvgTotalBps') is not None:
            self.avg_total_bps = m.get('AvgTotalBps')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeInternetTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('MaxBandwidthTime') is not None:
            self.max_bandwidth_time = m.get('MaxBandwidthTime')
        if m.get('MaxDayExceedBytes') is not None:
            self.max_day_exceed_bytes = m.get('MaxDayExceedBytes')
        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')
        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')
        if m.get('MaxSession') is not None:
            self.max_session = m.get('MaxSession')
        if m.get('MaxTotalBps') is not None:
            self.max_total_bps = m.get('MaxTotalBps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalExceedBytes') is not None:
            self.total_exceed_bytes = m.get('TotalExceedBytes')
        if m.get('TotalInBytes') is not None:
            self.total_in_bytes = m.get('TotalInBytes')
        if m.get('TotalOutBytes') is not None:
            self.total_out_bytes = m.get('TotalOutBytes')
        if m.get('TotalSession') is not None:
            self.total_session = m.get('TotalSession')
        return self


class DescribeInternetTrafficTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInternetTrafficTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInternetTrafficTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvadeEventListRequest(TeaModel):
    def __init__(
        self,
        assets_ip: str = None,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        current_page: str = None,
        end_time: str = None,
        event_key: str = None,
        event_name: str = None,
        event_uuid: str = None,
        is_ignore: str = None,
        lang: str = None,
        member_uid: int = None,
        page_size: str = None,
        process_status_list: List[int] = None,
        risk_level: List[int] = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The IP address of the affected asset.
        self.assets_ip = assets_ip
        # The ID of the instance.
        self.assets_instance_id = assets_instance_id
        # The name of the instance.
        self.assets_instance_name = assets_instance_name
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you do not specify this parameter, the query ends at the current time.
        self.end_time = end_time
        # The ID of the breach awareness event.
        self.event_key = event_key
        # The name of the breach awareness event.
        self.event_name = event_name
        # The UUID of the breach awareness event.
        self.event_uuid = event_uuid
        # Specifies whether the breach awareness event is ignored. Valid values:
        # 
        # *   **true**: The breach awareness event is ignored.
        # *   **false**: The breach awareness event is not ignored.
        self.is_ignore = is_ignore
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the member.
        self.member_uid = member_uid
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 10.
        self.page_size = page_size
        # The handling status of breach awareness events.
        self.process_status_list = process_status_list
        # The risk levels.
        self.risk_level = risk_level
        # The source IP address of the request.
        self.source_ip = source_ip
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you do not specify this parameter, the query starts from 30 days before the current time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_ip is not None:
            result['AssetsIP'] = self.assets_ip
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_key is not None:
            result['EventKey'] = self.event_key
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status_list is not None:
            result['ProcessStatusList'] = self.process_status_list
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsIP') is not None:
            self.assets_ip = m.get('AssetsIP')
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatusList') is not None:
            self.process_status_list = m.get('ProcessStatusList')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInvadeEventListResponseBodyEventList(TeaModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        assets_type: str = None,
        event_key: str = None,
        event_name: str = None,
        event_src: str = None,
        event_uuid: str = None,
        first_time: int = None,
        is_ignore: bool = None,
        last_time: int = None,
        member_uid: str = None,
        private_ip: str = None,
        process_status: int = None,
        public_ip: str = None,
        public_ip_type: str = None,
        risk_level: int = None,
    ):
        # The ID of the affected asset.
        self.assets_instance_id = assets_instance_id
        # The name of the affected asset.
        self.assets_instance_name = assets_instance_name
        # The type of the affected asset. Valid values:
        # 
        # *   **BastionHostIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.assets_type = assets_type
        # The ID of the breach awareness event.
        self.event_key = event_key
        # The name of the breach awareness event.
        self.event_name = event_name
        # The type of the breach awareness event. Valid values:
        # 
        # *   **IPS**: intrusion prevention event
        # *   **offline**: disconnection event
        self.event_src = event_src
        # The UUID of the breach awareness event.
        self.event_uuid = event_uuid
        # The time when the breach awareness event first occurred. The value is a UNIX timestamp. Unit: seconds.
        self.first_time = first_time
        # Indicates whether the breach awareness event is ignored. Valid values:
        # 
        # *   **true**: The breach awareness event is ignored.
        # *   **false**: The breach awareness event is not ignored.
        self.is_ignore = is_ignore
        # The time when the breach awareness event last occurred. The value is a UNIX timestamp. Unit: seconds.
        self.last_time = last_time
        # The ID of the member.
        self.member_uid = member_uid
        # The private IP address of the affected asset.
        self.private_ip = private_ip
        # The handling status of the breach awareness event. Valid values:
        # 
        # *   **0**: unhandled
        # *   **20**: handled
        self.process_status = process_status
        # The public IP address of the affected asset.
        self.public_ip = public_ip
        # The type of the affected asset. Valid values:
        # 
        # *   **BastionHostIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the EIP of an ECS instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an ENI
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of an SLB instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the HAVIP
        self.public_ip_type = public_ip_type
        # The risk level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.event_key is not None:
            result['EventKey'] = self.event_key
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_src is not None:
            result['EventSrc'] = self.event_src
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.public_ip_type is not None:
            result['PublicIpType'] = self.public_ip_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventSrc') is not None:
            self.event_src = m.get('EventSrc')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('PublicIpType') is not None:
            self.public_ip_type = m.get('PublicIpType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeInvadeEventListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of breach awareness events.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInvadeEventListResponseBody(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeInvadeEventListResponseBodyEventList] = None,
        high_level_percent: int = None,
        low_level_percent: int = None,
        middle_level_percent: int = None,
        page_info: DescribeInvadeEventListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of breach awareness events.
        self.event_list = event_list
        # The percentage of high-risk events.
        self.high_level_percent = high_level_percent
        # The percentage of low-risk events.
        self.low_level_percent = low_level_percent
        # The percentage of medium-risk events.
        self.middle_level_percent = middle_level_percent
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.high_level_percent is not None:
            result['HighLevelPercent'] = self.high_level_percent
        if self.low_level_percent is not None:
            result['LowLevelPercent'] = self.low_level_percent
        if self.middle_level_percent is not None:
            result['MiddleLevelPercent'] = self.middle_level_percent
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeInvadeEventListResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('HighLevelPercent') is not None:
            self.high_level_percent = m.get('HighLevelPercent')
        if m.get('LowLevelPercent') is not None:
            self.low_level_percent = m.get('LowLevelPercent')
        if m.get('MiddleLevelPercent') is not None:
            self.middle_level_percent = m.get('MiddleLevelPercent')
        if m.get('PageInfo') is not None:
            temp_model = DescribeInvadeEventListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInvadeEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvadeEventListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInvadeEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatAclPageStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeNatAclPageStatusResponseBody(TeaModel):
    def __init__(
        self,
        detail: str = None,
        nat_acl_page_enable: bool = None,
        request_id: str = None,
    ):
        # Extra error information.
        self.detail = detail
        # Indicates whether pagination for access control policies for NAT firewalls is supported.
        self.nat_acl_page_enable = nat_acl_page_enable
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.nat_acl_page_enable is not None:
            result['NatAclPageEnable'] = self.nat_acl_page_enable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('NatAclPageEnable') is not None:
            self.nat_acl_page_enable = m.get('NatAclPageEnable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNatAclPageStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNatAclPageStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNatAclPageStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action
        # The UUID of the access control policy.
        self.acl_uuid = acl_uuid
        # The page number.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        self.description = description
        # The destination address in the access control policy. Fuzzy match is supported. The value of this parameter varies based on the value of the DestinationType parameter.
        # 
        # *   If DestinationType is set to `net`, the value of Destination must be a CIDR block. Example: 10.0.3.0/24.
        # *   If DestinationType is set to `domain`, the value of Destination must be a domain name. Example: aliyun.
        # *   If DestinationType is set to `group`, the value of Destination must be the name of an address book. Example: db_group.
        # *   If DestinationType is set to `location`, the value of Destination is a location. For more information about location codes, see [AddControlPolicy](https://help.aliyun.com/document_detail/474128.html). Example: ["BJ11", "ZB"].
        # 
        # > If you do not specify this parameter, all types of destination addresses are queried.
        self.destination = destination
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The type of the protocol in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all types of protocols
        # 
        # > If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto
        # Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.release = release
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy match is supported. The value of this parameter varies based on the value of the SourceType parameter.
        # 
        # *   If SourceType is set to `net`, the value of Source must be a CIDR block. Example: 192.0.XX.XX/24.
        # *   If SourceType is set to `group`, the value of Source must be the name of an address book. Example: db_group. If the db_group address book does not contain addresses, all source addresses are queried.
        # *   If SourceType is set to `location`, the value of Source must be a location. Example: beijing.
        # 
        # > If you do not specify this parameter, all types of source addresses are queried.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeNatFirewallControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
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
        dns_result: str = None,
        dns_result_time: int = None,
        domain_resolve_type: int = None,
        end_time: int = None,
        hit_last_time: int = None,
        hit_times: int = None,
        modify_time: int = None,
        nat_gateway_id: str = None,
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
        spread_cnt: str = None,
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
        # The destination address in the access control policy. The value of this parameter varies based on the value of DestinationType. Valid values:
        # 
        # *   If the value of **DestinationType** is **net**, the value of this parameter is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If the value of **DestinationType** is **domain**, the value of this parameter is a domain name. Example: aliyuncs.com.
        # *   If the value of **DestinationType** is **group**, the value of this parameter is the name of an address book. Example: db_group.
        # *   If the value of **DestinationType** is **location**, the value of this parameter is a location. For more information about location codes, see [AddControlPolicy](https://help.aliyun.com/document_detail/138867.html). Example: ["BJ11", "ZB"].
        self.destination = destination
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more CIDR blocks
        # *   **domain**: an address book that includes one or more domain names
        self.destination_group_type = destination_group_type
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: location
        self.destination_type = destination_type
        # The DNS resolution result.
        self.dns_result = dns_result
        # The time when the Domain Name System (DNS) resolution was performed. The value is a UNIX timestamp. Unit: seconds.
        self.dns_result_time = dns_result_time
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **0**: fully qualified domain name (FQDN)-based resolution
        # *   **1**: DNS-based dynamic resolution
        # *   **2**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The end time must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
        self.end_time = end_time
        # The time when the access control policy was last hit. The value is a UNIX timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time
        # The number of hits for the access control policy.
        self.hit_times = hit_times
        # The time when the access control policy was modified.
        self.modify_time = modify_time
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.order = order
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        self.proto = proto
        # The status of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If RepeatType is set to `Permanent`, `None`, or `Daily`, the value of this parameter is an empty array. Example: [].
        # *   If RepeatType is set to Weekly, this parameter must be specified. Example: [0, 6].
        # 
        # >  If RepeatType is set to Weekly, the fields in the value of this parameter cannot be repeated.
        # 
        # *   If RepeatType is set to `Monthly`, this parameter must be specified. Example: [1, 31].
        # 
        # >  If RepeatType is set to Monthly, the fields in the value of this parameter cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The end time must be on the hour or on the half hour, and at least 30 minutes later than the start time.
        # 
        # >  If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The start time must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If RepeatType is set to Permanent or None, this parameter is left empty. If RepeatType is set to Daily, Weekly, or Monthly, this parameter must be specified.
        self.repeat_start_time = repeat_start_time
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Valid values:
        # 
        # *   If the value of **SourceType** is `net`, the value of this parameter is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If the value of **SourceType** is `group`, the value of this parameter is the name of an address book. Example: db_group.
        # *   If the value of **SourceType** is `location`, the value of this parameter is a location. For more information about location codes, see [AddControlPolicy](https://help.aliyun.com/document_detail/138867.html). Example: ["BJ11", "ZB"].
        self.source = source
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the access control policy. The value is fixed as **ip**. The value indicates an address book that includes one or more CIDR blocks.
        self.source_group_type = source_group_type
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        self.source_type = source_type
        # The total quota consumed by the returned access control policies, which is the sum of the quota consumed by each policy. The quota that is consumed by an access control policy is calculated by using the following formula: Quota that is consumed by an access control policy = Number of source addresses (number of CIDR blocks or regions) × Number of destination addresses (number of CIDR blocks, regions, or domain names) × Number of port ranges × Number of applications.
        self.spread_cnt = spread_cnt
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The start time must be on the hour or on the half hour, and at least 30 minutes earlier than the end time.
        # 
        # >  If RepeatType is set to Permanent, this parameter is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, this parameter must be specified.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
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
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
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
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
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


class DescribeNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policys: List[DescribeNatFirewallControlPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the access control policies.
        self.policys = policys
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policys:
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeNatFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNatFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNatFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatFirewallListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: int = None,
        nat_gateway_id: str = None,
        page_no: int = None,
        page_size: int = None,
        proxy_id: str = None,
        proxy_name: str = None,
        region_no: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The language of the content within the response. Valid values:
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # Default value: **10**.**** Maximum value: **50**.
        self.page_size = page_size
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The name of the NAT firewall. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). The name cannot start with an underscore.
        self.proxy_name = proxy_name
        # The region ID of the virtual private cloud (VPC).
        self.region_no = region_no
        # The status of the NAT firewall. Valid values:
        # 
        # *   configuring
        # *   deleting
        # *   normal
        # *   abnormal
        # *   opening
        # *   closing
        # *   closed
        self.status = status
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the default route.
        self.destination_cidr = destination_cidr
        # The next hop of the original NAT gateway.
        self.next_hop_id = next_hop_id
        # The network type of the next hop. The value is fixed as NatGateway.
        self.next_hop_type = next_hop_type
        # The route table to which the default route of the NAT gateway belongs.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeNatFirewallListResponseBodyNatFirewallList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        error_detail: str = None,
        member_uid: int = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        nat_route_entry_list: List[DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList] = None,
        proxy_id: str = None,
        proxy_name: str = None,
        proxy_status: str = None,
        region_id: str = None,
        strict_mode: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The UID of the Alibaba Cloud account.
        # 
        # >  The value of this parameter indicates the management account to which the member is added.
        self.ali_uid = ali_uid
        # The cause of the error.
        self.error_detail = error_detail
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The name of the NAT gateway.
        self.nat_gateway_name = nat_gateway_name
        # The default route entries of the NAT gateway.
        self.nat_route_entry_list = nat_route_entry_list
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The name of the NAT firewall.
        self.proxy_name = proxy_name
        # The status of the NAT firewall. Valid values:
        # 
        # *   configuring
        # *   deleting
        # *   normal
        # *   abnormal
        # *   opening
        # *   closing
        # *   closed
        self.proxy_status = proxy_status
        # The region ID of your Cloud Firewall.
        # 
        # >  For more information about the supported regions of Cloud Firewall, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_id = region_id
        # Indicates whether the strict mode is enabled. Valid values: 1, which specifies yes, and 0, which specifies no.
        self.strict_mode = strict_mode
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.nat_route_entry_list:
            for k in self.nat_route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name
        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k.to_map() if k else None)
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name
        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')
        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k in m.get('NatRouteEntryList'):
                temp_model = DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k))
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')
        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeNatFirewallListResponseBody(TeaModel):
    def __init__(
        self,
        nat_firewall_list: List[DescribeNatFirewallListResponseBodyNatFirewallList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The NAT firewalls.
        self.nat_firewall_list = nat_firewall_list
        # The request ID.
        self.request_id = request_id
        # The total number of NAT firewalls.
        self.total_count = total_count

    def validate(self):
        if self.nat_firewall_list:
            for k in self.nat_firewall_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NatFirewallList'] = []
        if self.nat_firewall_list is not None:
            for k in self.nat_firewall_list:
                result['NatFirewallList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_firewall_list = []
        if m.get('NatFirewallList') is not None:
            for k in m.get('NatFirewallList'):
                temp_model = DescribeNatFirewallListResponseBodyNatFirewallList()
                self.nat_firewall_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNatFirewallListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNatFirewallListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNatFirewallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatFirewallPolicyPriorUsedRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
    ):
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The IP version supported by the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        self.ip_version = ip_version
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DescribeNatFirewallPolicyPriorUsedResponseBody(TeaModel):
    def __init__(
        self,
        end: int = None,
        request_id: str = None,
        start: int = None,
    ):
        # The lowest priority for the access control policy.
        self.end = end
        # The request ID.
        self.request_id = request_id
        # The highest priority for the access control policy.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeNatFirewallPolicyPriorUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNatFirewallPolicyPriorUsedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNatFirewallPolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutgoingDestinationIPRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        category_id: str = None,
        current_page: str = None,
        dst_ip: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        port: str = None,
        private_ip: str = None,
        public_ip: str = None,
        sort: str = None,
        start_time: str = None,
        tag_id_new: str = None,
    ):
        # The application type in the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # 
        # >  The value of this parameter depends on the value of Proto. If you set Proto to TCP, you can set ApplicationNameList to any valid value. If you specify both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name = application_name
        # The ID of the service to which the destination IP address belongs. This parameter is left empty by default. Valid values:
        # 
        # *   **All**: all services
        # *   **RiskDomain**: risky domain names
        # *   **RiskIP**: risky IP addresses
        # *   **AliYun**: Alibaba Cloud services
        # *   **NotAliYun**: third-party services
        self.category_id = category_id
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page
        # The destination IP address in the outbound connection that is initiated to access a domain name.
        self.dst_ip = dst_ip
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The method that you want to use to sort the query results. Valid values:
        # 
        # *   **asc**\
        # *   **desc** (default)
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 10.
        self.page_size = page_size
        # The port number.
        self.port = port
        # The private IP address of the ECS instance that initiates the outbound connection.
        self.private_ip = private_ip
        # The public IP address of the Elastic Compute Service (ECS) instance that initiates the outbound connection.
        self.public_ip = public_ip
        # The field based on which you want to sort the query results. Valid values:
        # 
        # *   **SessionCount** (default): the number of requests.
        # *   **TotalBytes**: the total volume of traffic.
        self.sort = sort
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tag. Valid values:
        # 
        # *   **AliYun**: Alibaba Cloud service
        # *   **RiskDomain**: risky domain name
        # *   **RiskIP**: risky IP address
        # *   **TrustedDomain**: trusted website
        # *   **AliPay**: Alipay
        # *   **DingDing**: DingTalk
        # *   **WeChat**: WeChat
        # *   **QQ**: Tencent QQ
        # *   **SecurityService**: security service
        # *   **Microsoft**: Microsoft
        # *   **Amazon**: Amazon Web Services (AWS)
        # *   **Pan**: cloud disk
        # *   **Map**: map
        # *   **Code**: code hosting
        # *   **SystemService**: system service
        # *   **Taobao**: Taobao
        # *   **Google**: Google
        # *   **ThirdPartyService**: third-party service
        # *   **FirstFlow**: the first time
        # *   **Downloader**: malicious download
        # *   **Alexa Top1M**: popular website
        # *   **Miner**: mining pool
        # *   **Intelligence**: threat intelligence
        # *   **DDoS**: DDoS trojan
        # *   **Ransomware**: ransomware
        # *   **Spyware**: spyware
        # *   **Rogue**: rogue software
        # *   **Botnet**: botnet
        # *   **Suspicious**: suspicious website
        # *   **C\\&C**: command and control (C\\&C)
        # *   **Gang**: gang
        # *   **CVE**: Common Vulnerabilities and Exposures (CVE)
        # *   **Backdoor**: webshell
        # *   **Phishing**: phishing website
        # *   **APT**: advanced persistent threat (APT) attack
        # *   **Supply Chain Attack**: supply chain attack
        # *   **Malicious software**: malware
        self.tag_id_new = tag_id_new

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_id_new is not None:
            result['TagIdNew'] = self.tag_id_new
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList(TeaModel):
    def __init__(
        self,
        address_group_name: str = None,
        address_group_uuid: str = None,
    ):
        # The name of the address book.
        self.address_group_name = address_group_name
        # The UUID of the address book.
        self.address_group_uuid = address_group_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_group_name is not None:
            result['AddressGroupName'] = self.address_group_name
        if self.address_group_uuid is not None:
            result['AddressGroupUUID'] = self.address_group_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressGroupName') is not None:
            self.address_group_name = m.get('AddressGroupName')
        if m.get('AddressGroupUUID') is not None:
            self.address_group_uuid = m.get('AddressGroupUUID')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        port: int = None,
    ):
        # The application type used in the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # 
        # >  The value of this parameter depends on the value of the Proto parameter. If you set Proto to TCP, you can set ApplicationNameList to any valid value. If you configure both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name = application_name
        # The application port.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListTagList(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.class_id = class_id
        # The risk level. Valid values:
        # 
        # *   **1**: low.
        # *   **2**: medium.
        # *   **3**: high.
        self.risk_level = risk_level
        # The description of the tag.
        self.tag_describe = tag_describe
        # The ID of the tag.
        self.tag_id = tag_id
        # The name of the tag.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPList(TeaModel):
    def __init__(
        self,
        acl_coverage: str = None,
        acl_recommend_detail: str = None,
        acl_status: str = None,
        address_group_list: List[DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList] = None,
        application_port_list: List[DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList] = None,
        asset_count: int = None,
        category_class_id: str = None,
        category_id: str = None,
        category_name: str = None,
        dst_ip: str = None,
        group_name: str = None,
        has_acl: str = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        is_mark_normal: bool = None,
        location_name: str = None,
        out_bytes: int = None,
        private_asset_count: int = None,
        rule_id: str = None,
        rule_name: str = None,
        security_reason: str = None,
        security_suggest: str = None,
        session_count: int = None,
        tag_list: List[DescribeOutgoingDestinationIPResponseBodyDstIPListTagList] = None,
        total_bytes: str = None,
    ):
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **Uncovered**: no
        # *   **FullCoverage**: yes
        self.acl_coverage = acl_coverage
        # The suggestion to configure an access control policy.
        self.acl_recommend_detail = acl_recommend_detail
        # The status of the access control policy. Valid values:
        # 
        # *   **normal**: healthy
        # *   **Abnormal**: unhealthy
        self.acl_status = acl_status
        # The information about the address book.
        self.address_group_list = address_group_list
        # The application ports.
        # 
        # >  Only the first 100 application ports are displayed.
        self.application_port_list = application_port_list
        # The outbound asset count.
        self.asset_count = asset_count
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.category_class_id = category_class_id
        # The ID of the service type. Valid values:
        # 
        # *   **Aliyun**: Alibaba Cloud services
        # *   **NotAliyun**: third-party services
        self.category_id = category_id
        # The type of the service to which the destination IP address belongs. Valid values:
        # 
        # *   **Alibaba Cloud services**\
        # *   **Third-party services**\
        self.category_name = category_name
        # The destination IP addresses in outbound connections.
        self.dst_ip = dst_ip
        # The name of the group to which the access control policy belongs.
        self.group_name = group_name
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.has_acl = has_acl
        # Indicates whether an access control policy is recommended. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.has_acl_recommend = has_acl_recommend
        # The inbound traffic. Unit: bytes.
        self.in_bytes = in_bytes
        # Indicates whether the destination IP address is added to a whitelist. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_mark_normal = is_mark_normal
        # Location name.
        self.location_name = location_name
        # The outbound traffic. Unit: bytes.
        self.out_bytes = out_bytes
        # The outbound private asset count.
        self.private_asset_count = private_asset_count
        # The UUID of the access control policy.
        self.rule_id = rule_id
        # The name of the access control policy.
        self.rule_name = rule_name
        # The reason why the domain name is secure.
        self.security_reason = security_reason
        # The suggestion to handle the traffic of the domain name in outbound connections. Valid values:
        # 
        # *   **pass**: allow
        # *   **alert**: deny
        # *   **drop**: monitor
        self.security_suggest = security_suggest
        # The number of requests.
        self.session_count = session_count
        # The tags.
        self.tag_list = tag_list
        # The total traffic. Unit: bytes
        self.total_bytes = total_bytes

    def validate(self):
        if self.address_group_list:
            for k in self.address_group_list:
                if k:
                    k.validate()
        if self.application_port_list:
            for k in self.application_port_list:
                if k:
                    k.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        result['AddressGroupList'] = []
        if self.address_group_list is not None:
            for k in self.address_group_list:
                result['AddressGroupList'].append(k.to_map() if k else None)
        result['ApplicationPortList'] = []
        if self.application_port_list is not None:
            for k in self.application_port_list:
                result['ApplicationPortList'].append(k.to_map() if k else None)
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count
        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_acl is not None:
            result['HasAcl'] = self.has_acl
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.private_asset_count is not None:
            result['PrivateAssetCount'] = self.private_asset_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.security_reason is not None:
            result['SecurityReason'] = self.security_reason
        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        self.address_group_list = []
        if m.get('AddressGroupList') is not None:
            for k in m.get('AddressGroupList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList()
                self.address_group_list.append(temp_model.from_map(k))
        self.application_port_list = []
        if m.get('ApplicationPortList') is not None:
            for k in m.get('ApplicationPortList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList()
                self.application_port_list.append(temp_model.from_map(k))
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')
        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasAcl') is not None:
            self.has_acl = m.get('HasAcl')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('PrivateAssetCount') is not None:
            self.private_asset_count = m.get('PrivateAssetCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecurityReason') is not None:
            self.security_reason = m.get('SecurityReason')
        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        return self


class DescribeOutgoingDestinationIPResponseBody(TeaModel):
    def __init__(
        self,
        dst_iplist: List[DescribeOutgoingDestinationIPResponseBodyDstIPList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The IP addresses in outbound connections.
        self.dst_iplist = dst_iplist
        # The ID of the request.
        self.request_id = request_id
        # The total number of destination IP addresses in outbound connections.
        self.total_count = total_count

    def validate(self):
        if self.dst_iplist:
            for k in self.dst_iplist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DstIPList'] = []
        if self.dst_iplist is not None:
            for k in self.dst_iplist:
                result['DstIPList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dst_iplist = []
        if m.get('DstIPList') is not None:
            for k in m.get('DstIPList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPList()
                self.dst_iplist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOutgoingDestinationIPResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOutgoingDestinationIPResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOutgoingDestinationIPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutgoingDomainRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        current_page: str = None,
        domain: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        public_ip: str = None,
        sort: str = None,
        start_time: str = None,
        tag_id_new: str = None,
    ):
        # The type of the service. This parameter is empty by default. Valid values:
        # 
        # *   **All**: all services
        # *   **RiskDomain**: risky domain names
        # *   **RiskIP**: risky IP addresses
        # *   **AliYun**: Alibaba Cloud services
        # *   **NotAliYun**: third-party services
        self.category_id = category_id
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page
        # The domain name in outbound connections.
        self.domain = domain
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the request. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The method that is used to sort the results. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc** (default): the descending order.
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 100.
        self.page_size = page_size
        # The public IP address of the Elastic Compute Service (ECS) instance that initiates outbound connections.
        self.public_ip = public_ip
        # The field based on which you want to sort the query results. Valid values:
        # 
        # *   **SessionCount** (default): the number of requests.
        # *   **TotalBytes**: the total volume of traffic.
        self.sort = sort
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tag. Valid values:
        # 
        # *   **AliYun**: Alibaba Cloud service
        # *   **RiskDomain**: risky domain name
        # *   **RiskIP**: risky IP address
        # *   **TrustedDomain**: trusted website
        # *   **AliPay**: Alipay
        # *   **DingDing**: DingTalk
        # *   **WeChat**: WeChat
        # *   **QQ**: Tencent QQ
        # *   **SecurityService**: security service
        # *   **Microsoft**: Microsoft
        # *   **Amazon**: Amazon Web Services (AWS)
        # *   **Pan**: cloud disk
        # *   **Map**: map
        # *   **Code**: code hosting
        # *   **SystemService**: system service
        # *   **Taobao**: Taobao
        # *   **Google**: Google
        # *   **ThirdPartyService**: third-party service
        # *   **FirstFlow**: the first time when an outbound connection is initiated
        # *   **Downloader**: malicious download
        # *   **Alexa Top1M**: popular website
        # *   **Miner**: mining pool
        # *   **Intelligence**: threat intelligence
        # *   **DDoS**: DDoS trojan
        # *   **Ransomware**: ransomware
        # *   **Spyware**: spyware
        # *   **Rogue**: rogue software
        # *   **Botnet**: botnet
        # *   **Suspicious**: suspicious website
        # *   **C\\&C**: command and control (C\\&C)
        # *   **Gang**: gang
        # *   **CVE**: Common Vulnerabilities and Exposures (CVE)
        # *   **Backdoor**: webshell
        # *   **Phishing**: phishing website
        # *   **APT**: advanced persistent threat (APT) attack
        # *   **Supply Chain Attack**: supply chain attack
        # *   **Malicious software**: malware
        self.tag_id_new = tag_id_new

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_id_new is not None:
            result['TagIdNew'] = self.tag_id_new
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')
        return self


class DescribeOutgoingDomainResponseBodyDomainListTagList(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.class_id = class_id
        # The risk level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.risk_level = risk_level
        # The description of the tag.
        self.tag_describe = tag_describe
        # The ID of the tag.
        self.tag_id = tag_id
        # The name of the tag.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeOutgoingDomainResponseBodyDomainList(TeaModel):
    def __init__(
        self,
        acl_coverage: str = None,
        acl_recommend_detail: str = None,
        acl_status: str = None,
        address_group_name: str = None,
        address_group_uuid: str = None,
        application_name_list: List[str] = None,
        asset_count: int = None,
        business: str = None,
        category_class_id: str = None,
        category_id: str = None,
        category_name: str = None,
        domain: str = None,
        group_name: str = None,
        has_acl: str = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        is_mark_normal: bool = None,
        organization: str = None,
        out_bytes: int = None,
        private_asset_count: int = None,
        rule_id: str = None,
        rule_name: str = None,
        security_reason: str = None,
        security_suggest: str = None,
        session_count: int = None,
        tag_list: List[DescribeOutgoingDomainResponseBodyDomainListTagList] = None,
        total_bytes: str = None,
    ):
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **Uncovered**: no
        # *   **FullCoverage**: yes
        self.acl_coverage = acl_coverage
        # The suggestion in an access control policy.
        self.acl_recommend_detail = acl_recommend_detail
        # The state of the access control policy. Valid values:
        # 
        # *   **normal**: healthy
        # *   **abnormal**: unhealthy
        self.acl_status = acl_status
        # The name of the address book.
        self.address_group_name = address_group_name
        # The UUID of the address book.
        self.address_group_uuid = address_group_uuid
        # The application names.
        self.application_name_list = application_name_list
        # The outbound asset count.
        self.asset_count = asset_count
        # The website service.
        self.business = business
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.category_class_id = category_class_id
        # The type ID of the service to which the domain name belongs. Valid values:
        # 
        # *   **Aliyun**: Alibaba Cloud services
        # *   **NotAliyun**: third-party services
        self.category_id = category_id
        # The type of the service to which the domain name belongs. Valid values:
        # 
        # *   **Alibaba Cloud services**\
        # *   **Third-party services**\
        self.category_name = category_name
        # The domain name in outbound connections.
        self.domain = domain
        # The name of the group to which the access control policy belongs.
        self.group_name = group_name
        # Indicates whether an `access control policy` is configured for the domain name. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl = has_acl
        # Indicates whether an access control policy is recommended. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl_recommend = has_acl_recommend
        # The volume of inbound traffic.
        self.in_bytes = in_bytes
        # Indicates whether the domain name is marked as normal. Valid values:
        # 
        # *   **true**: normal
        # *   **false**: abnormal
        self.is_mark_normal = is_mark_normal
        # The name of the organization.
        self.organization = organization
        # The volume of outbound traffic.
        self.out_bytes = out_bytes
        # The outbound private asset count.
        self.private_asset_count = private_asset_count
        # The ID of the access control policy.
        self.rule_id = rule_id
        # The name of the access control policy.
        self.rule_name = rule_name
        # The reason why the domain name is secure.
        self.security_reason = security_reason
        # The suggestion to handle the traffic of the domain name in outbound connections. Valid values:
        # 
        # *   **pass**: allow
        # *   **alert**: monitor
        # *   **drop**: deny
        self.security_suggest = security_suggest
        # The number of requests.
        self.session_count = session_count
        # An array that consists of tags.
        self.tag_list = tag_list
        # The total volume of traffic. Unit: bytes.
        self.total_bytes = total_bytes

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_group_name is not None:
            result['AddressGroupName'] = self.address_group_name
        if self.address_group_uuid is not None:
            result['AddressGroupUUID'] = self.address_group_uuid
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count
        if self.business is not None:
            result['Business'] = self.business
        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_acl is not None:
            result['HasAcl'] = self.has_acl
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.private_asset_count is not None:
            result['PrivateAssetCount'] = self.private_asset_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.security_reason is not None:
            result['SecurityReason'] = self.security_reason
        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressGroupName') is not None:
            self.address_group_name = m.get('AddressGroupName')
        if m.get('AddressGroupUUID') is not None:
            self.address_group_uuid = m.get('AddressGroupUUID')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasAcl') is not None:
            self.has_acl = m.get('HasAcl')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('PrivateAssetCount') is not None:
            self.private_asset_count = m.get('PrivateAssetCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecurityReason') is not None:
            self.security_reason = m.get('SecurityReason')
        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeOutgoingDomainResponseBodyDomainListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        return self


class DescribeOutgoingDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_list: List[DescribeOutgoingDomainResponseBodyDomainList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names in outbound connections.
        self.domain_list = domain_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of the domain names in outbound connections.
        self.total_count = total_count

    def validate(self):
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainList'] = []
        if self.domain_list is not None:
            for k in self.domain_list:
                result['DomainList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_list = []
        if m.get('DomainList') is not None:
            for k in m.get('DomainList'):
                temp_model = DescribeOutgoingDomainResponseBodyDomainList()
                self.domain_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOutgoingDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOutgoingDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOutgoingDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyAdvancedConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribePolicyAdvancedConfigResponseBody(TeaModel):
    def __init__(
        self,
        internet_switch: str = None,
        request_id: str = None,
    ):
        # Indicates whether the strict mode is enabled for the access control policy. Valid values:
        # 
        # *   **on**: The strict mode is enabled.
        # *   **off**: The strict mode is disabled.
        self.internet_switch = internet_switch
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyAdvancedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyAdvancedConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyPriorUsedRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound.
        # *   **out**: outbound.
        # 
        # This parameter is required.
        self.direction = direction
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4** (default): IPv4.
        # *   **6**: IPv6.
        self.ip_version = ip_version
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribePolicyPriorUsedResponseBody(TeaModel):
    def __init__(
        self,
        end: int = None,
        request_id: str = None,
        start: int = None,
    ):
        # The lowest priority of existing access control policies.
        # 
        # >  The value -1 indicates the lowest priority.
        self.end = end
        # The request ID.
        self.request_id = request_id
        # The highest priority of existing access control policies.
        # 
        # >  The value 0 indicates the highest priority.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribePolicyPriorUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyPriorUsedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePostpayTrafficDetailRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: int = None,
        region_no: str = None,
        search_item: str = None,
        start_time: str = None,
        traffic_type: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The end of the time range to query. Specify a value in the YYYYMMDD format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The field based on which you want to sort the query results. Valid values:
        # 
        # *   **resourceId**\
        # *   **trafficDay**\
        self.order = order
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The region ID.
        self.region_no = region_no
        # The instance ID or the IP address of the asset.
        self.search_item = search_item
        # The beginning of the time range to query. Specify a value in the YYYYMMDD format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The traffic type. This parameter is required. Valid values:
        # 
        # *   **EIP_TRAFFIC**: traffic for the Internet firewall.
        # *   **NatGateway_TRAFFIC**: traffic for NAT firewalls.
        # *   **VPC_TRAFFIC**: traffic for virtual private cloud (VPC) firewalls.
        # 
        # This parameter is required.
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')
        return self


class DescribePostpayTrafficDetailResponseBodyTrafficList(TeaModel):
    def __init__(
        self,
        in_bytes: int = None,
        instance_id: str = None,
        instance_type: str = None,
        out_bytes: int = None,
        protection_duration: int = None,
        region_no: str = None,
        resource_id: str = None,
        total_bytes: int = None,
        traffic_day: str = None,
        traffic_type: str = None,
    ):
        # The inbound network throughput, which indicates the total number of bytes that are received Unit: bytes.
        self.in_bytes = in_bytes
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The asset type. This value takes effect only for the Internet firewall.
        self.instance_type = instance_type
        # The outbound network throughput, which indicates the total number of bytes that are sent. Unit: bytes.
        self.out_bytes = out_bytes
        # Protection duration. Unit: hours.
        self.protection_duration = protection_duration
        # The region ID.
        self.region_no = region_no
        # The resource ID. The resource ID for the Internet firewall is the public IP address that is protected the Internet firewall, and the resource ID for a NAT firewall is the instance ID of the NAT firewall.
        self.resource_id = resource_id
        # The total inbound and outbound network throughput, which indicates the total number of bytes that are received and sent. Unit: bytes.
        self.total_bytes = total_bytes
        # The date on which the statistics are collected.
        self.traffic_day = traffic_day
        # The traffic type. Valid values:
        # 
        # *   **EIP_TRAFFIC**: traffic for the Internet firewall
        # *   **NatGateway_TRAFFIC**: traffic for NAT firewalls
        # *   **VPC_TRAFFIC**: traffic for VPC firewalls
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.protection_duration is not None:
            result['ProtectionDuration'] = self.protection_duration
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.traffic_day is not None:
            result['TrafficDay'] = self.traffic_day
        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('ProtectionDuration') is not None:
            self.protection_duration = m.get('ProtectionDuration')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TrafficDay') is not None:
            self.traffic_day = m.get('TrafficDay')
        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')
        return self


class DescribePostpayTrafficDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        traffic_list: List[DescribePostpayTrafficDetailResponseBodyTrafficList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The statistics on traffic.
        self.traffic_list = traffic_list

    def validate(self):
        if self.traffic_list:
            for k in self.traffic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrafficList'] = []
        if self.traffic_list is not None:
            for k in self.traffic_list:
                result['TrafficList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.traffic_list = []
        if m.get('TrafficList') is not None:
            for k in m.get('TrafficList'):
                temp_model = DescribePostpayTrafficDetailResponseBodyTrafficList()
                self.traffic_list.append(temp_model.from_map(k))
        return self


class DescribePostpayTrafficDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePostpayTrafficDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePostpayTrafficDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePostpayTrafficTotalRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribePostpayTrafficTotalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_assets: int = None,
        total_bill_traffic: int = None,
        total_internet_assets: int = None,
        total_internet_traffic: int = None,
        total_nat_assets: int = None,
        total_nat_traffic: int = None,
        total_traffic: int = None,
        total_vpc_assets: int = None,
        total_vpc_traffic: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of assets protected all types of firewalls.
        self.total_assets = total_assets
        # The volume of burstable protected traffic for which fees are generated. Unit: bytes.
        self.total_bill_traffic = total_bill_traffic
        # The total number of assets protected by the Internet firewall.
        self.total_internet_assets = total_internet_assets
        # The total traffic for the Internet firewall. If you use Cloud Firewall that uses the subscription billing method, this parameter indicates the total volume of burstable protected traffic on the Internet boundary. Unit: bytes.
        self.total_internet_traffic = total_internet_traffic
        # The total number of assets protected by NAT firewalls.
        self.total_nat_assets = total_nat_assets
        # The total traffic for NAT firewalls. If you use Cloud Firewall that uses the subscription billing method, this parameter indicates the total volume of burstable protected traffic on the NAT boundary. Unit: bytes.
        self.total_nat_traffic = total_nat_traffic
        # The total volume of traffic. If you use Cloud Firewall that uses the subscription billing method, this parameter indicates the total volume of burstable protected traffic. Unit: bytes.
        self.total_traffic = total_traffic
        # The total number of assets protected by virtual private cloud (VPC) firewalls.
        self.total_vpc_assets = total_vpc_assets
        # The total traffic for VPC firewalls. If you use Cloud Firewall that uses the subscription billing method, this parameter indicates the total volume of burstable protected traffic on the VPC boundary. Unit: bytes.
        self.total_vpc_traffic = total_vpc_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_assets is not None:
            result['TotalAssets'] = self.total_assets
        if self.total_bill_traffic is not None:
            result['TotalBillTraffic'] = self.total_bill_traffic
        if self.total_internet_assets is not None:
            result['TotalInternetAssets'] = self.total_internet_assets
        if self.total_internet_traffic is not None:
            result['TotalInternetTraffic'] = self.total_internet_traffic
        if self.total_nat_assets is not None:
            result['TotalNatAssets'] = self.total_nat_assets
        if self.total_nat_traffic is not None:
            result['TotalNatTraffic'] = self.total_nat_traffic
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.total_vpc_assets is not None:
            result['TotalVpcAssets'] = self.total_vpc_assets
        if self.total_vpc_traffic is not None:
            result['TotalVpcTraffic'] = self.total_vpc_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalAssets') is not None:
            self.total_assets = m.get('TotalAssets')
        if m.get('TotalBillTraffic') is not None:
            self.total_bill_traffic = m.get('TotalBillTraffic')
        if m.get('TotalInternetAssets') is not None:
            self.total_internet_assets = m.get('TotalInternetAssets')
        if m.get('TotalInternetTraffic') is not None:
            self.total_internet_traffic = m.get('TotalInternetTraffic')
        if m.get('TotalNatAssets') is not None:
            self.total_nat_assets = m.get('TotalNatAssets')
        if m.get('TotalNatTraffic') is not None:
            self.total_nat_traffic = m.get('TotalNatTraffic')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TotalVpcAssets') is not None:
            self.total_vpc_assets = m.get('TotalVpcAssets')
        if m.get('TotalVpcTraffic') is not None:
            self.total_vpc_traffic = m.get('TotalVpcTraffic')
        return self


class DescribePostpayTrafficTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePostpayTrafficTotalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePostpayTrafficTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrefixListsRequest(TeaModel):
    def __init__(
        self,
        region_no: str = None,
        source_ip: str = None,
    ):
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_no = region_no
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribePrefixListsResponseBodyPrefixList(TeaModel):
    def __init__(
        self,
        address_family: str = None,
        association_count: int = None,
        creation_time: str = None,
        description: str = None,
        max_entries: int = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
    ):
        # The IP address family of the prefix list. Valid values:
        # 
        # *   IPv4
        # *   IPv6
        self.address_family = address_family
        # The number of associated resources.
        self.association_count = association_count
        # The creation time.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The maximum number of entries in the prefix list.
        self.max_entries = max_entries
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list.
        self.prefix_list_name = prefix_list_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family
        if self.association_count is not None:
            result['AssociationCount'] = self.association_count
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id
        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')
        if m.get('AssociationCount') is not None:
            self.association_count = m.get('AssociationCount')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')
        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')
        return self


class DescribePrefixListsResponseBody(TeaModel):
    def __init__(
        self,
        prefix_list: List[DescribePrefixListsResponseBodyPrefixList] = None,
        request_id: str = None,
    ):
        # Details about the prefix lists.
        self.prefix_list = prefix_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.prefix_list:
            for k in self.prefix_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrefixList'] = []
        if self.prefix_list is not None:
            for k in self.prefix_list:
                result['PrefixList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix_list = []
        if m.get('PrefixList') is not None:
            for k in m.get('PrefixList'):
                temp_model = DescribePrefixListsResponseBodyPrefixList()
                self.prefix_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePrefixListsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePrefixListsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePrefixListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskEventGroupRequest(TeaModel):
    def __init__(
        self,
        attack_app: List[str] = None,
        attack_type: str = None,
        buy_version: int = None,
        current_page: str = None,
        data_type: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_network_instance_id: str = None,
        end_time: str = None,
        event_name: str = None,
        firewall_type: str = None,
        is_only_private_assoc: str = None,
        lang: str = None,
        no_location: str = None,
        order: str = None,
        page_size: str = None,
        rule_result: str = None,
        rule_source: str = None,
        sort: str = None,
        src_ip: str = None,
        src_network_instance_id: str = None,
        start_time: str = None,
        vul_level: str = None,
    ):
        # The names of attacked applications. Set the value in the `["AttackApp1","AttackApp2"]` format.
        self.attack_app = attack_app
        # The attack type of the intrusion events. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # > If you do not specify this parameter, the intrusion events of all attack types are queried.
        self.attack_type = attack_type
        # The edition of Cloud Firewall that you purchase. Valid values:
        # 
        # *   **2**: Premium Edition
        # *   **3**: Enterprise Edition
        # *   **4**: Ultimate Edition
        # *   **10**: Cloud Firewall that uses the pay-as-you-go billing method
        self.buy_version = buy_version
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The type of the risk events.\\
        # Set the value to **session**, which indicates intrusion events.
        # 
        # This parameter is required.
        self.data_type = data_type
        # The direction of the traffic for the intrusion events. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # > If you do not specify this parameter, the intrusion events that are recorded for both inbound and outbound traffic are queried.
        self.direction = direction
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip
        # The ID of the destination VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.dst_network_instance_id = dst_network_instance_id
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the intrusion event.
        self.event_name = event_name
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall**: Internet firewall (default)
        self.firewall_type = firewall_type
        # Whether to query only the data that has completed private network tracing.
        self.is_only_private_assoc = is_only_private_assoc
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # Specifies whether to query the information about the geographical locations of IP addresses.
        # 
        # *   **true**: does not query the information about the geographical locations of IP addresses.
        # *   **false**: queries the information about the geographical locations of IP addresses. This is the default value.
        self.no_location = no_location
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: **6**. Maximum value: **10**.
        self.page_size = page_size
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        # 
        # > If you do not specify this parameter, all intrusion events that are detected by the firewall are queried, regardless of the firewall status.
        self.rule_result = rule_result
        # The module of the rule that is used to detect the intrusion events. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        # 
        # > If you do not specify this parameter, the intrusion events that are detected by all rules are queried.
        self.rule_source = rule_source
        # The field based on which you want to sort the results. Valid values:
        # 
        # *   **VulLevel**: The results are sorted based on the risk level field. This is the default value.
        # *   **LastTime**: The results are sorted based on the most recent occurrence time.
        self.sort = sort
        # The source IP address to query. If you specify this parameter, all intrusion events with the specified source IP address are queried.
        self.src_ip = src_ip
        # The ID of the source VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.src_network_instance_id = src_network_instance_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The risk level of the intrusion events. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        # 
        # > If you do not specify this parameter, the intrusion events that are at all risk levels are queried.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_network_instance_id is not None:
            result['DstNetworkInstanceId'] = self.dst_network_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
        if self.is_only_private_assoc is not None:
            result['IsOnlyPrivateAssoc'] = self.is_only_private_assoc
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.no_location is not None:
            result['NoLocation'] = self.no_location
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_network_instance_id is not None:
            result['SrcNetworkInstanceId'] = self.src_network_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstNetworkInstanceId') is not None:
            self.dst_network_instance_id = m.get('DstNetworkInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
        if m.get('IsOnlyPrivateAssoc') is not None:
            self.is_only_private_assoc = m.get('IsOnlyPrivateAssoc')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NoLocation') is not None:
            self.no_location = m.get('NoLocation')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcNetworkInstanceId') is not None:
            self.src_network_instance_id = m.get('SrcNetworkInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        return self


class DescribeRiskEventGroupResponseBodyDataListIPLocationInfo(TeaModel):
    def __init__(
        self,
        city_id: str = None,
        city_name: str = None,
        country_id: str = None,
        country_name: str = None,
    ):
        # The ID of the city to which the IP address belongs.
        self.city_id = city_id
        # The name of the city to which the IP address belongs.
        self.city_name = city_name
        # The ID of the country to which the IP address belongs.
        self.country_id = country_id
        # The name of the country to which the IP address belongs.
        self.country_name = country_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        return self


class DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList(TeaModel):
    def __init__(
        self,
        region_no: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_private_ip: str = None,
    ):
        # The ID of the region to which the private IP address belongs.
        self.region_no = region_no
        # The ID of the instance that uses the private IP address.
        self.resource_instance_id = resource_instance_id
        # The name of the instance that uses the private IP address.
        self.resource_instance_name = resource_instance_name
        # The private IP address.
        self.resource_private_ip = resource_private_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name
        if self.resource_private_ip is not None:
            result['ResourcePrivateIP'] = self.resource_private_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')
        if m.get('ResourcePrivateIP') is not None:
            self.resource_private_ip = m.get('ResourcePrivateIP')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcDstInfo(TeaModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        region_no: str = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The ID of the VPC.
        self.network_instance_id = network_instance_id
        # The name of the VPC.
        self.network_instance_name = network_instance_name
        # The ID of the region in which the destination VPC resides.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo(TeaModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        region_no: str = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The ID of the VPC.
        self.network_instance_id = network_instance_id
        # The name of the VPC.
        self.network_instance_name = network_instance_name
        # The ID of the region in which the source VPC resides.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataList(TeaModel):
    def __init__(
        self,
        attack_app: str = None,
        attack_type: int = None,
        description: str = None,
        direction: str = None,
        dst_ip: str = None,
        event_count: int = None,
        event_id: str = None,
        event_name: str = None,
        first_event_time: int = None,
        iplocation_info: DescribeRiskEventGroupResponseBodyDataListIPLocationInfo = None,
        last_event_time: int = None,
        resource_private_iplist: List[DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList] = None,
        resource_type: str = None,
        rule_id: str = None,
        rule_result: int = None,
        rule_source: int = None,
        src_ip: str = None,
        src_iptag: str = None,
        src_private_iplist: List[str] = None,
        tag: str = None,
        vpc_dst_info: DescribeRiskEventGroupResponseBodyDataListVpcDstInfo = None,
        vpc_src_info: DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo = None,
        vul_level: int = None,
    ):
        # The name of the attacked application.
        self.attack_app = attack_app
        # The attack type of the intrusion event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        self.attack_type = attack_type
        # The description of the intrusion event.
        self.description = description
        # The direction of the traffic for the intrusion event. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.direction = direction
        # The destination IP address that is included in the intrusion event.
        self.dst_ip = dst_ip
        # The number of intrusion events.
        self.event_count = event_count
        # The ID of the intrusion event.
        self.event_id = event_id
        # The name of the intrusion event.
        self.event_name = event_name
        # The time when the intrusion event was first detected. The value is a UNIX timestamp. Unit: seconds.
        self.first_event_time = first_event_time
        # The geographical information about the IP address. The value is a struct that contains the following parameters: **CityId**, **CityName**, **CountryId**, and **CountryName**.\\
        # ****************\
        self.iplocation_info = iplocation_info
        # The time when the intrusion event was last detected. The value is a UNIX timestamp. Unit: seconds.
        self.last_event_time = last_event_time
        # The information about the private IP address in the intrusion event. The value is an array that contains the following parameters: **RegionNo**, **ResourceInstanceId**, **ResourceInstanceName**, and **ResourcePrivateIP**.\\
        # ****************\
        self.resource_private_iplist = resource_private_iplist
        # The type of the public IP address in the intrusion event. Valid values:
        # 
        # *   **EIP**: the elastic IP address (EIP)
        # *   **EcsPublicIP**: the public IP address of an Elastic Compute Service (ECS) instance
        # *   **EcsEIP**: the EIP of an ECS instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **NatEIP**: the EIP of a NAT gateway
        self.resource_type = resource_type
        # The ID of the rule that is used to detect the intrusion event.
        self.rule_id = rule_id
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        self.rule_result = rule_result
        # The module of the rule that is used to detect the intrusion event. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        self.rule_source = rule_source
        # The source IP address that is included in the intrusion event.
        self.src_ip = src_ip
        # The tag added to the source IP address. The tag helps identify whether the source IP address is a back-to-origin IP address for a cloud service.
        self.src_iptag = src_iptag
        # An array that consists of the source private IP addresses in the intrusion event.
        self.src_private_iplist = src_private_iplist
        # The tag added to the threat intelligence that is provided for major events.
        self.tag = tag
        # The information about the destination VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\\
        # ********************\
        self.vpc_dst_info = vpc_dst_info
        # The information about the source VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\\
        # ********************\
        self.vpc_src_info = vpc_src_info
        # The risk level of the intrusion event. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.vul_level = vul_level

    def validate(self):
        if self.iplocation_info:
            self.iplocation_info.validate()
        if self.resource_private_iplist:
            for k in self.resource_private_iplist:
                if k:
                    k.validate()
        if self.vpc_dst_info:
            self.vpc_dst_info.validate()
        if self.vpc_src_info:
            self.vpc_src_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.description is not None:
            result['Description'] = self.description
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.first_event_time is not None:
            result['FirstEventTime'] = self.first_event_time
        if self.iplocation_info is not None:
            result['IPLocationInfo'] = self.iplocation_info.to_map()
        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time
        result['ResourcePrivateIPList'] = []
        if self.resource_private_iplist is not None:
            for k in self.resource_private_iplist:
                result['ResourcePrivateIPList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_iptag is not None:
            result['SrcIPTag'] = self.src_iptag
        if self.src_private_iplist is not None:
            result['SrcPrivateIPList'] = self.src_private_iplist
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.vpc_dst_info is not None:
            result['VpcDstInfo'] = self.vpc_dst_info.to_map()
        if self.vpc_src_info is not None:
            result['VpcSrcInfo'] = self.vpc_src_info.to_map()
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('FirstEventTime') is not None:
            self.first_event_time = m.get('FirstEventTime')
        if m.get('IPLocationInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListIPLocationInfo()
            self.iplocation_info = temp_model.from_map(m['IPLocationInfo'])
        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')
        self.resource_private_iplist = []
        if m.get('ResourcePrivateIPList') is not None:
            for k in m.get('ResourcePrivateIPList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList()
                self.resource_private_iplist.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcIPTag') is not None:
            self.src_iptag = m.get('SrcIPTag')
        if m.get('SrcPrivateIPList') is not None:
            self.src_private_iplist = m.get('SrcPrivateIPList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('VpcDstInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcDstInfo()
            self.vpc_dst_info = temp_model.from_map(m['VpcDstInfo'])
        if m.get('VpcSrcInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo()
            self.vpc_src_info = temp_model.from_map(m['VpcSrcInfo'])
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        return self


class DescribeRiskEventGroupResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeRiskEventGroupResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details of the intrusion events.
        self.data_list = data_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of risk events.
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRiskEventGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRiskEventGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRiskEventGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskEventPayloadRequest(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_vpc_id: str = None,
        end_time: str = None,
        firewall_type: str = None,
        public_ip: str = None,
        src_ip: str = None,
        src_vpc_id: str = None,
        start_time: str = None,
        uuid: str = None,
    ):
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip
        # The ID of the destination VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the destination VPC are queried.
        self.dst_vpc_id = dst_vpc_id
        # The end of the time range to query. The value is a timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall** (default): Internet firewall
        self.firewall_type = firewall_type
        # The public IP address. If you specify this parameter, all intrusion events that contain the specified public IP address are queried.
        self.public_ip = public_ip
        # The source IP address to query. If you specify this parameter, all intrusion events from the specified source IP address are queried.
        self.src_ip = src_ip
        # The ID of the source VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the source VPC are queried.
        self.src_vpc_id = src_vpc_id
        # The beginning of the time range to query. The value is a timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The UUID of the intrusion event.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class DescribeRiskEventPayloadResponseBody(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: int = None,
        dst_vpc_id: str = None,
        hit_content_type: int = None,
        hit_to: int = None,
        parsed_content: str = None,
        payload: str = None,
        payload_len: int = None,
        proto: str = None,
        real_ip: str = None,
        request_id: str = None,
        src_ip: str = None,
        src_port: int = None,
        src_vpc_id: str = None,
        xforward_for: str = None,
    ):
        # The destination IP address of the intrusion event.
        self.dst_ip = dst_ip
        # The destination port of the intrusion event.
        self.dst_port = dst_port
        # The destination VPC ID of the intrusion event.
        self.dst_vpc_id = dst_vpc_id
        # Type of the hit.
        self.hit_content_type = hit_content_type
        # The position where the hit ends.
        self.hit_to = hit_to
        # Hit payload.
        self.parsed_content = parsed_content
        # The attack payload of the intrusion event.
        self.payload = payload
        # The length of the attack payload of the intrusion event.
        self.payload_len = payload_len
        # The protocol type of intrusion event. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        self.proto = proto
        # The HTTP X-Real-IP field.
        self.real_ip = real_ip
        # The request ID.
        self.request_id = request_id
        # The source IP address of the intrusion event.
        self.src_ip = src_ip
        # The source port of the intrusion event.
        self.src_port = src_port
        # The source VPC ID of the intrusion event.
        self.src_vpc_id = src_vpc_id
        # The HTTP X-Forwarded-For field.
        self.xforward_for = xforward_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id
        if self.hit_content_type is not None:
            result['HitContentType'] = self.hit_content_type
        if self.hit_to is not None:
            result['HitTo'] = self.hit_to
        if self.parsed_content is not None:
            result['ParsedContent'] = self.parsed_content
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.real_ip is not None:
            result['RealIp'] = self.real_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id
        if self.xforward_for is not None:
            result['XForwardFor'] = self.xforward_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')
        if m.get('HitContentType') is not None:
            self.hit_content_type = m.get('HitContentType')
        if m.get('HitTo') is not None:
            self.hit_to = m.get('HitTo')
        if m.get('ParsedContent') is not None:
            self.parsed_content = m.get('ParsedContent')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('PayloadLen') is not None:
            self.payload_len = m.get('PayloadLen')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('RealIp') is not None:
            self.real_ip = m.get('RealIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')
        if m.get('XForwardFor') is not None:
            self.xforward_for = m.get('XForwardFor')
        return self


class DescribeRiskEventPayloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRiskEventPayloadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRiskEventPayloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSignatureLibVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The type.
        # 
        # Valid values:
        # 
        # *   ips
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Basic Rules and Virtual Patching
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   intelligence
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Threat Intelligence
        # 
        #     <!-- -->
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSignatureLibVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        version: List[DescribeSignatureLibVersionResponseBodyVersion] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the versions.
        self.version = version

    def validate(self):
        if self.version:
            for k in self.version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Version'] = []
        if self.version is not None:
            for k in self.version:
                result['Version'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.version = []
        if m.get('Version') is not None:
            for k in m.get('Version'):
                temp_model = DescribeSignatureLibVersionResponseBodyVersion()
                self.version.append(temp_model.from_map(k))
        return self


class DescribeSignatureLibVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSignatureLibVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSignatureLibVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListRequest(TeaModel):
    def __init__(
        self,
        candidate_list: List[DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The traffic redirection instances.
        self.candidate_list = candidate_list
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        if self.candidate_list:
            for k in self.candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CandidateList'] = []
        if self.candidate_list is not None:
            for k in self.candidate_list:
                result['CandidateList'].append(k.to_map() if k else None)
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.candidate_list = []
        if m.get('CandidateList') is not None:
            for k in m.get('CandidateList'):
                temp_model = DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList()
                self.candidate_list.append(temp_model.from_map(k))
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListShrinkRequest(TeaModel):
    def __init__(
        self,
        candidate_list_shrink: str = None,
        firewall_id: str = None,
        lang: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The traffic redirection instances.
        self.candidate_list_shrink = candidate_list_shrink
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_list_shrink is not None:
            result['CandidateList'] = self.candidate_list_shrink
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateList') is not None:
            self.candidate_list_shrink = m.get('CandidateList')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_name: str = None,
        candidate_type: str = None,
        current_route_table_id: str = None,
        original_route_table_id: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The name of the traffic redirection instance.
        self.candidate_name = candidate_name
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type
        # The route table that is used after traffic redirection.
        self.current_route_table_id = current_route_table_id
        # The ID of the route table.
        self.original_route_table_id = original_route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_name is not None:
            result['CandidateName'] = self.candidate_name
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        if self.current_route_table_id is not None:
            result['CurrentRouteTableId'] = self.current_route_table_id
        if self.original_route_table_id is not None:
            result['OriginalRouteTableId'] = self.original_route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateName') is not None:
            self.candidate_name = m.get('CandidateName')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        if m.get('CurrentRouteTableId') is not None:
            self.current_route_table_id = m.get('CurrentRouteTableId')
        if m.get('OriginalRouteTableId') is not None:
            self.original_route_table_id = m.get('OriginalRouteTableId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponseBody(TeaModel):
    def __init__(
        self,
        policy_association_backup_configs: List[DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs] = None,
        request_id: str = None,
    ):
        # The route tables.
        self.policy_association_backup_configs = policy_association_backup_configs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_association_backup_configs:
            for k in self.policy_association_backup_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyAssociationBackupConfigs'] = []
        if self.policy_association_backup_configs is not None:
            for k in self.policy_association_backup_configs:
                result['PolicyAssociationBackupConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_association_backup_configs = []
        if m.get('PolicyAssociationBackupConfigs') is not None:
            for k in m.get('PolicyAssociationBackupConfigs'):
                temp_model = DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs()
                self.policy_association_backup_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrFirewallPolicyBackUpAssociationListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrFirewallPolicyBackUpAssociationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallV2RoutePolicyListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        firewall_id: str = None,
        lang: str = None,
        page_size: int = None,
        policy_id: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the routing policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the secondary traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the secondary traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the primary traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the primary traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies(TeaModel):
    def __init__(
        self,
        dest_candidate_list: List[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList] = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_status: str = None,
        policy_type: str = None,
        src_candidate_list: List[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList] = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The description of the routing policy.
        self.policy_description = policy_description
        # The name of the routing policy.
        self.policy_name = policy_name
        # The status of the routing policy. Valid values:
        # 
        # *   creating: The policy is being created.
        # *   deleting: The policy is being deleted.
        # *   opening: The policy is being enabled.
        # *   opened: The policy is enabled.
        # *   closing: The policy is being disabled.
        # *   closed: The policy is disabled.
        self.policy_status = policy_status
        # The type of the traffic redirection scenario of the VPC firewall. Valid values:
        # 
        # *   **fullmesh**: interconnected instances
        # *   **one_to_one**: instance to instance
        # *   **end_to_end**: instance to instances
        self.policy_type = policy_type
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        tr_firewall_route_policies: List[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The routing policies.
        self.tr_firewall_route_policies = tr_firewall_route_policies

    def validate(self):
        if self.tr_firewall_route_policies:
            for k in self.tr_firewall_route_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrFirewallRoutePolicies'] = []
        if self.tr_firewall_route_policies is not None:
            for k in self.tr_firewall_route_policies:
                result['TrFirewallRoutePolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tr_firewall_route_policies = []
        if m.get('TrFirewallRoutePolicies') is not None:
            for k in m.get('TrFirewallRoutePolicies'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies()
                self.tr_firewall_route_policies.append(temp_model.from_map(k))
        return self


class DescribeTrFirewallV2RoutePolicyListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrFirewallV2RoutePolicyListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrFirewallV2RoutePolicyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2DetailRequest(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeTrFirewallsV2DetailResponseBody(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_description: str = None,
        firewall_eni_id: str = None,
        firewall_eni_vpc_id: str = None,
        firewall_eni_vswitch_id: str = None,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_status: str = None,
        firewall_subnet_cidr: str = None,
        firewall_switch_status: str = None,
        firewall_vpc_cidr: str = None,
        region_no: str = None,
        request_id: str = None,
        route_mode: str = None,
        tr_attachment_master_cidr: str = None,
        tr_attachment_slave_cidr: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The description of the VPC firewall.
        self.firewall_description = firewall_description
        # The ID of the Elastic Network Interface (ENI) with which the VPC firewall is associated.
        self.firewall_eni_id = firewall_eni_id
        # The ID of the VPC to which the ENI is attached.
        self.firewall_eni_vpc_id = firewall_eni_vpc_id
        # The ID of the vSwitch with which the ENI is associated.
        self.firewall_eni_vswitch_id = firewall_eni_vswitch_id
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The name of the VPC firewall.
        self.firewall_name = firewall_name
        # The status of the VPC firewall. Valid values:
        # 
        # *   Creating
        # *   Deleting
        # *   Ready
        self.firewall_status = firewall_status
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The region ID of the transit router.
        self.region_no = region_no
        # The request ID.
        self.request_id = request_id
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description
        if self.firewall_eni_id is not None:
            result['FirewallEniId'] = self.firewall_eni_id
        if self.firewall_eni_vpc_id is not None:
            result['FirewallEniVpcId'] = self.firewall_eni_vpc_id
        if self.firewall_eni_vswitch_id is not None:
            result['FirewallEniVswitchId'] = self.firewall_eni_vswitch_id
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_status is not None:
            result['FirewallStatus'] = self.firewall_status
        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr
        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')
        if m.get('FirewallEniId') is not None:
            self.firewall_eni_id = m.get('FirewallEniId')
        if m.get('FirewallEniVpcId') is not None:
            self.firewall_eni_vpc_id = m.get('FirewallEniVpcId')
        if m.get('FirewallEniVswitchId') is not None:
            self.firewall_eni_vswitch_id = m.get('FirewallEniVswitchId')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallStatus') is not None:
            self.firewall_status = m.get('FirewallStatus')
        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')
        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class DescribeTrFirewallsV2DetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrFirewallsV2DetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrFirewallsV2DetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2ListRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        current_page: int = None,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        owner_id: str = None,
        page_size: int = None,
        region_no: str = None,
        route_mode: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The name of the VPC firewall.
        self.firewall_name = firewall_name
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # >  If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        self.owner_id = owner_id
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID of the transit router.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        # 
        # >  If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig(TeaModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose.
        # *   **2**: medium.
        # *   **3**: strict.
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource(TeaModel):
    def __init__(
        self,
        count: int = None,
        ecr_list: List[str] = None,
        peer_tr_list: List[str] = None,
        vbr_list: List[str] = None,
        vpc_list: List[str] = None,
        vpn_list: List[str] = None,
    ):
        # The number of protected resources.
        self.count = count
        # The protected express connect routers.
        self.ecr_list = ecr_list
        # The protected peer transit routers.
        self.peer_tr_list = peer_tr_list
        # The protected virtual border routers (VBRs).
        self.vbr_list = vbr_list
        # The protected VPCs.
        self.vpc_list = vpc_list
        # The protected VPN gateways.
        self.vpn_list = vpn_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.ecr_list is not None:
            result['EcrList'] = self.ecr_list
        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list
        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list
        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list
        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EcrList') is not None:
            self.ecr_list = m.get('EcrList')
        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')
        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')
        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')
        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource(TeaModel):
    def __init__(
        self,
        count: int = None,
        ecr_list: List[str] = None,
        peer_tr_list: List[str] = None,
        vbr_list: List[str] = None,
        vpc_list: List[str] = None,
        vpn_list: List[str] = None,
    ):
        # The number of unprotected resources.
        self.count = count
        # The unprotected express connect routers.
        self.ecr_list = ecr_list
        # The unprotected peer transit routers.
        self.peer_tr_list = peer_tr_list
        # The unprotected VBRs.
        self.vbr_list = vbr_list
        # The unprotected VPCs.
        self.vpc_list = vpc_list
        # The unprotected VPN gateways.
        self.vpn_list = vpn_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.ecr_list is not None:
            result['EcrList'] = self.ecr_list
        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list
        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list
        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list
        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EcrList') is not None:
            self.ecr_list = m.get('EcrList')
        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')
        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')
        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')
        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_name: str = None,
        cloud_firewall_vpc_order_type: str = None,
        firewall_id: str = None,
        firewall_switch_status: str = None,
        ips_config: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig = None,
        owner_id: int = None,
        precheck_status: str = None,
        protected_resource: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource = None,
        region_no: str = None,
        region_status: str = None,
        result_code: str = None,
        route_mode: str = None,
        transit_router_id: str = None,
        unprotected_resource: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource = None,
        vpc_firewall_name: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The party responsible for the TR fees generated by the VPC firewall. Values:
        # 
        # - **PayByCloudFirewall**: Fees are borne by the Cloud Firewall.
        # - **PayByCenOwner**: Fees are borne by the account to which the CEN instance belongs.
        self.cloud_firewall_vpc_order_type = cloud_firewall_vpc_order_type
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # >  If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The intrusion prevention system (IPS) configurations.
        self.ips_config = ips_config
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # Indicates whether the VPC firewall can be automatically enabled. Valid values:
        # 
        # *   **passed**: yes
        # *   **failed**: no
        # *   **unknown**\
        self.precheck_status = precheck_status
        # The protected resources.
        self.protected_resource = protected_resource
        # The region ID of the transit router.
        self.region_no = region_no
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **RegionDisable**: VPC Firewall is not supported in the region of the network instance. You cannot create a VPC firewall for the network instance.
        # *   **Empty string**: You can create a VPC firewall for the network instance.
        self.result_code = result_code
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The unprotected resources.
        self.unprotected_resource = unprotected_resource
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.protected_resource:
            self.protected_resource.validate()
        if self.unprotected_resource:
            self.unprotected_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_name is not None:
            result['CenName'] = self.cen_name
        if self.cloud_firewall_vpc_order_type is not None:
            result['CloudFirewallVpcOrderType'] = self.cloud_firewall_vpc_order_type
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status
        if self.protected_resource is not None:
            result['ProtectedResource'] = self.protected_resource.to_map()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.unprotected_resource is not None:
            result['UnprotectedResource'] = self.unprotected_resource.to_map()
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')
        if m.get('CloudFirewallVpcOrderType') is not None:
            self.cloud_firewall_vpc_order_type = m.get('CloudFirewallVpcOrderType')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')
        if m.get('ProtectedResource') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource()
            self.protected_resource = temp_model.from_map(m['ProtectedResource'])
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('UnprotectedResource') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource()
            self.unprotected_resource = temp_model.from_map(m['UnprotectedResource'])
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeTrFirewallsV2ListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        vpc_tr_firewalls: List[DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the VPC firewalls.
        self.vpc_tr_firewalls = vpc_tr_firewalls

    def validate(self):
        if self.vpc_tr_firewalls:
            for k in self.vpc_tr_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcTrFirewalls'] = []
        if self.vpc_tr_firewalls is not None:
            for k in self.vpc_tr_firewalls:
                result['VpcTrFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_tr_firewalls = []
        if m.get('VpcTrFirewalls') is not None:
            for k in m.get('VpcTrFirewalls'):
                temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls()
                self.vpc_tr_firewalls.append(temp_model.from_map(k))
        return self


class DescribeTrFirewallsV2ListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrFirewallsV2ListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2RouteListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        firewall_id: str = None,
        lang: str = None,
        page_size: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The instance ID of the virtual private cloud (VPC) firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList(TeaModel):
    def __init__(
        self,
        tr_firewall_route_destination: str = None,
        tr_firewall_route_nexthop: str = None,
        tr_firewall_route_policy_id: str = None,
        tr_firewall_route_table_id: str = None,
    ):
        # The destination address of the route.
        self.tr_firewall_route_destination = tr_firewall_route_destination
        # The ID of the next hop for the route.
        self.tr_firewall_route_nexthop = tr_firewall_route_nexthop
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id
        # The ID of the route table to which the route entry belongs.
        self.tr_firewall_route_table_id = tr_firewall_route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tr_firewall_route_destination is not None:
            result['TrFirewallRouteDestination'] = self.tr_firewall_route_destination
        if self.tr_firewall_route_nexthop is not None:
            result['TrFirewallRouteNexthop'] = self.tr_firewall_route_nexthop
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        if self.tr_firewall_route_table_id is not None:
            result['TrFirewallRouteTableId'] = self.tr_firewall_route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrFirewallRouteDestination') is not None:
            self.tr_firewall_route_destination = m.get('TrFirewallRouteDestination')
        if m.get('TrFirewallRouteNexthop') is not None:
            self.tr_firewall_route_nexthop = m.get('TrFirewallRouteNexthop')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        if m.get('TrFirewallRouteTableId') is not None:
            self.tr_firewall_route_table_id = m.get('TrFirewallRouteTableId')
        return self


class DescribeTrFirewallsV2RouteListResponseBody(TeaModel):
    def __init__(
        self,
        firewall_route_detail_list: List[DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList] = None,
        request_id: str = None,
    ):
        # The route tables of Cloud Firewall.
        self.firewall_route_detail_list = firewall_route_detail_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.firewall_route_detail_list:
            for k in self.firewall_route_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FirewallRouteDetailList'] = []
        if self.firewall_route_detail_list is not None:
            for k in self.firewall_route_detail_list:
                result['FirewallRouteDetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.firewall_route_detail_list = []
        if m.get('FirewallRouteDetailList') is not None:
            for k in m.get('FirewallRouteDetailList'):
                temp_model = DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList()
                self.firewall_route_detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrFirewallsV2RouteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrFirewallsV2RouteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrFirewallsV2RouteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAssetIPTrafficInfoRequest(TeaModel):
    def __init__(
        self,
        asset_ip: str = None,
        lang: str = None,
        traffic_time: str = None,
    ):
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.asset_ip = asset_ip
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.traffic_time = traffic_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')
        return self


class DescribeUserAssetIPTrafficInfoResponseBody(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        in_bps: int = None,
        in_pps: int = None,
        new_conn: int = None,
        out_bps: int = None,
        out_pps: int = None,
        request_id: str = None,
        session_count: int = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The network throughput, which indicates the inbound traffic rate. Unit: bit/s.
        self.in_bps = in_bps
        # The inbound network throughput, which indicates the number of packets that are sent inbound per second. Unit: packets per second (pps).
        self.in_pps = in_pps
        # The new connection creation rate.
        self.new_conn = new_conn
        # The network throughput, which indicates the outbound traffic rate. Unit: bit/s.
        self.out_bps = out_bps
        # The outbound network throughput, which indicates the number of packets that are sent outbound per second. Unit: pps.
        self.out_pps = out_pps
        # The request ID.
        self.request_id = request_id
        # The number of requests.
        self.session_count = session_count
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.new_conn is not None:
            result['NewConn'] = self.new_conn
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserAssetIPTrafficInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserAssetIPTrafficInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserAssetIPTrafficInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBuyVersionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # Instance ID. If the Instance ID is provided, the query will be based on this ID. If not provided, the latest instance will be queried by default.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeUserBuyVersionResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        expire: int = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_bandwidth: int = None,
        ip_number: int = None,
        log_status: bool = None,
        log_storage: int = None,
        max_overflow: int = None,
        nat_bandwidth: int = None,
        request_id: str = None,
        start_time: int = None,
        user_status: bool = None,
        version: int = None,
        vpc_bandwidth: int = None,
        vpc_number: int = None,
    ):
        # The ID of the Alibaba Cloud account that is used to purchase Cloud Firewall.
        self.ali_uid = ali_uid
        # The time when Cloud Firewall expires.
        # 
        # >  The value is a timestamp in milliseconds.
        # 
        # >  If you use Cloud Firewall that uses the pay-as-you-go billing method, ignore this parameter.
        self.expire = expire
        # The instance ID of Cloud Firewall.
        # 
        # >  If you use a trial of Cloud Firewall, ignore this parameter.
        self.instance_id = instance_id
        # The status of Cloud Firewall. Valid values:
        # 
        # *   **normal**: Cloud Firewall is running as expected.
        # *   **init**: Cloud Firewall is being initialized.
        # *   **deleting**: Cloud Firewall is being deleted.
        # *   **abnormal**: An exception occurs in Cloud Firewall.
        # *   **free**: Cloud Firewall is invalid.
        self.instance_status = instance_status
        self.internet_bandwidth = internet_bandwidth
        # The number of public IP addresses that can be protected.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.ip_number = ip_number
        # Indicates whether log delivery is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.log_status = log_status
        # The log storage capacity.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.log_storage = log_storage
        # The status of the burstable protected traffic feature. Valid values:
        # 
        # *   **1000000**: enabled.
        # *   **0**: disabled.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.max_overflow = max_overflow
        self.nat_bandwidth = nat_bandwidth
        # The request ID.
        self.request_id = request_id
        # The time when Cloud Firewall was activated.
        # 
        # >  The value is a timestamp in milliseconds.
        self.start_time = start_time
        # Indicates whether Cloud Firewall is valid. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.user_status = user_status
        # The edition of Cloud Firewall. Valid values:
        # 
        # *   **2**: Premium Edition.
        # *   **3**: Enterprise Edition.
        # *   **4**: Ultimate Edition.
        # *   **10**: Cloud Firewall that uses the pay-as-you-go billing method.
        self.version = version
        self.vpc_bandwidth = vpc_bandwidth
        # The number of virtual private clouds (VPCs) that can be protected.
        # 
        # >  This parameter takes effect only for Cloud Firewall that uses the subscription billing method.
        self.vpc_number = vpc_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth
        if self.ip_number is not None:
            result['IpNumber'] = self.ip_number
        if self.log_status is not None:
            result['LogStatus'] = self.log_status
        if self.log_storage is not None:
            result['LogStorage'] = self.log_storage
        if self.max_overflow is not None:
            result['MaxOverflow'] = self.max_overflow
        if self.nat_bandwidth is not None:
            result['NatBandwidth'] = self.nat_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_bandwidth is not None:
            result['VpcBandwidth'] = self.vpc_bandwidth
        if self.vpc_number is not None:
            result['VpcNumber'] = self.vpc_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')
        if m.get('IpNumber') is not None:
            self.ip_number = m.get('IpNumber')
        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')
        if m.get('LogStorage') is not None:
            self.log_storage = m.get('LogStorage')
        if m.get('MaxOverflow') is not None:
            self.max_overflow = m.get('MaxOverflow')
        if m.get('NatBandwidth') is not None:
            self.nat_bandwidth = m.get('NatBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcBandwidth') is not None:
            self.vpc_bandwidth = m.get('VpcBandwidth')
        if m.get('VpcNumber') is not None:
            self.vpc_number = m.get('VpcNumber')
        return self


class DescribeUserBuyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserBuyVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserBuyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserIPSWhitelistRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUserIPSWhitelistResponseBodyIpv6Whitelists(TeaModel):
    def __init__(
        self,
        direction: int = None,
        list_type: int = None,
        list_value: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.list_type = list_type
        self.list_value = list_value
        self.white_list_value = white_list_value
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class DescribeUserIPSWhitelistResponseBodyWhitelists(TeaModel):
    def __init__(
        self,
        direction: int = None,
        list_type: int = None,
        list_value: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.list_type = list_type
        self.list_value = list_value
        self.white_list_value = white_list_value
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class DescribeUserIPSWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        ipv_6whitelists: List[DescribeUserIPSWhitelistResponseBodyIpv6Whitelists] = None,
        request_id: str = None,
        whitelists: List[DescribeUserIPSWhitelistResponseBodyWhitelists] = None,
    ):
        self.ipv_6whitelists = ipv_6whitelists
        self.request_id = request_id
        self.whitelists = whitelists

    def validate(self):
        if self.ipv_6whitelists:
            for k in self.ipv_6whitelists:
                if k:
                    k.validate()
        if self.whitelists:
            for k in self.whitelists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ipv6Whitelists'] = []
        if self.ipv_6whitelists is not None:
            for k in self.ipv_6whitelists:
                result['Ipv6Whitelists'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Whitelists'] = []
        if self.whitelists is not None:
            for k in self.whitelists:
                result['Whitelists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6whitelists = []
        if m.get('Ipv6Whitelists') is not None:
            for k in m.get('Ipv6Whitelists'):
                temp_model = DescribeUserIPSWhitelistResponseBodyIpv6Whitelists()
                self.ipv_6whitelists.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k in m.get('Whitelists'):
                temp_model = DescribeUserIPSWhitelistResponseBodyWhitelists()
                self.whitelists.append(temp_model.from_map(k))
        return self


class DescribeUserIPSWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserIPSWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallAclGroupListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        firewall_configure_status: str = None,
        lang: str = None,
        page_size: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # Specifies whether VPC firewalls are configured. Valid values:
        # 
        # *   **notconfigured**: VPC firewalls are not configured.
        # *   **configured**: VPC firewalls are configured.
        # *   If you do not specify this parameter, the access control policies of all VPC firewalls are queried.
        self.firewall_configure_status = firewall_configure_status
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Maximum value: 50.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_configure_status is not None:
            result['FirewallConfigureStatus'] = self.firewall_configure_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallConfigureStatus') is not None:
            self.firewall_configure_status = m.get('FirewallConfigureStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVpcFirewallAclGroupListResponseBodyAclGroupList(TeaModel):
    def __init__(
        self,
        acl_group_id: str = None,
        acl_group_name: str = None,
        acl_rule_count: int = None,
        is_default: bool = None,
        member_uid: str = None,
    ):
        # The ID of the policy group.
        # 
        # Valid values:
        # 
        # *   If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\\*\\*\\*\\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*\
        self.acl_group_id = acl_group_id
        # The name of the policy group. Valid values:
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter is the name of the CEN instance.
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the instance name of the VPC firewall.
        self.acl_group_name = acl_group_name
        # The number of access control policies in the policy group.
        self.acl_rule_count = acl_rule_count
        # 是否是默认防火墙。取值：
        # - **true**：是默认防火墙。
        # - **false**：不是默认防火墙。
        self.is_default = is_default
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_group_id is not None:
            result['AclGroupId'] = self.acl_group_id
        if self.acl_group_name is not None:
            result['AclGroupName'] = self.acl_group_name
        if self.acl_rule_count is not None:
            result['AclRuleCount'] = self.acl_rule_count
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclGroupId') is not None:
            self.acl_group_id = m.get('AclGroupId')
        if m.get('AclGroupName') is not None:
            self.acl_group_name = m.get('AclGroupName')
        if m.get('AclRuleCount') is not None:
            self.acl_rule_count = m.get('AclRuleCount')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class DescribeVpcFirewallAclGroupListResponseBody(TeaModel):
    def __init__(
        self,
        acl_group_list: List[DescribeVpcFirewallAclGroupListResponseBodyAclGroupList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the policy groups.
        self.acl_group_list = acl_group_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of the policy groups that are returned.
        self.total_count = total_count

    def validate(self):
        if self.acl_group_list:
            for k in self.acl_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclGroupList'] = []
        if self.acl_group_list is not None:
            for k in self.acl_group_list:
                result['AclGroupList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_group_list = []
        if m.get('AclGroupList') is not None:
            for k in m.get('AclGroupList'):
                temp_model = DescribeVpcFirewallAclGroupListResponseBodyAclGroupList()
                self.acl_group_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVpcFirewallAclGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallAclGroupListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallAclGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallCenDetailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        network_instance_id: str = None,
        vpc_firewall_id: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the VPC for which the VPC firewall is created.
        self.network_instance_id = network_instance_id
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyFirewallVpc(TeaModel):
    def __init__(
        self,
        allow_configuration: int = None,
        vpc_cidr: str = None,
        vpc_id: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether you can specify a CIDR block when you create a VPC firewall for a Basic Edition transit router of a CEN instance. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.allow_configuration = allow_configuration
        # The CIDR block of the VPC.
        self.vpc_cidr = vpc_cidr
        # The VPC ID.
        self.vpc_id = vpc_id
        # The CIDR block of the vSwitch.
        self.vswitch_cidr = vswitch_cidr
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_configuration is not None:
            result['AllowConfiguration'] = self.allow_configuration
        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowConfiguration') is not None:
            self.allow_configuration = m.get('AllowConfiguration')
        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        eni_vswitch_id: str = None,
    ):
        # The ID of the ENI that belongs to the VPC.
        self.eni_id = eni_id
        # The private IP address of the ENI that belongs to the VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The ID of the vSwitch to which the ENI is connected.
        self.eni_vswitch_id = eni_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.eni_vswitch_id is not None:
            result['EniVSwitchId'] = self.eni_vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('EniVSwitchId') is not None:
            self.eni_vswitch_id = m.get('EniVSwitchId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries for the VPC.
        self.route_entry_list = route_entry_list
        # The route table ID of the VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpc(TeaModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_name: str = None,
        defend_cidr_list: List[str] = None,
        eni_list: List[DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList] = None,
        manual_vswitch_id: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        owner_id: str = None,
        region_no: str = None,
        route_mode: str = None,
        support_manual_mode: str = None,
        transit_router_id: str = None,
        transit_router_type: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the connection between two network instances.
        self.attachment_id = attachment_id
        # The name of the connection between two network instances.
        self.attachment_name = attachment_name
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list
        # The Elastic Network Interfaces (ENIs).
        self.eni_list = eni_list
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id
        # The ID of the VPC for which the VPC firewall is created.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance. The value is fixed as **VPC**.
        self.network_instance_type = network_instance_type
        # The UID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The ID of the region in which the VPC resides.
        self.region_no = region_no
        # The routing mode. Valid values:
        # 
        # *   auto: automatic mode
        # *   manual: manual mode
        self.route_mode = route_mode
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode
        # The instance ID of the CEN transit router.
        self.transit_router_id = transit_router_id
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition
        # *   **Enterprise**: Enterprise Edition
        self.transit_router_type = transit_router_type
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.eni_list:
            for k in self.eni_list:
                if k:
                    k.validate()
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list
        result['EniList'] = []
        if self.eni_list is not None:
            for k in self.eni_list:
                result['EniList'].append(k.to_map() if k else None)
        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')
        self.eni_list = []
        if m.get('EniList') is not None:
            for k in m.get('EniList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList()
                self.eni_list.append(temp_model.from_map(k))
        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallCenDetailResponseBody(TeaModel):
    def __init__(
        self,
        connect_type: str = None,
        firewall_switch_status: str = None,
        firewall_vpc: DescribeVpcFirewallCenDetailResponseBodyFirewallVpc = None,
        local_vpc: DescribeVpcFirewallCenDetailResponseBodyLocalVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The connection type of the VPC firewall. The value is fixed as **cen**, which indicates CEN instances.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: enabled
        # *   **closed**: disabled
        # *   **notconfigured**: not configured
        self.firewall_switch_status = firewall_switch_status
        # The VPC that is automatically created for the firewall.
        self.firewall_vpc = firewall_vpc
        # The details about the VPC.
        self.local_vpc = local_vpc
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.firewall_vpc:
            self.firewall_vpc.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.firewall_vpc is not None:
            result['FirewallVpc'] = self.firewall_vpc.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('FirewallVpc') is not None:
            temp_model = DescribeVpcFirewallCenDetailResponseBodyFirewallVpc()
            self.firewall_vpc = temp_model.from_map(m['FirewallVpc'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallCenDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallCenDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallCenListRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        current_page: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_id: str = None,
        owner_id: str = None,
        page_size: str = None,
        region_no: str = None,
        route_mode: str = None,
        transit_router_type: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured but is not enabled.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        self.owner_id = owner_id
        # The number of entries to return on each page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        # 
        # > If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode
        # The type of the transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig(TeaModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose.
        # *   **2**: medium.
        # *   **3**: strict.
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries for the VPC.
        self.route_entry_list = route_entry_list
        # The route table ID of the VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc(TeaModel):
    def __init__(
        self,
        authorization_status: str = None,
        defend_cidr_list: List[str] = None,
        manual_vswitch_id: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        owner_id: int = None,
        region_no: str = None,
        route_mode: str = None,
        support_manual_mode: str = None,
        transit_router_type: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether the VPC is granted the required permissions. The value is fixed as **authorized**, which indicates that the VPC is granted the required permissions.
        self.authorization_status = authorization_status
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**\
        # *   **VBR**\
        # *   **CCN**\
        self.network_instance_type = network_instance_type
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The region ID of the VPC.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list
        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')
        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewalls(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_name: str = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        ips_config: DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig = None,
        local_vpc: DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc = None,
        member_uid: str = None,
        precheck_status: str = None,
        region_status: str = None,
        result_code: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The connection type of the VPC firewall. The value is fixed as cen, which indicates a CEN instance.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status
        # The intrusion prevention system (IPS) configurations.
        self.ips_config = ips_config
        # The details about the VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is manged by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid
        # Indicates whether the VPC firewall can be automatically enabled to protect VPC traffic based on route learning. Valid values:
        # 
        # *   **passed**: The VPC firewall can be automatically enabled.
        # *   **failed**: The VPC firewall cannot be automatically enabled.
        # *   **unknown**: The VPC firewall is in an unknown state.
        self.precheck_status = precheck_status
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **OpsDisable**: You are not allowed to create the VPC firewall.
        # *   **VbrNotSupport**: The VPC firewall cannot be created for a VBR that is attached to the CEN instance.
        # *   Empty string: You can create a VPC firewall for the network instance.
        self.result_code = result_code
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_name is not None:
            result['CenName'] = self.cen_name
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_firewalls: List[DescribeVpcFirewallCenListResponseBodyVpcFirewalls] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of VPC firewalls.
        self.total_count = total_count
        # The information about the VPC firewalls.
        self.vpc_firewalls = vpc_firewalls

    def validate(self):
        if self.vpc_firewalls:
            for k in self.vpc_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcFirewalls'] = []
        if self.vpc_firewalls is not None:
            for k in self.vpc_firewalls:
                result['VpcFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_firewalls = []
        if m.get('VpcFirewalls') is not None:
            for k in m.get('VpcFirewalls'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallCenListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallCenListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallCenListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
        vpc_firewall_id: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: blocks the traffic.
        # *   **log**: monitors the traffic.
        # 
        # > If you do not specify this parameter, access control policies are queried based on all actions.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The number of the page to return.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy match is supported.
        self.description = description
        # The destination address in the access control policy. Fuzzy match is supported.
        # 
        # > The value of this parameter can be a CIDR block or an address book name.
        self.destination = destination
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The number of entries to return on each page.
        # 
        # Maximum value: 50.
        self.page_size = page_size
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all protocol types
        # 
        # > If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.release = release
        # The recurrence type for the access control policy to take effect. Valid values:
        # 
        # *   **Permanent** (default): The policy always takes effect.
        # *   **None**: The policy takes effect for only once.
        # *   **Daily**: The policy takes effect on a daily basis.
        # *   **Weekly**: The policy takes effect on a weekly basis.
        # *   **Monthly**: The policy takes effect on a monthly basis.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy match is supported.
        # 
        # > The value of this parameter can be a CIDR block or an address book name.
        self.source = source
        # The instance ID of the VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects the traffic between two VPCs that are connected by using a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # *   If the VPC firewall protects the traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallControlPolicyResponseBodyPolicys(TeaModel):
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
        # The application types supported by the access control policy. We recommend that you specify ApplicationNameList. Valid values:
        # 
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **MySQL**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **RDP**\
        # *   **VNC**\
        # *   **SSH**\
        # *   **Redis**\
        # *   **MQTT**\
        # *   **MongoDB**\
        # *   **Memcache**\
        # *   **SSL**\
        # *   **ANY**: all application types
        self.application_name = application_name
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list
        # The time when the access control policy was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The description of the access control policy.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The ports in the destination port address book of the access control policy.
        self.dest_port_group_ports = dest_port_group_ports
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy. Valid values:
        # 
        # *   If **DestinationType** is set to `net`, the value of this parameter is a CIDR block.
        # *   If **DestinationType** is set to `domain`, the value of this parameter is a domain name.
        # *   If **DestinationType** is set to `group`, the value of this parameter is an address book name.
        self.destination = destination
        # The CIDR blocks in the destination address book of the access control policy.
        self.destination_group_cidrs = destination_group_cidrs
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more CIDR blocks
        # *   **domain**: an address book that includes one or more domain names
        self.destination_group_type = destination_group_type
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        self.destination_type = destination_type
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of StartTime.
        # 
        # >  If RepeatType is set to Permanent, EndTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, EndTime must be specified.
        self.end_time = end_time
        # The time when the access control policy was last hit. The value is a UNIX timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time
        # The number of hits for the access control policy.
        self.hit_times = hit_times
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The time when the access control policy was modified. The value is a UNIX timestamp. Unit: seconds.
        self.modify_time = modify_time
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.order = order
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all protocol types
        self.proto = proto
        # Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # >  If RepeatType is set to Permanent or None, RepeatEndTime is left empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatEndTime must be specified.
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
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of this parameter is a CIDR block.
        # *   If **SourceType** is set to `group`, the value of this parameter is an address book name.
        self.source = source
        # The CIDR blocks in the source address book of the access control policy.
        self.source_group_cidrs = source_group_cidrs
        # The type of the source address book in the access control policy. The value is fixed as **ip**. The value indicates an address book that includes one or more CIDR blocks.
        self.source_group_type = source_group_type
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        self.source_type = source_type
        # The total quota consumed by the returned access control policies, which is the sum of the quota consumed by each policy. The quota that is consumed by an access control policy is calculated by using the following formula: Quota that is consumed by an access control policy = Number of source addresses × Number of destination addresses (number of CIDR blocks or domain names) × Number of applications × Number of port ranges.
        self.spread_cnt = spread_cnt
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of EndTime.
        # 
        # >  If RepeatType is set to Permanent, StartTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, StartTime must be specified.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policys: List[DescribeVpcFirewallControlPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The details of the access control policies.
        self.policys = policys
        # The ID of the request.
        self.request_id = request_id
        # The total number of access control policies returned.
        self.total_count = total_count

    def validate(self):
        if self.policys:
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeVpcFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallDefaultIPSConfigRequest(TeaModel):
    def __init__(
        self,
        member_uid: str = None,
        vpc_firewall_id: str = None,
    ):
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the IDs of CEN instances.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall. You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallDefaultIPSConfigResponseBody(TeaModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        request_id: str = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic policies are enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The ID of the request.
        self.request_id = request_id
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose.
        # *   **2**: medium.
        # *   **3**: strict.
        self.rule_class = rule_class
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallDefaultIPSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallDefaultIPSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallDetailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        local_vpc_id: str = None,
        peer_vpc_id: str = None,
        vpc_firewall_id: str = None,
    ):
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the local VPC.
        self.local_vpc_id = local_vpc_id
        # The ID of the peer VPC.
        self.peer_vpc_id = peer_vpc_id
        # The instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_id is not None:
            result['LocalVpcId'] = self.local_vpc_id
        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcId') is not None:
            self.local_vpc_id = m.get('LocalVpcId')
        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the local VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries of the local VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the local VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpc(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        region_no: str = None,
        router_interface_id: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the ENI for the local VPC.
        self.eni_id = eni_id
        # The private IP address of the elastic network interface (ENI) for the local VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The region ID of the local VPC.
        self.region_no = region_no
        # The router interface ID of the local VPC.
        self.router_interface_id = router_interface_id
        # The CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the local VPC.
        self.vpc_id = vpc_id
        # The name of the local VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the peer VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries of the peer VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the peer VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpc(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        region_no: str = None,
        router_interface_id: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the ENI for the peer VPC.
        self.eni_id = eni_id
        # The private IP address of the ENI for the peer VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The region ID of the peer VPC.
        self.region_no = region_no
        # The router interface ID of the peer VPC.
        self.router_interface_id = router_interface_id
        # The CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the peer VPC.
        self.vpc_id = vpc_id
        # The name of the peer VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallDetailResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        local_vpc: DescribeVpcFirewallDetailResponseBodyLocalVpc = None,
        member_uid: str = None,
        peer_vpc: DescribeVpcFirewallDetailResponseBodyPeerVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates Express Connect circuits.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        self.firewall_switch_status = firewall_switch_status
        # The details about the local VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.local_vpc:
            self.local_vpc.validate()
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpc') is not None:
            temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpc()
            self.peer_vpc = temp_model.from_map(m['PeerVpc'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallIPSWhitelistRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: int = None,
        vpc_firewall_id: str = None,
    ):
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists(TeaModel):
    def __init__(
        self,
        list_type: int = None,
        list_value: str = None,
        vpc_firewall_id: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        # The type of the list. Valid values:
        # 
        # *   **1**: user-defined
        # *   **2**: address book
        self.list_type = list_type
        # The entries in the list.
        self.list_value = list_value
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # An array of entries in the list.
        self.white_list_value = white_list_value
        # The type of the whitelist. Valid values:
        # 
        # *   **1**: destination
        # *   **2**: source
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class DescribeVpcFirewallIPSWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        whitelists: List[DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the IPS whitelist of the VPC firewall.
        self.whitelists = whitelists

    def validate(self):
        if self.whitelists:
            for k in self.whitelists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Whitelists'] = []
        if self.whitelists is not None:
            for k in self.whitelists:
                result['Whitelists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k in m.get('Whitelists'):
                temp_model = DescribeVpcFirewallIPSWhitelistResponseBodyWhitelists()
                self.whitelists.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallIPSWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallIPSWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallListRequest(TeaModel):
    def __init__(
        self,
        connect_sub_type: str = None,
        current_page: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        peer_uid: str = None,
        region_no: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
        vpc_id: str = None,
    ):
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type
        # The number of the page to return.
        # 
        # Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The number of entries to return on each page.
        # 
        # Default value: **10**. Maximum value: **50**.
        self.page_size = page_size
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.peer_uid = peer_uid
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.peer_uid is not None:
            result['PeerUid'] = self.peer_uid
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PeerUid') is not None:
            self.peer_uid = m.get('PeerUid')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig(TeaModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the local VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries of the local VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the local VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc(TeaModel):
    def __init__(
        self,
        authorization_status: str = None,
        owner_id: int = None,
        region_no: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether Cloud Firewall is authorized to access the local VPC. The value is fixed as authorized, which indicates that Cloud Firewall is authorized to access the local VPC.
        self.authorization_status = authorization_status
        # The UID of the Alibaba Cloud account to which the local VPC belongs.
        self.owner_id = owner_id
        # The region ID of the local VPC.
        self.region_no = region_no
        # An array that consists of the CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the local VPC.
        self.vpc_id = vpc_id
        # The name of the local VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the peer VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList(TeaModel):
    def __init__(
        self,
        route_entry_list: List[DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries of the peer VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the peer VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc(TeaModel):
    def __init__(
        self,
        authorization_status: str = None,
        owner_id: int = None,
        region_no: str = None,
        vpc_cidr_table_list: List[DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether Cloud Firewall is authorized to access the peer VPC. The value is fixed as **authorized**, which indicates that Cloud Firewall is authorized to access the peer VPC.
        self.authorization_status = authorization_status
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.owner_id = owner_id
        # The region ID of the peer VPC.
        self.region_no = region_no
        # An array that consists of the CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the peer VPC.
        self.vpc_id = vpc_id
        # The name of the peer VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewalls(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        connect_sub_type: str = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        ips_config: DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig = None,
        local_vpc: DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc = None,
        member_uid: str = None,
        peer_vpc: DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc = None,
        region_status: str = None,
        result_code: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates an Express Connect connection.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status
        # The intrusion prevention system (IPS) configurations.
        self.ips_config = ips_config
        # The details about the local VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **Empty string**: You can create a VPC firewall for the network instance.
        self.result_code = result_code
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.local_vpc:
            self.local_vpc.validate()
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpc') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc()
            self.peer_vpc = temp_model.from_map(m['PeerVpc'])
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_firewalls: List[DescribeVpcFirewallListResponseBodyVpcFirewalls] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of VPC firewalls.
        self.total_count = total_count
        # The information about the VPC firewalls.
        self.vpc_firewalls = vpc_firewalls

    def validate(self):
        if self.vpc_firewalls:
            for k in self.vpc_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcFirewalls'] = []
        if self.vpc_firewalls is not None:
            for k in self.vpc_firewalls:
                result['VpcFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_firewalls = []
        if m.get('VpcFirewalls') is not None:
            for k in m.get('VpcFirewalls'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallPolicyPriorUsedRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        vpc_firewall_id: str = None,
    ):
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The ID of the access control policy group. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # *   If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\\*\\*\\*\\*.
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallPolicyPriorUsedResponseBody(TeaModel):
    def __init__(
        self,
        end: int = None,
        request_id: str = None,
        start: int = None,
    ):
        # The lowest priority for the access control policies.
        self.end = end
        # The request ID.
        self.request_id = request_id
        # The highest priority for the access control policies.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeVpcFirewallPolicyPriorUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcFirewallPolicyPriorUsedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallPolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcListLiteRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_no: str = None,
        source_ip: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The region ID of the VPC.
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcListLiteResponseBodyVpcList(TeaModel):
    def __init__(
        self,
        region_no: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The region ID of the VPC.
        self.region_no = region_no
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcListLiteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_list: List[DescribeVpcListLiteResponseBodyVpcList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the VPCs.
        self.vpc_list = vpc_list

    def validate(self):
        if self.vpc_list:
            for k in self.vpc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VpcList'] = []
        if self.vpc_list is not None:
            for k in self.vpc_list:
                result['VpcList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k in m.get('VpcList'):
                temp_model = DescribeVpcListLiteResponseBodyVpcList()
                self.vpc_list.append(temp_model.from_map(k))
        return self


class DescribeVpcListLiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcListLiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcListLiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcZoneRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        lang: str = None,
        member_uid: str = None,
        region_no: str = None,
    ):
        # The environment. Valid values:
        # 
        # *   **VPC**\
        # *   **TransitRouter**\
        self.environment = environment
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid
        # The region ID.
        # 
        # This parameter is required.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeVpcZoneResponseBodyZoneList(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        # The name of the zone.
        self.local_name = local_name
        # The zone ID.
        self.zone_id = zone_id
        # The zone type. Default value: AvailabilityZone. This value indicates Alibaba Cloud zones.
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeVpcZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: List[DescribeVpcZoneResponseBodyZoneList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The zones.
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            for k in self.zone_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ZoneList'] = []
        if self.zone_list is not None:
            for k in self.zone_list:
                result['ZoneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zone_list = []
        if m.get('ZoneList') is not None:
            for k in m.get('ZoneList'):
                temp_model = DescribeVpcZoneResponseBodyZoneList()
                self.zone_list.append(temp_model.from_map(k))
        return self


class DescribeVpcZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcZoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulnerabilityProtectedListRequest(TeaModel):
    def __init__(
        self,
        attack_type: str = None,
        buy_version: int = None,
        current_page: str = None,
        end_time: str = None,
        lang: str = None,
        member_uid: str = None,
        order: str = None,
        page_size: str = None,
        sort_key: str = None,
        source_ip: str = None,
        start_time: str = None,
        user_type: str = None,
        vuln_cve_name: str = None,
        vuln_level: str = None,
        vuln_resource: str = None,
        vuln_status: str = None,
        vuln_type: str = None,
    ):
        # The attack type of the vulnerability prevention event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leakage
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: webshell
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # >  If you do not specify this parameter, the intrusion events of all attack types are queried.
        self.attack_type = attack_type
        # The edition of Cloud Firewall. If you use Cloud Firewall that uses the pay-as-you-go billing method, set the value to 10. You do not need to specify this parameter for other editions.
        self.buy_version = buy_version
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The order in which you want to sort the queried information. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order
        # The number of entries to return on each page. Maximum value: 50.
        self.page_size = page_size
        # The sorting basis. Set the value to **attackCnt**, which indicates the number of attacks.
        self.sort_key = sort_key
        # The IP address of the access source.
        self.source_ip = source_ip
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the user. Set the value to **buy**, which indicates user of a paid edition of Cloud Firewall.
        self.user_type = user_type
        # The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        self.vuln_cve_name = vuln_cve_name
        # The risk level of the vulnerability. Valid values:
        # 
        # *   **high**\
        # *   **medium**\
        # *   **low**\
        self.vuln_level = vuln_level
        # The number of assets that are affected by the vulnerability.
        self.vuln_resource = vuln_resource
        # The status of vulnerability protection. Valid values:
        # 
        # *   **partProtected**: partially protected
        # *   **protected**: protected
        # *   **unProtected**: unprotected
        self.vuln_status = vuln_status
        # The type of the vulnerability. Valid values:
        # 
        # *   **App**: application vulnerability
        # *   **emg**: urgent vulnerability
        # *   **cms**: Web-CMS vulnerability
        self.vuln_type = vuln_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.vuln_cve_name is not None:
            result['VulnCveName'] = self.vuln_cve_name
        if self.vuln_level is not None:
            result['VulnLevel'] = self.vuln_level
        if self.vuln_resource is not None:
            result['VulnResource'] = self.vuln_resource
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        if self.vuln_type is not None:
            result['VulnType'] = self.vuln_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VulnCveName') is not None:
            self.vuln_cve_name = m.get('VulnCveName')
        if m.get('VulnLevel') is not None:
            self.vuln_level = m.get('VulnLevel')
        if m.get('VulnResource') is not None:
            self.vuln_resource = m.get('VulnResource')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        if m.get('VulnType') is not None:
            self.vuln_type = m.get('VulnType')
        return self


class DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList(TeaModel):
    def __init__(
        self,
        eip: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        vuln_status: str = None,
    ):
        # The elastic IP address (EIP) that is associated with the instance.
        self.eip = eip
        # The public IP address of the instance.
        self.internet_ip = internet_ip
        # The private IP address of the instance.
        self.intranet_ip = intranet_ip
        # The region ID of your Cloud Firewall.
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_id = region_id
        # The ID of the instance.
        self.resource_id = resource_id
        # The name of the instance.
        self.resource_name = resource_name
        # The type of the asset. Valid values:
        # 
        # *   **SLB**\
        # *   **EIP**\
        # *   **ECS**\
        self.resource_type = resource_type
        # The status of the vulnerability prevention feature. Valid values:
        # 
        # *   **partProtected**: enabled for partial assets
        # *   **protected**: enabled
        # *   **unProtected**: disabled
        self.vuln_status = vuln_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        return self


class DescribeVulnerabilityProtectedListResponseBodyVulnList(TeaModel):
    def __init__(
        self,
        attack_cnt: int = None,
        attack_type: int = None,
        basic_rule_ids: str = None,
        cve_id: str = None,
        first_time: int = None,
        highlight_tag: int = None,
        last_time: int = None,
        member_uid: str = None,
        need_open_basic_rule: bool = None,
        need_open_basic_rule_uuids: str = None,
        need_open_run_mode: bool = None,
        need_open_virtual_patche: bool = None,
        need_open_virtual_patche_uuids: str = None,
        need_rule_class: int = None,
        resource_cnt: int = None,
        resource_list: List[DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList] = None,
        virtual_patche_ids: str = None,
        vuln_key: str = None,
        vuln_level: str = None,
        vuln_name: str = None,
        vuln_status: str = None,
        vuln_type: str = None,
    ):
        # The number of vulnerability attacks.
        self.attack_cnt = attack_cnt
        # The attack type of the vulnerability prevention event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leakage
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: webshell
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        self.attack_type = attack_type
        # The IDs of associated basic protection policies.
        self.basic_rule_ids = basic_rule_ids
        # The CVE IDs.
        self.cve_id = cve_id
        # The time when the first attack was launched.
        self.first_time = first_time
        # Indicates whether you need to pay special attention to the vulnerability. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.highlight_tag = highlight_tag
        # The time when the last attack was launched.
        self.last_time = last_time
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # Indicates whether the basic protection policy that related to the vulnerability is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If the value of this parameter is true, you must set the action of the basic protection policy related to the vulnerability to Block.
        self.need_open_basic_rule = need_open_basic_rule
        # The UUIDs of the basic protection policies for which the action needs to be changed to Block.
        self.need_open_basic_rule_uuids = need_open_basic_rule_uuids
        # Indicates whether Threat Engine Mode needs to be configured when you enable protection. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.need_open_run_mode = need_open_run_mode
        # Indicates whether the virtual patching policy that related to the vulnerability is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If the value of this parameter is true, you must set the action of the virtual patching policy that related to the vulnerability to Block.
        self.need_open_virtual_patche = need_open_virtual_patche
        # The UUIDs of the virtual patching policies for which the action needs to be changed to Block.
        self.need_open_virtual_patche_uuids = need_open_virtual_patche_uuids
        # The type of the rule group. Valid values:
        # 
        # *   **1** (default): loose
        # *   **2**: medium
        # *   **3**: strict
        self.need_rule_class = need_rule_class
        # The number of assets on which vulnerabilities are detected.
        self.resource_cnt = resource_cnt
        # The assets on which the vulnerability is detected.
        self.resource_list = resource_list
        # The IDs of associated virtual patching policies.
        self.virtual_patche_ids = virtual_patche_ids
        # The code of the vulnerability.
        self.vuln_key = vuln_key
        # The risk level of the vulnerability. Valid values:
        # 
        # *   **high**\
        # *   **medium**\
        # *   **low**\
        self.vuln_level = vuln_level
        # The name of the vulnerability.
        self.vuln_name = vuln_name
        # The status of the vulnerability prevention feature. Valid values:
        # 
        # *   **partProtected**: enabled for partial assets
        # *   **protected**: enabled
        # *   **unProtected**: disabled
        self.vuln_status = vuln_status
        # The type of the vulnerability. Valid values:
        # 
        # *   **emg**: urgent vulnerability
        # *   **webcms**: Web-CMS vulnerability
        # *   **app**: application vulnerability
        self.vuln_type = vuln_type

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.basic_rule_ids is not None:
            result['BasicRuleIds'] = self.basic_rule_ids
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.highlight_tag is not None:
            result['HighlightTag'] = self.highlight_tag
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.need_open_basic_rule is not None:
            result['NeedOpenBasicRule'] = self.need_open_basic_rule
        if self.need_open_basic_rule_uuids is not None:
            result['NeedOpenBasicRuleUuids'] = self.need_open_basic_rule_uuids
        if self.need_open_run_mode is not None:
            result['NeedOpenRunMode'] = self.need_open_run_mode
        if self.need_open_virtual_patche is not None:
            result['NeedOpenVirtualPatche'] = self.need_open_virtual_patche
        if self.need_open_virtual_patche_uuids is not None:
            result['NeedOpenVirtualPatcheUuids'] = self.need_open_virtual_patche_uuids
        if self.need_rule_class is not None:
            result['NeedRuleClass'] = self.need_rule_class
        if self.resource_cnt is not None:
            result['ResourceCnt'] = self.resource_cnt
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.virtual_patche_ids is not None:
            result['VirtualPatcheIds'] = self.virtual_patche_ids
        if self.vuln_key is not None:
            result['VulnKey'] = self.vuln_key
        if self.vuln_level is not None:
            result['VulnLevel'] = self.vuln_level
        if self.vuln_name is not None:
            result['VulnName'] = self.vuln_name
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        if self.vuln_type is not None:
            result['VulnType'] = self.vuln_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BasicRuleIds') is not None:
            self.basic_rule_ids = m.get('BasicRuleIds')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('HighlightTag') is not None:
            self.highlight_tag = m.get('HighlightTag')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NeedOpenBasicRule') is not None:
            self.need_open_basic_rule = m.get('NeedOpenBasicRule')
        if m.get('NeedOpenBasicRuleUuids') is not None:
            self.need_open_basic_rule_uuids = m.get('NeedOpenBasicRuleUuids')
        if m.get('NeedOpenRunMode') is not None:
            self.need_open_run_mode = m.get('NeedOpenRunMode')
        if m.get('NeedOpenVirtualPatche') is not None:
            self.need_open_virtual_patche = m.get('NeedOpenVirtualPatche')
        if m.get('NeedOpenVirtualPatcheUuids') is not None:
            self.need_open_virtual_patche_uuids = m.get('NeedOpenVirtualPatcheUuids')
        if m.get('NeedRuleClass') is not None:
            self.need_rule_class = m.get('NeedRuleClass')
        if m.get('ResourceCnt') is not None:
            self.resource_cnt = m.get('ResourceCnt')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('VirtualPatcheIds') is not None:
            self.virtual_patche_ids = m.get('VirtualPatcheIds')
        if m.get('VulnKey') is not None:
            self.vuln_key = m.get('VulnKey')
        if m.get('VulnLevel') is not None:
            self.vuln_level = m.get('VulnLevel')
        if m.get('VulnName') is not None:
            self.vuln_name = m.get('VulnName')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        if m.get('VulnType') is not None:
            self.vuln_type = m.get('VulnType')
        return self


class DescribeVulnerabilityProtectedListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vuln_list: List[DescribeVulnerabilityProtectedListResponseBodyVulnList] = None,
        zero_resource_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of vulnerabilities that are detected by Cloud Firewall.
        self.total_count = total_count
        # The vulnerabilities.
        self.vuln_list = vuln_list
        # The number of assets on which no vulnerabilities are detected.
        self.zero_resource_count = zero_resource_count

    def validate(self):
        if self.vuln_list:
            for k in self.vuln_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VulnList'] = []
        if self.vuln_list is not None:
            for k in self.vuln_list:
                result['VulnList'].append(k.to_map() if k else None)
        if self.zero_resource_count is not None:
            result['ZeroResourceCount'] = self.zero_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vuln_list = []
        if m.get('VulnList') is not None:
            for k in m.get('VulnList'):
                temp_model = DescribeVulnerabilityProtectedListResponseBodyVulnList()
                self.vuln_list.append(temp_model.from_map(k))
        if m.get('ZeroResourceCount') is not None:
            self.zero_resource_count = m.get('ZeroResourceCount')
        return self


class DescribeVulnerabilityProtectedListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVulnerabilityProtectedListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVulnerabilityProtectedListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAddressBookRequestTagList(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of ECS tag N that you want to match.
        self.tag_key = tag_key
        # The value of ECS tag N that you want to match.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyAddressBookRequest(TeaModel):
    def __init__(
        self,
        address_list: str = None,
        auto_add_tag_ecs: str = None,
        description: str = None,
        group_name: str = None,
        group_uuid: str = None,
        lang: str = None,
        modify_mode: str = None,
        source_ip: str = None,
        tag_list: List[ModifyAddressBookRequestTagList] = None,
        tag_relation: str = None,
    ):
        # The addresses in the address book. Separate multiple addresses with commas (,). If you set GroupType to **ip**, **port**, or **domain**, you must specify this parameter.
        # 
        # *   If you set GroupType to **ip**, you must specify IP addresses for the address book. Example: 1.2.XX.XX/32,1.2.XX.XX/24.
        # *   If you set GroupType to **port**, you must specify port numbers or port ranges for the address book. Example: 80/80,100/200.
        # *   If you set GroupType to **domain**, you must specify domain names for the address book. Example: demo1.aliyun.com,demo2.aliyun.com.
        self.address_list = address_list
        # Specifies whether to automatically add public IP addresses of Elastic Compute Service (ECS) instances to the address book if the instances match the specified tags. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        # 
        # This parameter is required.
        self.description = description
        # The name of the address book.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ID of the address book.
        # 
        # >  To modify the address book, you must provide the ID of the address book. You can call the [DescribeAddressBook](https://help.aliyun.com/document_detail/138869.html) operation to query the ID.
        # 
        # This parameter is required.
        self.group_uuid = group_uuid
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # Modification mode with the following values:
        # 
        # - **Cover**: Use the value of the AddressList parameter to overwrite the original address book.
        # - **Append**: After the original address book, append addresses using the value of the AddressList parameter.
        # - **Delete**: Delete addresses using the value of the AddressList parameter from the address book.
        # 
        # >When GroupType is **ip**, **ipv6**, **port**, or **domain**, if this parameter is not configured, the default is to use the **Cover** method to modify the address book.
        # >Notice: When GroupType is **tag**, this parameter must be empty.</notice>
        self.modify_mode = modify_mode
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ECS tags that you want to match.
        self.tag_list = tag_list
        # The logical relationship among ECS tags. Valid values:
        # 
        # *   **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # *   **or**: The public IP addresses of ECS instances that match one of the specified tags can be added to the address book.
        self.tag_relation = tag_relation

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ModifyAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class ModifyAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
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
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The UUID of the access control policy.
        # 
        # >  To modify an access control policy, you must specify the UUID of the policy. You can call the [DescribeControlPolicy](https://help.aliyun.com/document_detail/138866.html) interface to query the UUID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The type of the application that the access control policy supports. Valid values:
        # 
        # *   **ANY**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **MySQL**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **RDP**\
        # *   **VNC**\
        # *   **SSH**\
        # *   **Redis**\
        # *   **MQTT**\
        # *   **MongoDB**\
        # *   **Memcache**\
        # *   **SSL**\
        # 
        # >  The value **ANY** indicates all types of applications.
        # 
        # >  You must specify one of the ApplicationNameList and ApplicationName parameters. If you configure both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name = application_name
        # The application names.
        # 
        # >  You must specify one of the ApplicationNameList and ApplicationName parameters. If you configure both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to net, the value of **Destination** is a CIDR block. Example: 1.2.XX.XX/24.
        # *   If **DestinationType** is set to group, the value of **Destination** is an address book. Example: db_group.
        # *   If **DestinationType** is set to domain, the value of **Destination** is a domain name. Example: \\*.aliyuncs.com.
        # *   If **DestinationType** is set to location, the value of **Destination** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: ["BJ11", "ZB"].
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: location
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of StartTime.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.end_time = end_time
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The protocol type that the access control policy supports. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # 
        # >  The value **ANY** indicates all types of applications.
        # 
        # >  If the traffic direction is outbound and the destination address is a threat intelligence address book of the domain name type or a cloud service address book, you can set Proto to TCP or ANY. If you set Proto to TCP, you can set ApplicationName to HTTP, HTTPS, SMTP, SMTPS, and SSL. If you set Proto to ANY, you can set ApplicationName to ANY.
        # 
        # This parameter is required.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If you set RepeatType to `Permanent`, `None`, or `Daily`, the value of this parameter is an empty array. Example: []
        # *   If you set RepeatType to Weekly, you must specify this parameter. Example: [0, 6]
        # 
        # >  If you set RepeatType to Weekly, the fields in the value of this parameter cannot be repeated.
        # 
        # *   If you set RepeatType to `Monthly`, you must specify this parameter. Example: [1, 31]
        # 
        # >  If you set RepeatType to Monthly, the fields in the value of this parameter cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of RepeatStartTime.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of RepeatEndTime.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
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
        # *   If **SourceType** is set to net, the value of **Source** is a CIDR block. Example: 1.2.XX.XX/24.
        # *   If **SourceType** is set to group, the value of **Source** is an address book. Example: db_group.
        # *   If **SourceType** is set to location, the value of **Source** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: ["BJ11", "ZB"]
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of EndTime.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
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


class ModifyControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyPositionRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        lang: str = None,
        new_order: str = None,
        old_order: str = None,
        source_ip: str = None,
    ):
        # The direction of the traffic to which the IPv4 access control policy applies. Valid values:
        # 
        # *   in: inbound traffic
        # *   out: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   zh: Chinese (default)
        # *   en: English
        self.lang = lang
        # The new priority of the IPv4 access control policy. You must specify a numeric value for this parameter. The value 1 indicates the highest priority. A larger value indicates a lower priority.
        # 
        # >  The new priority cannot exceed the priority range of the IPv4 access control policy. Otherwise, an error occurs when you call this operation. Before you call this operation, we recommend that you use the [DescribePolicyPriorUsed](https://help.aliyun.com/document_detail/138862.html) operation to query the priority range of the IPv4 access control policy in the specified direction.
        # 
        # This parameter is required.
        self.new_order = new_order
        # The original priority of the IPv4 access control policy.
        # 
        # This parameter is required.
        self.old_order = old_order
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyControlPolicyPositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyControlPolicyPositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyControlPolicyPositionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefaultIPSConfigRequest(TeaModel):
    def __init__(
        self,
        basic_rules: str = None,
        cti_rules: str = None,
        lang: str = None,
        max_sdl: int = None,
        patch_rules: str = None,
        rule_class: str = None,
        run_mode: str = None,
    ):
        # Specifies whether to enable basic protection. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.basic_rules = basic_rules
        # Specifies whether to enable threat intelligence. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.cti_rules = cti_rules
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        self.max_sdl = max_sdl
        # Specifies whether to enable virtual patching. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.patch_rules = patch_rules
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        # 
        # This parameter is required.
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.cti_rules is not None:
            result['CtiRules'] = self.cti_rules
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_sdl is not None:
            result['MaxSdl'] = self.max_sdl
        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('CtiRules') is not None:
            self.cti_rules = m.get('CtiRules')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxSdl') is not None:
            self.max_sdl = m.get('MaxSdl')
        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class ModifyDefaultIPSConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDefaultIPSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDefaultIPSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirewallV2RoutePolicySwitchRequest(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        tr_firewall_route_policy_id: str = None,
        tr_firewall_route_policy_switch_status: str = None,
    ):
        # The instance ID of the virtual private cloud (VPC) firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to restore the traffic redirection configurations. Valid values:
        # 
        # *   true: roll back
        # *   false: withdraw
        self.should_recover = should_recover
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id
        # The status of the routing policy. Valid values:
        # 
        # *   open: enabled
        # *   close: disabled
        self.tr_firewall_route_policy_switch_status = tr_firewall_route_policy_switch_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        if self.tr_firewall_route_policy_switch_status is not None:
            result['TrFirewallRoutePolicySwitchStatus'] = self.tr_firewall_route_policy_switch_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        if m.get('TrFirewallRoutePolicySwitchStatus') is not None:
            self.tr_firewall_route_policy_switch_status = m.get('TrFirewallRoutePolicySwitchStatus')
        return self


class ModifyFirewallV2RoutePolicySwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFirewallV2RoutePolicySwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFirewallV2RoutePolicySwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFirewallV2RoutePolicySwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMemberAttributesRequestMembers(TeaModel):
    def __init__(
        self,
        member_desc: str = None,
        member_uid: int = None,
    ):
        # The remarks of the member in Cloud Firewall.
        # 
        # This parameter is required.
        self.member_desc = member_desc
        # The UID of the member in Cloud Firewall.
        # 
        # This parameter is required.
        self.member_uid = member_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class ModifyInstanceMemberAttributesRequest(TeaModel):
    def __init__(
        self,
        members: List[ModifyInstanceMemberAttributesRequestMembers] = None,
    ):
        # The members that to be modified.
        # 
        # This parameter is required.
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = ModifyInstanceMemberAttributesRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class ModifyInstanceMemberAttributesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceMemberAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceMemberAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMemberAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNatFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
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
        lang: str = None,
        nat_gateway_id: str = None,
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
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The UUID of the access control policy.
        # 
        # To modify the configurations of an access control policy, you must provide the UUID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The name of the application.
        self.application_name_list = application_name_list
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy.
        # 
        # > If **DestPortType** is set to `port`, you must specify this parameter.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to net, the value of **Destination** is a CIDR block. Example: 1.2.3.4/24
        # *   If **DestinationType** is set to group, the value of **Destination** is an address book. Example: db_group
        # *   If **DestinationType** is set to domain, the value of **Destination** is a domain name. Example: \\*.aliyuncs.com
        # *   If **DestinationType** is set to location, the value of **Destination** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: ["BJ11", "ZB"]
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: destination location
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid value:
        # 
        # *   **out**: outbound.
        self.direction = direction
        # The domain name resolution method of the access control policy. Valid values:
        # 
        # *   **0**: Fully qualified domain name (FQDN)-based resolution
        # *   **1**: Domain Name System (DNS)-based dynamic resolution
        # *   **2**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of StartTime.
        # 
        # >  If RepeatType is set to Permanent, EndTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, EndTime must be specified.
        self.end_time = end_time
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # 
        # >  The value **ANY** indicates all types of applications.
        # 
        # >  If the destination address type is a threat intelligence address book of the domain name type or a cloud service address book, you can set Proto to TCP. If you set Proto to TCP, you can set application types to HTTP, HTTPS, SMTP, SMTPS, and SSL.
        # 
        # This parameter is required.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
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
        # >  If RepeatType is set to Permanent or None, RepeatEndTime is left empty. If RepeatType is set to Daily, Weekly, or Monthly, RepeatEndTime must be specified.
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
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of this parameter is a CIDR block. Example: 10.2.XX.XX/24.
        # *   If **SourceType** is set to `group`, the value of this parameter is an address book name. Example: db_group.
        # 
        # This parameter is required.
        self.source = source
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of EndTime.
        # 
        # >  If RepeatType is set to Permanent, StartTime is left empty. If RepeatType is set to None, Daily, Weekly, or Monthly, StartTime must be specified.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
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


class ModifyNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNatFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNatFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNatFirewallControlPolicyPositionRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        direction: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        new_order: int = None,
    ):
        # The UUID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The direction of the traffic to which the access control policy applies.
        # 
        # *   Set the value to **out**.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The new priority of the IPv4 access control policy. You must specify a numeric value for this parameter. The value 1 indicates the highest priority. A larger value indicates a lower priority.
        # 
        # > Make sure that the value of this parameter is within the priority range of existing IPv4 access control policies. Otherwise, an error occurs when you call this operation.
        # 
        # Before you call this operation, we recommend that you call the DescribeNatFirewallPolicyPriorUsed operation to query the priority range of the IPv4 access control policies in the specified traffic direction.
        # 
        # This parameter is required.
        self.new_order = new_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        return self


class ModifyNatFirewallControlPolicyPositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNatFirewallControlPolicyPositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNatFirewallControlPolicyPositionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNatFirewallControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyObjectGroupOperationRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        direction: str = None,
        lang: str = None,
        object_list: List[str] = None,
        object_operation: str = None,
        object_type: str = None,
        source_ip: str = None,
    ):
        # The remarks of the operation.
        self.comment = comment
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound.
        # *   **out**: outbound.
        # 
        # This parameter is required.
        self.direction = direction
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The operation objects.
        # 
        # This parameter is required.
        self.object_list = object_list
        # The operation. Valid values:
        # 
        # *   **ignore**: adds the operation object to the whitelist.
        # *   **cancelIgnore**: removes the operation object from the whitelist.
        # *   **subscribe**: follows the operation object.
        # *   **unsubscribe**: unfollows the operation object.
        # 
        # This parameter is required.
        self.object_operation = object_operation
        # The type of the operation object.
        # 
        # Valid values:
        # 
        # *   **assetsIp**: the asset IP address.
        # *   **destinationIp**: the destination IP address.
        # *   **destinationPort**: the destination port.
        # *   **destinationDomain**: the destination domain name.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.object_list is not None:
            result['ObjectList'] = self.object_list
        if self.object_operation is not None:
            result['ObjectOperation'] = self.object_operation
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ObjectList') is not None:
            self.object_list = m.get('ObjectList')
        if m.get('ObjectOperation') is not None:
            self.object_operation = m.get('ObjectOperation')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyObjectGroupOperationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyObjectGroupOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyObjectGroupOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyObjectGroupOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyAdvancedConfigRequest(TeaModel):
    def __init__(
        self,
        internet_switch: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # Specifies whether to enable the strict mode for the access control policy. Valid values:
        # 
        # *   **on**: enables the strict mode.
        # *   **off**: disables the strict mode.
        # 
        # This parameter is required.
        self.internet_switch = internet_switch
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyPolicyAdvancedConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPolicyAdvancedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyAdvancedConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrFirewallV2ConfigurationRequest(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        firewall_name: str = None,
        lang: str = None,
    ):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The instance name of the VPC firewall.
        self.firewall_name = firewall_name
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ModifyTrFirewallV2ConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTrFirewallV2ConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTrFirewallV2ConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTrFirewallV2ConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList(TeaModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequest(TeaModel):
    def __init__(
        self,
        dest_candidate_list: List[ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        src_candidate_list: List[ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList] = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The instance ID of the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *  **zh** (default): Chinese
        # *  **en**: English
        self.lang = lang
        # Specifies whether to restore the traffic redirection configurations. Valid values:
        # 
        # *   true: roll back
        # *   false: withdraw
        self.should_recover = should_recover
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list
        # The ID of the routing policy.
        # 
        # This parameter is required.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeShrinkRequest(TeaModel):
    def __init__(
        self,
        dest_candidate_list_shrink: str = None,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        src_candidate_list_shrink: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list_shrink = dest_candidate_list_shrink
        # The instance ID of the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *  **zh** (default): Chinese
        # *  **en**: English
        self.lang = lang
        # Specifies whether to restore the traffic redirection configurations. Valid values:
        # 
        # *   true: roll back
        # *   false: withdraw
        self.should_recover = should_recover
        # The primary traffic redirection instances.
        self.src_candidate_list_shrink = src_candidate_list_shrink
        # The ID of the routing policy.
        # 
        # This parameter is required.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_candidate_list_shrink is not None:
            result['DestCandidateList'] = self.dest_candidate_list_shrink
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover
        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')
        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTrFirewallV2RoutePolicyScopeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTrFirewallV2RoutePolicyScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserIPSWhitelistRequest(TeaModel):
    def __init__(
        self,
        direction: int = None,
        ip_version: str = None,
        lang: str = None,
        list_type: int = None,
        list_value: str = None,
        source_ip: str = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.ip_version = ip_version
        self.lang = lang
        self.list_type = list_type
        self.list_value = list_value
        self.source_ip = source_ip
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class ModifyUserIPSWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserIPSWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserIPSWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUserIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class ModifyVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallCenConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallCenSwitchStatusRequest(TeaModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id: str = None,
    ):
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: yes
        # *   **close**: no
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallCenSwitchStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallCenSwitchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallCenSwitchStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallCenSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        local_vpc_cidr_table_list: str = None,
        member_uid: str = None,
        peer_vpc_cidr_table_list: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The CIDR blocks of the local VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the local VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the local VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the local VPC.
        # 
        # > You can call the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR blocks of local VPCs for VPC firewalls.
        # 
        # This parameter is required.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The CIDR blocks of the peer VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the peer VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the peer VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the peer VPC.
        # 
        # > You can call the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR blocks of peer VPCs for VPC firewalls.
        # 
        # This parameter is required.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class ModifyVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallConfigureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallConfigureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        application_name: str = None,
        application_name_list: List[str] = None,
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        domain_resolve_type: str = None,
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
        vpc_firewall_id: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: blocks the traffic.
        # *   **log**: monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        # 
        # If you want to modify the configurations of an access control policy, you must provide the unique ID of the policy. You can call the [DescribeVpcFirewallControlPolicy](https://help.aliyun.com/document_detail/159758.html) operation to query the ID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The type of the application that the access control policy supports.
        # 
        # Valid values:
        # 
        # *   ANY: all application types
        # *   FTP
        # *   HTTP
        # *   HTTPS
        # *   MySQL
        # *   SMTP
        # *   SMTPS
        # *   RDP
        # *   VNC
        # *   SSH
        # *   Redis
        # *   MQTT
        # *   MongoDB
        # *   Memcache
        # *   SSL
        self.application_name = application_name
        # The application names.
        self.application_name_list = application_name_list
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination port in the access control policy.
        self.dest_port = dest_port
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group
        # The type of the destination port in the access control policy.
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to `net`, the value of this parameter must be a CIDR block.
        # 
        #     Example: 10.2.3.0/24
        # 
        # *   If **DestinationType** is set to `group`, the value of this parameter must be an address book name.
        # 
        #     Example: db_group
        # 
        # *   If **DestinationType** is set to `domain`, the value of this parameter must be a domain name.
        # 
        #     Example: \\*.aliyuncs.com
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
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # * **FQDN**: fully qualified domain name (FQDN)-based resolution
        # * **DNS**: DNS-based dynamic resolution
        # * **FQDN_AND_DNS**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type
        # The time when the access control policy stops taking effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of StartTime.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.end_time = end_time
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The protocol type in the access control policy.
        # 
        # Valid values:
        # 
        # *   ANY: all protocol types
        # *   TCP
        # *   UDP
        # *   ICMP
        # 
        # This parameter is required.
        self.proto = proto
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: enables the access control policy.
        # *   **false**: disables the access control policy.
        self.release = release
        # The days of a week or of a month on which the access control policy takes effect.
        # 
        # *   If you set RepeatType to `Permanent`, `None`, or `Daily`, the value of this parameter is an empty array. Example: [].
        # *   If you set RepeatType to Weekly, you must specify this parameter. Example: [0, 6].
        # 
        # >  If you set RepeatType to Weekly, the fields in the value of this parameter cannot be repeated.
        # 
        # *   If you set RepeatType to `Monthly`, you must specify this parameter. Example: [1, 31].
        # 
        # >  If you set RepeatType to Monthly, the fields in the value of this parameter cannot be repeated.
        self.repeat_days = repeat_days
        # The point in time when the recurrence ends. Example: 23:30. The value must be on the hour or on the half hour, and at least 30 minutes later than the value of RepeatStartTime.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
        self.repeat_end_time = repeat_end_time
        # The point in time when the recurrence starts. Example: 08:00. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of RepeatEndTime.
        # 
        # >  If you set RepeatType to Permanent or None, leave this parameter empty. If you set RepeatType to Daily, Weekly, or Monthly, you must specify this parameter.
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
        # *   If **SourceType** is set to `net`, the value of this parameter must be a CIDR block.
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
        # *   **net**: CIDR block
        # *   **group**: address book
        # 
        # This parameter is required.
        self.source_type = source_type
        # The time when the access control policy starts to take effect. The value is a UNIX timestamp. Unit: seconds. The value must be on the hour or on the half hour, and at least 30 minutes earlier than the value of EndTime.
        # 
        # >  If you set RepeatType to Permanent, leave this parameter empty. If you set RepeatType to None, Daily, Weekly, or Monthly, you must specify this parameter.
        self.start_time = start_time
        # The instance ID of the VPC firewall. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\\*\\*\\*\\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*\
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
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
        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type
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
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
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
        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')
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
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyPositionRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
        new_order: str = None,
        old_order: str = None,
        vpc_firewall_id: str = None,
    ):
        # The UUID of the access control policy.
        # 
        # If you want to modify the configurations of an access control policy, you must provide the UUID of the policy. You can call the [DescribeVpcFirewallControlPolicy](https://help.aliyun.com/document_detail/159758.html) operation to query the UUID.
        self.acl_uuid = acl_uuid
        # The language of the content within the request and the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The new priority of the access control policy.
        # 
        # >  For more information about the valid values of the new priority, see [DescribeVpcFirewallPolicyPriorUsed](https://help.aliyun.com/document_detail/474145.html).
        # 
        # This parameter is required.
        self.new_order = new_order
        # The original priority of the access control policy.
        # 
        # > This parameter is not recommended. We recommend that you use the AclUuid parameter to specify the policy that you want to modify.
        self.old_order = old_order
        # The ID of the group to which the access control policy belongs. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # Valid values:
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\\*\\*\\*\\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*\
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallControlPolicyPositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallControlPolicyPositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallControlPolicyPositionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallDefaultIPSConfigRequest(TeaModel):
    def __init__(
        self,
        basic_rules: str = None,
        enable_all_patch: str = None,
        lang: str = None,
        member_uid: str = None,
        rule_class: str = None,
        run_mode: str = None,
        source_ip: str = None,
        vpc_firewall_id: str = None,
    ):
        # Specifies whether to enable basic protection. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        # 
        # This parameter is required.
        self.basic_rules = basic_rules
        # Specifies whether to enable virtual patching. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        # 
        # This parameter is required.
        self.enable_all_patch = enable_all_patch
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode.
        # *   **0**: monitor mode.
        # 
        # This parameter is required.
        self.run_mode = run_mode
        # The source IP address of the request.
        self.source_ip = source_ip
        # The instance ID of the VPC firewall.
        # 
        # *   If the VPC firewall protects traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the IDs of CEN instances.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall. You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallDefaultIPSConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallDefaultIPSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallDefaultIPSConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallIPSWhitelistRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        list_type: int = None,
        list_value: str = None,
        member_uid: int = None,
        vpc_firewall_id: str = None,
        white_type: int = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The type of the list. Valid values:
        # 
        # *   **1**: user-defined
        # *   **2**: address book
        # 
        # This parameter is required.
        self.list_type = list_type
        # The entry in the list.
        self.list_value = list_value
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
        # The type of the whitelist. Valid values:
        # 
        # *   **1**: destination
        # *   **2**: source
        # 
        # This parameter is required.
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class ModifyVpcFirewallIPSWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallIPSWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallIPSWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallSwitchStatusRequest(TeaModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id: str = None,
    ):
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: yes
        # *   **close**: no
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallSwitchStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVpcFirewallSwitchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVpcFirewallSwitchStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableAllFwSwitchRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The language of the content within the request and response. Valid values: Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutDisableAllFwSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutDisableAllFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutDisableAllFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutDisableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableFwSwitchRequest(TeaModel):
    def __init__(
        self,
        ipaddr_list: List[str] = None,
        lang: str = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
        source_ip: str = None,
    ):
        # The IP addresses.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.ipaddr_list = ipaddr_list
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The regions.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.region_list = region_list
        # The types of the assets.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.resource_type_list = resource_type_list
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutDisableFwSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutDisableFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutDisableFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutDisableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableAllFwSwitchRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutEnableAllFwSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutEnableAllFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEnableAllFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutEnableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableFwSwitchRequest(TeaModel):
    def __init__(
        self,
        ipaddr_list: List[str] = None,
        lang: str = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
        source_ip: str = None,
    ):
        # The IP addresses.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.ipaddr_list = ipaddr_list
        # The language of the content within the response.
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The regions.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.region_list = region_list
        # The types of the assets.
        # 
        # Valid values:
        # 
        # *   BastionHostIP: the egress IP address of a bastion host
        # *   BastionHostIngressIP: the ingress IP address of a bastion host
        # *   EcsEIP: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   EcsPublicIP: the public IP address of an ECS instance
        # *   EIP: the EIP
        # *   EniEIP: the EIP of an elastic network interface (ENI)
        # *   NatEIP: the EIP of a NAT gateway
        # *   SlbEIP: the EIP of a Server Load Balancer (SLB) instance
        # *   SlbPublicIP: the public IP address of an SLB instance
        # *   NatPublicIP: the public IP address of a NAT gateway
        # *   HAVIP: the high-availability virtual IP address (HAVIP)
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.resource_type_list = resource_type_list
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutEnableFwSwitchResponseBodyAbnormalResourceStatusList(TeaModel):
    def __init__(
        self,
        msg: str = None,
        resource: str = None,
        status: str = None,
    ):
        # The message displayed when the asset is not synchronized to Cloud Firewall. Valid values:
        # 
        # *   cloudfirewall do not sync this ip address: This IP address is not synchronized to Cloud Firewall.
        self.msg = msg
        # The IP address of the asset.
        self.resource = resource
        # The status of the asset when it is not synchronized to Cloud Firewall. Valid values:
        # 
        # *   ip_not_sync: The asset is not synchronized.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PutEnableFwSwitchResponseBody(TeaModel):
    def __init__(
        self,
        abnormal_resource_status_list: List[PutEnableFwSwitchResponseBodyAbnormalResourceStatusList] = None,
        request_id: str = None,
    ):
        # The status information of the asset when it is not synchronized to Cloud Firewall.
        self.abnormal_resource_status_list = abnormal_resource_status_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.abnormal_resource_status_list:
            for k in self.abnormal_resource_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AbnormalResourceStatusList'] = []
        if self.abnormal_resource_status_list is not None:
            for k in self.abnormal_resource_status_list:
                result['AbnormalResourceStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abnormal_resource_status_list = []
        if m.get('AbnormalResourceStatusList') is not None:
            for k in m.get('AbnormalResourceStatusList'):
                temp_model = PutEnableFwSwitchResponseBodyAbnormalResourceStatusList()
                self.abnormal_resource_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutEnableFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEnableFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutEnableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePostInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the Cloud Firewall instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleasePostInstanceResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        release_status: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether the release was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.release_status = release_status
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.release_status is not None:
            result['ReleaseStatus'] = self.release_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ReleaseStatus') is not None:
            self.release_status = m.get('ReleaseStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleasePostInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleasePostInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleasePostInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNatFirewallRuleHitCountRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
    ):
        # The UUID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class ResetNatFirewallRuleHitCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetNatFirewallRuleHitCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetNatFirewallRuleHitCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetNatFirewallRuleHitCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetVpcFirewallRuleHitCountRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
    ):
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The natural language of the request and response. 
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ResetVpcFirewallRuleHitCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetVpcFirewallRuleHitCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetVpcFirewallRuleHitCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetVpcFirewallRuleHitCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSecurityProxyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        proxy_id: str = None,
        switch: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**\
        self.lang = lang
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id
        # Specifies whether to enable the NAT firewall. Valid values:
        # 
        # *   open: yes
        # *   close: no
        # 
        # This parameter is required.
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.switch is not None:
            result['Switch'] = self.switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        return self


class SwitchSecurityProxyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchSecurityProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchSecurityProxyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchSecurityProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


