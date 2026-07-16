# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFrontVulPatchListRequest(DaraModel):
    def __init__(
        self,
        info: str = None,
        lang: str = None,
        operate_type: str = None,
        type: str = None,
    ):
        # The information about the Windows system vulnerability to query. The value is a JSON string that contains the following fields:
        # - **name**: the vulnerability name.
        # - **uuid**: the UUID of the server that has the vulnerability.
        # - **tag**: the vulnerability tag. Set this field to **system**, which indicates a system vulnerability.
        # 
        # This parameter is required.
        self.info = info
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The method to handle the vulnerability. Set this parameter to **vul_fix**, which indicates fixing the vulnerability.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The type of vulnerability to query. Set this parameter to **sys**, which indicates a Windows vulnerability.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

