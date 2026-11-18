# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAiModelProviderRequest(DaraModel):
    def __init__(
        self,
        default_service_id: str = None,
        display_name: str = None,
        service_ids: List[str] = None,
    ):
        # The optional default AI service ID. If not empty, it must be a service in the updated association set. Omitting this parameter retains the saved default. An explicit empty string clears the default. A non-empty value sets the default. The value can be up to 64 characters in length.
        self.default_service_id = default_service_id
        # The display name of the model provider. This parameter is required and can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The complete set of AI service IDs to associate with the model provider. If you do not specify this parameter, the existing associations are retained. If you pass an empty array, all associations are cleared. Duplicate and empty values are normalized.
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_service_id is not None:
            result['defaultServiceId'] = self.default_service_id

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultServiceId') is not None:
            self.default_service_id = m.get('defaultServiceId')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        return self

