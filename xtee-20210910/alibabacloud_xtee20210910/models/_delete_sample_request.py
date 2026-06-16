# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSampleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        sample_id: int = None,
    ):
        # Language of the error message returned by the API. Valid values: zh: Chinese; en: English. Default value: en.
        self.lang = lang
        # area encoding.
        self.reg_id = reg_id
        # ID of the sample to delete.
        self.sample_id = sample_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        return self

