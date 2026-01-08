# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetOpenIpResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeInternetOpenIpResponseBodyDataList] = None,
        page_info: main_models.DescribeInternetOpenIpResponseBodyPageInfo = None,
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
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeInternetOpenIpResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeInternetOpenIpResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInternetOpenIpResponseBodyPageInfo(DaraModel):
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

class DescribeInternetOpenIpResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acl_recommend_detail: str = None,
        assets_instance_id: str = None,
        assets_name: str = None,
        assets_type: str = None,
        detail_num: int = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        member_uid: int = None,
        out_bytes: int = None,
        port_list: List[str] = None,
        public_ip: str = None,
        region_no: str = None,
        risk_level: int = None,
        risk_reason: str = None,
        service_name_list: List[str] = None,
        src_ip_cnt: int = None,
        total_bytes: int = None,
        total_reply_bytes: int = None,
        traffic_percent_1day: str = None,
        traffic_percent_30day: str = None,
        traffic_percent_7day: str = None,
        unknown_reason: List[str] = None,
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
        # *   **true**
        # *   **false**
        self.has_acl_recommend = has_acl_recommend
        # The inbound network throughput, which indicates the total number of bytes that are sent inbound. Unit: bytes.
        self.in_bytes = in_bytes
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The outbound network throughput, which indicates the total number of bytes that are sent outbound. Unit: bytes.
        self.out_bytes = out_bytes
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
        # The total inbound and outbound network throughput, which indicates the total number of bytes that are sent inbound and outbound. Unit: bytes.
        self.total_bytes = total_bytes
        # Outbound traffic in the last 7 days.
        self.total_reply_bytes = total_reply_bytes
        # For detailed traffic information, see the TotalBytes field.
        self.traffic_percent_1day = traffic_percent_1day
        # For detailed traffic information, see the TotalBytes field.
        self.traffic_percent_30day = traffic_percent_30day
        # For detailed traffic information, see the TotalBytes field.
        self.traffic_percent_7day = traffic_percent_7day
        # Reasons for not analyzing the protocol when the protocol is identified as Unknown.
        self.unknown_reason = unknown_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

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

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.total_reply_bytes is not None:
            result['TotalReplyBytes'] = self.total_reply_bytes

        if self.traffic_percent_1day is not None:
            result['TrafficPercent1Day'] = self.traffic_percent_1day

        if self.traffic_percent_30day is not None:
            result['TrafficPercent30Day'] = self.traffic_percent_30day

        if self.traffic_percent_7day is not None:
            result['TrafficPercent7Day'] = self.traffic_percent_7day

        if self.unknown_reason is not None:
            result['UnknownReason'] = self.unknown_reason

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

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

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

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalReplyBytes') is not None:
            self.total_reply_bytes = m.get('TotalReplyBytes')

        if m.get('TrafficPercent1Day') is not None:
            self.traffic_percent_1day = m.get('TrafficPercent1Day')

        if m.get('TrafficPercent30Day') is not None:
            self.traffic_percent_30day = m.get('TrafficPercent30Day')

        if m.get('TrafficPercent7Day') is not None:
            self.traffic_percent_7day = m.get('TrafficPercent7Day')

        if m.get('UnknownReason') is not None:
            self.unknown_reason = m.get('UnknownReason')

        return self

