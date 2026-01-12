# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AIMasterMessage(DaraModel):
    def __init__(
        self,
        extended: str = None,
        job_restart_count: int = None,
        message_content: str = None,
        message_event: str = None,
        message_version: int = None,
        restart_type: str = None,
    ):
        self.extended = extended
        self.job_restart_count = job_restart_count
        self.message_content = message_content
        self.message_event = message_event
        self.message_version = message_version
        self.restart_type = restart_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended is not None:
            result['Extended'] = self.extended

        if self.job_restart_count is not None:
            result['JobRestartCount'] = self.job_restart_count

        if self.message_content is not None:
            result['MessageContent'] = self.message_content

        if self.message_event is not None:
            result['MessageEvent'] = self.message_event

        if self.message_version is not None:
            result['MessageVersion'] = self.message_version

        if self.restart_type is not None:
            result['RestartType'] = self.restart_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extended') is not None:
            self.extended = m.get('Extended')

        if m.get('JobRestartCount') is not None:
            self.job_restart_count = m.get('JobRestartCount')

        if m.get('MessageContent') is not None:
            self.message_content = m.get('MessageContent')

        if m.get('MessageEvent') is not None:
            self.message_event = m.get('MessageEvent')

        if m.get('MessageVersion') is not None:
            self.message_version = m.get('MessageVersion')

        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')

        return self

