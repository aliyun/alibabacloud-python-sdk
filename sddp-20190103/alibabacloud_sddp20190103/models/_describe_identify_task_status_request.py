# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIdentifyTaskStatusRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        # The ID of the task. Obtain this ID from the Id field in the response from calling the CreateScanTask or ScanOssObjectV1 operation.
        # 
        # This parameter is required.
        self.id = id
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Simplified Chinese
        # 
        # - **en_us**: U.S. English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

