# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAttemptsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        attempt_id: str = None,
        callee: str = None,
        caller: str = None,
        campaign_id: str = None,
        case_id: str = None,
        contact_id: str = None,
        criteria: str = None,
        end_time: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        queue_id: str = None,
        start_time: int = None,
    ):
        # Filter by agent ID. This parameter is optional and defaults to empty.
        self.agent_id = agent_id
        # Call record ID, which has the same value as the call ID.
        self.attempt_id = attempt_id
        # Filter by called number. Optional. Default is empty.
        self.callee = callee
        # Filter by caller number. This parameter is optional and defaults to empty.
        self.caller = caller
        # Predictive outbound dialing Activity ID.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # System-generated contact ID. Customers do not need to concern themselves with this value.
        # 
        # This parameter is required.
        self.case_id = case_id
        # Filter by call ID. This parameter is optional and defaults to empty.
        self.contact_id = contact_id
        # Extended query conditions in JSON format. Currently supports caseIds for batch queries.
        self.criteria = criteria
        # End Time. This parameter is optional. If not specified, it defaults to the End Time of the predictive outbound dialing Activity. The format is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Page number. The product of PageNumber and PageSize must not exceed 10 000.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size. The product of PageNumber and PageSize must not exceed 10 000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Filter by skill group ID. This parameter is optional and defaults to empty, which means no filtering is applied.
        self.queue_id = queue_id
        # Start Time. This parameter is optional. If not specified, it defaults to the Start Time of the predictive outbound dialing Activity. The format is a UNIX timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

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

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

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

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

