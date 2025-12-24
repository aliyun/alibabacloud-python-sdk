# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoShowListTasksResponseBody(DaraModel):
    def __init__(
        self,
        auto_show_list_tasks: str = None,
        request_id: str = None,
    ):
        # The information about the scheduled tasks. The following fields are included:
        # 
        # *   Status: the status of the scheduled task. Valid values: 0 and 1. A value of 0 indicates that the scheduled task is paused. A value of 1 indicates that the scheduled task is started.
        # *   LiveTemplate: the transcoding templates.
        # *   TranscodeConfig: the transcoding configuration for the source URL.
        # *   CasterId: the ID of the production studio.
        self.auto_show_list_tasks = auto_show_list_tasks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_show_list_tasks is not None:
            result['AutoShowListTasks'] = self.auto_show_list_tasks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoShowListTasks') is not None:
            self.auto_show_list_tasks = m.get('AutoShowListTasks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

