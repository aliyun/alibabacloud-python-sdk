# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowChartResponseBody(DaraModel):
    def __init__(
        self,
        flow_chart: List[main_models.DescribeFlowChartResponseBodyFlowChart] = None,
        request_id: str = None,
    ):
        # The traffic statistics.
        self.flow_chart = flow_chart
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.flow_chart:
            for v1 in self.flow_chart:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowChart'] = []
        if self.flow_chart is not None:
            for k1 in self.flow_chart:
                result['FlowChart'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_chart = []
        if m.get('FlowChart') is not None:
            for k1 in m.get('FlowChart'):
                temp_model = main_models.DescribeFlowChartResponseBodyFlowChart()
                self.flow_chart.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFlowChartResponseBodyFlowChart(DaraModel):
    def __init__(
        self,
        acl_custom_block_sum: int = None,
        acl_custom_reports_sum: int = None,
        anti_scan_block_sum: int = None,
        antibot_block_sum: int = None,
        antibot_report_sum: str = None,
        antiscan_reports_sum: int = None,
        blacklist_block_sum: str = None,
        blacklist_reports_sum: int = None,
        cc_custom_block_sum: int = None,
        cc_custom_reports_sum: int = None,
        cc_system_blocks_sum: int = None,
        cc_system_reports_sum: int = None,
        count: int = None,
        in_bytes: int = None,
        index: int = None,
        max_pv: int = None,
        out_bytes: int = None,
        ratelimit_block_sum: int = None,
        ratelimit_report_sum: int = None,
        region_block_blocks_sum: int = None,
        region_block_reports_sum: int = None,
        robot_count: int = None,
        waf_block_sum: int = None,
        waf_report_sum: str = None,
    ):
        # The number of requests that are blocked by custom access control list (ACL) rules.
        self.acl_custom_block_sum = acl_custom_block_sum
        # The number of requests that are monitored by custom ACL rules.
        self.acl_custom_reports_sum = acl_custom_reports_sum
        # The number of requests that are blocked by scan protection rules.
        self.anti_scan_block_sum = anti_scan_block_sum
        # The number of requests that are blocked by bot management rules.
        self.antibot_block_sum = antibot_block_sum
        # The number of requests that are monitored by bot management rules.
        self.antibot_report_sum = antibot_report_sum
        # The number of requests that are monitored by scan protection rules.
        self.antiscan_reports_sum = antiscan_reports_sum
        # The number of requests that are blocked by the IP address blacklist.
        self.blacklist_block_sum = blacklist_block_sum
        # The number of requests that are monitored by the IP address blacklist.
        self.blacklist_reports_sum = blacklist_reports_sum
        # The number of requests that are blocked by custom HTTP flood protection rules.
        self.cc_custom_block_sum = cc_custom_block_sum
        # The number of requests that are monitored by custom HTTP flood protection rules.
        self.cc_custom_reports_sum = cc_custom_reports_sum
        # The number of requests that are blocked by HTTP flood protection rules created by the system.
        self.cc_system_blocks_sum = cc_system_blocks_sum
        # The number of requests that are monitored by HTTP flood protection rules created by the system.
        self.cc_system_reports_sum = cc_system_reports_sum
        # The total number of requests.
        self.count = count
        # The total number of requests that are redirected to the WAF instance.
        self.in_bytes = in_bytes
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
        self.index = index
        # The peak traffic.
        self.max_pv = max_pv
        # The total number of requests that are forwarded by the WAF instance.
        self.out_bytes = out_bytes
        # The number of requests that are blocked by rate limiting rules.
        self.ratelimit_block_sum = ratelimit_block_sum
        # The number of requests that are monitored by rate limiting rules.
        self.ratelimit_report_sum = ratelimit_report_sum
        # The number of requests that are blocked by region blacklist rules.
        self.region_block_blocks_sum = region_block_blocks_sum
        # The number of requests that are monitored by region blacklist rules.
        self.region_block_reports_sum = region_block_reports_sum
        # The total number of bot requests.
        self.robot_count = robot_count
        # The number of requests that are blocked by basic protection rules.
        self.waf_block_sum = waf_block_sum
        # The number of requests that are monitored by basic protection rules.
        self.waf_report_sum = waf_report_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_custom_block_sum is not None:
            result['AclCustomBlockSum'] = self.acl_custom_block_sum

        if self.acl_custom_reports_sum is not None:
            result['AclCustomReportsSum'] = self.acl_custom_reports_sum

        if self.anti_scan_block_sum is not None:
            result['AntiScanBlockSum'] = self.anti_scan_block_sum

        if self.antibot_block_sum is not None:
            result['AntibotBlockSum'] = self.antibot_block_sum

        if self.antibot_report_sum is not None:
            result['AntibotReportSum'] = self.antibot_report_sum

        if self.antiscan_reports_sum is not None:
            result['AntiscanReportsSum'] = self.antiscan_reports_sum

        if self.blacklist_block_sum is not None:
            result['BlacklistBlockSum'] = self.blacklist_block_sum

        if self.blacklist_reports_sum is not None:
            result['BlacklistReportsSum'] = self.blacklist_reports_sum

        if self.cc_custom_block_sum is not None:
            result['CcCustomBlockSum'] = self.cc_custom_block_sum

        if self.cc_custom_reports_sum is not None:
            result['CcCustomReportsSum'] = self.cc_custom_reports_sum

        if self.cc_system_blocks_sum is not None:
            result['CcSystemBlocksSum'] = self.cc_system_blocks_sum

        if self.cc_system_reports_sum is not None:
            result['CcSystemReportsSum'] = self.cc_system_reports_sum

        if self.count is not None:
            result['Count'] = self.count

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.index is not None:
            result['Index'] = self.index

        if self.max_pv is not None:
            result['MaxPv'] = self.max_pv

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.ratelimit_block_sum is not None:
            result['RatelimitBlockSum'] = self.ratelimit_block_sum

        if self.ratelimit_report_sum is not None:
            result['RatelimitReportSum'] = self.ratelimit_report_sum

        if self.region_block_blocks_sum is not None:
            result['RegionBlockBlocksSum'] = self.region_block_blocks_sum

        if self.region_block_reports_sum is not None:
            result['RegionBlockReportsSum'] = self.region_block_reports_sum

        if self.robot_count is not None:
            result['RobotCount'] = self.robot_count

        if self.waf_block_sum is not None:
            result['WafBlockSum'] = self.waf_block_sum

        if self.waf_report_sum is not None:
            result['WafReportSum'] = self.waf_report_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCustomBlockSum') is not None:
            self.acl_custom_block_sum = m.get('AclCustomBlockSum')

        if m.get('AclCustomReportsSum') is not None:
            self.acl_custom_reports_sum = m.get('AclCustomReportsSum')

        if m.get('AntiScanBlockSum') is not None:
            self.anti_scan_block_sum = m.get('AntiScanBlockSum')

        if m.get('AntibotBlockSum') is not None:
            self.antibot_block_sum = m.get('AntibotBlockSum')

        if m.get('AntibotReportSum') is not None:
            self.antibot_report_sum = m.get('AntibotReportSum')

        if m.get('AntiscanReportsSum') is not None:
            self.antiscan_reports_sum = m.get('AntiscanReportsSum')

        if m.get('BlacklistBlockSum') is not None:
            self.blacklist_block_sum = m.get('BlacklistBlockSum')

        if m.get('BlacklistReportsSum') is not None:
            self.blacklist_reports_sum = m.get('BlacklistReportsSum')

        if m.get('CcCustomBlockSum') is not None:
            self.cc_custom_block_sum = m.get('CcCustomBlockSum')

        if m.get('CcCustomReportsSum') is not None:
            self.cc_custom_reports_sum = m.get('CcCustomReportsSum')

        if m.get('CcSystemBlocksSum') is not None:
            self.cc_system_blocks_sum = m.get('CcSystemBlocksSum')

        if m.get('CcSystemReportsSum') is not None:
            self.cc_system_reports_sum = m.get('CcSystemReportsSum')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('MaxPv') is not None:
            self.max_pv = m.get('MaxPv')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('RatelimitBlockSum') is not None:
            self.ratelimit_block_sum = m.get('RatelimitBlockSum')

        if m.get('RatelimitReportSum') is not None:
            self.ratelimit_report_sum = m.get('RatelimitReportSum')

        if m.get('RegionBlockBlocksSum') is not None:
            self.region_block_blocks_sum = m.get('RegionBlockBlocksSum')

        if m.get('RegionBlockReportsSum') is not None:
            self.region_block_reports_sum = m.get('RegionBlockReportsSum')

        if m.get('RobotCount') is not None:
            self.robot_count = m.get('RobotCount')

        if m.get('WafBlockSum') is not None:
            self.waf_block_sum = m.get('WafBlockSum')

        if m.get('WafReportSum') is not None:
            self.waf_report_sum = m.get('WafReportSum')

        return self

