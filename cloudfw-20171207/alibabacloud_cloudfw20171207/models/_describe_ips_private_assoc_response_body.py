# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeIpsPrivateAssocResponseBody(DaraModel):
    def __init__(
        self,
        ips_private_assoc: List[main_models.DescribeIpsPrivateAssocResponseBodyIpsPrivateAssoc] = None,
        request_id: str = None,
        total_count: int = None,
        total_open_count: int = None,
    ):
        self.ips_private_assoc = ips_private_assoc
        self.request_id = request_id
        self.total_count = total_count
        self.total_open_count = total_open_count

    def validate(self):
        if self.ips_private_assoc:
            for v1 in self.ips_private_assoc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpsPrivateAssoc'] = []
        if self.ips_private_assoc is not None:
            for k1 in self.ips_private_assoc:
                result['IpsPrivateAssoc'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_open_count is not None:
            result['TotalOpenCount'] = self.total_open_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips_private_assoc = []
        if m.get('IpsPrivateAssoc') is not None:
            for k1 in m.get('IpsPrivateAssoc'):
                temp_model = main_models.DescribeIpsPrivateAssocResponseBodyIpsPrivateAssoc()
                self.ips_private_assoc.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalOpenCount') is not None:
            self.total_open_count = m.get('TotalOpenCount')

        return self

class DescribeIpsPrivateAssocResponseBodyIpsPrivateAssoc(DaraModel):
    def __init__(
        self,
        assoc_info_status: str = None,
        error_msg: str = None,
        member_uid: int = None,
        protected_ip_list: List[str] = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        status: str = None,
        unprotected_ip_list: List[str] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.assoc_info_status = assoc_info_status
        self.error_msg = error_msg
        self.member_uid = member_uid
        self.protected_ip_list = protected_ip_list
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.status = status
        self.unprotected_ip_list = unprotected_ip_list
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assoc_info_status is not None:
            result['AssocInfoStatus'] = self.assoc_info_status

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.protected_ip_list is not None:
            result['ProtectedIpList'] = self.protected_ip_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.status is not None:
            result['Status'] = self.status

        if self.unprotected_ip_list is not None:
            result['UnprotectedIpList'] = self.unprotected_ip_list

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssocInfoStatus') is not None:
            self.assoc_info_status = m.get('AssocInfoStatus')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('ProtectedIpList') is not None:
            self.protected_ip_list = m.get('ProtectedIpList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnprotectedIpList') is not None:
            self.unprotected_ip_list = m.get('UnprotectedIpList')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

