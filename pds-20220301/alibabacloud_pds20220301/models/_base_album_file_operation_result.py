# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseAlbumFileOperationResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file: main_models.CommonFileItem = None,
        is_succeed: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.file = file
        self.is_succeed = is_succeed

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.file is not None:
            result['file'] = self.file.to_map()

        if self.is_succeed is not None:
            result['is_succeed'] = self.is_succeed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('file') is not None:
            temp_model = main_models.CommonFileItem()
            self.file = temp_model.from_map(m.get('file'))

        if m.get('is_succeed') is not None:
            self.is_succeed = m.get('is_succeed')

        return self

