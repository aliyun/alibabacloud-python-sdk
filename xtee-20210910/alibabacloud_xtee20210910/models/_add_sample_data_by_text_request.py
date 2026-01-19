# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSampleDataByTextRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        data_value: str = None,
        reg_id: str = None,
        sample_batch_uuid: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # List data.
        self.data_value = data_value
        # Region code
        self.reg_id = reg_id
        # Sample UUID.
        self.sample_batch_uuid = sample_batch_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.data_value is not None:
            result['dataValue'] = self.data_value

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_batch_uuid is not None:
            result['sampleBatchUuid'] = self.sample_batch_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('dataValue') is not None:
            self.data_value = m.get('dataValue')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleBatchUuid') is not None:
            self.sample_batch_uuid = m.get('sampleBatchUuid')

        return self

