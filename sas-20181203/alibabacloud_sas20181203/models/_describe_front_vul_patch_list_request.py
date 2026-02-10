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
        # The information about the Windows system vulnerability. The value is a JSON string that contains the following fields:
        # 
        # *   **name**: the name of the vulnerability.
        # *   **uuid**: the UUID of the server on which the vulnerability is detected.
        # *   **tag**: the tag that is added to the vulnerability. Set this field to **system**, which indicates Windows system vulnerabilities.
        # 
        # This parameter is required.
        self.info = info
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The operation that you want to perform on the vulnerability. Set the value to **vul_fix**, which indicates vulnerability fixing.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The type of the vulnerability. Set the value to **sys**, which indicates Windows system vulnerabilities.
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

