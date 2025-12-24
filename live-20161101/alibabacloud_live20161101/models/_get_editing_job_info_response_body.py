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
        # The ID of the production studio.
        self.caster_id = caster_id
        # The information about editing tasks. The following fields are returned for each editing task:
        # 
        # *   **OutputVodId**: the ID of the output video-on-demand (VOD) file.
        # *   **TaskStatus**: the status of the editing task. Valid values: -1, 0, 1, 2, and 3. A value of -1 indicates that the editing task fails. A value of 0 indicates that the editing task is being initialized. A value of 1 indicates that editing is in progress. A value of 2 indicates that the output VOD file is being uploaded. A value of 3 indicates that the editing task is successful.
        # *   **StorageLocation**: the storage location in ApsaraVideo VOD.
        # *   **FileName**: the name of the file that is edited.
        # *   **ShowId**: the ID of the episode.
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

