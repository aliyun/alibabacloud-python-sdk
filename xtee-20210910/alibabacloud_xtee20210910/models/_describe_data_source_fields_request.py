# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataSourceFieldsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        data_source_code: str = None,
        reg_id: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Data source code
        # 
        # This parameter is required.
        self.data_source_code = data_source_code
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.data_source_code is not None:
            result['dataSourceCode'] = self.data_source_code

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('dataSourceCode') is not None:
            self.data_source_code = m.get('dataSourceCode')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

