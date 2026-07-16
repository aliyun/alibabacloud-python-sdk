# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class UploadTranslationFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        file_object: BinaryIO = None,
        file_name: str = None,
    ):
        self.apikey = apikey
        # This parameter is required.
        self.file_object = file_object
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.file_object is not None:
            result['File'] = self.file_object

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('File') is not None:
            self.file_object = m.get('File')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

