# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListAttemptsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAttemptsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAttemptsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAttemptsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAttemptsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListAttemptsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAttemptsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_established_time: int = None,
        agent_id: str = None,
        agent_ring_duration: int = None,
        assign_agent_time: int = None,
        attempt_id: str = None,
        callee: str = None,
        caller: str = None,
        campaign_id: str = None,
        case_id: str = None,
        contact_id: str = None,
        customer_established_time: int = None,
        customer_released_time: int = None,
        dial_duration: int = None,
        dial_time: int = None,
        enqueue_time: int = None,
        enter_ivr_time: int = None,
        instance_id: str = None,
        ivr_duration: int = None,
        queue_duration: int = None,
        queue_id: str = None,
    ):
        self.agent_established_time = agent_established_time
        self.agent_id = agent_id
        self.agent_ring_duration = agent_ring_duration
        self.assign_agent_time = assign_agent_time
        self.attempt_id = attempt_id
        self.callee = callee
        self.caller = caller
        self.campaign_id = campaign_id
        self.case_id = case_id
        self.contact_id = contact_id
        self.customer_established_time = customer_established_time
        self.customer_released_time = customer_released_time
        self.dial_duration = dial_duration
        self.dial_time = dial_time
        self.enqueue_time = enqueue_time
        self.enter_ivr_time = enter_ivr_time
        self.instance_id = instance_id
        self.ivr_duration = ivr_duration
        self.queue_duration = queue_duration
        self.queue_id = queue_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_established_time is not None:
            result['AgentEstablishedTime'] = self.agent_established_time

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_ring_duration is not None:
            result['AgentRingDuration'] = self.agent_ring_duration

        if self.assign_agent_time is not None:
            result['AssignAgentTime'] = self.assign_agent_time

        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.customer_established_time is not None:
            result['CustomerEstablishedTime'] = self.customer_established_time

        if self.customer_released_time is not None:
            result['CustomerReleasedTime'] = self.customer_released_time

        if self.dial_duration is not None:
            result['DialDuration'] = self.dial_duration

        if self.dial_time is not None:
            result['DialTime'] = self.dial_time

        if self.enqueue_time is not None:
            result['EnqueueTime'] = self.enqueue_time

        if self.enter_ivr_time is not None:
            result['EnterIvrTime'] = self.enter_ivr_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ivr_duration is not None:
            result['IvrDuration'] = self.ivr_duration

        if self.queue_duration is not None:
            result['QueueDuration'] = self.queue_duration

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentEstablishedTime') is not None:
            self.agent_established_time = m.get('AgentEstablishedTime')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentRingDuration') is not None:
            self.agent_ring_duration = m.get('AgentRingDuration')

        if m.get('AssignAgentTime') is not None:
            self.assign_agent_time = m.get('AssignAgentTime')

        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('CustomerEstablishedTime') is not None:
            self.customer_established_time = m.get('CustomerEstablishedTime')

        if m.get('CustomerReleasedTime') is not None:
            self.customer_released_time = m.get('CustomerReleasedTime')

        if m.get('DialDuration') is not None:
            self.dial_duration = m.get('DialDuration')

        if m.get('DialTime') is not None:
            self.dial_time = m.get('DialTime')

        if m.get('EnqueueTime') is not None:
            self.enqueue_time = m.get('EnqueueTime')

        if m.get('EnterIvrTime') is not None:
            self.enter_ivr_time = m.get('EnterIvrTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IvrDuration') is not None:
            self.ivr_duration = m.get('IvrDuration')

        if m.get('QueueDuration') is not None:
            self.queue_duration = m.get('QueueDuration')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        return self

