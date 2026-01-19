# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSampleApiRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        data_value: str = None,
        lang: str = None,
        reg_id: str = None,
        sample_batch_type: str = None,
        service_list: str = None,
    ):
        # Same as input parameter
        self.data_type = data_type
        # Specific data value
        self.data_value = data_value
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # regionId
        self.reg_id = reg_id
        # Sample batch type
        self.sample_batch_type = sample_batch_type
        # Service list.
        self.service_list = service_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.data_value is not None:
            result['DataValue'] = self.data_value

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.sample_batch_type is not None:
            result['SampleBatchType'] = self.sample_batch_type

        if self.service_list is not None:
            result['ServiceList'] = self.service_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SampleBatchType') is not None:
            self.sample_batch_type = m.get('SampleBatchType')

        if m.get('ServiceList') is not None:
            self.service_list = m.get('ServiceList')

        return self

