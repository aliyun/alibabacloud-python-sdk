# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAnnotationMissionShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_key: str = None,
        annotation_mission_data_source_type: int = None,
        annotation_mission_debug_data_source_list_shrink: str = None,
        annotation_mission_debug_data_source_list_json_string: str = None,
        annotation_mission_name: str = None,
        chatbot_id: str = None,
        conversation_time_end_filter: int = None,
        conversation_time_start_filter: int = None,
        exclude_other_session: bool = None,
        finished: bool = None,
        instance_id: str = None,
        sampling_count: int = None,
        sampling_rate: int = None,
        sampling_type: int = None,
        script_id: str = None,
        session_end_reason_filter_list: List[int] = None,
        session_end_reason_filter_list_json_string: str = None,
    ):
        self.agent_id = agent_id
        self.agent_key = agent_key
        self.annotation_mission_data_source_type = annotation_mission_data_source_type
        self.annotation_mission_debug_data_source_list_shrink = annotation_mission_debug_data_source_list_shrink
        self.annotation_mission_debug_data_source_list_json_string = annotation_mission_debug_data_source_list_json_string
        self.annotation_mission_name = annotation_mission_name
        self.chatbot_id = chatbot_id
        self.conversation_time_end_filter = conversation_time_end_filter
        self.conversation_time_start_filter = conversation_time_start_filter
        self.exclude_other_session = exclude_other_session
        self.finished = finished
        self.instance_id = instance_id
        self.sampling_count = sampling_count
        self.sampling_rate = sampling_rate
        self.sampling_type = sampling_type
        self.script_id = script_id
        self.session_end_reason_filter_list = session_end_reason_filter_list
        self.session_end_reason_filter_list_json_string = session_end_reason_filter_list_json_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.annotation_mission_data_source_type is not None:
            result['AnnotationMissionDataSourceType'] = self.annotation_mission_data_source_type

        if self.annotation_mission_debug_data_source_list_shrink is not None:
            result['AnnotationMissionDebugDataSourceList'] = self.annotation_mission_debug_data_source_list_shrink

        if self.annotation_mission_debug_data_source_list_json_string is not None:
            result['AnnotationMissionDebugDataSourceListJsonString'] = self.annotation_mission_debug_data_source_list_json_string

        if self.annotation_mission_name is not None:
            result['AnnotationMissionName'] = self.annotation_mission_name

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.conversation_time_end_filter is not None:
            result['ConversationTimeEndFilter'] = self.conversation_time_end_filter

        if self.conversation_time_start_filter is not None:
            result['ConversationTimeStartFilter'] = self.conversation_time_start_filter

        if self.exclude_other_session is not None:
            result['ExcludeOtherSession'] = self.exclude_other_session

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sampling_count is not None:
            result['SamplingCount'] = self.sampling_count

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.sampling_type is not None:
            result['SamplingType'] = self.sampling_type

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.session_end_reason_filter_list is not None:
            result['SessionEndReasonFilterList'] = self.session_end_reason_filter_list

        if self.session_end_reason_filter_list_json_string is not None:
            result['SessionEndReasonFilterListJsonString'] = self.session_end_reason_filter_list_json_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AnnotationMissionDataSourceType') is not None:
            self.annotation_mission_data_source_type = m.get('AnnotationMissionDataSourceType')

        if m.get('AnnotationMissionDebugDataSourceList') is not None:
            self.annotation_mission_debug_data_source_list_shrink = m.get('AnnotationMissionDebugDataSourceList')

        if m.get('AnnotationMissionDebugDataSourceListJsonString') is not None:
            self.annotation_mission_debug_data_source_list_json_string = m.get('AnnotationMissionDebugDataSourceListJsonString')

        if m.get('AnnotationMissionName') is not None:
            self.annotation_mission_name = m.get('AnnotationMissionName')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('ConversationTimeEndFilter') is not None:
            self.conversation_time_end_filter = m.get('ConversationTimeEndFilter')

        if m.get('ConversationTimeStartFilter') is not None:
            self.conversation_time_start_filter = m.get('ConversationTimeStartFilter')

        if m.get('ExcludeOtherSession') is not None:
            self.exclude_other_session = m.get('ExcludeOtherSession')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SamplingCount') is not None:
            self.sampling_count = m.get('SamplingCount')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('SamplingType') is not None:
            self.sampling_type = m.get('SamplingType')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SessionEndReasonFilterList') is not None:
            self.session_end_reason_filter_list = m.get('SessionEndReasonFilterList')

        if m.get('SessionEndReasonFilterListJsonString') is not None:
            self.session_end_reason_filter_list_json_string = m.get('SessionEndReasonFilterListJsonString')

        return self

