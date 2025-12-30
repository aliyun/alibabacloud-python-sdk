# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendLiveTranscodeJobCommandRequest(DaraModel):
    def __init__(
        self,
        command: str = None,
        job_id: str = None,
    ):
        # The operation command. Only the stop command is supported. This command is used to stop a transcoding job.
        # 
        # This parameter is required.
        self.command = command
        # The ID of the transcoding job.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

