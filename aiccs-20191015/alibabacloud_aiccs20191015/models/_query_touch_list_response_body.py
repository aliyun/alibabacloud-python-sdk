# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryTouchListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_data: main_models.QueryTouchListResponseBodyResultData = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_data = result_data
        self.success = success

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultData') is not None:
            temp_model = main_models.QueryTouchListResponseBodyResultData()
            self.result_data = temp_model.from_map(m.get('ResultData'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTouchListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.QueryTouchListResponseBodyResultDataData] = None,
        empty: bool = None,
        next_page: int = None,
        one_page_size: int = None,
        previous_page: int = None,
        total_page: int = None,
        total_results: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.empty = empty
        self.next_page = next_page
        self.one_page_size = one_page_size
        self.previous_page = previous_page
        self.total_page = total_page
        self.total_results = total_results

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.empty is not None:
            result['Empty'] = self.empty

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size

        if self.previous_page is not None:
            result['PreviousPage'] = self.previous_page

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryTouchListResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Empty') is not None:
            self.empty = m.get('Empty')

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')

        if m.get('PreviousPage') is not None:
            self.previous_page = m.get('PreviousPage')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class QueryTouchListResponseBodyResultDataData(DaraModel):
    def __init__(
        self,
        bu_id: int = None,
        channel_id: str = None,
        channel_type: int = None,
        close_time: int = None,
        common_queue_name: str = None,
        dep_id: int = None,
        ext_attrs: main_models.QueryTouchListResponseBodyResultDataDataExtAttrs = None,
        ext_attrs_string: Dict[str, Any] = None,
        feedback: str = None,
        first_time: int = None,
        from_id: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        member_id: int = None,
        member_name: str = None,
        parent_touch_id: int = None,
        queue_id: int = None,
        servicer_id: int = None,
        servicer_name: str = None,
        status: int = None,
        switch_user: str = None,
        to_id: int = None,
        touch_content: str = None,
        touch_end_reason: int = None,
        touch_id: str = None,
        touch_time: str = None,
        touch_type: int = None,
        user_touch_id: int = None,
    ):
        self.bu_id = bu_id
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.close_time = close_time
        self.common_queue_name = common_queue_name
        self.dep_id = dep_id
        self.ext_attrs = ext_attrs
        self.ext_attrs_string = ext_attrs_string
        self.feedback = feedback
        self.first_time = first_time
        self.from_id = from_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.member_id = member_id
        self.member_name = member_name
        self.parent_touch_id = parent_touch_id
        self.queue_id = queue_id
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.status = status
        self.switch_user = switch_user
        self.to_id = to_id
        self.touch_content = touch_content
        self.touch_end_reason = touch_end_reason
        self.touch_id = touch_id
        self.touch_time = touch_time
        self.touch_type = touch_type
        self.user_touch_id = user_touch_id

    def validate(self):
        if self.ext_attrs:
            self.ext_attrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bu_id is not None:
            result['BuId'] = self.bu_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.close_time is not None:
            result['CloseTime'] = self.close_time

        if self.common_queue_name is not None:
            result['CommonQueueName'] = self.common_queue_name

        if self.dep_id is not None:
            result['DepId'] = self.dep_id

        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs.to_map()

        if self.ext_attrs_string is not None:
            result['ExtAttrsString'] = self.ext_attrs_string

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.parent_touch_id is not None:
            result['ParentTouchId'] = self.parent_touch_id

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_user is not None:
            result['SwitchUser'] = self.switch_user

        if self.to_id is not None:
            result['ToId'] = self.to_id

        if self.touch_content is not None:
            result['TouchContent'] = self.touch_content

        if self.touch_end_reason is not None:
            result['TouchEndReason'] = self.touch_end_reason

        if self.touch_id is not None:
            result['TouchId'] = self.touch_id

        if self.touch_time is not None:
            result['TouchTime'] = self.touch_time

        if self.touch_type is not None:
            result['TouchType'] = self.touch_type

        if self.user_touch_id is not None:
            result['UserTouchId'] = self.user_touch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CloseTime') is not None:
            self.close_time = m.get('CloseTime')

        if m.get('CommonQueueName') is not None:
            self.common_queue_name = m.get('CommonQueueName')

        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')

        if m.get('ExtAttrs') is not None:
            temp_model = main_models.QueryTouchListResponseBodyResultDataDataExtAttrs()
            self.ext_attrs = temp_model.from_map(m.get('ExtAttrs'))

        if m.get('ExtAttrsString') is not None:
            self.ext_attrs_string = m.get('ExtAttrsString')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('ParentTouchId') is not None:
            self.parent_touch_id = m.get('ParentTouchId')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchUser') is not None:
            self.switch_user = m.get('SwitchUser')

        if m.get('ToId') is not None:
            self.to_id = m.get('ToId')

        if m.get('TouchContent') is not None:
            self.touch_content = m.get('TouchContent')

        if m.get('TouchEndReason') is not None:
            self.touch_end_reason = m.get('TouchEndReason')

        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')

        if m.get('TouchTime') is not None:
            self.touch_time = m.get('TouchTime')

        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')

        if m.get('UserTouchId') is not None:
            self.user_touch_id = m.get('UserTouchId')

        return self

class QueryTouchListResponseBodyResultDataDataExtAttrs(DaraModel):
    def __init__(
        self,
        ani: str = None,
        dnis: str = None,
        evaluation_level: int = None,
        evaluation_score: int = None,
        evaluation_solution: int = None,
        evaluation_status: int = None,
        online_join_resp_interval: int = None,
        online_session_source: int = None,
        out_call_route_number: str = None,
    ):
        self.ani = ani
        self.dnis = dnis
        self.evaluation_level = evaluation_level
        self.evaluation_score = evaluation_score
        self.evaluation_solution = evaluation_solution
        self.evaluation_status = evaluation_status
        self.online_join_resp_interval = online_join_resp_interval
        self.online_session_source = online_session_source
        self.out_call_route_number = out_call_route_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ani is not None:
            result['Ani'] = self.ani

        if self.dnis is not None:
            result['Dnis'] = self.dnis

        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level

        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score

        if self.evaluation_solution is not None:
            result['EvaluationSolution'] = self.evaluation_solution

        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status

        if self.online_join_resp_interval is not None:
            result['OnlineJoinRespInterval'] = self.online_join_resp_interval

        if self.online_session_source is not None:
            result['OnlineSessionSource'] = self.online_session_source

        if self.out_call_route_number is not None:
            result['OutCallRouteNumber'] = self.out_call_route_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')

        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')

        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')

        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')

        if m.get('EvaluationSolution') is not None:
            self.evaluation_solution = m.get('EvaluationSolution')

        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')

        if m.get('OnlineJoinRespInterval') is not None:
            self.online_join_resp_interval = m.get('OnlineJoinRespInterval')

        if m.get('OnlineSessionSource') is not None:
            self.online_session_source = m.get('OnlineSessionSource')

        if m.get('OutCallRouteNumber') is not None:
            self.out_call_route_number = m.get('OutCallRouteNumber')

        return self

