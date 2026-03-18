# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeDdosOriginInstanceBillResponseBody(DaraModel):
    def __init__(
        self,
        asset_status: int = None,
        debt_status: int = None,
        flow_list: List[main_models.DescribeDdosOriginInstanceBillResponseBodyFlowList] = None,
        flow_region: Dict[str, Any] = None,
        instance_id: str = None,
        ip_count: int = None,
        ip_count_or_function_list: List[main_models.DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList] = None,
        ip_info: str = None,
        monthly_summary_list: List[main_models.DescribeDdosOriginInstanceBillResponseBodyMonthlySummaryList] = None,
        request_id: str = None,
        standard_assets_flow_list: List[main_models.DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList] = None,
        standard_assets_flow_region: Dict[str, Any] = None,
        standard_assets_total_flow_cn: int = None,
        standard_assets_total_flow_ov: int = None,
        status: int = None,
        total_flow_cn: int = None,
        total_flow_ov: int = None,
    ):
        # The asset status.
        # 
        # *   **0**: No asset is added to the instance for protection.
        # *   **1**: Assets are added to the instance for protection.
        self.asset_status = asset_status
        # The payment status. Valid values:
        # 
        # *   **0**: The payment is not overdue.
        # *   **1**: The payment is overdue.
        self.debt_status = debt_status
        # The details about the traffic of EIPs with Anti-DDoS (Enhanced) enabled.
        self.flow_list = flow_list
        # The traffic distribution of EIPs with Anti-DDoS (Enhanced) enabled by region.
        self.flow_region = flow_region
        # The ID of the Anti-DDoS Origin (Pay-as-you-go) instance to query.
        self.instance_id = instance_id
        # The number of protected IP addresses.
        self.ip_count = ip_count
        # The protected IP addresses and enabled features.
        self.ip_count_or_function_list = ip_count_or_function_list
        # The IP address distribution. The JSON struct contains the following fields:
        # 
        # *   **eipCnIpCount**: the number of EIPs with Anti-DDoS (Enhanced) enabled in the Chinese mainland.
        # *   **eipOvIpCount**: the number of EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland.
        # *   **standardAssetsCnIpCount**: the number of IP addresses of regular Alibaba Cloud services in the Chinese mainland.
        # *   **standardAssetsOvIpCount**: the number of IP addresses of regular Alibaba Cloud services outside the Chinese mainland.
        self.ip_info = ip_info
        # The information about the monthly summary bills.
        self.monthly_summary_list = monthly_summary_list
        # The request ID.
        self.request_id = request_id
        # The details about the traffic of regular Alibaba Cloud services.
        self.standard_assets_flow_list = standard_assets_flow_list
        # The traffic distribution of regular Alibaba Cloud services by region.
        self.standard_assets_flow_region = standard_assets_flow_region
        # The total traffic of regular Alibaba Cloud services in the Chinese mainland in the current month.
        self.standard_assets_total_flow_cn = standard_assets_total_flow_cn
        # The total traffic of regular Alibaba Cloud services outside the Chinese mainland in the current month.
        self.standard_assets_total_flow_ov = standard_assets_total_flow_ov
        # The instance status. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        # *   **3**: released
        self.status = status
        # The total traffic of EIPs with Anti-DDoS (Enhanced) enabled in the Chinese mainland in the current month. Unit: bytes.
        self.total_flow_cn = total_flow_cn
        # The total traffic of EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland in the current month. Unit: bytes.
        self.total_flow_ov = total_flow_ov

    def validate(self):
        if self.flow_list:
            for v1 in self.flow_list:
                 if v1:
                    v1.validate()
        if self.ip_count_or_function_list:
            for v1 in self.ip_count_or_function_list:
                 if v1:
                    v1.validate()
        if self.monthly_summary_list:
            for v1 in self.monthly_summary_list:
                 if v1:
                    v1.validate()
        if self.standard_assets_flow_list:
            for v1 in self.standard_assets_flow_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_status is not None:
            result['AssetStatus'] = self.asset_status

        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status

        result['FlowList'] = []
        if self.flow_list is not None:
            for k1 in self.flow_list:
                result['FlowList'].append(k1.to_map() if k1 else None)

        if self.flow_region is not None:
            result['FlowRegion'] = self.flow_region

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        result['IpCountOrFunctionList'] = []
        if self.ip_count_or_function_list is not None:
            for k1 in self.ip_count_or_function_list:
                result['IpCountOrFunctionList'].append(k1.to_map() if k1 else None)

        if self.ip_info is not None:
            result['IpInfo'] = self.ip_info

        result['MonthlySummaryList'] = []
        if self.monthly_summary_list is not None:
            for k1 in self.monthly_summary_list:
                result['MonthlySummaryList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StandardAssetsFlowList'] = []
        if self.standard_assets_flow_list is not None:
            for k1 in self.standard_assets_flow_list:
                result['StandardAssetsFlowList'].append(k1.to_map() if k1 else None)

        if self.standard_assets_flow_region is not None:
            result['StandardAssetsFlowRegion'] = self.standard_assets_flow_region

        if self.standard_assets_total_flow_cn is not None:
            result['StandardAssetsTotalFlowCn'] = self.standard_assets_total_flow_cn

        if self.standard_assets_total_flow_ov is not None:
            result['StandardAssetsTotalFlowOv'] = self.standard_assets_total_flow_ov

        if self.status is not None:
            result['Status'] = self.status

        if self.total_flow_cn is not None:
            result['TotalFlowCn'] = self.total_flow_cn

        if self.total_flow_ov is not None:
            result['TotalFlowOv'] = self.total_flow_ov

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetStatus') is not None:
            self.asset_status = m.get('AssetStatus')

        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')

        self.flow_list = []
        if m.get('FlowList') is not None:
            for k1 in m.get('FlowList'):
                temp_model = main_models.DescribeDdosOriginInstanceBillResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k1))

        if m.get('FlowRegion') is not None:
            self.flow_region = m.get('FlowRegion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        self.ip_count_or_function_list = []
        if m.get('IpCountOrFunctionList') is not None:
            for k1 in m.get('IpCountOrFunctionList'):
                temp_model = main_models.DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList()
                self.ip_count_or_function_list.append(temp_model.from_map(k1))

        if m.get('IpInfo') is not None:
            self.ip_info = m.get('IpInfo')

        self.monthly_summary_list = []
        if m.get('MonthlySummaryList') is not None:
            for k1 in m.get('MonthlySummaryList'):
                temp_model = main_models.DescribeDdosOriginInstanceBillResponseBodyMonthlySummaryList()
                self.monthly_summary_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.standard_assets_flow_list = []
        if m.get('StandardAssetsFlowList') is not None:
            for k1 in m.get('StandardAssetsFlowList'):
                temp_model = main_models.DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList()
                self.standard_assets_flow_list.append(temp_model.from_map(k1))

        if m.get('StandardAssetsFlowRegion') is not None:
            self.standard_assets_flow_region = m.get('StandardAssetsFlowRegion')

        if m.get('StandardAssetsTotalFlowCn') is not None:
            self.standard_assets_total_flow_cn = m.get('StandardAssetsTotalFlowCn')

        if m.get('StandardAssetsTotalFlowOv') is not None:
            self.standard_assets_total_flow_ov = m.get('StandardAssetsTotalFlowOv')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalFlowCn') is not None:
            self.total_flow_cn = m.get('TotalFlowCn')

        if m.get('TotalFlowOv') is not None:
            self.total_flow_ov = m.get('TotalFlowOv')

        return self

class DescribeDdosOriginInstanceBillResponseBodyStandardAssetsFlowList(DaraModel):
    def __init__(
        self,
        member_flow: str = None,
        region_flow: str = None,
        time: int = None,
        total_flow: int = None,
    ):
        # The traffic distribution by region. The JSON struct contains the following fields:
        # 
        # *   **bytes**: the traffic volume of regular Alibaba Cloud services in a region. Unit: bytes.
        # *   **memberUid**: the owner account.
        # *   **instanceId**: the ID of the pay-as-you-go instance that protects the regular Alibaba Cloud services.
        # *   **ip**: the IP address of the regular Alibaba Cloud service protected by the Anti-DDoS Origin instance.
        # *   **region**: the region.
        # 
        # >  If the memberUid field in the JSON struct is empty, the information about the current account is returned. The value of the bytes parameter in the outermost level of the JSON struct indicates the total traffic, and the values of the bytes parameters in inner levels indicate the traffic of the account.
        self.member_flow = member_flow
        # The traffic distribution by region. The JSON struct contains the following fields:
        # 
        # *   **bytes**: the traffic volume of regular Alibaba Cloud services in a region. Unit: bytes.
        # *   **instanceId**: the ID of the pay-as-you-go instance that protects the regular Alibaba Cloud services.
        # *   **ip**: the IP address protected by the Anti-DDoS Origin instance.
        # *   **region**: the region.
        self.region_flow = region_flow
        # The timestamp. Unit: milliseconds.
        self.time = time
        # The traffic of regular Alibaba Cloud services. Unit: bytes.
        self.total_flow = total_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_flow is not None:
            result['MemberFlow'] = self.member_flow

        if self.region_flow is not None:
            result['RegionFlow'] = self.region_flow

        if self.time is not None:
            result['Time'] = self.time

        if self.total_flow is not None:
            result['TotalFlow'] = self.total_flow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberFlow') is not None:
            self.member_flow = m.get('MemberFlow')

        if m.get('RegionFlow') is not None:
            self.region_flow = m.get('RegionFlow')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalFlow') is not None:
            self.total_flow = m.get('TotalFlow')

        return self

class DescribeDdosOriginInstanceBillResponseBodyMonthlySummaryList(DaraModel):
    def __init__(
        self,
        enable_days: int = None,
        flow_cn: int = None,
        flow_intl: int = None,
        ip_count_cn: int = None,
        ip_count_intl: int = None,
        member_uid: str = None,
        standard_assets_flow_cn: int = None,
        standard_assets_flow_intl: int = None,
        uid: str = None,
    ):
        # The number of days that the instance is activated.
        self.enable_days = enable_days
        # The total traffic of EIPs with Anti-DDoS (Enhanced) enabled in the Chinese mainland. Unit: bytes.
        self.flow_cn = flow_cn
        # The total traffic of EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland. Unit: bytes.
        self.flow_intl = flow_intl
        # The total number of protected IP addresses in the Chinese mainland.
        # 
        # >  The total number of protected IP addresses is the sum of the daily numbers of protected IP addresses in a month.
        self.ip_count_cn = ip_count_cn
        # The total number of protected IP addresses outside the Chinese mainland.
        # 
        # >  The total number of protected IP addresses is the sum of the daily numbers of protected IP addresses in a month.
        self.ip_count_intl = ip_count_intl
        # The ID of the member.
        self.member_uid = member_uid
        # The total traffic of regular Alibaba Cloud services in the Chinese mainland. Unit: bytes.
        self.standard_assets_flow_cn = standard_assets_flow_cn
        # The total traffic of regular Alibaba Cloud services outside the Chinese mainland. Unit: bytes.
        self.standard_assets_flow_intl = standard_assets_flow_intl
        # The ID of the administrator account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_days is not None:
            result['EnableDays'] = self.enable_days

        if self.flow_cn is not None:
            result['FlowCn'] = self.flow_cn

        if self.flow_intl is not None:
            result['FlowIntl'] = self.flow_intl

        if self.ip_count_cn is not None:
            result['IpCountCn'] = self.ip_count_cn

        if self.ip_count_intl is not None:
            result['IpCountIntl'] = self.ip_count_intl

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.standard_assets_flow_cn is not None:
            result['StandardAssetsFlowCn'] = self.standard_assets_flow_cn

        if self.standard_assets_flow_intl is not None:
            result['StandardAssetsFlowIntl'] = self.standard_assets_flow_intl

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDays') is not None:
            self.enable_days = m.get('EnableDays')

        if m.get('FlowCn') is not None:
            self.flow_cn = m.get('FlowCn')

        if m.get('FlowIntl') is not None:
            self.flow_intl = m.get('FlowIntl')

        if m.get('IpCountCn') is not None:
            self.ip_count_cn = m.get('IpCountCn')

        if m.get('IpCountIntl') is not None:
            self.ip_count_intl = m.get('IpCountIntl')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('StandardAssetsFlowCn') is not None:
            self.standard_assets_flow_cn = m.get('StandardAssetsFlowCn')

        if m.get('StandardAssetsFlowIntl') is not None:
            self.standard_assets_flow_intl = m.get('StandardAssetsFlowIntl')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class DescribeDdosOriginInstanceBillResponseBodyIpCountOrFunctionList(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        ip_cnt_cn: int = None,
        ip_cnt_ov: int = None,
        member_ip_cnt: str = None,
        time: int = None,
    ):
        # The application scope of the instance. Valid values:
        # 
        # *   **only_mainland_china**: regions in the Chinese mainland.
        # *   **global**: all regions.
        # *   **international_and_hmt**: regions outside the Chinese mainland.
        self.coverage = coverage
        # The number of IP addresses protected by the pay-as-you-go instance in the Chinese mainland.
        self.ip_cnt_cn = ip_cnt_cn
        # The number of IP addresses protected by the pay-as-you-go instance outside the Chinese mainland.
        self.ip_cnt_ov = ip_cnt_ov
        # The bill distribution by account. The JSON struct contains the following fields:
        # 
        # *   **eipCnIpCount**: the number of EIPs with Anti-DDoS (Enhanced) enabled in the Chinese mainland.
        # *   **eipOvIpCount**: the number of EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland.
        # *   **memberUid**: the owner account.
        # *   **standardAssetsCnIpCount**: the number of IP addresses of regular Alibaba Cloud services in the Chinese mainland.
        # *   **standardAssetsOvIpCount**: the number of IP addresses of regular Alibaba Cloud services outside the Chinese mainland.
        # 
        # >  If the memberUid field in the JSON struct is empty, the information about the current account is returned.
        self.member_ip_cnt = member_ip_cnt
        # The billing time. Unit: milliseconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.ip_cnt_cn is not None:
            result['IpCntCn'] = self.ip_cnt_cn

        if self.ip_cnt_ov is not None:
            result['IpCntOv'] = self.ip_cnt_ov

        if self.member_ip_cnt is not None:
            result['MemberIpCnt'] = self.member_ip_cnt

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('IpCntCn') is not None:
            self.ip_cnt_cn = m.get('IpCntCn')

        if m.get('IpCntOv') is not None:
            self.ip_cnt_ov = m.get('IpCntOv')

        if m.get('MemberIpCnt') is not None:
            self.member_ip_cnt = m.get('MemberIpCnt')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class DescribeDdosOriginInstanceBillResponseBodyFlowList(DaraModel):
    def __init__(
        self,
        member_flow: str = None,
        region_flow: str = None,
        time: int = None,
        total_bill_flow: int = None,
        total_flow: int = None,
    ):
        # The traffic distribution by region. The JSON struct contains the following fields:
        # 
        # *   **bytes**: the traffic volume of EIPs with Anti-DDoS (Enhanced) enabled in a region. Unit: bytes.
        # *   **memberUid**: the owner account.
        # *   **instanceId**: the ID of the pay-as-you-go instance that protects the EIPs with Anti-DDoS (Enhanced) enabled.
        # *   **ip**: the EIPs with Anti-DDoS (Enhanced) enabled.
        # *   **region**: the region.
        # 
        # >  If the memberUid field in the JSON struct is empty, the information about the current account is returned. The value of the bytes parameter in the outermost level of the JSON struct indicates the total traffic, and the values of the bytes parameters in inner levels indicate the traffic of the account.
        self.member_flow = member_flow
        # The traffic distribution by region. The JSON struct contains the following fields:
        # 
        # *   **bytes**: the traffic volume of EIPs with Anti-DDoS (Enhanced) enabled in a region. Unit: bytes.
        # *   **instanceId**: the ID of the pay-as-you-go instance that protects the EIPs with Anti-DDoS (Enhanced) enabled.
        # *   **ip**: the EIPs with Anti-DDoS (Enhanced) enabled.
        # *   **region**: the region.
        self.region_flow = region_flow
        # The timestamp. Unit: milliseconds.
        self.time = time
        # The total IP traffic of regular Alibaba Cloud services.
        self.total_bill_flow = total_bill_flow
        # The traffic of EIPs with Anti-DDoS (Enhanced) enabled. Unit: bytes.
        self.total_flow = total_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_flow is not None:
            result['MemberFlow'] = self.member_flow

        if self.region_flow is not None:
            result['RegionFlow'] = self.region_flow

        if self.time is not None:
            result['Time'] = self.time

        if self.total_bill_flow is not None:
            result['TotalBillFlow'] = self.total_bill_flow

        if self.total_flow is not None:
            result['TotalFlow'] = self.total_flow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberFlow') is not None:
            self.member_flow = m.get('MemberFlow')

        if m.get('RegionFlow') is not None:
            self.region_flow = m.get('RegionFlow')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalBillFlow') is not None:
            self.total_bill_flow = m.get('TotalBillFlow')

        if m.get('TotalFlow') is not None:
            self.total_flow = m.get('TotalFlow')

        return self

