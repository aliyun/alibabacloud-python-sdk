# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetContextLogsResponseBody(DaraModel):
    def __init__(
        self,
        back_lines: int = None,
        forward_lines: int = None,
        logs: List[Dict[str, Any]] = None,
        progress: str = None,
        total_lines: int = None,
    ):
        # The number of logs that are generated before the generation time of the start log.
        self.back_lines = back_lines
        # The number of logs that are generated after the generation time of the start log.
        self.forward_lines = forward_lines
        # The logs that are returned.
        self.logs = logs
        # Indicates whether the query and analysis results are complete. Valid values:
        # 
        # *   Complete: The query is successful, and the complete query and analysis results are returned.
        # *   Incomplete: The query is successful, but the query and analysis results are incomplete. To obtain the complete results, you must repeat the request.
        self.progress = progress
        # The total number of logs that are returned. The logs include the start log that is specified in the request.
        self.total_lines = total_lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines

        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines

        if self.logs is not None:
            result['logs'] = self.logs

        if self.progress is not None:
            result['progress'] = self.progress

        if self.total_lines is not None:
            result['total_lines'] = self.total_lines

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')

        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')

        if m.get('logs') is not None:
            self.logs = m.get('logs')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('total_lines') is not None:
            self.total_lines = m.get('total_lines')

        return self

