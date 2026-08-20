# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebFetchRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        output_format: str = None,
        region_id: str = None,
        url: str = None,
    ):
        self.agent_name = agent_name
        # The output format. Valid values:
        # 
        # - **markdown**: Markdown format.
        # 
        # - **html**: HTML format.
        # 
        # - **text**: Plain text format.
        self.output_format = output_format
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The URL of the target web page to crawl.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

