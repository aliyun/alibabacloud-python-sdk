# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetStatisticResponseBody(DaraModel):
    def __init__(
        self,
        general_instance_spec_statistic: main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatistic = None,
        request_id: str = None,
        resource_spec_statistic: main_models.DescribeAssetStatisticResponseBodyResourceSpecStatistic = None,
    ):
        self.general_instance_spec_statistic = general_instance_spec_statistic
        # The request ID.
        self.request_id = request_id
        # The statistics on specifications.
        self.resource_spec_statistic = resource_spec_statistic

    def validate(self):
        if self.general_instance_spec_statistic:
            self.general_instance_spec_statistic.validate()
        if self.resource_spec_statistic:
            self.resource_spec_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.general_instance_spec_statistic is not None:
            result['GeneralInstanceSpecStatistic'] = self.general_instance_spec_statistic.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_spec_statistic is not None:
            result['ResourceSpecStatistic'] = self.resource_spec_statistic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeneralInstanceSpecStatistic') is not None:
            temp_model = main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatistic()
            self.general_instance_spec_statistic = temp_model.from_map(m.get('GeneralInstanceSpecStatistic'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceSpecStatistic') is not None:
            temp_model = main_models.DescribeAssetStatisticResponseBodyResourceSpecStatistic()
            self.resource_spec_statistic = temp_model.from_map(m.get('ResourceSpecStatistic'))

        return self

class DescribeAssetStatisticResponseBodyResourceSpecStatistic(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatistic(DaraModel):
    def __init__(
        self,
        cfw_general_instance_region_statistic: List[main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwGeneralInstanceRegionStatistic] = None,
        cfw_total_general_instance_region_statistic: List[main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwTotalGeneralInstanceRegionStatistic] = None,
        total_cfw_general_instance_cnt: int = None,
        total_cfw_general_instance_used_cnt: int = None,
        total_general_instance_used_cnt: int = None,
        total_nat_general_instance_cnt: int = None,
        total_nat_general_instance_used_cnt: int = None,
        total_vfw_general_instance_used_cnt: int = None,
    ):
        self.cfw_general_instance_region_statistic = cfw_general_instance_region_statistic
        self.cfw_total_general_instance_region_statistic = cfw_total_general_instance_region_statistic
        self.total_cfw_general_instance_cnt = total_cfw_general_instance_cnt
        self.total_cfw_general_instance_used_cnt = total_cfw_general_instance_used_cnt
        self.total_general_instance_used_cnt = total_general_instance_used_cnt
        self.total_nat_general_instance_cnt = total_nat_general_instance_cnt
        self.total_nat_general_instance_used_cnt = total_nat_general_instance_used_cnt
        self.total_vfw_general_instance_used_cnt = total_vfw_general_instance_used_cnt

    def validate(self):
        if self.cfw_general_instance_region_statistic:
            for v1 in self.cfw_general_instance_region_statistic:
                 if v1:
                    v1.validate()
        if self.cfw_total_general_instance_region_statistic:
            for v1 in self.cfw_total_general_instance_region_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CfwGeneralInstanceRegionStatistic'] = []
        if self.cfw_general_instance_region_statistic is not None:
            for k1 in self.cfw_general_instance_region_statistic:
                result['CfwGeneralInstanceRegionStatistic'].append(k1.to_map() if k1 else None)

        result['CfwTotalGeneralInstanceRegionStatistic'] = []
        if self.cfw_total_general_instance_region_statistic is not None:
            for k1 in self.cfw_total_general_instance_region_statistic:
                result['CfwTotalGeneralInstanceRegionStatistic'].append(k1.to_map() if k1 else None)

        if self.total_cfw_general_instance_cnt is not None:
            result['TotalCfwGeneralInstanceCnt'] = self.total_cfw_general_instance_cnt

        if self.total_cfw_general_instance_used_cnt is not None:
            result['TotalCfwGeneralInstanceUsedCnt'] = self.total_cfw_general_instance_used_cnt

        if self.total_general_instance_used_cnt is not None:
            result['TotalGeneralInstanceUsedCnt'] = self.total_general_instance_used_cnt

        if self.total_nat_general_instance_cnt is not None:
            result['TotalNatGeneralInstanceCnt'] = self.total_nat_general_instance_cnt

        if self.total_nat_general_instance_used_cnt is not None:
            result['TotalNatGeneralInstanceUsedCnt'] = self.total_nat_general_instance_used_cnt

        if self.total_vfw_general_instance_used_cnt is not None:
            result['TotalVfwGeneralInstanceUsedCnt'] = self.total_vfw_general_instance_used_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cfw_general_instance_region_statistic = []
        if m.get('CfwGeneralInstanceRegionStatistic') is not None:
            for k1 in m.get('CfwGeneralInstanceRegionStatistic'):
                temp_model = main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwGeneralInstanceRegionStatistic()
                self.cfw_general_instance_region_statistic.append(temp_model.from_map(k1))

        self.cfw_total_general_instance_region_statistic = []
        if m.get('CfwTotalGeneralInstanceRegionStatistic') is not None:
            for k1 in m.get('CfwTotalGeneralInstanceRegionStatistic'):
                temp_model = main_models.DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwTotalGeneralInstanceRegionStatistic()
                self.cfw_total_general_instance_region_statistic.append(temp_model.from_map(k1))

        if m.get('TotalCfwGeneralInstanceCnt') is not None:
            self.total_cfw_general_instance_cnt = m.get('TotalCfwGeneralInstanceCnt')

        if m.get('TotalCfwGeneralInstanceUsedCnt') is not None:
            self.total_cfw_general_instance_used_cnt = m.get('TotalCfwGeneralInstanceUsedCnt')

        if m.get('TotalGeneralInstanceUsedCnt') is not None:
            self.total_general_instance_used_cnt = m.get('TotalGeneralInstanceUsedCnt')

        if m.get('TotalNatGeneralInstanceCnt') is not None:
            self.total_nat_general_instance_cnt = m.get('TotalNatGeneralInstanceCnt')

        if m.get('TotalNatGeneralInstanceUsedCnt') is not None:
            self.total_nat_general_instance_used_cnt = m.get('TotalNatGeneralInstanceUsedCnt')

        if m.get('TotalVfwGeneralInstanceUsedCnt') is not None:
            self.total_vfw_general_instance_used_cnt = m.get('TotalVfwGeneralInstanceUsedCnt')

        return self

class DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwTotalGeneralInstanceRegionStatistic(DaraModel):
    def __init__(
        self,
        member_list: List[str] = None,
        region_no: str = None,
    ):
        self.member_list = member_list
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_list is not None:
            result['MemberList'] = self.member_list

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeAssetStatisticResponseBodyGeneralInstanceSpecStatisticCfwGeneralInstanceRegionStatistic(DaraModel):
    def __init__(
        self,
        member_list: List[str] = None,
        region_no: str = None,
    ):
        self.member_list = member_list
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_list is not None:
            result['MemberList'] = self.member_list

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

