# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOssObjectDetailRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        # The ID of the OSS object.
        # 
        # >  You can call the [DescribeOssObjects](https://help.aliyun.com/document_detail/410152.html) operation to obtain the ID of the OSS object.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
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

