# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterModelEnhancementResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        model_enhancement_key_number: int = None,
        model_enhancement_keys: List[main_models.DescribeDBClusterModelEnhancementResponseBodyModelEnhancementKeys] = None,
        model_enhancement_status: str = None,
        request_id: str = None,
    ):
        # The time when the model enhancement feature was enabled, in the ISO 8601 UTC format (YYYY-MM-DDThh:mm:ssZ).
        self.create_time = create_time
        # The number of API keys for model enhancement.
        self.model_enhancement_key_number = model_enhancement_key_number
        # The list of API keys for model enhancement.
        self.model_enhancement_keys = model_enhancement_keys
        # The status of the model enhancement feature. A value of ON indicates that the feature is enabled.
        self.model_enhancement_status = model_enhancement_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.model_enhancement_keys:
            for v1 in self.model_enhancement_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.model_enhancement_key_number is not None:
            result['ModelEnhancementKeyNumber'] = self.model_enhancement_key_number

        result['ModelEnhancementKeys'] = []
        if self.model_enhancement_keys is not None:
            for k1 in self.model_enhancement_keys:
                result['ModelEnhancementKeys'].append(k1.to_map() if k1 else None)

        if self.model_enhancement_status is not None:
            result['ModelEnhancementStatus'] = self.model_enhancement_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModelEnhancementKeyNumber') is not None:
            self.model_enhancement_key_number = m.get('ModelEnhancementKeyNumber')

        self.model_enhancement_keys = []
        if m.get('ModelEnhancementKeys') is not None:
            for k1 in m.get('ModelEnhancementKeys'):
                temp_model = main_models.DescribeDBClusterModelEnhancementResponseBodyModelEnhancementKeys()
                self.model_enhancement_keys.append(temp_model.from_map(k1))

        if m.get('ModelEnhancementStatus') is not None:
            self.model_enhancement_status = m.get('ModelEnhancementStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterModelEnhancementResponseBodyModelEnhancementKeys(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_key_id: str = None,
        create_time: str = None,
        description: str = None,
        expire_time: str = None,
    ):
        # The value of the API key.
        self.api_key = api_key
        # The ID of the API key.
        self.api_key_id = api_key_id
        # The time when the API key was created, in the ISO 8601 UTC format (YYYY-MM-DDThh:mm:ssZ).
        self.create_time = create_time
        # The description of the API key.
        self.description = description
        # The expiration time of the API key, in the ISO 8601 UTC format (YYYY-MM-DDThh:mm:ssZ).
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        return self

