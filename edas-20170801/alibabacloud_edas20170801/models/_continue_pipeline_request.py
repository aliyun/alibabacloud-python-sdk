# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContinuePipelineRequest(DaraModel):
    def __init__(
        self,
        confirm: bool = None,
        pipeline_id: str = None,
    ):
        # Specifies whether to release the next batch. Valid values:
        # 
        # - true: releases the next batch.
        # 
        # - false: does not release the next batch.
        self.confirm = confirm
        # The ID of the change process. You can call the GetChangeOrderInfo operation to query the ID of the change process that corresponds to a specific batch. For more information, see [GetChangeOrderInfo](https://help.aliyun.com/document_detail/62072.html).
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm is not None:
            result['Confirm'] = self.confirm

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confirm') is not None:
            self.confirm = m.get('Confirm')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

