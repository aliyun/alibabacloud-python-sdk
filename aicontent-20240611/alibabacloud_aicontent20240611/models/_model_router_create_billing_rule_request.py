# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ModelRouterCreateBillingRuleRequest(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        effective_time: str = None,
        expire_time: str = None,
        model_id: int = None,
        pricing_config: Any = None,
        version: int = None,
    ):
        # The billing type. The value must be `configurable`.
        self.billing_type = billing_type
        # The effective time, in RFC3339 format.
        self.effective_time = effective_time
        # The expiration time, in RFC3339 format.
        self.expire_time = expire_time
        # The model ID.
        # 
        # This parameter is required.
        self.model_id = model_id
        # The `pricingConfig` is a JSON object whose internal field structure varies depending on the billing type.
        # 
        # 1. **Tiered token billing**<br>Applicable to chat models. This type uses tiered pricing based on the number of input tokens and supports different rates for standard mode, thinking mode, and cache hits.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:Constraints:
        # 
        # 2. **Per-image billing**<br>Applicable to `ImageGeneration` and `ImageEdit` models. Billing is based on the number of images generated or processed.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:
        # 
        # 3. **Video matrix billing**<br>Applicable to `VideoGeneration` and `VideoImageGeneration` models. Pricing is based on a combination of video resolution and the presence of an audio track.<br>Note: While the frontend UI may use a `matrix` field, API calls must use the `tiers` field to save the configuration. The `matrix` field is automatically converted to `tiers` on the server side. The format below is the standard API format.<br>JSON format:<br><br><br><br>
        # 
        #    Field descriptions:Constraints:
        # 
        # 4. **Billing by duration**<br>Applicable to automatic speech recognition (ASR) models. Billing is based on the audio duration.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:
        # 
        # 5. **Per-character billing**<br>Applicable to text-to-speech (TTS) models. Billing is based on the number of characters in the synthesized text.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:
        # 
        # 6. **Flat-rate token billing**<br>Applicable to models such as `Embedding`, `Rerank`, `MultimodalEmbedding`, and `MultimodalRerank`. This type uses a flat-rate pricing model without tiers.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:
        # 
        # 7. **Full-modal multi-dimensional billing**<br>Applicable to full-modal models such as `ChatFullmodal` (e.g., `qwen3.5-omni-plus`). It sets separate prices for the input and output of different modalities, such as text, audio, images, and video.<br>JSON format:<br><br><br>
        # 
        #    Field descriptions:
        self.pricing_config = pricing_config
        # The billing rule version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['billingType'] = self.billing_type

        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.pricing_config is not None:
            result['pricingConfig'] = self.pricing_config

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')

        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('pricingConfig') is not None:
            self.pricing_config = m.get('pricingConfig')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

