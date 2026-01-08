# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInvadeEventListResponseBody(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.DescribeInvadeEventListResponseBodyEventList] = None,
        high_level_percent: int = None,
        low_level_percent: int = None,
        middle_level_percent: int = None,
        page_info: main_models.DescribeInvadeEventListResponseBodyPageInfo = None,
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
            for v1 in self.event_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('EventList'):
                temp_model = main_models.DescribeInvadeEventListResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('HighLevelPercent') is not None:
            self.high_level_percent = m.get('HighLevelPercent')

        if m.get('LowLevelPercent') is not None:
            self.low_level_percent = m.get('LowLevelPercent')

        if m.get('MiddleLevelPercent') is not None:
            self.middle_level_percent = m.get('MiddleLevelPercent')

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeInvadeEventListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvadeEventListResponseBodyPageInfo(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeInvadeEventListResponseBodyEventList(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

