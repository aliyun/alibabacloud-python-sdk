# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDocParserJobResultRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        job_id: str = None,
        region_id: str = None,
        result_type: str = None,
    ):
        # The agent name.
        self.agent_name = agent_name
        # The document parsing task ID, obtained by calling CreateDocParserJob.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The result type.
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        return self

