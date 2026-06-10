# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFaqShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        solution_content: str = None,
        solution_type: int = None,
        start_date: str = None,
        tag_id_list_shrink: str = None,
        title: str = None,
    ):
        # The agent key. If omitted, the default agent is used. Find this key on the Agent Management page.
        self.agent_key = agent_key
        # The ID of the knowledge category.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The knowledge end time. The time is in UTC and in ISO 8601 format.
        self.end_date = end_date
        # The content of the default solution. Required if the fallback feature is enabled.
        self.solution_content = solution_content
        # The type of the default solution. Valid values: `0` (plain text) and `1` (rich text).
        self.solution_type = solution_type
        # The knowledge start time. The time is in UTC and in ISO 8601 format.
        self.start_date = start_date
        # A list of tag IDs to associate with the knowledge.
        self.tag_id_list_shrink = tag_id_list_shrink
        # The knowledge title. Max length: 120 characters.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.solution_content is not None:
            result['SolutionContent'] = self.solution_content

        if self.solution_type is not None:
            result['SolutionType'] = self.solution_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('SolutionContent') is not None:
            self.solution_content = m.get('SolutionContent')

        if m.get('SolutionType') is not None:
            self.solution_type = m.get('SolutionType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

