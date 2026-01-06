# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatisticsReportResponseBody(DaraModel):
    def __init__(
        self,
        comment_num: int = None,
        comment_user_num: int = None,
        like_num: int = None,
        read_num: int = None,
        request_id: str = None,
    ):
        self.comment_num = comment_num
        self.comment_user_num = comment_user_num
        self.like_num = like_num
        self.read_num = read_num
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment_num is not None:
            result['commentNum'] = self.comment_num

        if self.comment_user_num is not None:
            result['commentUserNum'] = self.comment_user_num

        if self.like_num is not None:
            result['likeNum'] = self.like_num

        if self.read_num is not None:
            result['readNum'] = self.read_num

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commentNum') is not None:
            self.comment_num = m.get('commentNum')

        if m.get('commentUserNum') is not None:
            self.comment_user_num = m.get('commentUserNum')

        if m.get('likeNum') is not None:
            self.like_num = m.get('likeNum')

        if m.get('readNum') is not None:
            self.read_num = m.get('readNum')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

