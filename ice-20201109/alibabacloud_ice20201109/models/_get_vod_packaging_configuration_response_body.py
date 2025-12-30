# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetVodPackagingConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        packaging_configuration: main_models.VodPackagingConfiguration = None,
        request_id: str = None,
    ):
        # The information about the packaging configuration.
        self.packaging_configuration = packaging_configuration
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.packaging_configuration:
            self.packaging_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.packaging_configuration is not None:
            result['PackagingConfiguration'] = self.packaging_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackagingConfiguration') is not None:
            temp_model = main_models.VodPackagingConfiguration()
            self.packaging_configuration = temp_model.from_map(m.get('PackagingConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

