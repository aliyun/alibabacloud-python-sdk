# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmPipelineBatchRequest(DaraModel):
    def __init__(
        self,
        confirm: bool = None,
        pipeline_id: str = None,
    ):
        # Specifies whether to start the next batch. Valid values:
        # 
        # - **true**: Start the next batch.
        # 
        # - **false**: Terminate the process.
        # 
        # This parameter is required.
        self.confirm = confirm
        # The pipeline ID. To obtain the ID, call the <props="china">[DescribeChangeOrder](https://help.aliyun.com/zh/sae/serverless-app-engine-upgrade/developer-reference/api-sae-2019-05-06-describechangeorder?spm=a2c4g.11186623.help-menu-search-118957.d_0)<props="intl">[DescribeChangeOrder](https://www.alibabacloud.com/help/zh/sae/serverless-app-engine-classic/developer-reference/api-sae-2019-05-06-describechangeorder-old?spm=a2c63.p38356.help-menu-search-118957.d_0) operation.
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

