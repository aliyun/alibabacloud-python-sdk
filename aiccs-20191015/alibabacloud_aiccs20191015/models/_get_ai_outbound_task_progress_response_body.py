# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAiOutboundTaskProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAiOutboundTaskProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetAiOutboundTaskProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAiOutboundTaskProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        callout_progress: main_models.GetAiOutboundTaskProgressResponseBodyDataCalloutProgress = None,
        task_id: int = None,
        task_progress: main_models.GetAiOutboundTaskProgressResponseBodyDataTaskProgress = None,
        type: int = None,
    ):
        self.callout_progress = callout_progress
        self.task_id = task_id
        self.task_progress = task_progress
        self.type = type

    def validate(self):
        if self.callout_progress:
            self.callout_progress.validate()
        if self.task_progress:
            self.task_progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callout_progress is not None:
            result['CalloutProgress'] = self.callout_progress.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalloutProgress') is not None:
            temp_model = main_models.GetAiOutboundTaskProgressResponseBodyDataCalloutProgress()
            self.callout_progress = temp_model.from_map(m.get('CalloutProgress'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskProgress') is not None:
            temp_model = main_models.GetAiOutboundTaskProgressResponseBodyDataTaskProgress()
            self.task_progress = temp_model.from_map(m.get('TaskProgress'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAiOutboundTaskProgressResponseBodyDataTaskProgress(DaraModel):
    def __init__(
        self,
        calling_count: int = None,
        connect_count: int = None,
        connect_rate: float = None,
        finish_count: int = None,
        finish_rate: float = None,
        servicer_pickup_count: int = None,
        servicer_pickup_rate: float = None,
        terminate_count: int = None,
        total_count: int = None,
        user_pickup_count: int = None,
        user_pickup_rate: float = None,
        waiting_call_count: int = None,
        waiting_recall_count: int = None,
    ):
        self.calling_count = calling_count
        self.connect_count = connect_count
        self.connect_rate = connect_rate
        self.finish_count = finish_count
        self.finish_rate = finish_rate
        self.servicer_pickup_count = servicer_pickup_count
        self.servicer_pickup_rate = servicer_pickup_rate
        self.terminate_count = terminate_count
        self.total_count = total_count
        self.user_pickup_count = user_pickup_count
        self.user_pickup_rate = user_pickup_rate
        self.waiting_call_count = waiting_call_count
        self.waiting_recall_count = waiting_recall_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_count is not None:
            result['CallingCount'] = self.calling_count

        if self.connect_count is not None:
            result['ConnectCount'] = self.connect_count

        if self.connect_rate is not None:
            result['ConnectRate'] = self.connect_rate

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate

        if self.servicer_pickup_count is not None:
            result['ServicerPickupCount'] = self.servicer_pickup_count

        if self.servicer_pickup_rate is not None:
            result['ServicerPickupRate'] = self.servicer_pickup_rate

        if self.terminate_count is not None:
            result['TerminateCount'] = self.terminate_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_pickup_count is not None:
            result['UserPickupCount'] = self.user_pickup_count

        if self.user_pickup_rate is not None:
            result['UserPickupRate'] = self.user_pickup_rate

        if self.waiting_call_count is not None:
            result['WaitingCallCount'] = self.waiting_call_count

        if self.waiting_recall_count is not None:
            result['WaitingRecallCount'] = self.waiting_recall_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingCount') is not None:
            self.calling_count = m.get('CallingCount')

        if m.get('ConnectCount') is not None:
            self.connect_count = m.get('ConnectCount')

        if m.get('ConnectRate') is not None:
            self.connect_rate = m.get('ConnectRate')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')

        if m.get('ServicerPickupCount') is not None:
            self.servicer_pickup_count = m.get('ServicerPickupCount')

        if m.get('ServicerPickupRate') is not None:
            self.servicer_pickup_rate = m.get('ServicerPickupRate')

        if m.get('TerminateCount') is not None:
            self.terminate_count = m.get('TerminateCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserPickupCount') is not None:
            self.user_pickup_count = m.get('UserPickupCount')

        if m.get('UserPickupRate') is not None:
            self.user_pickup_rate = m.get('UserPickupRate')

        if m.get('WaitingCallCount') is not None:
            self.waiting_call_count = m.get('WaitingCallCount')

        if m.get('WaitingRecallCount') is not None:
            self.waiting_recall_count = m.get('WaitingRecallCount')

        return self

class GetAiOutboundTaskProgressResponseBodyDataCalloutProgress(DaraModel):
    def __init__(
        self,
        call_loss_count: int = None,
        call_loss_rate: float = None,
        call_out_connect_count: int = None,
        call_out_connect_rate: float = None,
        call_out_count: int = None,
        call_out_servicer_pickup_count: int = None,
        call_out_servicer_pickup_rate: float = None,
        call_out_user_pickup_count: int = None,
        call_out_user_pickup_rate: float = None,
    ):
        self.call_loss_count = call_loss_count
        self.call_loss_rate = call_loss_rate
        self.call_out_connect_count = call_out_connect_count
        self.call_out_connect_rate = call_out_connect_rate
        self.call_out_count = call_out_count
        self.call_out_servicer_pickup_count = call_out_servicer_pickup_count
        self.call_out_servicer_pickup_rate = call_out_servicer_pickup_rate
        self.call_out_user_pickup_count = call_out_user_pickup_count
        self.call_out_user_pickup_rate = call_out_user_pickup_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_loss_count is not None:
            result['CallLossCount'] = self.call_loss_count

        if self.call_loss_rate is not None:
            result['CallLossRate'] = self.call_loss_rate

        if self.call_out_connect_count is not None:
            result['CallOutConnectCount'] = self.call_out_connect_count

        if self.call_out_connect_rate is not None:
            result['CallOutConnectRate'] = self.call_out_connect_rate

        if self.call_out_count is not None:
            result['CallOutCount'] = self.call_out_count

        if self.call_out_servicer_pickup_count is not None:
            result['CallOutServicerPickupCount'] = self.call_out_servicer_pickup_count

        if self.call_out_servicer_pickup_rate is not None:
            result['CallOutServicerPickupRate'] = self.call_out_servicer_pickup_rate

        if self.call_out_user_pickup_count is not None:
            result['CallOutUserPickupCount'] = self.call_out_user_pickup_count

        if self.call_out_user_pickup_rate is not None:
            result['CallOutUserPickupRate'] = self.call_out_user_pickup_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallLossCount') is not None:
            self.call_loss_count = m.get('CallLossCount')

        if m.get('CallLossRate') is not None:
            self.call_loss_rate = m.get('CallLossRate')

        if m.get('CallOutConnectCount') is not None:
            self.call_out_connect_count = m.get('CallOutConnectCount')

        if m.get('CallOutConnectRate') is not None:
            self.call_out_connect_rate = m.get('CallOutConnectRate')

        if m.get('CallOutCount') is not None:
            self.call_out_count = m.get('CallOutCount')

        if m.get('CallOutServicerPickupCount') is not None:
            self.call_out_servicer_pickup_count = m.get('CallOutServicerPickupCount')

        if m.get('CallOutServicerPickupRate') is not None:
            self.call_out_servicer_pickup_rate = m.get('CallOutServicerPickupRate')

        if m.get('CallOutUserPickupCount') is not None:
            self.call_out_user_pickup_count = m.get('CallOutUserPickupCount')

        if m.get('CallOutUserPickupRate') is not None:
            self.call_out_user_pickup_rate = m.get('CallOutUserPickupRate')

        return self

