# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskDetailVoteInfo(DaraModel):
    def __init__(
        self,
        min_vote: int = None,
        vote_num: int = None,
    ):
        self.min_vote = min_vote
        self.vote_num = vote_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.min_vote is not None:
            result['MinVote'] = self.min_vote

        if self.vote_num is not None:
            result['VoteNum'] = self.vote_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinVote') is not None:
            self.min_vote = m.get('MinVote')

        if m.get('VoteNum') is not None:
            self.vote_num = m.get('VoteNum')

        return self

