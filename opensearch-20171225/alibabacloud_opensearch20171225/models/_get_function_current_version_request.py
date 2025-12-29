# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFunctionCurrentVersionRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        function_type: str = None,
        model_type: str = None,
    ):
        # The category. By default, this parameter is left empty.
        self.category = category
        # The industry. By default, this parameter is left empty, which indicates General-purpose Edition.
        self.domain = domain
        # The type of the feature. Valid values:
        # 
        # *   PAAS. This is the default value.
        # *   SAAS.
        self.function_type = function_type
        # The type of the model. The following features correspond to different model types:
        # 
        # *   CTR model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Shading model: offline_inference
        # *   Drop-down suggestion model: offline_inference
        # *   Word segmentation model: text
        # *   Word weight model: tf_checkpoint
        # 
        # This parameter is required.
        self.model_type = model_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.domain is not None:
            result['domain'] = self.domain

        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.model_type is not None:
            result['modelType'] = self.model_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        return self

