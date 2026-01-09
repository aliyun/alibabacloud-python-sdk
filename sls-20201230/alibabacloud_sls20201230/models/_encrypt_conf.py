# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class EncryptConf(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        encrypt_type: str = None,
        user_cmk_info: main_models.EncryptUserCmkConf = None,
    ):
        # This parameter is required.
        self.enable = enable
        self.encrypt_type = encrypt_type
        self.user_cmk_info = user_cmk_info

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.encrypt_type is not None:
            result['encrypt_type'] = self.encrypt_type

        if self.user_cmk_info is not None:
            result['user_cmk_info'] = self.user_cmk_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('encrypt_type') is not None:
            self.encrypt_type = m.get('encrypt_type')

        if m.get('user_cmk_info') is not None:
            temp_model = main_models.EncryptUserCmkConf()
            self.user_cmk_info = temp_model.from_map(m.get('user_cmk_info'))

        return self

