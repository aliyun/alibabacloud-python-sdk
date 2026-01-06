# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CommentListReportResponseBody(DaraModel):
    def __init__(
        self,
        comments: List[main_models.CommentListReportResponseBodyComments] = None,
        has_more: bool = None,
        next_cursor: int = None,
        request_id: str = None,
    ):
        self.comments = comments
        self.has_more = has_more
        self.next_cursor = next_cursor
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.comments:
            for v1 in self.comments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['comments'] = []
        if self.comments is not None:
            for k1 in self.comments:
                result['comments'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comments = []
        if m.get('comments') is not None:
            for k1 in m.get('comments'):
                temp_model = main_models.CommentListReportResponseBodyComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CommentListReportResponseBodyComments(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        userid: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.userid = userid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.userid is not None:
            result['Userid'] = self.userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Userid') is not None:
            self.userid = m.get('Userid')

        return self

