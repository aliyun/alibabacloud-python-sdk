# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddShowIntoShowListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        show_id: str = None,
        failed_list: str = None,
        successful_show_ids: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the episode.
        self.show_id = show_id
        # The list of resources that failed to be added and the reason for failure.
        self.failed_list = failed_list
        # The IDs of the episodes that were added.
        self.successful_show_ids = successful_show_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        if self.failed_list is not None:
            result['failedList'] = self.failed_list

        if self.successful_show_ids is not None:
            result['successfulShowIds'] = self.successful_show_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        if m.get('failedList') is not None:
            self.failed_list = m.get('failedList')

        if m.get('successfulShowIds') is not None:
            self.successful_show_ids = m.get('successfulShowIds')

        return self

