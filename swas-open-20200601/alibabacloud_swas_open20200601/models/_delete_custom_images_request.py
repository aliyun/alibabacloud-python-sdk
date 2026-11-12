# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomImagesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_ids: str = None,
        region_id: str = None,
    ):
        # Ensures the idempotence of the request. Generate the value from your client and ensure that it is unique across different requests. **ClientToken** supports only ASCII characters and can be up to 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance IDs of the simple application servers. The value can be a JSON array that consists of multiple instance IDs. You can specify up to 15 IDs. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.image_ids = image_ids
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

