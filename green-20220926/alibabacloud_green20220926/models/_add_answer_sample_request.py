# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAnswerSampleRequest(DaraModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
        sample_object: str = None,
        samples: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id
        self.sample_object = sample_object
        self.samples = samples

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sample_object is not None:
            result['SampleObject'] = self.sample_object

        if self.samples is not None:
            result['Samples'] = self.samples

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SampleObject') is not None:
            self.sample_object = m.get('SampleObject')

        if m.get('Samples') is not None:
            self.samples = m.get('Samples')

        return self

