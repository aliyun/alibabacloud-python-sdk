# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FeedbackDialogueRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        customer_response: str = None,
        good_text: str = None,
        modified_response: str = None,
        rating: str = None,
        rating_tags: List[str] = None,
        session_id: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.customer_response = customer_response
        self.good_text = good_text
        self.modified_response = modified_response
        self.rating = rating
        self.rating_tags = rating_tags
        # This parameter is required.
        self.session_id = session_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.customer_response is not None:
            result['CustomerResponse'] = self.customer_response

        if self.good_text is not None:
            result['GoodText'] = self.good_text

        if self.modified_response is not None:
            result['ModifiedResponse'] = self.modified_response

        if self.rating is not None:
            result['Rating'] = self.rating

        if self.rating_tags is not None:
            result['RatingTags'] = self.rating_tags

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CustomerResponse') is not None:
            self.customer_response = m.get('CustomerResponse')

        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')

        if m.get('ModifiedResponse') is not None:
            self.modified_response = m.get('ModifiedResponse')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        if m.get('RatingTags') is not None:
            self.rating_tags = m.get('RatingTags')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

