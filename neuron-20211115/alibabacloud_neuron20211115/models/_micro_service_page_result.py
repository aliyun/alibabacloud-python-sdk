# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MicroServicePageResult(DaraModel):
    def __init__(
        self,
        micro_service_digests: List[main_models.MicroServiceDigest] = None,
        int_total: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.micro_service_digests = micro_service_digests
        self.int_total = int_total
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.micro_service_digests:
            for v1 in self.micro_service_digests:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MicroServiceDigests'] = []
        if self.micro_service_digests is not None:
            for k1 in self.micro_service_digests:
                result['MicroServiceDigests'].append(k1.to_map() if k1 else None)

        if self.int_total is not None:
            result['intTotal'] = self.int_total

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.micro_service_digests = []
        if m.get('MicroServiceDigests') is not None:
            for k1 in m.get('MicroServiceDigests'):
                temp_model = main_models.MicroServiceDigest()
                self.micro_service_digests.append(temp_model.from_map(k1))

        if m.get('intTotal') is not None:
            self.int_total = m.get('intTotal')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

