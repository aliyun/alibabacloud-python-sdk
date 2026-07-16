# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class HotlineSessionQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.HotlineSessionQueryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code. A value of "Success" indicates that the request succeeded.
        self.code = code
        # Call data.
        self.data = data
        # Description of the status code.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the API call succeeded.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.HotlineSessionQueryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class HotlineSessionQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        call_detail_record: List[main_models.HotlineSessionQueryResponseBodyDataCallDetailRecord] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Call detail records.
        self.call_detail_record = call_detail_record
        # Current page number.
        self.page_number = page_number
        # Number of items per page.
        self.page_size = page_size
        # Total number of records.
        self.total_count = total_count

    def validate(self):
        if self.call_detail_record:
            for v1 in self.call_detail_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallDetailRecord'] = []
        if self.call_detail_record is not None:
            for k1 in self.call_detail_record:
                result['CallDetailRecord'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_detail_record = []
        if m.get('CallDetailRecord') is not None:
            for k1 in m.get('CallDetailRecord'):
                temp_model = main_models.HotlineSessionQueryResponseBodyDataCallDetailRecord()
                self.call_detail_record.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class HotlineSessionQueryResponseBodyDataCallDetailRecord(DaraModel):
    def __init__(
        self,
        acid: str = None,
        active_transfer_id: str = None,
        call_continue_time: int = None,
        call_result: str = None,
        call_type: int = None,
        called_number: str = None,
        calling_number: str = None,
        create_time: str = None,
        evaluation_level: int = None,
        evaluation_score: int = None,
        group_id: int = None,
        group_name: str = None,
        hang_up_role: str = None,
        hang_up_time: str = None,
        id: str = None,
        in_queue_time: str = None,
        member_id: str = None,
        member_name: str = None,
        out_queue_time: str = None,
        passive_transfer_id: str = None,
        passive_transfer_id_type: str = None,
        pick_up_time: str = None,
        queue_up_continue_time: int = None,
        ring_continue_time: int = None,
        ring_end_time: str = None,
        ring_start_time: str = None,
        servicer_id: str = None,
        servicer_name: str = None,
        trunk_call: str = None,
    ):
        # Session ID. The acid in WebSocket after an incoming call.
        self.acid = acid
        # Agent ID.  
        # 
        # > This field is null in non–change owner scenarios.
        self.active_transfer_id = active_transfer_id
        # Call duration, in seconds.  
        # 
        # > Unconnected calls do not include call duration.
        self.call_continue_time = call_continue_time
        # Call result. Valid values:
        # 
        # - **normal**: Normal hang-up.
        # - **touchRouteError**: Queue hang-up.
        # - **touchInQueue**: Queue hang-up.
        # - **touchInLoss**: Queue hang-up.
        # - **userHangup**: User hang-up or IVR hang-up.
        # - **sysHangup**: System hang-up or IVR hang-up.
        # - **transferAgent**: User hang-up or IVR hang-up.
        # - **dailing**: Agent hang-up or ring-off hang-up.
        # - **TouchRingCallLoss**: Queue hang-up or ring-off hang-up.
        self.call_result = call_result
        # Call type. Valid values:
        # - **1**: Outbound call
        # - **2**: Inbound call
        # - **3**: Change owner
        self.call_type = call_type
        # Called number.
        self.called_number = called_number
        # Calling party number, such as a user\\"s phone number, agent number, or machine number.
        self.calling_number = calling_number
        # Call creation time.
        # 
        # > - In outbound scenarios, this is the time when the outbound call was initiated.
        # > - In inbound scenarios, this is the time when the call entered the ACC system.
        self.create_time = create_time
        # Satisfaction rating, indicated by star level. Valid values:
        # 
        # - **2**: Two-star satisfaction
        # - **3**: Three-star satisfaction
        # - **4**: Four-star satisfaction
        # - **5**: Five-star satisfaction
        # 
        # > This field has no data in outbound scenarios or scenarios where the call was not answered.
        self.evaluation_level = evaluation_level
        # Satisfaction score. Valid values:
        # - **1**: Very dissatisfied
        # - **2**: Dissatisfied
        # - **3**: Neutral
        # - **4**: Satisfied
        # - **5**: Very satisfied
        # 
        # > This field has no data in outbound scenarios or scenarios where the call was not answered.
        self.evaluation_score = evaluation_score
        # Skill group ID.  
        # 
        # > When CallType is **1**, outbound call scenarios do not include skill group information.
        self.group_id = group_id
        # Skill group name.  
        # > When CallType is **1**, outbound call scenarios do not include skill group information.
        self.group_name = group_name
        # Party that hung up. Valid values:  
        # 
        # - **1**: System hung up  
        # - **2**: Customer hung up  
        # - **3**: Agent hung up  
        # - **null**: Unknown
        self.hang_up_role = hang_up_role
        # Hang-up time.
        self.hang_up_time = hang_up_time
        # The GUID of the call detail record.
        self.id = id
        # Time when the call entered the queue for assignment.  
        # 
        # > Outbound call scenarios do not include queue entry time.
        self.in_queue_time = in_queue_time
        # Membership ID.
        self.member_id = member_id
        # Membership name.
        self.member_name = member_name
        # The time when the hotline call is assigned and dequeued.
        # 
        # > Outbound scenarios do not have a dequeue time.
        self.out_queue_time = out_queue_time
        # Agent ID. The phone number to which the call is transferred.
        # > This field is null in non-transfer scenarios.
        self.passive_transfer_id = passive_transfer_id
        # The recipient of the transferred session. Valid values:
        # - **1**: Agent ID.
        # - **2**: Transferred phone number.
        # 
        # > This field is null in non-transfer scenarios.
        self.passive_transfer_id_type = passive_transfer_id_type
        # The time when the call is answered.
        self.pick_up_time = pick_up_time
        # Queue duration.
        self.queue_up_continue_time = queue_up_continue_time
        # Ringing duration, in seconds.
        # 
        # > Outbound scenarios do not have ringing duration.
        self.ring_continue_time = ring_continue_time
        # The time when ringing ends.
        # 
        # > Outbound scenarios do not have a ring end time.
        self.ring_end_time = ring_end_time
        # Ringing start time.  
        # 
        # > Outbound call scenarios do not include ringing start time.
        self.ring_start_time = ring_start_time
        # Agent ID.  
        # > In inbound scenarios, agent information is unavailable until the call is assigned to an agent.
        self.servicer_id = servicer_id
        # Agent name.
        # > Agent information is unavailable before the call is assigned to an agent in inbound scenarios.
        self.servicer_name = servicer_name
        # Long-distance call.
        self.trunk_call = trunk_call

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.active_transfer_id is not None:
            result['ActiveTransferId'] = self.active_transfer_id

        if self.call_continue_time is not None:
            result['CallContinueTime'] = self.call_continue_time

        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level

        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.hang_up_role is not None:
            result['HangUpRole'] = self.hang_up_role

        if self.hang_up_time is not None:
            result['HangUpTime'] = self.hang_up_time

        if self.id is not None:
            result['Id'] = self.id

        if self.in_queue_time is not None:
            result['InQueueTime'] = self.in_queue_time

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.out_queue_time is not None:
            result['OutQueueTime'] = self.out_queue_time

        if self.passive_transfer_id is not None:
            result['PassiveTransferId'] = self.passive_transfer_id

        if self.passive_transfer_id_type is not None:
            result['PassiveTransferIdType'] = self.passive_transfer_id_type

        if self.pick_up_time is not None:
            result['PickUpTime'] = self.pick_up_time

        if self.queue_up_continue_time is not None:
            result['QueueUpContinueTime'] = self.queue_up_continue_time

        if self.ring_continue_time is not None:
            result['RingContinueTime'] = self.ring_continue_time

        if self.ring_end_time is not None:
            result['RingEndTime'] = self.ring_end_time

        if self.ring_start_time is not None:
            result['RingStartTime'] = self.ring_start_time

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.trunk_call is not None:
            result['TrunkCall'] = self.trunk_call

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('ActiveTransferId') is not None:
            self.active_transfer_id = m.get('ActiveTransferId')

        if m.get('CallContinueTime') is not None:
            self.call_continue_time = m.get('CallContinueTime')

        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')

        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HangUpRole') is not None:
            self.hang_up_role = m.get('HangUpRole')

        if m.get('HangUpTime') is not None:
            self.hang_up_time = m.get('HangUpTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InQueueTime') is not None:
            self.in_queue_time = m.get('InQueueTime')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('OutQueueTime') is not None:
            self.out_queue_time = m.get('OutQueueTime')

        if m.get('PassiveTransferId') is not None:
            self.passive_transfer_id = m.get('PassiveTransferId')

        if m.get('PassiveTransferIdType') is not None:
            self.passive_transfer_id_type = m.get('PassiveTransferIdType')

        if m.get('PickUpTime') is not None:
            self.pick_up_time = m.get('PickUpTime')

        if m.get('QueueUpContinueTime') is not None:
            self.queue_up_continue_time = m.get('QueueUpContinueTime')

        if m.get('RingContinueTime') is not None:
            self.ring_continue_time = m.get('RingContinueTime')

        if m.get('RingEndTime') is not None:
            self.ring_end_time = m.get('RingEndTime')

        if m.get('RingStartTime') is not None:
            self.ring_start_time = m.get('RingStartTime')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('TrunkCall') is not None:
            self.trunk_call = m.get('TrunkCall')

        return self

