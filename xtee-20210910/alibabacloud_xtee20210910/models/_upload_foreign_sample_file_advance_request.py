# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class UploadForeignSampleFileAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_object: BinaryIO = None,
        lang: str = None,
        reg_id: str = None,
        tab: str = None,
    ):
        # OSS path of the file.
        self.file_object = file_object
        # Set the language type for requests and received messages. The default value is **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # area encoding.
        self.reg_id = reg_id
        # scenario.
        self.tab = tab

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_object is not None:
            result['File'] = self.file_object

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.tab is not None:
            result['Tab'] = self.tab

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('File') is not None:
            self.file_object = m.get('File')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        return self

