# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePocSampleRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        lang: str = None,
        reg_id: str = None,
        remark: str = None,
        sample_name: str = None,
        tab: str = None,
        type: str = None,
    ):
        self.file_name = file_name
        self.file_url = file_url
        self.lang = lang
        self.reg_id = reg_id
        self.remark = remark
        self.sample_name = sample_name
        self.tab = tab
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

