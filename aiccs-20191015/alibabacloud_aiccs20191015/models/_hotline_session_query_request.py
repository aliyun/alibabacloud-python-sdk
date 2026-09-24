# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HotlineSessionQueryRequest(DaraModel):
    def __init__(
        self,
        acid: str = None,
        acid_list: List[str] = None,
        call_result: str = None,
        call_result_list: List[str] = None,
        call_type: int = None,
        call_type_list: List[int] = None,
        called_number: str = None,
        called_number_list: List[str] = None,
        calling_number: str = None,
        calling_number_list: List[str] = None,
        group_id: int = None,
        group_id_list: List[int] = None,
        group_name: str = None,
        id: str = None,
        instance_id: str = None,
        member_id: str = None,
        member_id_list: List[str] = None,
        member_name: str = None,
        page_no: int = None,
        page_size: int = None,
        params: str = None,
        query_end_time: int = None,
        query_start_time: int = None,
        request_id: str = None,
        servicer_id: str = None,
        servicer_id_list: List[str] = None,
        servicer_name: str = None,
    ):
        # The session ID. The acid in the websocket after an inbound call.
        self.acid = acid
        # The list of session IDs.
        self.acid_list = acid_list
        # The call result. Valid values:
        # 
        # - **normal**: normal hangup.
        # - **touchRouteError**: queue hangup.
        # - **touchInQueue**: queue hangup.
        # - **touchInLoss**: queue hangup.
        # - **userHangup**: user hangup or IVR hangup.
        # - **sysHangup**: system hangup or IVR hangup.
        # - **transferAgent**: user hangup or IVR hangup.
        # - **dailing**: agent hangup or ringing hangup.
        # - **TouchRingCallLoss**: queue hangup or ringing hangup.
        self.call_result = call_result
        # The list of call results.
        self.call_result_list = call_result_list
        # The call type. Valid values:
        # - **1**: outbound call.
        # - **2**: inbound call.
        # - **3**: transferred call.
        self.call_type = call_type
        # The list of call types.
        self.call_type_list = call_type_list
        # The number of the caller. For example, a mobile phone number of a user, an agent number, or a robot number.
        self.called_number = called_number
        # The list of called numbers.
        self.called_number_list = called_number_list
        # The number of the callee. For example, a mobile phone number of a user, an agent number, or a robot number.
        self.calling_number = calling_number
        # The list of calling numbers.
        self.calling_number_list = calling_number_list
        # The ID of the skill group.
        self.group_id = group_id
        # The list of skill group IDs.
        self.group_id_list = group_id_list
        # The name of the skill group.
        self.group_name = group_name
        # The globally unique ID of the call details.
        self.id = id
        # The ID of the Artificial Intelligence Cloud Call Service (AICCS) instance.
        # You can obtain the instance ID from <b>Instance Management</b> in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The member ID.
        self.member_id = member_id
        # The list of member IDs.
        self.member_id_list = member_id_list
        # The member name.
        self.member_name = member_name
        # The current page number. The value must be greater than **0**. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than **0**. Default value: **20**.
        self.page_size = page_size
        # The extended parameters.
        self.params = params
        # The end timestamp. Unit: milliseconds.
        self.query_end_time = query_end_time
        # The start timestamp. Unit: milliseconds.
        self.query_start_time = query_start_time
        # The request ID.
        self.request_id = request_id
        # The agent ID.
        self.servicer_id = servicer_id
        # The list of agent IDs.
        self.servicer_id_list = servicer_id_list
        # The agent name.
        self.servicer_name = servicer_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.acid_list is not None:
            result['AcidList'] = self.acid_list

        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.call_result_list is not None:
            result['CallResultList'] = self.call_result_list

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.call_type_list is not None:
            result['CallTypeList'] = self.call_type_list

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_number_list is not None:
            result['CalledNumberList'] = self.called_number_list

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.calling_number_list is not None:
            result['CallingNumberList'] = self.calling_number_list

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_id_list is not None:
            result['MemberIdList'] = self.member_id_list

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.params is not None:
            result['Params'] = self.params

        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_id_list is not None:
            result['ServicerIdList'] = self.servicer_id_list

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('AcidList') is not None:
            self.acid_list = m.get('AcidList')

        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('CallResultList') is not None:
            self.call_result_list = m.get('CallResultList')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CallTypeList') is not None:
            self.call_type_list = m.get('CallTypeList')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalledNumberList') is not None:
            self.called_number_list = m.get('CalledNumberList')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('CallingNumberList') is not None:
            self.calling_number_list = m.get('CallingNumberList')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberIdList') is not None:
            self.member_id_list = m.get('MemberIdList')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerIdList') is not None:
            self.servicer_id_list = m.get('ServicerIdList')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        return self

