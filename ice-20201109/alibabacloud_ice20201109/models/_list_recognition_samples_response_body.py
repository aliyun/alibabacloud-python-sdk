# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListRecognitionSamplesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        samples: main_models.ListRecognitionSamplesResponseBodySamples = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The samples.
        self.samples = samples
        # The total number of samples.
        self.total_count = total_count

    def validate(self):
        if self.samples:
            self.samples.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samples is not None:
            result['Samples'] = self.samples.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Samples') is not None:
            temp_model = main_models.ListRecognitionSamplesResponseBodySamples()
            self.samples = temp_model.from_map(m.get('Samples'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecognitionSamplesResponseBodySamples(DaraModel):
    def __init__(
        self,
        sample: List[main_models.ListRecognitionSamplesResponseBodySamplesSample] = None,
    ):
        self.sample = sample

    def validate(self):
        if self.sample:
            for v1 in self.sample:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sample'] = []
        if self.sample is not None:
            for k1 in self.sample:
                result['Sample'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sample = []
        if m.get('Sample') is not None:
            for k1 in m.get('Sample'):
                temp_model = main_models.ListRecognitionSamplesResponseBodySamplesSample()
                self.sample.append(temp_model.from_map(k1))

        return self

class ListRecognitionSamplesResponseBodySamplesSample(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        image_url: str = None,
        lib_id: str = None,
        sample_id: str = None,
    ):
        self.entity_id = entity_id
        # The URL of the image sample.
        self.image_url = image_url
        self.lib_id = lib_id
        # The sample ID.
        self.sample_id = sample_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        return self

