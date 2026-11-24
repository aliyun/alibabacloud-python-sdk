# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsumerAccessOverviewRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        include_model_tpm: bool = None,
    ):
        # The target AI gateway instance ID. Quotas and resources are isolated by instance.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Specifies whether to also query the model TPM limits. Default value: false. If set to true, modelTpmLimits is returned for dedicated instances.
        self.include_model_tpm = include_model_tpm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.include_model_tpm is not None:
            result['includeModelTpm'] = self.include_model_tpm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('includeModelTpm') is not None:
            self.include_model_tpm = m.get('includeModelTpm')

        return self

