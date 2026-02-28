# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCallDetailRecordsV2Request(DaraModel):
    def __init__(
        self,
        access_channel_type_list: str = None,
        agent_id: str = None,
        analytics_report_ready: bool = None,
        broker: str = None,
        called_number: str = None,
        calling_number: str = None,
        contact_disposition_list: str = None,
        contact_id_list: str = None,
        contact_type_list: str = None,
        early_media_state_list: str = None,
        end_time: int = None,
        first_agent_id: str = None,
        instance_id: str = None,
        media_type: str = None,
        number: str = None,
        order_by_field: str = None,
        page_number: int = None,
        page_size: int = None,
        release_initiator_list: str = None,
        release_reason_list: str = None,
        satisfaction_description_list: str = None,
        satisfaction_rate_list: str = None,
        satisfaction_survey_channel: str = None,
        search_pattern: str = None,
        skill_group_id_list: str = None,
        sort_order: str = None,
        start_time: int = None,
    ):
        self.access_channel_type_list = access_channel_type_list
        self.agent_id = agent_id
        self.analytics_report_ready = analytics_report_ready
        self.broker = broker
        self.called_number = called_number
        self.calling_number = calling_number
        self.contact_disposition_list = contact_disposition_list
        self.contact_id_list = contact_id_list
        self.contact_type_list = contact_type_list
        self.early_media_state_list = early_media_state_list
        self.end_time = end_time
        self.first_agent_id = first_agent_id
        # This parameter is required.
        self.instance_id = instance_id
        self.media_type = media_type
        self.number = number
        self.order_by_field = order_by_field
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.release_initiator_list = release_initiator_list
        self.release_reason_list = release_reason_list
        self.satisfaction_description_list = satisfaction_description_list
        self.satisfaction_rate_list = satisfaction_rate_list
        self.satisfaction_survey_channel = satisfaction_survey_channel
        self.search_pattern = search_pattern
        self.skill_group_id_list = skill_group_id_list
        self.sort_order = sort_order
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_type_list is not None:
            result['AccessChannelTypeList'] = self.access_channel_type_list

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.analytics_report_ready is not None:
            result['AnalyticsReportReady'] = self.analytics_report_ready

        if self.broker is not None:
            result['Broker'] = self.broker

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.contact_disposition_list is not None:
            result['ContactDispositionList'] = self.contact_disposition_list

        if self.contact_id_list is not None:
            result['ContactIdList'] = self.contact_id_list

        if self.contact_type_list is not None:
            result['ContactTypeList'] = self.contact_type_list

        if self.early_media_state_list is not None:
            result['EarlyMediaStateList'] = self.early_media_state_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.first_agent_id is not None:
            result['FirstAgentId'] = self.first_agent_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.number is not None:
            result['Number'] = self.number

        if self.order_by_field is not None:
            result['OrderByField'] = self.order_by_field

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.release_initiator_list is not None:
            result['ReleaseInitiatorList'] = self.release_initiator_list

        if self.release_reason_list is not None:
            result['ReleaseReasonList'] = self.release_reason_list

        if self.satisfaction_description_list is not None:
            result['SatisfactionDescriptionList'] = self.satisfaction_description_list

        if self.satisfaction_rate_list is not None:
            result['SatisfactionRateList'] = self.satisfaction_rate_list

        if self.satisfaction_survey_channel is not None:
            result['SatisfactionSurveyChannel'] = self.satisfaction_survey_channel

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelTypeList') is not None:
            self.access_channel_type_list = m.get('AccessChannelTypeList')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AnalyticsReportReady') is not None:
            self.analytics_report_ready = m.get('AnalyticsReportReady')

        if m.get('Broker') is not None:
            self.broker = m.get('Broker')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ContactDispositionList') is not None:
            self.contact_disposition_list = m.get('ContactDispositionList')

        if m.get('ContactIdList') is not None:
            self.contact_id_list = m.get('ContactIdList')

        if m.get('ContactTypeList') is not None:
            self.contact_type_list = m.get('ContactTypeList')

        if m.get('EarlyMediaStateList') is not None:
            self.early_media_state_list = m.get('EarlyMediaStateList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirstAgentId') is not None:
            self.first_agent_id = m.get('FirstAgentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('OrderByField') is not None:
            self.order_by_field = m.get('OrderByField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReleaseInitiatorList') is not None:
            self.release_initiator_list = m.get('ReleaseInitiatorList')

        if m.get('ReleaseReasonList') is not None:
            self.release_reason_list = m.get('ReleaseReasonList')

        if m.get('SatisfactionDescriptionList') is not None:
            self.satisfaction_description_list = m.get('SatisfactionDescriptionList')

        if m.get('SatisfactionRateList') is not None:
            self.satisfaction_rate_list = m.get('SatisfactionRateList')

        if m.get('SatisfactionSurveyChannel') is not None:
            self.satisfaction_survey_channel = m.get('SatisfactionSurveyChannel')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

