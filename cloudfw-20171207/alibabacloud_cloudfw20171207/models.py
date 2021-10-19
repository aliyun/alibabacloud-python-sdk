# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddAddressBookRequestTagList(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class AddAddressBookRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        address_list: str = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        auto_add_tag_ecs: str = None,
        tag_relation: str = None,
        tag_list: List[AddAddressBookRequestTagList] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.address_list = address_list
        self.description = description
        self.group_name = group_name
        self.group_type = group_type
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.tag_relation = tag_relation
        self.tag_list = tag_list

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
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = AddAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        return self


class AddAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        group_uuid: str = None,
        request_id: str = None,
    ):
        self.group_uuid = group_uuid
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
        body: AddAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddControlPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        acl_action: str = None,
        application_name: str = None,
        description: str = None,
        dest_port: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        proto: str = None,
        source: str = None,
        source_type: str = None,
        new_order: str = None,
        dest_port_type: str = None,
        dest_port_group: str = None,
        release: str = None,
        ip_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.acl_action = acl_action
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.destination = destination
        self.destination_type = destination_type
        self.direction = direction
        self.proto = proto
        self.source = source
        self.source_type = source_type
        self.new_order = new_order
        self.dest_port_type = dest_port_type
        self.dest_port_group = dest_port_group
        self.release = release
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.release is not None:
            result['Release'] = self.release
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class AddControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        self.acl_uuid = acl_uuid
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
        body: AddControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.member_desc = member_desc
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
        body: AddInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        acl_action: str = None,
        application_name: str = None,
        description: str = None,
        dest_port: str = None,
        destination: str = None,
        destination_type: str = None,
        vpc_firewall_id: str = None,
        proto: str = None,
        source: str = None,
        source_type: str = None,
        new_order: str = None,
        dest_port_type: str = None,
        dest_port_group: str = None,
    ):
        self.lang = lang
        self.acl_action = acl_action
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.destination = destination
        self.destination_type = destination_type
        self.vpc_firewall_id = vpc_firewall_id
        self.proto = proto
        self.source = source
        self.source_type = source_type
        self.new_order = new_order
        self.dest_port_type = dest_port_type
        self.dest_port_group = dest_port_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        return self


class CreateVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        request_id: str = None,
    ):
        self.acl_uuid = acl_uuid
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
        body: CreateVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAddressBookRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        group_uuid: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.group_uuid = group_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        return self


class DeleteAddressBookResponseBody(TeaModel):
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


class DeleteAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        acl_uuid: str = None,
        direction: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.acl_uuid = acl_uuid
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        return self


class DeleteControlPolicyResponseBody(TeaModel):
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


class DeleteControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        member_uids: List[int] = None,
    ):
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
        body: DeleteInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        acl_uuid: str = None,
        vpc_firewall_id: str = None,
    ):
        self.lang = lang
        self.acl_uuid = acl_uuid
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
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DeleteVpcFirewallControlPolicyResponseBody(TeaModel):
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


class DeleteVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressBookRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        current_page: str = None,
        page_size: str = None,
        query: str = None,
        group_type: str = None,
        contain_port: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.current_page = current_page
        self.page_size = page_size
        self.query = query
        self.group_type = group_type
        self.contain_port = contain_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.contain_port is not None:
            result['ContainPort'] = self.contain_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('ContainPort') is not None:
            self.contain_port = m.get('ContainPort')
        return self


class DescribeAddressBookResponseBodyAclsTagList(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeAddressBookResponseBodyAcls(TeaModel):
    def __init__(
        self,
        address_list_count: int = None,
        group_uuid: str = None,
        auto_add_tag_ecs: int = None,
        description: str = None,
        group_name: str = None,
        reference_count: int = None,
        group_type: str = None,
        tag_relation: str = None,
        global_: int = None,
        tag_list: List[DescribeAddressBookResponseBodyAclsTagList] = None,
        address_list: List[str] = None,
    ):
        self.address_list_count = address_list_count
        self.group_uuid = group_uuid
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.description = description
        self.group_name = group_name
        self.reference_count = reference_count
        self.group_type = group_type
        self.tag_relation = tag_relation
        self.global_ = global_
        self.tag_list = tag_list
        self.address_list = address_list

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
        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        if self.global_ is not None:
            result['Global'] = self.global_
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressListCount') is not None:
            self.address_list_count = m.get('AddressListCount')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        if m.get('Global') is not None:
            self.global_ = m.get('Global')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeAddressBookResponseBodyAclsTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        return self


class DescribeAddressBookResponseBody(TeaModel):
    def __init__(
        self,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
        acls: List[DescribeAddressBookResponseBodyAcls] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.acls = acls

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = DescribeAddressBookResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        return self


class DescribeAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        current_page: str = None,
        page_size: str = None,
        region_no: str = None,
        status: str = None,
        search_item: str = None,
        type: str = None,
        resource_type: str = None,
        sg_status: str = None,
        ip_version: str = None,
        member_uid: int = None,
        user_type: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.current_page = current_page
        self.page_size = page_size
        self.region_no = region_no
        self.status = status
        self.search_item = search_item
        self.type = type
        self.resource_type = resource_type
        self.sg_status = sg_status
        self.ip_version = ip_version
        self.member_uid = member_uid
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
        if self.type is not None:
            result['Type'] = self.type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeAssetListResponseBodyAssets(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        bind_instance_name: str = None,
        type: str = None,
        sg_status_time: int = None,
        resource_instance_id: str = None,
        member_uid: int = None,
        intranet_address: str = None,
        sync_status: str = None,
        ali_uid: int = None,
        protect_status: str = None,
        internet_address: str = None,
        bind_instance_id: str = None,
        region_id: str = None,
        region_status: str = None,
        resource_type: str = None,
        ip_version: int = None,
        sg_status: str = None,
        note: str = None,
        name: str = None,
    ):
        self.risk_level = risk_level
        self.bind_instance_name = bind_instance_name
        self.type = type
        self.sg_status_time = sg_status_time
        self.resource_instance_id = resource_instance_id
        self.member_uid = member_uid
        self.intranet_address = intranet_address
        self.sync_status = sync_status
        self.ali_uid = ali_uid
        self.protect_status = protect_status
        self.internet_address = internet_address
        self.bind_instance_id = bind_instance_id
        self.region_id = region_id
        self.region_status = region_status
        self.resource_type = resource_type
        self.ip_version = ip_version
        self.sg_status = sg_status
        self.note = note
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.bind_instance_name is not None:
            result['BindInstanceName'] = self.bind_instance_name
        if self.type is not None:
            result['Type'] = self.type
        if self.sg_status_time is not None:
            result['SgStatusTime'] = self.sg_status_time
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.protect_status is not None:
            result['ProtectStatus'] = self.protect_status
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.note is not None:
            result['Note'] = self.note
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('BindInstanceName') is not None:
            self.bind_instance_name = m.get('BindInstanceName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SgStatusTime') is not None:
            self.sg_status_time = m.get('SgStatusTime')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ProtectStatus') is not None:
            self.protect_status = m.get('ProtectStatus')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAssetListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        assets: List[DescribeAssetListResponseBodyAssets] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.assets = assets

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Assets'] = []
        if self.assets is not None:
            for k in self.assets:
                result['Assets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.assets = []
        if m.get('Assets') is not None:
            for k in m.get('Assets'):
                temp_model = DescribeAssetListResponseBodyAssets()
                self.assets.append(temp_model.from_map(k))
        return self


class DescribeAssetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAssetListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAssetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeControlPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        direction: str = None,
        current_page: str = None,
        page_size: str = None,
        source: str = None,
        destination: str = None,
        description: str = None,
        proto: str = None,
        acl_action: str = None,
        release: str = None,
        acl_uuid: str = None,
        ip_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.direction = direction
        self.current_page = current_page
        self.page_size = page_size
        self.source = source
        self.destination = destination
        self.description = description
        self.proto = proto
        self.acl_action = acl_action
        self.release = release
        self.acl_uuid = acl_uuid
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.description is not None:
            result['Description'] = self.description
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.release is not None:
            result['Release'] = self.release
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribeControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(
        self,
        direction: str = None,
        order: int = None,
        source_type: str = None,
        application_name: str = None,
        hit_times: int = None,
        description: str = None,
        source_group_type: str = None,
        dns_result_time: int = None,
        dns_result: str = None,
        proto: str = None,
        destination_group_type: str = None,
        destination: str = None,
        hit_last_time: int = None,
        dest_port_group: str = None,
        acl_uuid: str = None,
        dest_port_type: str = None,
        source: str = None,
        destination_type: str = None,
        dest_port: str = None,
        ip_version: int = None,
        acl_action: str = None,
        release: str = None,
        application_id: str = None,
        destination_group_cidrs: List[str] = None,
        dest_port_group_ports: List[str] = None,
        source_group_cidrs: List[str] = None,
    ):
        self.direction = direction
        self.order = order
        self.source_type = source_type
        self.application_name = application_name
        self.hit_times = hit_times
        self.description = description
        self.source_group_type = source_group_type
        self.dns_result_time = dns_result_time
        self.dns_result = dns_result
        self.proto = proto
        self.destination_group_type = destination_group_type
        self.destination = destination
        self.hit_last_time = hit_last_time
        self.dest_port_group = dest_port_group
        self.acl_uuid = acl_uuid
        self.dest_port_type = dest_port_type
        self.source = source
        self.destination_type = destination_type
        self.dest_port = dest_port
        self.ip_version = ip_version
        self.acl_action = acl_action
        self.release = release
        self.application_id = application_id
        self.destination_group_cidrs = destination_group_cidrs
        self.dest_port_group_ports = dest_port_group_ports
        self.source_group_cidrs = source_group_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.order is not None:
            result['Order'] = self.order
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.description is not None:
            result['Description'] = self.description
        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type
        if self.dns_result_time is not None:
            result['DnsResultTime'] = self.dns_result_time
        if self.dns_result is not None:
            result['DnsResult'] = self.dns_result
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.source is not None:
            result['Source'] = self.source
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.release is not None:
            result['Release'] = self.release
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs
        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')
        if m.get('DnsResultTime') is not None:
            self.dns_result_time = m.get('DnsResultTime')
        if m.get('DnsResult') is not None:
            self.dns_result = m.get('DnsResult')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')
        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        return self


class DescribeControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
        policys: List[DescribeControlPolicyResponseBodyPolicys] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.policys = policys

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        return self


class DescribeControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolveRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        ip_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribeDomainResolveResponseBodyResolveResult(TeaModel):
    def __init__(
        self,
        ip_addrs: str = None,
        update_time: int = None,
    ):
        self.ip_addrs = ip_addrs
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
        self.request_id = request_id
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
        body: DescribeDomainResolveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainResolveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        page_size: str = None,
        member_uid: str = None,
        member_display_name: str = None,
        member_desc: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.member_uid = member_uid
        self.member_display_name = member_display_name
        self.member_desc = member_desc

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
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        return self


class DescribeInstanceMembersResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
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


class DescribeInstanceMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        member_desc: str = None,
        member_display_name: str = None,
        create_time: int = None,
        member_uid: int = None,
        member_status: str = None,
        modify_time: int = None,
    ):
        self.member_desc = member_desc
        self.member_display_name = member_display_name
        self.create_time = create_time
        self.member_uid = member_uid
        self.member_status = member_status
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeInstanceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_info: DescribeInstanceMembersResponseBodyPageInfo = None,
        members: List[DescribeInstanceMembersResponseBodyMembers] = None,
    ):
        self.request_id = request_id
        self.page_info = page_info
        self.members = members

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageInfo') is not None:
            temp_model = DescribeInstanceMembersResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeInstanceMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        return self


class DescribeInstanceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyAdvancedConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribePolicyAdvancedConfigResponseBody(TeaModel):
    def __init__(
        self,
        internet_switch: str = None,
        request_id: str = None,
    ):
        self.internet_switch = internet_switch
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
        body: DescribePolicyAdvancedConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyPriorUsedRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        direction: str = None,
        ip_version: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.direction = direction
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribePolicyPriorUsedResponseBody(TeaModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
        request_id: str = None,
    ):
        self.end = end
        self.start = start
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyPriorUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePolicyPriorUsedResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskEventGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        start_time: str = None,
        end_time: str = None,
        direction: str = None,
        page_size: str = None,
        current_page: str = None,
        data_type: str = None,
        rule_source: str = None,
        rule_result: str = None,
        src_ip: str = None,
        dst_ip: str = None,
        vul_level: str = None,
        firewall_type: str = None,
        src_network_instance_id: str = None,
        dst_network_instance_id: str = None,
        attack_type: str = None,
        no_location: str = None,
        attack_app: List[str] = None,
    ):
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.direction = direction
        self.page_size = page_size
        self.current_page = current_page
        self.data_type = data_type
        self.rule_source = rule_source
        self.rule_result = rule_result
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.vul_level = vul_level
        self.firewall_type = firewall_type
        self.src_network_instance_id = src_network_instance_id
        self.dst_network_instance_id = dst_network_instance_id
        self.attack_type = attack_type
        self.no_location = no_location
        self.attack_app = attack_app

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
        if self.src_network_instance_id is not None:
            result['SrcNetworkInstanceId'] = self.src_network_instance_id
        if self.dst_network_instance_id is not None:
            result['DstNetworkInstanceId'] = self.dst_network_instance_id
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.no_location is not None:
            result['NoLocation'] = self.no_location
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
        if m.get('SrcNetworkInstanceId') is not None:
            self.src_network_instance_id = m.get('SrcNetworkInstanceId')
        if m.get('DstNetworkInstanceId') is not None:
            self.dst_network_instance_id = m.get('DstNetworkInstanceId')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('NoLocation') is not None:
            self.no_location = m.get('NoLocation')
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        return self


class DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList(TeaModel):
    def __init__(
        self,
        resource_instance_name: str = None,
        resource_private_ip: str = None,
        resource_instance_id: str = None,
        region_no: str = None,
    ):
        self.resource_instance_name = resource_instance_name
        self.resource_private_ip = resource_private_ip
        self.resource_instance_id = resource_instance_id
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name
        if self.resource_private_ip is not None:
            result['ResourcePrivateIP'] = self.resource_private_ip
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')
        if m.get('ResourcePrivateIP') is not None:
            self.resource_private_ip = m.get('ResourcePrivateIP')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo(TeaModel):
    def __init__(
        self,
        ecs_instance_name: str = None,
        network_instance_name: str = None,
        network_instance_id: str = None,
        ecs_instance_id: str = None,
        region_no: str = None,
    ):
        self.ecs_instance_name = ecs_instance_name
        self.network_instance_name = network_instance_name
        self.network_instance_id = network_instance_id
        self.ecs_instance_id = ecs_instance_id
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcDstInfo(TeaModel):
    def __init__(
        self,
        ecs_instance_name: str = None,
        network_instance_name: str = None,
        network_instance_id: str = None,
        ecs_instance_id: str = None,
        region_no: str = None,
    ):
        self.ecs_instance_name = ecs_instance_name
        self.network_instance_name = network_instance_name
        self.network_instance_id = network_instance_id
        self.ecs_instance_id = ecs_instance_id
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataListIPLocationInfo(TeaModel):
    def __init__(
        self,
        city_id: str = None,
        country_name: str = None,
        city_name: str = None,
        country_id: str = None,
    ):
        self.city_id = city_id
        self.country_name = country_name
        self.city_name = city_name
        self.country_id = country_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        return self


class DescribeRiskEventGroupResponseBodyDataList(TeaModel):
    def __init__(
        self,
        direction: str = None,
        event_name: str = None,
        dst_ip: str = None,
        attack_type: int = None,
        tag: str = None,
        rule_id: str = None,
        event_id: str = None,
        resource_type: str = None,
        first_event_time: int = None,
        description: str = None,
        event_count: int = None,
        vul_level: int = None,
        attack_app: str = None,
        rule_source: int = None,
        rule_result: int = None,
        src_ip: str = None,
        last_event_time: int = None,
        resource_private_iplist: List[DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList] = None,
        src_private_iplist: List[str] = None,
        vpc_src_info: DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo = None,
        vpc_dst_info: DescribeRiskEventGroupResponseBodyDataListVpcDstInfo = None,
        iplocation_info: DescribeRiskEventGroupResponseBodyDataListIPLocationInfo = None,
    ):
        self.direction = direction
        self.event_name = event_name
        self.dst_ip = dst_ip
        self.attack_type = attack_type
        self.tag = tag
        self.rule_id = rule_id
        self.event_id = event_id
        self.resource_type = resource_type
        self.first_event_time = first_event_time
        self.description = description
        self.event_count = event_count
        self.vul_level = vul_level
        self.attack_app = attack_app
        self.rule_source = rule_source
        self.rule_result = rule_result
        self.src_ip = src_ip
        self.last_event_time = last_event_time
        self.resource_private_iplist = resource_private_iplist
        self.src_private_iplist = src_private_iplist
        self.vpc_src_info = vpc_src_info
        self.vpc_dst_info = vpc_dst_info
        self.iplocation_info = iplocation_info

    def validate(self):
        if self.resource_private_iplist:
            for k in self.resource_private_iplist:
                if k:
                    k.validate()
        if self.vpc_src_info:
            self.vpc_src_info.validate()
        if self.vpc_dst_info:
            self.vpc_dst_info.validate()
        if self.iplocation_info:
            self.iplocation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.first_event_time is not None:
            result['FirstEventTime'] = self.first_event_time
        if self.description is not None:
            result['Description'] = self.description
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time
        result['ResourcePrivateIPList'] = []
        if self.resource_private_iplist is not None:
            for k in self.resource_private_iplist:
                result['ResourcePrivateIPList'].append(k.to_map() if k else None)
        if self.src_private_iplist is not None:
            result['SrcPrivateIPList'] = self.src_private_iplist
        if self.vpc_src_info is not None:
            result['VpcSrcInfo'] = self.vpc_src_info.to_map()
        if self.vpc_dst_info is not None:
            result['VpcDstInfo'] = self.vpc_dst_info.to_map()
        if self.iplocation_info is not None:
            result['IPLocationInfo'] = self.iplocation_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('FirstEventTime') is not None:
            self.first_event_time = m.get('FirstEventTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')
        self.resource_private_iplist = []
        if m.get('ResourcePrivateIPList') is not None:
            for k in m.get('ResourcePrivateIPList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList()
                self.resource_private_iplist.append(temp_model.from_map(k))
        if m.get('SrcPrivateIPList') is not None:
            self.src_private_iplist = m.get('SrcPrivateIPList')
        if m.get('VpcSrcInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo()
            self.vpc_src_info = temp_model.from_map(m['VpcSrcInfo'])
        if m.get('VpcDstInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcDstInfo()
            self.vpc_dst_info = temp_model.from_map(m['VpcDstInfo'])
        if m.get('IPLocationInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListIPLocationInfo()
            self.iplocation_info = temp_model.from_map(m['IPLocationInfo'])
        return self


class DescribeRiskEventGroupResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        data_list: List[DescribeRiskEventGroupResponseBodyDataList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.data_list = data_list

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class DescribeRiskEventGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskEventGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRiskEventGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallAclGroupListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        firewall_configure_status: str = None,
        current_page: str = None,
        page_size: str = None,
    ):
        self.lang = lang
        self.firewall_configure_status = firewall_configure_status
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.firewall_configure_status is not None:
            result['FirewallConfigureStatus'] = self.firewall_configure_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FirewallConfigureStatus') is not None:
            self.firewall_configure_status = m.get('FirewallConfigureStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVpcFirewallAclGroupListResponseBodyAclGroupList(TeaModel):
    def __init__(
        self,
        acl_group_id: str = None,
        acl_group_name: str = None,
    ):
        self.acl_group_id = acl_group_id
        self.acl_group_name = acl_group_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclGroupId') is not None:
            self.acl_group_id = m.get('AclGroupId')
        if m.get('AclGroupName') is not None:
            self.acl_group_name = m.get('AclGroupName')
        return self


class DescribeVpcFirewallAclGroupListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        acl_group_list: List[DescribeVpcFirewallAclGroupListResponseBodyAclGroupList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.acl_group_list = acl_group_list

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AclGroupList'] = []
        if self.acl_group_list is not None:
            for k in self.acl_group_list:
                result['AclGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.acl_group_list = []
        if m.get('AclGroupList') is not None:
            for k in m.get('AclGroupList'):
                temp_model = DescribeVpcFirewallAclGroupListResponseBodyAclGroupList()
                self.acl_group_list.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallAclGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcFirewallAclGroupListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallAclGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        vpc_firewall_id: str = None,
        current_page: str = None,
        page_size: str = None,
        source: str = None,
        destination: str = None,
        description: str = None,
        proto: str = None,
        acl_action: str = None,
    ):
        self.lang = lang
        self.vpc_firewall_id = vpc_firewall_id
        self.current_page = current_page
        self.page_size = page_size
        self.source = source
        self.destination = destination
        self.description = description
        self.proto = proto
        self.acl_action = acl_action

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.description is not None:
            result['Description'] = self.description
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        return self


class DescribeVpcFirewallControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(
        self,
        direction: str = None,
        destination: str = None,
        order: int = None,
        dest_port_group: str = None,
        source_type: str = None,
        application_name: str = None,
        acl_uuid: str = None,
        dest_port_type: str = None,
        source: str = None,
        destination_type: str = None,
        hit_times: int = None,
        dest_port: str = None,
        description: str = None,
        acl_action: str = None,
        application_id: str = None,
        proto: str = None,
        destination_group_cidrs: List[str] = None,
        dest_port_group_ports: List[str] = None,
        source_group_cidrs: List[str] = None,
    ):
        self.direction = direction
        self.destination = destination
        self.order = order
        self.dest_port_group = dest_port_group
        self.source_type = source_type
        self.application_name = application_name
        self.acl_uuid = acl_uuid
        self.dest_port_type = dest_port_type
        self.source = source
        self.destination_type = destination_type
        self.hit_times = hit_times
        self.dest_port = dest_port
        self.description = description
        self.acl_action = acl_action
        self.application_id = application_id
        self.proto = proto
        self.destination_group_cidrs = destination_group_cidrs
        self.dest_port_group_ports = dest_port_group_ports
        self.source_group_cidrs = source_group_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.order is not None:
            result['Order'] = self.order
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.source is not None:
            result['Source'] = self.source
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.description is not None:
            result['Description'] = self.description
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs
        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')
        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        return self


class DescribeVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        policys: List[DescribeVpcFirewallControlPolicyResponseBodyPolicys] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.policys = policys

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeVpcFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallPolicyPriorUsedRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        vpc_firewall_id: str = None,
    ):
        self.lang = lang
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
        start: int = None,
        request_id: str = None,
    ):
        self.end = end
        self.start = start
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVpcFirewallPolicyPriorUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcFirewallPolicyPriorUsedResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcFirewallPolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAddressBookRequestTagList(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ModifyAddressBookRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        address_list: str = None,
        description: str = None,
        group_name: str = None,
        group_uuid: str = None,
        auto_add_tag_ecs: str = None,
        tag_relation: str = None,
        tag_list: List[ModifyAddressBookRequestTagList] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.address_list = address_list
        self.description = description
        self.group_name = group_name
        self.group_uuid = group_uuid
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.tag_relation = tag_relation
        self.tag_list = tag_list

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
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ModifyAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        return self


class ModifyAddressBookResponseBody(TeaModel):
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


class ModifyAddressBookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        acl_action: str = None,
        application_name: str = None,
        description: str = None,
        dest_port: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        proto: str = None,
        source: str = None,
        acl_uuid: str = None,
        source_type: str = None,
        dest_port_type: str = None,
        dest_port_group: str = None,
        release: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.acl_action = acl_action
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.destination = destination
        self.destination_type = destination_type
        self.direction = direction
        self.proto = proto
        self.source = source
        self.acl_uuid = acl_uuid
        self.source_type = source_type
        self.dest_port_type = dest_port_type
        self.dest_port_group = dest_port_group
        self.release = release

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.source is not None:
            result['Source'] = self.source
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.release is not None:
            result['Release'] = self.release
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        return self


class ModifyControlPolicyResponseBody(TeaModel):
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


class ModifyControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyPositionRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        direction: str = None,
        new_order: str = None,
        old_order: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.direction = direction
        self.new_order = new_order
        self.old_order = old_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        return self


class ModifyControlPolicyPositionResponseBody(TeaModel):
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


class ModifyControlPolicyPositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyControlPolicyPositionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMemberAttributesRequestMembers(TeaModel):
    def __init__(
        self,
        member_desc: str = None,
        member_uid: int = None,
    ):
        self.member_desc = member_desc
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
        body: ModifyInstanceMemberAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMemberAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyAdvancedConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        internet_switch: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.internet_switch = internet_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')
        return self


class ModifyPolicyAdvancedConfigResponseBody(TeaModel):
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


class ModifyPolicyAdvancedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPolicyAdvancedConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        acl_action: str = None,
        application_name: str = None,
        description: str = None,
        dest_port: str = None,
        destination: str = None,
        destination_type: str = None,
        vpc_firewall_id: str = None,
        proto: str = None,
        source: str = None,
        acl_uuid: str = None,
        source_type: str = None,
        dest_port_type: str = None,
        dest_port_group: str = None,
    ):
        self.lang = lang
        self.acl_action = acl_action
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.destination = destination
        self.destination_type = destination_type
        self.vpc_firewall_id = vpc_firewall_id
        self.proto = proto
        self.source = source
        self.acl_uuid = acl_uuid
        self.source_type = source_type
        self.dest_port_type = dest_port_type
        self.dest_port_group = dest_port_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.source is not None:
            result['Source'] = self.source
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        return self


class ModifyVpcFirewallControlPolicyResponseBody(TeaModel):
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


class ModifyVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyPositionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        vpc_firewall_id: str = None,
        new_order: str = None,
        old_order: str = None,
    ):
        self.lang = lang
        self.vpc_firewall_id = vpc_firewall_id
        self.new_order = new_order
        self.old_order = old_order

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
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        return self


class ModifyVpcFirewallControlPolicyPositionResponseBody(TeaModel):
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


class ModifyVpcFirewallControlPolicyPositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVpcFirewallControlPolicyPositionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVpcFirewallControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableAllFwSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PutDisableAllFwSwitchResponseBody(TeaModel):
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


class PutDisableAllFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutDisableAllFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutDisableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableFwSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ipaddr_list: List[str] = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ipaddr_list = ipaddr_list
        self.region_list = region_list
        self.resource_type_list = resource_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        return self


class PutDisableFwSwitchResponseBody(TeaModel):
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


class PutDisableFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutDisableFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutDisableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableAllFwSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PutEnableAllFwSwitchResponseBody(TeaModel):
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


class PutEnableAllFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutEnableAllFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutEnableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableFwSwitchRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ipaddr_list: List[str] = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ipaddr_list = ipaddr_list
        self.region_list = region_list
        self.resource_type_list = resource_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        return self


class PutEnableFwSwitchResponseBody(TeaModel):
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


class PutEnableFwSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutEnableFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutEnableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetVpcFirewallRuleHitCountRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        acl_uuid: str = None,
    ):
        self.lang = lang
        self.acl_uuid = acl_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        return self


class ResetVpcFirewallRuleHitCountResponseBody(TeaModel):
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


class ResetVpcFirewallRuleHitCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetVpcFirewallRuleHitCountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetVpcFirewallRuleHitCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


