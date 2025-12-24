# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEdgeTranscodeJobRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_id: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_input: str = None,
        stream_output: str = None,
        template_id: str = None,
    ):
        # The ID of the data center.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the edge transcoding task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The task name.
        self.name = name
        self.owner_id = owner_id
        self.region_id = region_id
        # The URL of the input stream.
        self.stream_input = stream_input
        # The URL of the output stream.
        self.stream_output = stream_output
        # The template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input

        if self.stream_output is not None:
            result['StreamOutput'] = self.stream_output

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamInput') is not None:
            self.stream_input = m.get('StreamInput')

        if m.get('StreamOutput') is not None:
            self.stream_output = m.get('StreamOutput')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

