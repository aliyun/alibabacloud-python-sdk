# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudQueryObCdrRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        agent_number: str = None,
        call_type: int = None,
        city: str = None,
        clid: str = None,
        cno: str = None,
        customer_number: str = None,
        down_grade: int = None,
        end_time: int = None,
        enterprise_id: int = None,
        gno: str = None,
        is_real_answer: int = None,
        left_display_number: str = None,
        limit: int = None,
        order: int = None,
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
        # 座席姓名
        self.agent_name = agent_name
        # 座席号码
        self.agent_number = agent_number
        # 呼叫类型；为空表示全部，可选值为：4:预览外呼 6:主叫外呼 9:内部呼叫
        self.call_type = call_type
        # 客户电话归属城市；为空表示全部，如"成都"，此参数需要URLEncode
        self.city = city
        # 客户侧外显号码过滤条件
        self.clid = clid
        # 座席工号，单个座席工号3-10位，支持一个或多个座席工号查询，多个座席工号以英文逗号隔开，一次最多支持100个。不支持模糊匹配。
        self.cno = cno
        # 客户号码，支持一个或多个客户号码查询，多个客户号码以英文逗号隔开，一次最多支持100个。不支持模糊匹配。
        self.customer_number = customer_number
        # 是否呼叫降级；0-否, 1-是
        self.down_grade = down_grade
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
        # 客户侧真实外显号码过滤条件，当使用虚拟号进行AXB外呼且开关打开时，实际过滤的客户侧真实外显号码是虚拟号
        self.left_display_number = left_display_number
        # 需要取出的数据条数；大于0，最大不能超过1000，默认10
        self.limit = limit
        # 排序方式；取值说明：0: 按照记录产生的时序顺序排序，1：按照记录产生的时序逆序排序，2: 按照结束时间的时序顺序排序，3：按照结束时间的时序逆序排序
        self.order = order
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
        # 呼叫结果；参数说明：30 座席未接听; 31 座席接听,未呼叫客户; 32 座席接听,客户未接听; 33 双方接听; 50 主叫外呼接听; 51 主叫外呼,客户未接听; 52 主叫外呼,双方接听。
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
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_number is not None:
            result['AgentNumber'] = self.agent_number

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.city is not None:
            result['City'] = self.city

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_number is not None:
            result['CustomerNumber'] = self.customer_number

        if self.down_grade is not None:
            result['DownGrade'] = self.down_grade

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.gno is not None:
            result['Gno'] = self.gno

        if self.is_real_answer is not None:
            result['IsRealAnswer'] = self.is_real_answer

        if self.left_display_number is not None:
            result['LeftDisplayNumber'] = self.left_display_number

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.order is not None:
            result['Order'] = self.order

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
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentNumber') is not None:
            self.agent_number = m.get('AgentNumber')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerNumber') is not None:
            self.customer_number = m.get('CustomerNumber')

        if m.get('DownGrade') is not None:
            self.down_grade = m.get('DownGrade')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Gno') is not None:
            self.gno = m.get('Gno')

        if m.get('IsRealAnswer') is not None:
            self.is_real_answer = m.get('IsRealAnswer')

        if m.get('LeftDisplayNumber') is not None:
            self.left_display_number = m.get('LeftDisplayNumber')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Order') is not None:
            self.order = m.get('Order')

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

