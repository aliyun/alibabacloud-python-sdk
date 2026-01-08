# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePrivateDnsEndpointListResponseBody(DaraModel):
    def __init__(
        self,
        access_instance_list: List[main_models.DescribePrivateDnsEndpointListResponseBodyAccessInstanceList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_instance_list = access_instance_list
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_instance_list:
            for v1 in self.access_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessInstanceList'] = []
        if self.access_instance_list is not None:
            for k1 in self.access_instance_list:
                result['AccessInstanceList'].append(k1.to_map() if k1 else None)

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
        self.access_instance_list = []
        if m.get('AccessInstanceList') is not None:
            for k1 in m.get('AccessInstanceList'):
                temp_model = main_models.DescribePrivateDnsEndpointListResponseBodyAccessInstanceList()
                self.access_instance_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePrivateDnsEndpointListResponseBodyAccessInstanceList(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_instance_name: str = None,
        ali_uid: int = None,
        domain_name_count: int = None,
        firewall_type: List[str] = None,
        gmt_create: int = None,
        ip_protocol: int = None,
        member_uid: int = None,
        port: int = None,
        primary_dns: str = None,
        private_dns_type: str = None,
        region_no: str = None,
        standby_dns: str = None,
        status: int = None,
        task_id: str = None,
        vpc_id: str = None,
    ):
        self.access_instance_id = access_instance_id
        self.access_instance_name = access_instance_name
        self.ali_uid = ali_uid
        self.domain_name_count = domain_name_count
        self.firewall_type = firewall_type
        self.gmt_create = gmt_create
        self.ip_protocol = ip_protocol
        self.member_uid = member_uid
        self.port = port
        self.primary_dns = primary_dns
        self.private_dns_type = private_dns_type
        self.region_no = region_no
        self.standby_dns = standby_dns
        self.status = status
        self.task_id = task_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.access_instance_name is not None:
            result['AccessInstanceName'] = self.access_instance_name

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.domain_name_count is not None:
            result['DomainNameCount'] = self.domain_name_count

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.port is not None:
            result['Port'] = self.port

        if self.primary_dns is not None:
            result['PrimaryDns'] = self.primary_dns

        if self.private_dns_type is not None:
            result['PrivateDnsType'] = self.private_dns_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.standby_dns is not None:
            result['StandbyDns'] = self.standby_dns

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('AccessInstanceName') is not None:
            self.access_instance_name = m.get('AccessInstanceName')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DomainNameCount') is not None:
            self.domain_name_count = m.get('DomainNameCount')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrimaryDns') is not None:
            self.primary_dns = m.get('PrimaryDns')

        if m.get('PrivateDnsType') is not None:
            self.private_dns_type = m.get('PrivateDnsType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StandbyDns') is not None:
            self.standby_dns = m.get('StandbyDns')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

