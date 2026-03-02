# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LibraryReview(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        artificat_id: str = None,
        developer_name: str = None,
        feedback_library_instruction: str = None,
        feedback_library_schema: str = None,
        gmt_create: str = None,
        group_id: str = None,
        id: int = None,
        library_name: str = None,
        library_url: str = None,
        market_id: str = None,
        market_name: str = None,
        remain_time: str = None,
        request_id: str = None,
        reviewer_id: str = None,
        status: str = None,
    ):
        self.applicant = applicant
        self.artificat_id = artificat_id
        self.developer_name = developer_name
        self.feedback_library_instruction = feedback_library_instruction
        self.feedback_library_schema = feedback_library_schema
        self.gmt_create = gmt_create
        self.group_id = group_id
        self.id = id
        self.library_name = library_name
        self.library_url = library_url
        self.market_id = market_id
        self.market_name = market_name
        self.remain_time = remain_time
        self.request_id = request_id
        self.reviewer_id = reviewer_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.artificat_id is not None:
            result['artificatId'] = self.artificat_id

        if self.developer_name is not None:
            result['developerName'] = self.developer_name

        if self.feedback_library_instruction is not None:
            result['feedbackLibraryInstruction'] = self.feedback_library_instruction

        if self.feedback_library_schema is not None:
            result['feedbackLibrarySchema'] = self.feedback_library_schema

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        if self.library_url is not None:
            result['libraryUrl'] = self.library_url

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.market_name is not None:
            result['marketName'] = self.market_name

        if self.remain_time is not None:
            result['remainTime'] = self.remain_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('artificatId') is not None:
            self.artificat_id = m.get('artificatId')

        if m.get('developerName') is not None:
            self.developer_name = m.get('developerName')

        if m.get('feedbackLibraryInstruction') is not None:
            self.feedback_library_instruction = m.get('feedbackLibraryInstruction')

        if m.get('feedbackLibrarySchema') is not None:
            self.feedback_library_schema = m.get('feedbackLibrarySchema')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        if m.get('libraryUrl') is not None:
            self.library_url = m.get('libraryUrl')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('marketName') is not None:
            self.market_name = m.get('marketName')

        if m.get('remainTime') is not None:
            self.remain_time = m.get('remainTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

