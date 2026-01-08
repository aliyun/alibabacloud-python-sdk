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
        self.check_record = check_record
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
        self.acls = acls
        self.check_name = check_name
        self.description = description
        self.last_check_time = last_check_time
        self.level = level
        self.policy_total_count = policy_total_count
        self.record_assessment_detail = record_assessment_detail
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
        self.acl = acl
        self.acl_assessment_detail = acl_assessment_detail
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
        self.acl_action = acl_action
        self.acl_uuid = acl_uuid
        self.address_list = address_list
        self.address_list_count = address_list_count
        self.application_id = application_id
        self.application_name = application_name
        self.application_name_list = application_name_list
        self.auto_add_tag_ecs = auto_add_tag_ecs
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
        self.domain_resolve_type = domain_resolve_type
        self.end_time = end_time
        self.group_name = group_name
        self.group_type = group_type
        self.group_uuid = group_uuid
        self.hit_last_time = hit_last_time
        self.hit_times = hit_times
        self.ip_version = ip_version
        self.modify_time = modify_time
        self.nat_gateway_id = nat_gateway_id
        self.order = order
        self.proto = proto
        self.reference_count = reference_count
        self.release = release
        self.repeat_days = repeat_days
        self.repeat_end_time = repeat_end_time
        self.repeat_start_time = repeat_start_time
        self.repeat_type = repeat_type
        self.source = source
        self.source_group_cidrs = source_group_cidrs
        self.source_group_type = source_group_type
        self.source_type = source_type
        self.spread_cnt = spread_cnt
        self.start_time = start_time
        self.tag_list = tag_list
        self.tag_relation = tag_relation
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
        self.tag_key = tag_key
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

