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
        self.tag_key = tag_key
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
        self.address_list = address_list
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.description = description
        self.group_name = group_name
        self.group_type = group_type
        self.lang = lang
        self.source_ip = source_ip
        self.tag_list = tag_list
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
        status_code: int = None,
        body: AddAddressBookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        ip_version: str = None,
        lang: str = None,
        new_order: str = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_ip: str = None,
        source_type: str = None,
    ):
        self.acl_action = acl_action
        self.application_name = application_name
        self.application_name_list = application_name_list
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_type = destination_type
        self.direction = direction
        self.ip_version = ip_version
        self.lang = lang
        self.new_order = new_order
        self.proto = proto
        self.release = release
        self.source = source
        self.source_ip = source_ip
        self.source_type = source_type

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
        if self.source is not None:
            result['Source'] = self.source
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_type is not None:
            result['SourceType'] = self.source_type
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
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
        status_code: int = None,
        body: AddControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: AddInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.lang = lang
        self.source_ip = source_ip
        self.source_vpc_firewall_id = source_vpc_firewall_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class CreateVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_switch: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_id: str = None,
        vpc_firewall_name: str = None,
        vpc_region: str = None,
    ):
        self.cen_id = cen_id
        self.firewall_switch = firewall_switch
        self.lang = lang
        self.member_uid = member_uid
        self.network_instance_id = network_instance_id
        self.vpc_firewall_name = vpc_firewall_name
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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
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
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.firewall_switch = firewall_switch
        self.lang = lang
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        self.local_vpc_id = local_vpc_id
        self.local_vpc_region = local_vpc_region
        self.member_uid = member_uid
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        self.peer_vpc_id = peer_vpc_id
        self.peer_vpc_region = peer_vpc_region
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
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        lang: str = None,
        member_uid: str = None,
        new_order: str = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_type: str = None,
        vpc_firewall_id: str = None,
    ):
        self.acl_action = acl_action
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_type = destination_type
        self.lang = lang
        self.member_uid = member_uid
        self.new_order = new_order
        self.proto = proto
        self.release = release
        self.source = source
        self.source_type = source_type
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
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
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
        status_code: int = None,
        body: CreateVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.group_uuid = group_uuid
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.acl_uuid = acl_uuid
        self.direction = direction
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: DeleteInstanceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DeleteVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id_list: List[str] = None,
    ):
        self.lang = lang
        self.member_uid = member_uid
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.lang = lang
        self.member_uid = member_uid
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.acl_uuid = acl_uuid
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.contain_port = contain_port
        self.current_page = current_page
        self.group_type = group_type
        self.lang = lang
        self.page_size = page_size
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


class DescribeAddressBookResponseBodyAclsTagList(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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
        auto_add_tag_ecs: int = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        group_uuid: str = None,
        reference_count: int = None,
        tag_list: List[DescribeAddressBookResponseBodyAclsTagList] = None,
        tag_relation: str = None,
    ):
        self.address_list = address_list
        self.address_list_count = address_list_count
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.description = description
        self.group_name = group_name
        self.group_type = group_type
        self.group_uuid = group_uuid
        self.reference_count = reference_count
        self.tag_list = tag_list
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
        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count
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
        self.acls = acls
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        page_size: str = None,
        region_no: str = None,
        resource_type: str = None,
        search_item: str = None,
        sg_status: str = None,
        status: str = None,
        type: str = None,
        user_type: str = None,
    ):
        self.current_page = current_page
        self.ip_version = ip_version
        self.lang = lang
        self.member_uid = member_uid
        self.page_size = page_size
        self.region_no = region_no
        self.resource_type = resource_type
        self.search_item = search_item
        self.sg_status = sg_status
        self.status = status
        self.type = type
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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
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
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
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
        internet_address: str = None,
        intranet_address: str = None,
        ip_version: int = None,
        member_uid: int = None,
        name: str = None,
        note: str = None,
        protect_status: str = None,
        region_id: str = None,
        region_status: str = None,
        resource_instance_id: str = None,
        resource_type: str = None,
        risk_level: str = None,
        sg_status: str = None,
        sg_status_time: int = None,
        sync_status: str = None,
        type: str = None,
    ):
        self.ali_uid = ali_uid
        self.bind_instance_id = bind_instance_id
        self.bind_instance_name = bind_instance_name
        self.internet_address = internet_address
        self.intranet_address = intranet_address
        self.ip_version = ip_version
        self.member_uid = member_uid
        self.name = name
        self.note = note
        self.protect_status = protect_status
        self.region_id = region_id
        self.region_status = region_status
        self.resource_instance_id = resource_instance_id
        self.resource_type = resource_type
        self.risk_level = risk_level
        self.sg_status = sg_status
        self.sg_status_time = sg_status_time
        self.sync_status = sync_status
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
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        self.assets = assets
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        source: str = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.current_page = current_page
        self.description = description
        self.destination = destination
        self.direction = direction
        self.ip_version = ip_version
        self.lang = lang
        self.page_size = page_size
        self.proto = proto
        self.release = release
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
        hit_last_time: int = None,
        hit_times: int = None,
        ip_version: int = None,
        modify_time: int = None,
        order: int = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_group_cidrs: List[str] = None,
        source_group_type: str = None,
        source_type: str = None,
        spread_cnt: int = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.application_id = application_id
        self.application_name = application_name
        self.application_name_list = application_name_list
        self.create_time = create_time
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_group_ports = dest_port_group_ports
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_group_cidrs = destination_group_cidrs
        self.destination_group_type = destination_group_type
        self.destination_type = destination_type
        self.direction = direction
        self.dns_result = dns_result
        self.dns_result_time = dns_result_time
        self.hit_last_time = hit_last_time
        self.hit_times = hit_times
        self.ip_version = ip_version
        self.modify_time = modify_time
        self.order = order
        self.proto = proto
        self.release = release
        self.source = source
        self.source_group_cidrs = source_group_cidrs
        self.source_group_type = source_group_type
        self.source_type = source_type
        self.spread_cnt = spread_cnt

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
        self.page_no = page_no
        self.page_size = page_size
        self.policys = policys
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeDomainResolveRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ip_version: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.domain = domain
        self.ip_version = ip_version
        self.lang = lang
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
        status_code: int = None,
        body: DescribeDomainResolveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeInstanceMembersRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        member_desc: str = None,
        member_display_name: str = None,
        member_uid: str = None,
        page_size: str = None,
    ):
        self.current_page = current_page
        self.member_desc = member_desc
        self.member_display_name = member_display_name
        self.member_uid = member_uid
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
        self.create_time = create_time
        self.member_desc = member_desc
        self.member_display_name = member_display_name
        self.member_status = member_status
        self.member_uid = member_uid
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


class DescribeInstanceMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[DescribeInstanceMembersResponseBodyMembers] = None,
        page_info: DescribeInstanceMembersResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.members = members
        self.page_info = page_info
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.assets_ip = assets_ip
        self.assets_instance_id = assets_instance_id
        self.assets_instance_name = assets_instance_name
        self.current_page = current_page
        self.end_time = end_time
        self.event_key = event_key
        self.event_name = event_name
        self.event_uuid = event_uuid
        self.is_ignore = is_ignore
        self.lang = lang
        self.member_uid = member_uid
        self.page_size = page_size
        self.process_status_list = process_status_list
        self.risk_level = risk_level
        self.source_ip = source_ip
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
        self.assets_instance_id = assets_instance_id
        self.assets_instance_name = assets_instance_name
        self.assets_type = assets_type
        self.event_key = event_key
        self.event_name = event_name
        self.event_src = event_src
        self.event_uuid = event_uuid
        self.first_time = first_time
        self.is_ignore = is_ignore
        self.last_time = last_time
        self.member_uid = member_uid
        self.private_ip = private_ip
        self.process_status = process_status
        self.public_ip = public_ip
        self.public_ip_type = public_ip_type
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
        self.event_list = event_list
        self.high_level_percent = high_level_percent
        self.low_level_percent = low_level_percent
        self.middle_level_percent = middle_level_percent
        self.page_info = page_info
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeOutgoingDestinationIPRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
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
    ):
        self.application_name = application_name
        self.current_page = current_page
        self.dst_ip = dst_ip
        self.end_time = end_time
        self.lang = lang
        self.order = order
        self.page_size = page_size
        self.port = port
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.sort = sort
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
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
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList(TeaModel):
    def __init__(
        self,
        address_group_name: str = None,
        address_group_uuid: str = None,
    ):
        self.address_group_name = address_group_name
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
        self.application_name = application_name
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
        self.class_id = class_id
        self.risk_level = risk_level
        self.tag_describe = tag_describe
        self.tag_id = tag_id
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
        category_class_id: str = None,
        category_id: str = None,
        category_name: str = None,
        dst_ip: str = None,
        group_name: str = None,
        has_acl: str = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        is_mark_normal: bool = None,
        out_bytes: int = None,
        rule_id: str = None,
        rule_name: str = None,
        security_reason: str = None,
        security_suggest: str = None,
        session_count: int = None,
        tag_list: List[DescribeOutgoingDestinationIPResponseBodyDstIPListTagList] = None,
        total_bytes: str = None,
    ):
        self.acl_coverage = acl_coverage
        self.acl_recommend_detail = acl_recommend_detail
        self.acl_status = acl_status
        self.address_group_list = address_group_list
        self.application_port_list = application_port_list
        self.category_class_id = category_class_id
        self.category_id = category_id
        self.category_name = category_name
        self.dst_ip = dst_ip
        self.group_name = group_name
        self.has_acl = has_acl
        self.has_acl_recommend = has_acl_recommend
        self.in_bytes = in_bytes
        self.is_mark_normal = is_mark_normal
        self.out_bytes = out_bytes
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.security_reason = security_reason
        self.security_suggest = security_suggest
        self.session_count = session_count
        self.tag_list = tag_list
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
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
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
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
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
        self.dst_iplist = dst_iplist
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        current_page: str = None,
        domain: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        public_ip: str = None,
        sort: str = None,
        start_time: str = None,
    ):
        self.current_page = current_page
        self.domain = domain
        self.end_time = end_time
        self.lang = lang
        self.order = order
        self.page_size = page_size
        self.public_ip = public_ip
        self.sort = sort
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.class_id = class_id
        self.risk_level = risk_level
        self.tag_describe = tag_describe
        self.tag_id = tag_id
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
        rule_id: str = None,
        rule_name: str = None,
        security_reason: str = None,
        security_suggest: str = None,
        session_count: int = None,
        tag_list: List[DescribeOutgoingDomainResponseBodyDomainListTagList] = None,
        total_bytes: str = None,
    ):
        self.acl_coverage = acl_coverage
        self.acl_recommend_detail = acl_recommend_detail
        self.acl_status = acl_status
        self.address_group_name = address_group_name
        self.address_group_uuid = address_group_uuid
        self.business = business
        self.category_class_id = category_class_id
        self.category_id = category_id
        self.category_name = category_name
        self.domain = domain
        self.group_name = group_name
        self.has_acl = has_acl
        self.has_acl_recommend = has_acl_recommend
        self.in_bytes = in_bytes
        self.is_mark_normal = is_mark_normal
        self.organization = organization
        self.out_bytes = out_bytes
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.security_reason = security_reason
        self.security_suggest = security_suggest
        self.session_count = session_count
        self.tag_list = tag_list
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
        self.domain_list = domain_list
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: DescribePolicyAdvancedConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.direction = direction
        self.ip_version = ip_version
        self.lang = lang
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
        self.end = end
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        firewall_type: str = None,
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
        self.attack_app = attack_app
        self.attack_type = attack_type
        self.buy_version = buy_version
        self.current_page = current_page
        self.data_type = data_type
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_network_instance_id = dst_network_instance_id
        self.end_time = end_time
        self.firewall_type = firewall_type
        self.lang = lang
        self.no_location = no_location
        self.order = order
        self.page_size = page_size
        self.rule_result = rule_result
        self.rule_source = rule_source
        self.sort = sort
        self.src_ip = src_ip
        self.src_network_instance_id = src_network_instance_id
        self.start_time = start_time
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
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
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
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
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
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id
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
        self.region_no = region_no
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
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
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        self.network_instance_id = network_instance_id
        self.network_instance_name = network_instance_name
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
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        self.network_instance_id = network_instance_id
        self.network_instance_name = network_instance_name
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
        src_private_iplist: List[str] = None,
        tag: str = None,
        vpc_dst_info: DescribeRiskEventGroupResponseBodyDataListVpcDstInfo = None,
        vpc_src_info: DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo = None,
        vul_level: int = None,
    ):
        self.attack_app = attack_app
        self.attack_type = attack_type
        self.description = description
        self.direction = direction
        self.dst_ip = dst_ip
        self.event_count = event_count
        self.event_id = event_id
        self.event_name = event_name
        self.first_event_time = first_event_time
        self.iplocation_info = iplocation_info
        self.last_event_time = last_event_time
        self.resource_private_iplist = resource_private_iplist
        self.resource_type = resource_type
        self.rule_id = rule_id
        self.rule_result = rule_result
        self.rule_source = rule_source
        self.src_ip = src_ip
        self.src_private_iplist = src_private_iplist
        self.tag = tag
        self.vpc_dst_info = vpc_dst_info
        self.vpc_src_info = vpc_src_info
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
        self.data_list = data_list
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeUserAssetIPTrafficInfoRequest(TeaModel):
    def __init__(
        self,
        asset_ip: str = None,
        lang: str = None,
        traffic_time: str = None,
    ):
        self.asset_ip = asset_ip
        self.lang = lang
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
        self.end_time = end_time
        self.in_bps = in_bps
        self.in_pps = in_pps
        self.new_conn = new_conn
        self.out_bps = out_bps
        self.out_pps = out_pps
        self.request_id = request_id
        self.session_count = session_count
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeVpcFirewallAclGroupListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        firewall_configure_status: str = None,
        lang: str = None,
        page_size: str = None,
    ):
        self.current_page = current_page
        self.firewall_configure_status = firewall_configure_status
        self.lang = lang
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
        member_uid: str = None,
    ):
        self.acl_group_id = acl_group_id
        self.acl_group_name = acl_group_name
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
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclGroupId') is not None:
            self.acl_group_id = m.get('AclGroupId')
        if m.get('AclGroupName') is not None:
            self.acl_group_name = m.get('AclGroupName')
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
        self.acl_group_list = acl_group_list
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.lang = lang
        self.network_instance_id = network_instance_id
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


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList(TeaModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
    ):
        self.eni_id = eni_id
        self.eni_private_ip_address = eni_private_ip_address

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.attachment_id = attachment_id
        self.attachment_name = attachment_name
        self.defend_cidr_list = defend_cidr_list
        self.eni_list = eni_list
        self.manual_vswitch_id = manual_vswitch_id
        self.network_instance_id = network_instance_id
        self.network_instance_name = network_instance_name
        self.network_instance_type = network_instance_type
        self.owner_id = owner_id
        self.region_no = region_no
        self.route_mode = route_mode
        self.support_manual_mode = support_manual_mode
        self.transit_router_id = transit_router_id
        self.transit_router_type = transit_router_type
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        local_vpc: DescribeVpcFirewallCenDetailResponseBodyLocalVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        self.connect_type = connect_type
        self.firewall_switch_status = firewall_switch_status
        self.local_vpc = local_vpc
        self.request_id = request_id
        self.vpc_firewall_id = vpc_firewall_id
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.cen_id = cen_id
        self.current_page = current_page
        self.firewall_switch_status = firewall_switch_status
        self.lang = lang
        self.member_uid = member_uid
        self.network_instance_id = network_instance_id
        self.owner_id = owner_id
        self.page_size = page_size
        self.region_no = region_no
        self.route_mode = route_mode
        self.transit_router_type = transit_router_type
        self.vpc_firewall_id = vpc_firewall_id
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
        run_mode: int = None,
    ):
        self.basic_rules = basic_rules
        self.enable_all_patch = enable_all_patch
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
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.authorization_status = authorization_status
        self.defend_cidr_list = defend_cidr_list
        self.manual_vswitch_id = manual_vswitch_id
        self.network_instance_id = network_instance_id
        self.network_instance_name = network_instance_name
        self.network_instance_type = network_instance_type
        self.owner_id = owner_id
        self.region_no = region_no
        self.route_mode = route_mode
        self.support_manual_mode = support_manual_mode
        self.transit_router_type = transit_router_type
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        self.cen_id = cen_id
        self.cen_name = cen_name
        self.connect_type = connect_type
        self.firewall_switch_status = firewall_switch_status
        self.ips_config = ips_config
        self.local_vpc = local_vpc
        self.member_uid = member_uid
        self.precheck_status = precheck_status
        self.region_status = region_status
        self.result_code = result_code
        self.vpc_firewall_id = vpc_firewall_id
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
        self.request_id = request_id
        self.total_count = total_count
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        source: str = None,
        vpc_firewall_id: str = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.current_page = current_page
        self.description = description
        self.destination = destination
        self.lang = lang
        self.member_uid = member_uid
        self.page_size = page_size
        self.proto = proto
        self.release = release
        self.source = source
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
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_group_ports: List[str] = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_group_cidrs: List[str] = None,
        destination_type: str = None,
        hit_times: int = None,
        member_uid: str = None,
        order: int = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_group_cidrs: List[str] = None,
        source_type: str = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.application_id = application_id
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_group_ports = dest_port_group_ports
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_group_cidrs = destination_group_cidrs
        self.destination_type = destination_type
        self.hit_times = hit_times
        self.member_uid = member_uid
        self.order = order
        self.proto = proto
        self.release = release
        self.source = source
        self.source_group_cidrs = source_group_cidrs
        self.source_type = source_type

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
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.order is not None:
            result['Order'] = self.order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.source is not None:
            result['Source'] = self.source
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        if self.source_type is not None:
            result['SourceType'] = self.source_type
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
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DescribeVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policys: List[DescribeVpcFirewallControlPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.policys = policys
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.member_uid = member_uid
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
        run_mode: int = None,
    ):
        self.basic_rules = basic_rules
        self.enable_all_patch = enable_all_patch
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.lang = lang
        self.local_vpc_id = local_vpc_id
        self.peer_vpc_id = peer_vpc_id
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
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.eni_id = eni_id
        self.eni_private_ip_address = eni_private_ip_address
        self.region_no = region_no
        self.router_interface_id = router_interface_id
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.eni_id = eni_id
        self.eni_private_ip_address = eni_private_ip_address
        self.region_no = region_no
        self.router_interface_id = router_interface_id
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        peer_vpc: DescribeVpcFirewallDetailResponseBodyPeerVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        self.bandwidth = bandwidth
        self.connect_type = connect_type
        self.firewall_switch_status = firewall_switch_status
        self.local_vpc = local_vpc
        self.peer_vpc = peer_vpc
        self.request_id = request_id
        self.vpc_firewall_id = vpc_firewall_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DescribeVpcFirewallListRequest(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        region_no: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
        vpc_id: str = None,
    ):
        self.current_page = current_page
        self.firewall_switch_status = firewall_switch_status
        self.lang = lang
        self.member_uid = member_uid
        self.page_size = page_size
        self.region_no = region_no
        self.vpc_firewall_id = vpc_firewall_id
        self.vpc_firewall_name = vpc_firewall_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        run_mode: int = None,
    ):
        self.basic_rules = basic_rules
        self.enable_all_patch = enable_all_patch
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
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.authorization_status = authorization_status
        self.owner_id = owner_id
        self.region_no = region_no
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        self.destination_cidr = destination_cidr
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
        self.route_entry_list = route_entry_list
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
        self.authorization_status = authorization_status
        self.owner_id = owner_id
        self.region_no = region_no
        self.vpc_cidr_table_list = vpc_cidr_table_list
        self.vpc_id = vpc_id
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
        connect_type: str = None,
        firewall_switch_status: str = None,
        ips_config: DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig = None,
        local_vpc: DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc = None,
        member_uid: str = None,
        peer_vpc: DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc = None,
        region_status: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        self.bandwidth = bandwidth
        self.connect_type = connect_type
        self.firewall_switch_status = firewall_switch_status
        self.ips_config = ips_config
        self.local_vpc = local_vpc
        self.member_uid = member_uid
        self.peer_vpc = peer_vpc
        self.region_status = region_status
        self.vpc_firewall_id = vpc_firewall_id
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
        self.request_id = request_id
        self.total_count = total_count
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        request_id: str = None,
        start: int = None,
    ):
        self.end = end
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ModifyAddressBookRequestTagList(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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
        source_ip: str = None,
        tag_list: List[ModifyAddressBookRequestTagList] = None,
        tag_relation: str = None,
    ):
        self.address_list = address_list
        self.auto_add_tag_ecs = auto_add_tag_ecs
        self.description = description
        self.group_name = group_name
        self.group_uuid = group_uuid
        self.lang = lang
        self.source_ip = source_ip
        self.tag_list = tag_list
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        lang: str = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_ip: str = None,
        source_type: str = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.application_name = application_name
        self.application_name_list = application_name_list
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_type = destination_type
        self.direction = direction
        self.lang = lang
        self.proto = proto
        self.release = release
        self.source = source
        self.source_ip = source_ip
        self.source_type = source_type

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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.source is not None:
            result['Source'] = self.source
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_type is not None:
            result['SourceType'] = self.source_type
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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
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
        status_code: int = None,
        body: ModifyControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.direction = direction
        self.lang = lang
        self.new_order = new_order
        self.old_order = old_order
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: ModifyInstanceMemberAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ModifyPolicyAdvancedConfigRequest(TeaModel):
    def __init__(
        self,
        internet_switch: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.internet_switch = internet_switch
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ModifyVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        self.lang = lang
        self.member_uid = member_uid
        self.vpc_firewall_id = vpc_firewall_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.firewall_switch = firewall_switch
        self.lang = lang
        self.member_uid = member_uid
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.lang = lang
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        self.member_uid = member_uid
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        self.vpc_firewall_id = vpc_firewall_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        description: str = None,
        dest_port: str = None,
        dest_port_group: str = None,
        dest_port_type: str = None,
        destination: str = None,
        destination_type: str = None,
        lang: str = None,
        proto: str = None,
        release: str = None,
        source: str = None,
        source_type: str = None,
        vpc_firewall_id: str = None,
    ):
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.application_name = application_name
        self.description = description
        self.dest_port = dest_port
        self.dest_port_group = dest_port_group
        self.dest_port_type = dest_port_type
        self.destination = destination
        self.destination_type = destination_type
        self.lang = lang
        self.proto = proto
        self.release = release
        self.source = source
        self.source_type = source_type
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
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
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
        status_code: int = None,
        body: ModifyVpcFirewallControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        lang: str = None,
        new_order: str = None,
        old_order: str = None,
        vpc_firewall_id: str = None,
    ):
        self.lang = lang
        self.new_order = new_order
        self.old_order = old_order
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
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        run_mode: str = None,
        source_ip: str = None,
        vpc_firewall_id: str = None,
    ):
        self.basic_rules = basic_rules
        self.enable_all_patch = enable_all_patch
        self.lang = lang
        self.member_uid = member_uid
        self.run_mode = run_mode
        self.source_ip = source_ip
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ModifyVpcFirewallSwitchStatusRequest(TeaModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id: str = None,
    ):
        self.firewall_switch = firewall_switch
        self.lang = lang
        self.member_uid = member_uid
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.instance_id = instance_id
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.ipaddr_list = ipaddr_list
        self.lang = lang
        self.region_list = region_list
        self.resource_type_list = resource_type_list
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.instance_id = instance_id
        self.lang = lang
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.ipaddr_list = ipaddr_list
        self.lang = lang
        self.region_list = region_list
        self.resource_type_list = resource_type_list
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
        status_code: int = None,
        body: PutEnableFwSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ResetVpcFirewallRuleHitCountRequest(TeaModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
    ):
        self.acl_uuid = acl_uuid
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


