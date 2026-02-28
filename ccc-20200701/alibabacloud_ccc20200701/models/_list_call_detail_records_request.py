# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCallDetailRecordsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        called_number: str = None,
        calling_number: str = None,
        contact_disposition: str = None,
        contact_disposition_list: str = None,
        contact_id: str = None,
        contact_type: str = None,
        contact_type_list: str = None,
        criteria: str = None,
        early_media_state_list: str = None,
        end_time: int = None,
        instance_id: str = None,
        order_by_field: str = None,
        page_number: int = None,
        page_size: int = None,
        satisfaction_description_list: str = None,
        satisfaction_list: str = None,
        satisfaction_survey_channel: str = None,
        skill_group_id: str = None,
        sort_order: str = None,
        start_time: int = None,
    ):
        self.agent_id = agent_id
        self.called_number = called_number
        self.calling_number = calling_number
        self.contact_disposition = contact_disposition
        self.contact_disposition_list = contact_disposition_list
        self.contact_id = contact_id
        self.contact_type = contact_type
        self.contact_type_list = contact_type_list
        self.criteria = criteria
        self.early_media_state_list = early_media_state_list
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.order_by_field = order_by_field
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.satisfaction_description_list = satisfaction_description_list
        self.satisfaction_list = satisfaction_list
        self.satisfaction_survey_channel = satisfaction_survey_channel
        self.skill_group_id = skill_group_id
        self.sort_order = sort_order
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

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.contact_disposition is not None:
            result['ContactDisposition'] = self.contact_disposition

        if self.contact_disposition_list is not None:
            result['ContactDispositionList'] = self.contact_disposition_list

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.contact_type_list is not None:
            result['ContactTypeList'] = self.contact_type_list

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.early_media_state_list is not None:
            result['EarlyMediaStateList'] = self.early_media_state_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_by_field is not None:
            result['OrderByField'] = self.order_by_field

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.satisfaction_description_list is not None:
            result['SatisfactionDescriptionList'] = self.satisfaction_description_list

        if self.satisfaction_list is not None:
            result['SatisfactionList'] = self.satisfaction_list

        if self.satisfaction_survey_channel is not None:
            result['SatisfactionSurveyChannel'] = self.satisfaction_survey_channel

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ContactDisposition') is not None:
            self.contact_disposition = m.get('ContactDisposition')

        if m.get('ContactDispositionList') is not None:
            self.contact_disposition_list = m.get('ContactDispositionList')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('ContactTypeList') is not None:
            self.contact_type_list = m.get('ContactTypeList')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('EarlyMediaStateList') is not None:
            self.early_media_state_list = m.get('EarlyMediaStateList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderByField') is not None:
            self.order_by_field = m.get('OrderByField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SatisfactionDescriptionList') is not None:
            self.satisfaction_description_list = m.get('SatisfactionDescriptionList')

        if m.get('SatisfactionList') is not None:
            self.satisfaction_list = m.get('SatisfactionList')

        if m.get('SatisfactionSurveyChannel') is not None:
            self.satisfaction_survey_channel = m.get('SatisfactionSurveyChannel')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

