# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetAutoDisposeConfigResponseBody(DaraModel):
    def __init__(
        self,
        auto_dispose_config: main_models.GetAutoDisposeConfigResponseBodyAutoDisposeConfig = None,
        request_id: str = None,
    ):
        self.auto_dispose_config = auto_dispose_config
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.auto_dispose_config:
            self.auto_dispose_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_dispose_config is not None:
            result['AutoDisposeConfig'] = self.auto_dispose_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDisposeConfig') is not None:
            temp_model = main_models.GetAutoDisposeConfigResponseBodyAutoDisposeConfig()
            self.auto_dispose_config = temp_model.from_map(m.get('AutoDisposeConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAutoDisposeConfigResponseBodyAutoDisposeConfig(DaraModel):
    def __init__(
        self,
        auto_decision_status: str = None,
        product_code: str = None,
    ):
        self.auto_decision_status = auto_decision_status
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_decision_status is not None:
            result['AutoDecisionStatus'] = self.auto_decision_status

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDecisionStatus') is not None:
            self.auto_decision_status = m.get('AutoDecisionStatus')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

