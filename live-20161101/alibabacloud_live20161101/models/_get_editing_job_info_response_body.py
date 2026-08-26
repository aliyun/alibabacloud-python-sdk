# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEditingJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        editing_tasks_info: str = None,
        request_id: str = None,
    ):
        # The production studio ID.
        self.caster_id = caster_id
        # The video clip task information. This includes:
        # 
        # - **OutputVodId**: The ID of the output video-on-demand file.
        # 
        # - **TaskStatus**: The status of the video clip task. (-1: failed. 0: task initialized. 1: clipping in progress. 2: uploading. 3: task succeeded.)
        # 
        # - **StorageLocation**: The video-on-demand storage address.
        # 
        # - **FileName**: The name of the clipped file.
        # 
        # - **ShowId**: The show ID.
        self.editing_tasks_info = editing_tasks_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.editing_tasks_info is not None:
            result['EditingTasksInfo'] = self.editing_tasks_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EditingTasksInfo') is not None:
            self.editing_tasks_info = m.get('EditingTasksInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

