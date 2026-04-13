# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCandidateInstanceTypeResponseBody(DaraModel):
    def __init__(
        self,
        candidate_instance_types: List[str] = None,
        candidate_zone_ids: List[str] = None,
        request_id: str = None,
    ):
        self.candidate_instance_types = candidate_instance_types
        self.candidate_zone_ids = candidate_zone_ids
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_instance_types is not None:
            result['CandidateInstanceTypes'] = self.candidate_instance_types

        if self.candidate_zone_ids is not None:
            result['CandidateZoneIds'] = self.candidate_zone_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateInstanceTypes') is not None:
            self.candidate_instance_types = m.get('CandidateInstanceTypes')

        if m.get('CandidateZoneIds') is not None:
            self.candidate_zone_ids = m.get('CandidateZoneIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

