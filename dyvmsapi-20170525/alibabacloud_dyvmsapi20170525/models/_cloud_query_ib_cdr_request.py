# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudQueryIbCdrRequest(DaraModel):
    def __init__(
        self,
        callee_number: str = None,
        city: str = None,
        cno: str = None,
        customer_number: str = None,
        end_time: int = None,
        enterprise_id: int = None,
        hotline: str = None,
        join_queue_code: int = None,
        leave_queue_code: int = None,
        limit: int = None,
        province: str = None,
        qno: str = None,
        start: int = None,
        start_time: int = None,
        status: int = None,
        time_range_type: str = None,
        unique_id: str = None,
        user_field_value: str = None,
        user_fieldkey: str = None,
    ):
        # 座席号码
        self.callee_number = callee_number
        # 客户电话归属城市；为空表示全部，如"成都"，此参数需要URLEncode
        self.city = city
        # 座席工号,此字段支持传入多个座席工号，使用英文半角逗号隔开
        self.cno = cno
        # 客户号码
        self.customer_number = customer_number
        # 查询结束时间；时间戳格式,精确到s。startTime与endTime不允许跨月，默认值取当前月份最后一天
        self.end_time = end_time
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 热线号码
        self.hotline = hotline
        # 未进入队列原因 参数说明： 4: 无座席未进入队列 , 3: 队列满未进入队列
        self.join_queue_code = join_queue_code
        # 离开队列原因 参数说明： 2: 队列中放弃 , 3: 队列中超时溢出 , 4: 队列中无座席溢出
        self.leave_queue_code = leave_queue_code
        # 需要取出的数据条数；大于0，最大不能超过1000，默认10
        self.limit = limit
        # 客户电话归属省份；为空表示全部，如"四川"，此参数需要URLEncode
        self.province = province
        # 队列号 参数说明：-1: 未进入队列
        self.qno = qno
        # 从第几条开始取；大于等于0，默认0
        self.start = start
        # 查询开始时间；时间戳格式,精确到s。startTime与endTime不允许跨月，默认值取当前月份第一天
        self.start_time = start_time
        # 呼叫结果；参数说明： 1:座席接听 2:已呼叫座席，座席未接听 3:系统接听 4:系统未接听-IVR配置错误 5:系统未接听-停机 6:系统未接听-欠费 7:系统未接听-黑名单 8:系统未接听-未注册 9:系统未接听-彩铃 11:系统未接听-呼叫超出营帐中设置的最大限制 12:系统未接听-客户呼入系统后在系统未应答前挂机 13:其他错误 14:未进入队列 15:队列中放弃 16:队列中超时溢出 17:队列中无座席溢出 18:无座席未进入队列 19:队列满未进入队列
        self.status = status
        # 查询时间开始结束范围生效类型；通话记录startTime和endTime时间范围生效类型，当startTime和endTime不为空时生效；取值：1.呼叫开始时间 2.呼叫结束时间； 默认为1
        self.time_range_type = time_range_type
        # 如果uniqueId值不为空，则以下其它参数无效，即仅查询电话唯一标识为uniqueId的记录信息
        self.unique_id = unique_id
        # 用户自定义参数指定查询value；传递该参数时必须传递userFieldKey，仅查询一个字段，不支持模糊匹配， 构造的自定义字段查询条件为:{"userFieldkey":"userFieldvalue"}，此参数需要URLEncode
        self.user_field_value = user_field_value
        # 用户自定义参数指定查询key；传递该参数时必须传递userFieldValue，仅查询一个字段，不支持模糊匹配， 构造的自定义字段查询条件为:{"userFieldkey":"userFieldvalue"}，此参数需要URLEncode
        self.user_fieldkey = user_fieldkey

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.city is not None:
            result['City'] = self.city

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_number is not None:
            result['CustomerNumber'] = self.customer_number

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.hotline is not None:
            result['Hotline'] = self.hotline

        if self.join_queue_code is not None:
            result['JoinQueueCode'] = self.join_queue_code

        if self.leave_queue_code is not None:
            result['LeaveQueueCode'] = self.leave_queue_code

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.province is not None:
            result['Province'] = self.province

        if self.qno is not None:
            result['Qno'] = self.qno

        if self.start is not None:
            result['Start'] = self.start

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_range_type is not None:
            result['TimeRangeType'] = self.time_range_type

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.user_field_value is not None:
            result['UserFieldValue'] = self.user_field_value

        if self.user_fieldkey is not None:
            result['UserFieldkey'] = self.user_fieldkey

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerNumber') is not None:
            self.customer_number = m.get('CustomerNumber')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Hotline') is not None:
            self.hotline = m.get('Hotline')

        if m.get('JoinQueueCode') is not None:
            self.join_queue_code = m.get('JoinQueueCode')

        if m.get('LeaveQueueCode') is not None:
            self.leave_queue_code = m.get('LeaveQueueCode')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeRangeType') is not None:
            self.time_range_type = m.get('TimeRangeType')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('UserFieldValue') is not None:
            self.user_field_value = m.get('UserFieldValue')

        if m.get('UserFieldkey') is not None:
            self.user_fieldkey = m.get('UserFieldkey')

        return self

