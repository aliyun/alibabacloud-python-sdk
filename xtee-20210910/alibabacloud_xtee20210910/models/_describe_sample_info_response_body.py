# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSampleInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeSampleInfoResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeSampleInfoResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeSampleInfoResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        id: int = None,
        sample_tags: str = None,
        sample_type: str = None,
        sample_value: str = None,
        update_time: str = None,
        version: int = None,
    ):
        # Primary key ID
        self.id = id
        # Sample tags.
        self.sample_tags = sample_tags
        # Sample type
        self.sample_type = sample_type
        # Sample value.
        self.sample_value = sample_value
        # Update time.
        self.update_time = update_time
        # Version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.sample_tags is not None:
            result['sampleTags'] = self.sample_tags

        if self.sample_type is not None:
            result['sampleType'] = self.sample_type

        if self.sample_value is not None:
            result['sampleValue'] = self.sample_value

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sampleTags') is not None:
            self.sample_tags = m.get('sampleTags')

        if m.get('sampleType') is not None:
            self.sample_type = m.get('sampleType')

        if m.get('sampleValue') is not None:
            self.sample_value = m.get('sampleValue')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

