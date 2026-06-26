# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class ListConversationsResponseBody(DaraModel):
    def __init__(
        self,
        conversations: List[main_models.ListConversationsResponseBodyConversations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of conversation objects.
        self.conversations = conversations
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of conversations.
        self.total_count = total_count

    def validate(self):
        if self.conversations:
            for v1 in self.conversations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conversations'] = []
        if self.conversations is not None:
            for k1 in self.conversations:
                result['Conversations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversations = []
        if m.get('Conversations') is not None:
            for k1 in m.get('Conversations'):
                temp_model = main_models.ListConversationsResponseBodyConversations()
                self.conversations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListConversationsResponseBodyConversations(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        conversation_id: str = None,
        ds_report: str = None,
        ds_report_titles: List[str] = None,
        end_reason: int = None,
        end_time: int = None,
        has_last_playback_completed: bool = None,
        has_to_agent: bool = None,
        rounds: int = None,
        sand_box: bool = None,
        skill_group: str = None,
        start_time: int = None,
    ):
        # The called number.
        self.called_number = called_number
        # The calling number.
        self.calling_number = calling_number
        # The unique ID of the conversation.
        self.conversation_id = conversation_id
        self.ds_report = ds_report
        self.ds_report_titles = ds_report_titles
        # The reason that the conversation ended. Valid values:<br>1: The conversation completed normally.<br>2: The bot hung up after a recognition failure.<br>3: The call was disconnected due to a silence timeout.<br>4: The user hung up after a recognition failure.<br>5: The user hung up for an unknown reason.<br>6: The call was transferred to an agent because an intent was matched.<br>7: The call was transferred to an agent due to a recognition failure.<br>8: No interaction from the user.<br>9: The call was interrupted by a system error.<br>10: The call was transferred to an IVR system because an intent was matched.<br>11: The call was transferred to an IVR system due to a recognition failure.<br><br><br><br><br><br><br><br><br><br><br>
        self.end_reason = end_reason
        # The end time of the conversation, represented as a Unix timestamp in milliseconds.
        self.end_time = end_time
        # Indicates whether the final audio playback was completed before the call was disconnected.
        self.has_last_playback_completed = has_last_playback_completed
        # Indicates whether the conversation was transferred to an agent.
        self.has_to_agent = has_to_agent
        # The number of rounds in the conversation.
        self.rounds = rounds
        # Indicates whether the conversation was run in a sandbox environment.
        self.sand_box = sand_box
        # The ID of the skill group.
        self.skill_group = skill_group
        # The start time of the conversation, represented as a Unix timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.ds_report is not None:
            result['DsReport'] = self.ds_report

        if self.ds_report_titles is not None:
            result['DsReportTitles'] = self.ds_report_titles

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.has_last_playback_completed is not None:
            result['HasLastPlaybackCompleted'] = self.has_last_playback_completed

        if self.has_to_agent is not None:
            result['HasToAgent'] = self.has_to_agent

        if self.rounds is not None:
            result['Rounds'] = self.rounds

        if self.sand_box is not None:
            result['SandBox'] = self.sand_box

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('DsReport') is not None:
            self.ds_report = m.get('DsReport')

        if m.get('DsReportTitles') is not None:
            self.ds_report_titles = m.get('DsReportTitles')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HasLastPlaybackCompleted') is not None:
            self.has_last_playback_completed = m.get('HasLastPlaybackCompleted')

        if m.get('HasToAgent') is not None:
            self.has_to_agent = m.get('HasToAgent')

        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')

        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

