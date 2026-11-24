# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetModelTokenRateLimitResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetModelTokenRateLimitResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The result code of the request. The value is Ok if the request is successful.
        self.code = code
        # The saved quotas, versions, and rule IDs for the current model.
        self.data = data
        # The cause of the error. This parameter is omitted if the request is successful.
        self.message = message
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetModelTokenRateLimitResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetModelTokenRateLimitResponseBodyData(DaraModel):
    def __init__(
        self,
        applied_revision: int = None,
        consumer_rule_ids: Dict[str, str] = None,
        consumers: List[main_models.GetModelTokenRateLimitResponseBodyDataConsumers] = None,
        gateway_id: str = None,
        global_rule_id: str = None,
        global_tpm: int = None,
        model_id: str = None,
        revision: int = None,
    ):
        # The most recent configuration revision successfully delivered to the control plane.
        self.applied_revision = applied_revision
        # The mapping from consumer IDs to model throttling rule IDs.
        self.consumer_rule_ids = consumer_rule_ids
        # The list of configured consumer quotas for this model.
        self.consumers = consumers
        # The instance ID of the dedicated AI gateway.
        self.gateway_id = gateway_id
        # The rule ID for the global model quota, which can be matched with the rule hits in the gateway throttling logs. This parameter is returned only when the global quota is configured.
        self.global_rule_id = global_rule_id
        # The maximum number of tokens per minute (TPM) shared by all consumers for this model within the instance.
        self.global_tpm = global_tpm
        # The actual model card ID (prefixed with msc-) or the logical model ID (prefixed with vm-).
        self.model_id = model_id
        # The saved revision of the model throttling configuration. Pass this value as expectedRevision in subsequent modification requests.
        self.revision = revision

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
        if self.applied_revision is not None:
            result['appliedRevision'] = self.applied_revision

        if self.consumer_rule_ids is not None:
            result['consumerRuleIds'] = self.consumer_rule_ids

        result['consumers'] = []
        if self.consumers is not None:
            for k1 in self.consumers:
                result['consumers'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.global_rule_id is not None:
            result['globalRuleId'] = self.global_rule_id

        if self.global_tpm is not None:
            result['globalTpm'] = self.global_tpm

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.revision is not None:
            result['revision'] = self.revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appliedRevision') is not None:
            self.applied_revision = m.get('appliedRevision')

        if m.get('consumerRuleIds') is not None:
            self.consumer_rule_ids = m.get('consumerRuleIds')

        self.consumers = []
        if m.get('consumers') is not None:
            for k1 in m.get('consumers'):
                temp_model = main_models.GetModelTokenRateLimitResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k1))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('globalRuleId') is not None:
            self.global_rule_id = m.get('globalRuleId')

        if m.get('globalTpm') is not None:
            self.global_tpm = m.get('globalTpm')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        return self

class GetModelTokenRateLimitResponseBodyDataConsumers(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        tpm: int = None,
    ):
        # The ID of the consumer.
        self.consumer_id = consumer_id
        # The maximum number of tokens per minute (TPM) for this consumer using this model.
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

