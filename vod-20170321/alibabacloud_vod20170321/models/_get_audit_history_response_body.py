# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAuditHistoryResponseBody(DaraModel):
    def __init__(
        self,
        histories: List[main_models.GetAuditHistoryResponseBodyHistories] = None,
        request_id: str = None,
        status: str = None,
        total: int = None,
    ):
        # The review records.
        self.histories = histories
        # The ID of the request.
        self.request_id = request_id
        # The manual review result. Valid values:
        # - **Normal**: The video can be played.
        # - **Blocked**: The video is blocked.
        self.status = status
        # The total number of review records.
        self.total = total

    def validate(self):
        if self.histories:
            for v1 in self.histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Histories'] = []
        if self.histories is not None:
            for k1 in self.histories:
                result['Histories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.histories = []
        if m.get('Histories') is not None:
            for k1 in m.get('Histories'):
                temp_model = main_models.GetAuditHistoryResponseBodyHistories()
                self.histories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetAuditHistoryResponseBodyHistories(DaraModel):
    def __init__(
        self,
        auditor: str = None,
        comment: str = None,
        creation_time: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The reviewer.
        self.auditor = auditor
        # The review comments, which are provided by the reviewer.
        self.comment = comment
        # The time when the review record was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The reason why the video failed the review. If the video failed the review, specify the reason.
        self.reason = reason
        # The manual review result. Valid values:
        # - **Normal**: The video can be played.
        # - **Blocked**: The video is blocked.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auditor is not None:
            result['Auditor'] = self.auditor

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auditor') is not None:
            self.auditor = m.get('Auditor')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

