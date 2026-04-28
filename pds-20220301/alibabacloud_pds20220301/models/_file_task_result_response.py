# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FileTaskResultResponse(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        message: str = None,
        rst_file: main_models.FileIDInfo = None,
        src_file: main_models.FileIDInfo = None,
    ):
        self.err_code = err_code
        self.message = message
        self.rst_file = rst_file
        self.src_file = src_file

    def validate(self):
        if self.rst_file:
            self.rst_file.validate()
        if self.src_file:
            self.src_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['err_code'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.rst_file is not None:
            result['rst_file'] = self.rst_file.to_map()

        if self.src_file is not None:
            result['src_file'] = self.src_file.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('rst_file') is not None:
            temp_model = main_models.FileIDInfo()
            self.rst_file = temp_model.from_map(m.get('rst_file'))

        if m.get('src_file') is not None:
            temp_model = main_models.FileIDInfo()
            self.src_file = temp_model.from_map(m.get('src_file'))

        return self

