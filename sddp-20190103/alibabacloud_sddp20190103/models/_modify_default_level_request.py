# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDefaultLevelRequest(DaraModel):
    def __init__(
        self,
        default_id: int = None,
        lang: str = None,
        sensitive_ids: str = None,
    ):
        # The ID of the default threat level for unidentified data. Valid values:
        # 
        # - **1**: N/A.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        self.default_id = default_id
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The IDs of the threat levels for data classified as sensitive. If you specify multiple IDs, separate them with commas. Valid values:
        # 
        # - **1**: N/A.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        self.sensitive_ids = sensitive_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_id is not None:
            result['DefaultId'] = self.default_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sensitive_ids is not None:
            result['SensitiveIds'] = self.sensitive_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultId') is not None:
            self.default_id = m.get('DefaultId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SensitiveIds') is not None:
            self.sensitive_ids = m.get('SensitiveIds')

        return self

