# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class ListCasesRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        caller: str = None,
        campaign_id: str = None,
        case_completed: bool = None,
        case_ids: List[str] = None,
        disposition_codes: List[str] = None,
        disposition_reasons: List[str] = None,
        draft_version: bool = None,
        end_time: int = None,
        instance_id: str = None,
        label_search: Dict[str, str] = None,
        max_ringing_duration: int = None,
        max_talk_time: int = None,
        max_talk_turns: int = None,
        min_ringing_duration: int = None,
        min_talk_time: int = None,
        min_talk_turns: int = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
        script_id: str = None,
        start_time: int = None,
        states: List[str] = None,
    ):
        # The access channel ID.
        self.access_channel_id = access_channel_id
        # The access channel type.
        self.access_channel_type = access_channel_type
        # The caller number.
        self.caller = caller
        # The outbound campaign ID.
        self.campaign_id = campaign_id
        # Specifies whether the case is completed.
        self.case_completed = case_completed
        # The list of case IDs.
        self.case_ids = case_ids
        # The list of disposition codes.
        self.disposition_codes = disposition_codes
        # The list of disposition reasons.
        self.disposition_reasons = disposition_reasons
        # Specifies whether the version is a draft version.
        self.draft_version = draft_version
        # The end time.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The label search condition.
        self.label_search = label_search
        # The maximum ringing duration.
        self.max_ringing_duration = max_ringing_duration
        # The maximum talk time.
        self.max_talk_time = max_talk_time
        # The maximum number of conversation turns.
        self.max_talk_turns = max_talk_turns
        # The minimum ringing duration.
        self.min_ringing_duration = min_ringing_duration
        # The minimum talk time.
        self.min_talk_time = min_talk_time
        # The minimum number of conversation turns.
        self.min_talk_turns = min_talk_turns
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The called number.
        self.phone_number = phone_number
        # The script ID.
        self.script_id = script_id
        # The start time.
        self.start_time = start_time
        # The list of case states.
        self.states = states

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.case_completed is not None:
            result['CaseCompleted'] = self.case_completed

        if self.case_ids is not None:
            result['CaseIds'] = self.case_ids

        if self.disposition_codes is not None:
            result['DispositionCodes'] = self.disposition_codes

        if self.disposition_reasons is not None:
            result['DispositionReasons'] = self.disposition_reasons

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.label_search is not None:
            result['LabelSearch'] = self.label_search

        if self.max_ringing_duration is not None:
            result['MaxRingingDuration'] = self.max_ringing_duration

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_talk_turns is not None:
            result['MaxTalkTurns'] = self.max_talk_turns

        if self.min_ringing_duration is not None:
            result['MinRingingDuration'] = self.min_ringing_duration

        if self.min_talk_time is not None:
            result['MinTalkTime'] = self.min_talk_time

        if self.min_talk_turns is not None:
            result['MinTalkTurns'] = self.min_talk_turns

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.states is not None:
            result['States'] = self.states

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CaseCompleted') is not None:
            self.case_completed = m.get('CaseCompleted')

        if m.get('CaseIds') is not None:
            self.case_ids = m.get('CaseIds')

        if m.get('DispositionCodes') is not None:
            self.disposition_codes = m.get('DispositionCodes')

        if m.get('DispositionReasons') is not None:
            self.disposition_reasons = m.get('DispositionReasons')

        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LabelSearch') is not None:
            self.label_search = m.get('LabelSearch')

        if m.get('MaxRingingDuration') is not None:
            self.max_ringing_duration = m.get('MaxRingingDuration')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxTalkTurns') is not None:
            self.max_talk_turns = m.get('MaxTalkTurns')

        if m.get('MinRingingDuration') is not None:
            self.min_ringing_duration = m.get('MinRingingDuration')

        if m.get('MinTalkTime') is not None:
            self.min_talk_time = m.get('MinTalkTime')

        if m.get('MinTalkTurns') is not None:
            self.min_talk_turns = m.get('MinTalkTurns')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('States') is not None:
            self.states = m.get('States')

        return self

