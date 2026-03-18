# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribePackIpListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        ip_list: List[main_models.DescribePackIpListResponseBodyIpList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code of the request.
        # 
        # For more information about status codes, see [Common parameters](https://help.aliyun.com/document_detail/118841.html).
        self.code = code
        # The IP addresses that are protected by the instance.
        self.ip_list = ip_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success
        # The number of protected IP addresses.
        self.total = total

    def validate(self):
        if self.ip_list:
            for v1 in self.ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IpList'] = []
        if self.ip_list is not None:
            for k1 in self.ip_list:
                result['IpList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.ip_list = []
        if m.get('IpList') is not None:
            for k1 in m.get('IpList'):
                temp_model = main_models.DescribePackIpListResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePackIpListResponseBodyIpList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        member_uid: str = None,
        nsm_expire_at: int = None,
        nsm_start_at: int = None,
        nsm_status: int = None,
        product: str = None,
        region: str = None,
        remark: str = None,
        status: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The ID of the member.
        self.member_uid = member_uid
        # The time when the near-origin traffic diversion feature was disabled.
        self.nsm_expire_at = nsm_expire_at
        # The time when the near-origin traffic diversion feature was enabled.
        self.nsm_start_at = nsm_start_at
        # The status of the near-origin traffic diversion feature. Valid values:
        # 
        # *   **1**: The near-origin traffic diversion feature is enabled.
        # *   **0**: The near-origin traffic diversion feature is disabled.
        self.nsm_status = nsm_status
        # The type of the cloud asset to which the IP address belongs. Valid values:
        # 
        # *   **ECS**: an ECS instance.
        # *   **SLB**: a CLB (formerly SLB) instance.
        # *   **EIP**: an EIP. If the IP address belongs to an ALB instance, the value EIP is returned.
        # *   **WAF**: a WAF instance.
        self.product = product
        # The region to which the protected IP address belongs.
        # 
        # >  If the protected IP address is in the same region as the instance, this parameter is not returned.
        self.region = region
        # The description of the cloud asset to which the IP address belongs. The asset can be an ECS instance or an SLB instance.
        # 
        # >  If no descriptions are provided for the asset, this parameter is not returned.
        self.remark = remark
        # The status of the IP address. Valid values:
        # 
        # *   **normal**: The IP address is not under attack.
        # *   **hole_begin**: Blackhole filtering is triggered for the IP address.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.nsm_expire_at is not None:
            result['NsmExpireAt'] = self.nsm_expire_at

        if self.nsm_start_at is not None:
            result['NsmStartAt'] = self.nsm_start_at

        if self.nsm_status is not None:
            result['NsmStatus'] = self.nsm_status

        if self.product is not None:
            result['Product'] = self.product

        if self.region is not None:
            result['Region'] = self.region

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NsmExpireAt') is not None:
            self.nsm_expire_at = m.get('NsmExpireAt')

        if m.get('NsmStartAt') is not None:
            self.nsm_start_at = m.get('NsmStartAt')

        if m.get('NsmStatus') is not None:
            self.nsm_status = m.get('NsmStatus')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

