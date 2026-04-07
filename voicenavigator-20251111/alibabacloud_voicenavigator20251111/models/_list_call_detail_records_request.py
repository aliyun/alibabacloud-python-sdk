# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCallDetailRecordsRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        callee: str = None,
        caller: str = None,
        disposition_codes: List[str] = None,
        disposition_reasons: List[str] = None,
        draft_version: bool = None,
        end_time: str = None,
        instance_id: str = None,
        issue_resolved: bool = None,
        max_talk_turns: int = None,
        min_talk_turns: int = None,
        page_number: int = None,
        page_size: int = None,
        script_id: str = None,
        session_ids: List[str] = None,
        start_time: str = None,
    ):
        self.access_channel_id = access_channel_id
        self.access_channel_type = access_channel_type
        self.callee = callee
        self.caller = caller
        self.disposition_codes = disposition_codes
        self.disposition_reasons = disposition_reasons
        self.draft_version = draft_version
        self.end_time = end_time
        self.instance_id = instance_id
        self.issue_resolved = issue_resolved
        self.max_talk_turns = max_talk_turns
        self.min_talk_turns = min_talk_turns
        self.page_number = page_number
        self.page_size = page_size
        self.script_id = script_id
        self.session_ids = session_ids
        self.start_time = start_time

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

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

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

        if self.issue_resolved is not None:
            result['IssueResolved'] = self.issue_resolved

        if self.max_talk_turns is not None:
            result['MaxTalkTurns'] = self.max_talk_turns

        if self.min_talk_turns is not None:
            result['MinTalkTurns'] = self.min_talk_turns

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.session_ids is not None:
            result['SessionIds'] = self.session_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

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

        if m.get('IssueResolved') is not None:
            self.issue_resolved = m.get('IssueResolved')

        if m.get('MaxTalkTurns') is not None:
            self.max_talk_turns = m.get('MaxTalkTurns')

        if m.get('MinTalkTurns') is not None:
            self.min_talk_turns = m.get('MinTalkTurns')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SessionIds') is not None:
            self.session_ids = m.get('SessionIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

