# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateForeignPocSampleRequest(DaraModel):
    def __init__(
        self,
        file: str = None,
        lang: str = None,
        reg_id: str = None,
        remark: str = None,
        sample_name: str = None,
        tab: str = None,
    ):
        # OSS path of the file.
        self.file = file
        # Set the language type for requests and received messages. Default value is **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Area encoding.
        self.reg_id = reg_id
        # Remarks.
        self.remark = remark
        # Sample Name.
        self.sample_name = sample_name
        # Scenario.
        self.tab = tab

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file is not None:
            result['File'] = self.file

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        return self

