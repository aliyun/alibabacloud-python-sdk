# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubmitImageRequest(DaraModel):
    def __init__(
        self,
        destination_region_list: List[str] = None,
        task_id: str = None,
    ):
        # The list of destination regions to which the image is copied.
        self.destination_region_list = destination_region_list
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_list is not None:
            result['DestinationRegionList'] = self.destination_region_list

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionList') is not None:
            self.destination_region_list = m.get('DestinationRegionList')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

