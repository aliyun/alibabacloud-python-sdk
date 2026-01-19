# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSampleDataByCsvRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        oss_file_name: str = None,
        reg_id: str = None,
        sample_batch_uuid: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Uploaded OSS address.
        self.oss_file_name = oss_file_name
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

        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_batch_uuid is not None:
            result['sampleBatchUuid'] = self.sample_batch_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleBatchUuid') is not None:
            self.sample_batch_uuid = m.get('sampleBatchUuid')

        return self

