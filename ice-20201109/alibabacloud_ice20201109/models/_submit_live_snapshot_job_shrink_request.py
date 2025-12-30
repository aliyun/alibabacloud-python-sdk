# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitLiveSnapshotJobShrinkRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        job_name: str = None,
        snapshot_output_shrink: str = None,
        stream_input_shrink: str = None,
        template_id: str = None,
    ):
        # The snapshot callback URL.
        # 
        # *   It cannot exceed 255 characters in length.
        # *   Both HTTP and HTTPS URLs are supported.
        self.callback_url = callback_url
        # The name of the job.
        # 
        # *   It cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.job_name = job_name
        # The information about the output snapshot.
        # 
        # This parameter is required.
        self.snapshot_output_shrink = snapshot_output_shrink
        # The information about the input stream.
        # 
        # This parameter is required.
        self.stream_input_shrink = stream_input_shrink
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.snapshot_output_shrink is not None:
            result['SnapshotOutput'] = self.snapshot_output_shrink

        if self.stream_input_shrink is not None:
            result['StreamInput'] = self.stream_input_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('SnapshotOutput') is not None:
            self.snapshot_output_shrink = m.get('SnapshotOutput')

        if m.get('StreamInput') is not None:
            self.stream_input_shrink = m.get('StreamInput')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

