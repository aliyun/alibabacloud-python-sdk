# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateModelTokenRateLimitRequest(DaraModel):
    def __init__(
        self,
        consumers: List[main_models.UpdateModelTokenRateLimitRequestConsumers] = None,
        expected_revision: int = None,
        global_tpm: int = None,
    ):
        # The complete list of consumer limits. Pass an empty array to clear the consumer limits for the model.
        # 
        # This parameter is required.
        self.consumers = consumers
        # The revision returned by the last query. Set this parameter to 0 for the first configuration.
        # 
        # This parameter is required.
        self.expected_revision = expected_revision
        # The global tokens per minute (TPM) limit for the model within the instance. If this parameter is omitted, the global limit is disabled.
        self.global_tpm = global_tpm

    def validate(self):
        if self.consumers:
            for v1 in self.consumers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['consumers'] = []
        if self.consumers is not None:
            for k1 in self.consumers:
                result['consumers'].append(k1.to_map() if k1 else None)

        if self.expected_revision is not None:
            result['expectedRevision'] = self.expected_revision

        if self.global_tpm is not None:
            result['globalTpm'] = self.global_tpm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumers = []
        if m.get('consumers') is not None:
            for k1 in m.get('consumers'):
                temp_model = main_models.UpdateModelTokenRateLimitRequestConsumers()
                self.consumers.append(temp_model.from_map(k1))

        if m.get('expectedRevision') is not None:
            self.expected_revision = m.get('expectedRevision')

        if m.get('globalTpm') is not None:
            self.global_tpm = m.get('globalTpm')

        return self

class UpdateModelTokenRateLimitRequestConsumers(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        tpm: int = None,
    ):
        # The ID of the consumer.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The tokens per minute (TPM) limit for the consumer using this model.
        # 
        # This parameter is required.
        self.tpm = tpm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.tpm is not None:
            result['tpm'] = self.tpm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('tpm') is not None:
            self.tpm = m.get('tpm')

        return self

