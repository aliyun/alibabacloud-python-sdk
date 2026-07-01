# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaConvertJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config: str = None,
        pipeline_id: str = None,
        user_data: str = None,
    ):
        # A unique client token that ensures request idempotency.
        self.client_token = client_token
        # The transcoding job configuration. For more information, see [MediaConvertJobConfig](https://help.aliyun.com/document_detail/2999539.html).
        # 
        # This parameter is required.
        self.config = config
        # The ID of the pipeline for the transcoding job.
        self.pipeline_id = pipeline_id
        # Custom data to pass with the job.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config is not None:
            result['Config'] = self.config

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

