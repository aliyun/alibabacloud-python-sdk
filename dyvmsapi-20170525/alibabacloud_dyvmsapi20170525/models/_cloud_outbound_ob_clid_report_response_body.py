# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudOutboundObClidReportResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudOutboundObClidReportResponseBodyData = None,
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
            temp_model = main_models.CloudOutboundObClidReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudOutboundObClidReportResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudOutboundObClidReportResponseBodyDataList] = None,
    ):
        # 返回数据
        self.list = list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.CloudOutboundObClidReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudOutboundObClidReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        answered_count: str = None,
        avg_bridge_time: str = None,
        avg_preview_ob_wait_time: int = None,
        call_type: str = None,
        city: str = None,
        clid: str = None,
        clid_rate: str = None,
        create_time: str = None,
        customer_bill_minute: int = None,
        date_time_range: str = None,
        day: str = None,
        enterprise_id: int = None,
        hour: str = None,
        max_bridge_time: str = None,
        min_bridge_time: str = None,
        preview_ob_customer_ringing_count: int = None,
        preview_ob_customer_ringing_rate: str = None,
        province: str = None,
        row_name: str = None,
        total_bridge_time: str = None,
        total_count: str = None,
        trunk_group_key: str = None,
        valid_avg_bridge_time: str = None,
        valid_calls: str = None,
        valid_total_bridge_time: str = None,
    ):
        # 客户接听数
        self.answered_count = answered_count
        # 平均通话时长
        self.avg_bridge_time = avg_bridge_time
        # 平均等待时长
        self.avg_preview_ob_wait_time = avg_preview_ob_wait_time
        self.call_type = call_type
        # 城市
        self.city = city
        # 外显号码
        self.clid = clid
        # 号码接听率
        self.clid_rate = clid_rate
        # 创建日期
        self.create_time = create_time
        # 客户侧计费分钟数
        self.customer_bill_minute = customer_bill_minute
        # 时间范围
        self.date_time_range = date_time_range
        # 报表日期
        self.day = day
        # 企业Id
        self.enterprise_id = enterprise_id
        # 小时
        self.hour = hour
        # 最长通话时长
        self.max_bridge_time = max_bridge_time
        # 最短通话时长
        self.min_bridge_time = min_bridge_time
        # 响铃数
        self.preview_ob_customer_ringing_count = preview_ob_customer_ringing_count
        # 响铃率
        self.preview_ob_customer_ringing_rate = preview_ob_customer_ringing_rate
        # 省份
        self.province = province
        # 格式化日期
        self.row_name = row_name
        # 总通话时长
        self.total_bridge_time = total_bridge_time
        # 外呼总数
        self.total_count = total_count
        # 中继群组代号
        self.trunk_group_key = trunk_group_key
        # 有效通话平均时长
        self.valid_avg_bridge_time = valid_avg_bridge_time
        # 有效通话次数
        self.valid_calls = valid_calls
        # 有效通话总时长
        self.valid_total_bridge_time = valid_total_bridge_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answered_count is not None:
            result['AnsweredCount'] = self.answered_count

        if self.avg_bridge_time is not None:
            result['AvgBridgeTime'] = self.avg_bridge_time

        if self.avg_preview_ob_wait_time is not None:
            result['AvgPreviewObWaitTime'] = self.avg_preview_ob_wait_time

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.city is not None:
            result['City'] = self.city

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.clid_rate is not None:
            result['ClidRate'] = self.clid_rate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_bill_minute is not None:
            result['CustomerBillMinute'] = self.customer_bill_minute

        if self.date_time_range is not None:
            result['DateTimeRange'] = self.date_time_range

        if self.day is not None:
            result['Day'] = self.day

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.max_bridge_time is not None:
            result['MaxBridgeTime'] = self.max_bridge_time

        if self.min_bridge_time is not None:
            result['MinBridgeTime'] = self.min_bridge_time

        if self.preview_ob_customer_ringing_count is not None:
            result['PreviewObCustomerRingingCount'] = self.preview_ob_customer_ringing_count

        if self.preview_ob_customer_ringing_rate is not None:
            result['PreviewObCustomerRingingRate'] = self.preview_ob_customer_ringing_rate

        if self.province is not None:
            result['Province'] = self.province

        if self.row_name is not None:
            result['RowName'] = self.row_name

        if self.total_bridge_time is not None:
            result['TotalBridgeTime'] = self.total_bridge_time

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.trunk_group_key is not None:
            result['TrunkGroupKey'] = self.trunk_group_key

        if self.valid_avg_bridge_time is not None:
            result['ValidAvgBridgeTime'] = self.valid_avg_bridge_time

        if self.valid_calls is not None:
            result['ValidCalls'] = self.valid_calls

        if self.valid_total_bridge_time is not None:
            result['ValidTotalBridgeTime'] = self.valid_total_bridge_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnsweredCount') is not None:
            self.answered_count = m.get('AnsweredCount')

        if m.get('AvgBridgeTime') is not None:
            self.avg_bridge_time = m.get('AvgBridgeTime')

        if m.get('AvgPreviewObWaitTime') is not None:
            self.avg_preview_ob_wait_time = m.get('AvgPreviewObWaitTime')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('ClidRate') is not None:
            self.clid_rate = m.get('ClidRate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerBillMinute') is not None:
            self.customer_bill_minute = m.get('CustomerBillMinute')

        if m.get('DateTimeRange') is not None:
            self.date_time_range = m.get('DateTimeRange')

        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('MaxBridgeTime') is not None:
            self.max_bridge_time = m.get('MaxBridgeTime')

        if m.get('MinBridgeTime') is not None:
            self.min_bridge_time = m.get('MinBridgeTime')

        if m.get('PreviewObCustomerRingingCount') is not None:
            self.preview_ob_customer_ringing_count = m.get('PreviewObCustomerRingingCount')

        if m.get('PreviewObCustomerRingingRate') is not None:
            self.preview_ob_customer_ringing_rate = m.get('PreviewObCustomerRingingRate')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RowName') is not None:
            self.row_name = m.get('RowName')

        if m.get('TotalBridgeTime') is not None:
            self.total_bridge_time = m.get('TotalBridgeTime')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TrunkGroupKey') is not None:
            self.trunk_group_key = m.get('TrunkGroupKey')

        if m.get('ValidAvgBridgeTime') is not None:
            self.valid_avg_bridge_time = m.get('ValidAvgBridgeTime')

        if m.get('ValidCalls') is not None:
            self.valid_calls = m.get('ValidCalls')

        if m.get('ValidTotalBridgeTime') is not None:
            self.valid_total_bridge_time = m.get('ValidTotalBridgeTime')

        return self

