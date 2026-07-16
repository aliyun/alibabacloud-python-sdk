# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAITaskRequest(DaraModel):
    def __init__(
        self,
        output_option: str = None,
        task_id: str = None,
    ):
        # Specifies whether to return the TaskOutput parameter. The TaskOutput parameter specifies the outputs of the AI task. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # >  The value of TaskOutput may be excessively long. If you do not require the outputs of the task, we recommend that you set OutputOption to Disabled to improve the response speed of the API operation.
        self.output_option = output_option
        # The ID of the AI task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_option is not None:
            result['OutputOption'] = self.output_option

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

