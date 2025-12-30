# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateVodPackagingAssetResponseBody(DaraModel):
    def __init__(
        self,
        asset: main_models.VodPackagingAsset = None,
        request_id: str = None,
    ):
        # The information about the asset.
        self.asset = asset
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.asset:
            self.asset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = main_models.VodPackagingAsset()
            self.asset = temp_model.from_map(m.get('Asset'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

