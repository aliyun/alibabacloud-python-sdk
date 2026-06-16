# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSampleDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        sample_id: int = None,
    ):
        # The language type for the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The region code.
        self.reg_id = reg_id
        # The ID of the sample.
        # 
        # This parameter is required.
        self.sample_id = sample_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_id is not None:
            result['sampleId'] = self.sample_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleId') is not None:
            self.sample_id = m.get('sampleId')

        return self

