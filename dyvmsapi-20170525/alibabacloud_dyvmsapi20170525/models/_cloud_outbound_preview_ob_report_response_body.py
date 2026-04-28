# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudOutboundPreviewObReportResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudOutboundPreviewObReportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudOutboundPreviewObReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudOutboundPreviewObReportResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudOutboundPreviewObReportResponseBodyDataList] = None,
        page_size: str = None,
        total_count: str = None,
        total_page_count: str = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total_count = total_count
        self.total_page_count = total_page_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.CloudOutboundPreviewObReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')

        return self

class CloudOutboundPreviewObReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_answered_count: str = None,
        agent_name: str = None,
        agent_rate: str = None,
        avg_bridge_time: str = None,
        axb_both_answered_count: str = None,
        axb_both_answered_rate: str = None,
        axb_both_answered_time: str = None,
        axb_ob_total_count: str = None,
        both_answered_count: str = None,
        both_answered_time: str = None,
        call_bridged_rate: str = None,
        call_total_count: str = None,
        cno: str = None,
        customer_answered_count: str = None,
        customer_rate: str = None,
        date_time_range: str = None,
        enterprise_id: str = None,
        interception_count: str = None,
        interception_rate: str = None,
        landline_both_answered_count: str = None,
        landline_both_answered_rate: str = None,
        landline_both_answered_time: str = None,
        landline_ob_total_count: str = None,
        max_bridge_time: str = None,
        min_bridge_time: str = None,
        total_bridge_time: str = None,
        total_count: str = None,
        vad_rate: str = None,
        valid_avg_bridge_time: str = None,
        valid_calls: str = None,
        valid_total_bridge_time: str = None,
    ):
        # 座席接听数
        self.agent_answered_count = agent_answered_count
        # 座席姓名
        self.agent_name = agent_name
        # 座席接听率
        self.agent_rate = agent_rate
        # 平均通话时长
        self.avg_bridge_time = avg_bridge_time
        # AXB双方接听数
        self.axb_both_answered_count = axb_both_answered_count
        # AXB双方接听率 = AXB双方接听数 / AXB外呼总数
        self.axb_both_answered_rate = axb_both_answered_rate
        # AXB外呼双方接听分钟数
        self.axb_both_answered_time = axb_both_answered_time
        # AXB外呼总数
        self.axb_ob_total_count = axb_ob_total_count
        # 双方接听数
        self.both_answered_count = both_answered_count
        # 双方接听时长
        self.both_answered_time = both_answered_time
        # 呼叫接通率
        self.call_bridged_rate = call_bridged_rate
        # 发起呼叫次数
        self.call_total_count = call_total_count
        # 座席工号
        self.cno = cno
        # 客户接听数
        self.customer_answered_count = customer_answered_count
        # 客户接听率
        self.customer_rate = customer_rate
        # 统计周期
        self.date_time_range = date_time_range
        # 企业Id
        self.enterprise_id = enterprise_id
        # 拦截次数
        self.interception_count = interception_count
        # 拦截率
        self.interception_rate = interception_rate
        # 固话双方接听数
        self.landline_both_answered_count = landline_both_answered_count
        # 固话双方接听率 = 固话双方接听数 / 固话外呼总数
        self.landline_both_answered_rate = landline_both_answered_rate
        # 固话双方接听分钟数
        self.landline_both_answered_time = landline_both_answered_time
        # 固话外呼总数
        self.landline_ob_total_count = landline_ob_total_count
        # 最长通话时长
        self.max_bridge_time = max_bridge_time
        # 最短通话时长
        self.min_bridge_time = min_bridge_time
        # 总通话时长
        self.total_bridge_time = total_bridge_time
        # 外呼总数
        self.total_count = total_count
        # 通话占比
        self.vad_rate = vad_rate
        # 有效通话平均通话时长
        self.valid_avg_bridge_time = valid_avg_bridge_time
        # 有效通话次数
        self.valid_calls = valid_calls
        # 有效通话总通话时长
        self.valid_total_bridge_time = valid_total_bridge_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_answered_count is not None:
            result['AgentAnsweredCount'] = self.agent_answered_count

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_rate is not None:
            result['AgentRate'] = self.agent_rate

        if self.avg_bridge_time is not None:
            result['AvgBridgeTime'] = self.avg_bridge_time

        if self.axb_both_answered_count is not None:
            result['AxbBothAnsweredCount'] = self.axb_both_answered_count

        if self.axb_both_answered_rate is not None:
            result['AxbBothAnsweredRate'] = self.axb_both_answered_rate

        if self.axb_both_answered_time is not None:
            result['AxbBothAnsweredTime'] = self.axb_both_answered_time

        if self.axb_ob_total_count is not None:
            result['AxbObTotalCount'] = self.axb_ob_total_count

        if self.both_answered_count is not None:
            result['BothAnsweredCount'] = self.both_answered_count

        if self.both_answered_time is not None:
            result['BothAnsweredTime'] = self.both_answered_time

        if self.call_bridged_rate is not None:
            result['CallBridgedRate'] = self.call_bridged_rate

        if self.call_total_count is not None:
            result['CallTotalCount'] = self.call_total_count

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_answered_count is not None:
            result['CustomerAnsweredCount'] = self.customer_answered_count

        if self.customer_rate is not None:
            result['CustomerRate'] = self.customer_rate

        if self.date_time_range is not None:
            result['DateTimeRange'] = self.date_time_range

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.interception_count is not None:
            result['InterceptionCount'] = self.interception_count

        if self.interception_rate is not None:
            result['InterceptionRate'] = self.interception_rate

        if self.landline_both_answered_count is not None:
            result['LandlineBothAnsweredCount'] = self.landline_both_answered_count

        if self.landline_both_answered_rate is not None:
            result['LandlineBothAnsweredRate'] = self.landline_both_answered_rate

        if self.landline_both_answered_time is not None:
            result['LandlineBothAnsweredTime'] = self.landline_both_answered_time

        if self.landline_ob_total_count is not None:
            result['LandlineObTotalCount'] = self.landline_ob_total_count

        if self.max_bridge_time is not None:
            result['MaxBridgeTime'] = self.max_bridge_time

        if self.min_bridge_time is not None:
            result['MinBridgeTime'] = self.min_bridge_time

        if self.total_bridge_time is not None:
            result['TotalBridgeTime'] = self.total_bridge_time

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vad_rate is not None:
            result['VadRate'] = self.vad_rate

        if self.valid_avg_bridge_time is not None:
            result['ValidAvgBridgeTime'] = self.valid_avg_bridge_time

        if self.valid_calls is not None:
            result['ValidCalls'] = self.valid_calls

        if self.valid_total_bridge_time is not None:
            result['ValidTotalBridgeTime'] = self.valid_total_bridge_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentAnsweredCount') is not None:
            self.agent_answered_count = m.get('AgentAnsweredCount')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentRate') is not None:
            self.agent_rate = m.get('AgentRate')

        if m.get('AvgBridgeTime') is not None:
            self.avg_bridge_time = m.get('AvgBridgeTime')

        if m.get('AxbBothAnsweredCount') is not None:
            self.axb_both_answered_count = m.get('AxbBothAnsweredCount')

        if m.get('AxbBothAnsweredRate') is not None:
            self.axb_both_answered_rate = m.get('AxbBothAnsweredRate')

        if m.get('AxbBothAnsweredTime') is not None:
            self.axb_both_answered_time = m.get('AxbBothAnsweredTime')

        if m.get('AxbObTotalCount') is not None:
            self.axb_ob_total_count = m.get('AxbObTotalCount')

        if m.get('BothAnsweredCount') is not None:
            self.both_answered_count = m.get('BothAnsweredCount')

        if m.get('BothAnsweredTime') is not None:
            self.both_answered_time = m.get('BothAnsweredTime')

        if m.get('CallBridgedRate') is not None:
            self.call_bridged_rate = m.get('CallBridgedRate')

        if m.get('CallTotalCount') is not None:
            self.call_total_count = m.get('CallTotalCount')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerAnsweredCount') is not None:
            self.customer_answered_count = m.get('CustomerAnsweredCount')

        if m.get('CustomerRate') is not None:
            self.customer_rate = m.get('CustomerRate')

        if m.get('DateTimeRange') is not None:
            self.date_time_range = m.get('DateTimeRange')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('InterceptionCount') is not None:
            self.interception_count = m.get('InterceptionCount')

        if m.get('InterceptionRate') is not None:
            self.interception_rate = m.get('InterceptionRate')

        if m.get('LandlineBothAnsweredCount') is not None:
            self.landline_both_answered_count = m.get('LandlineBothAnsweredCount')

        if m.get('LandlineBothAnsweredRate') is not None:
            self.landline_both_answered_rate = m.get('LandlineBothAnsweredRate')

        if m.get('LandlineBothAnsweredTime') is not None:
            self.landline_both_answered_time = m.get('LandlineBothAnsweredTime')

        if m.get('LandlineObTotalCount') is not None:
            self.landline_ob_total_count = m.get('LandlineObTotalCount')

        if m.get('MaxBridgeTime') is not None:
            self.max_bridge_time = m.get('MaxBridgeTime')

        if m.get('MinBridgeTime') is not None:
            self.min_bridge_time = m.get('MinBridgeTime')

        if m.get('TotalBridgeTime') is not None:
            self.total_bridge_time = m.get('TotalBridgeTime')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VadRate') is not None:
            self.vad_rate = m.get('VadRate')

        if m.get('ValidAvgBridgeTime') is not None:
            self.valid_avg_bridge_time = m.get('ValidAvgBridgeTime')

        if m.get('ValidCalls') is not None:
            self.valid_calls = m.get('ValidCalls')

        if m.get('ValidTotalBridgeTime') is not None:
            self.valid_total_bridge_time = m.get('ValidTotalBridgeTime')

        return self

