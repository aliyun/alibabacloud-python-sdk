# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudQueryWebcallCdrRequest(DaraModel):
    def __init__(
        self,
        callee_clid: str = None,
        callee_display_number: str = None,
        callee_number: str = None,
        city: str = None,
        clid: str = None,
        cno: str = None,
        customer_number: str = None,
        display_number: str = None,
        end_time: int = None,
        enterprise_id: int = None,
        gno: str = None,
        is_real_answer: int = None,
        limit: int = None,
        province: str = None,
        request_unique_id: str = None,
        return_count: int = None,
        start: int = None,
        start_time: int = None,
        status: int = None,
        time_range_type: str = None,
        unique_id: str = None,
        user_field_value: str = None,
        user_fieldkey: str = None,
    ):
        # 第二侧外显号码
        self.callee_clid = callee_clid
        # 第二侧真实外显号码
        self.callee_display_number = callee_display_number
        # 座席号码
        self.callee_number = callee_number
        # 客户电话归属城市；为空表示全部，如"成都"，此参数需要URLEncode
        self.city = city
        # 外显号码
        self.clid = clid
        # 座席工号
        self.cno = cno
        # 客户号码
        self.customer_number = customer_number
        # 真实外显号码，当使用AXB场景进行外呼时，真实外显号码为虚拟号
        self.display_number = display_number
        # 查询结束时间；时间戳格式,精确到s。startTime与endTime不允许跨月，默认值取当前月份最后一天
        self.end_time = end_time
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 座席所属外呼组 单个外呼组号2-20位，支持一个或多个座席工号查询，多个座席工号以英文逗号隔开，一次最多支持10个。不支持模糊匹配。
        self.gno = gno
        # 真人接听；取值说明：1-是、0-否
        self.is_real_answer = is_real_answer
        # 需要取出的数据条数；大于0，最大不能超过1000，默认10
        self.limit = limit
        # 客户电话归属省份；为空表示全部，如"四川"，此参数需要URLEncode
        self.province = province
        # 查询请求唯一id对应的记录信息，默认查询当前月，如requestUniqueId不属于当前月，查询时请传递查询参数 查询开始时间(startTime)
        self.request_unique_id = request_unique_id
        # 是否返回总条数；取值说明：0: 不返回，1：返回，不传默认为1
        self.return_count = return_count
        # 从第几条开始取；大于等于0，默认0
        self.start = start
        # 查询开始时间；时间戳格式,精确到s。startTime与endTime不允许跨月，默认值取当前月份第一天
        self.start_time = start_time
        # 呼叫结果；参数说明： 20 webcall, TTS合成失败； 21 webcall, 客户未接 ； 22:webcall, 客户接听； 23: webcall； 已呼叫； 24: webcall, 双方接听；
        self.status = status
        # 查询时间开始结束范围生效类型；通话记录startTime和endTime时间范围生效类型，当startTime和endTime不为空时生效；取值：1.呼叫开始时间 2.呼叫结束时间； 默认为1
        self.time_range_type = time_range_type
        # 如果uniqueId值不为空，则以下其它参数无效，即仅查询电话唯一标识为uniqueId的记录信息
        self.unique_id = unique_id
        # 用户自定义参数指定查询value；传递该参数时必须传递userFieldKey，仅查询一个字段，不支持模糊匹配，构造的自定义字段查询条件为:{"userFieldkey":"userFieldvalue"}，此参数需要URLEncode
        self.user_field_value = user_field_value
        # 用户自定义参数指定查询key；传递该参数时必须传递userFieldValue，仅查询一个字段，不支持模糊匹配，构造的自定义字段查询条件为:{"userFieldkey":"userFieldvalue"}，此参数需要URLEncode
        self.user_fieldkey = user_fieldkey

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee_clid is not None:
            result['CalleeClid'] = self.callee_clid

        if self.callee_display_number is not None:
            result['CalleeDisplayNumber'] = self.callee_display_number

        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.city is not None:
            result['City'] = self.city

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_number is not None:
            result['CustomerNumber'] = self.customer_number

        if self.display_number is not None:
            result['DisplayNumber'] = self.display_number

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.gno is not None:
            result['Gno'] = self.gno

        if self.is_real_answer is not None:
            result['IsRealAnswer'] = self.is_real_answer

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.province is not None:
            result['Province'] = self.province

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

        if self.return_count is not None:
            result['ReturnCount'] = self.return_count

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
        if m.get('CalleeClid') is not None:
            self.callee_clid = m.get('CalleeClid')

        if m.get('CalleeDisplayNumber') is not None:
            self.callee_display_number = m.get('CalleeDisplayNumber')

        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerNumber') is not None:
            self.customer_number = m.get('CustomerNumber')

        if m.get('DisplayNumber') is not None:
            self.display_number = m.get('DisplayNumber')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Gno') is not None:
            self.gno = m.get('Gno')

        if m.get('IsRealAnswer') is not None:
            self.is_real_answer = m.get('IsRealAnswer')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

        if m.get('ReturnCount') is not None:
            self.return_count = m.get('ReturnCount')

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

