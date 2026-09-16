# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterAIDBClusterCustomModelResponseBody(DaraModel):
    def __init__(
        self,
        created: bool = None,
        display_model_name: str = None,
        model_id: int = None,
        model_name: str = None,
        model_type: str = None,
        oss_path: str = None,
        request_id: str = None,
    ):
        # Indicates whether the registration is newly created. A value of false indicates that an existing registration was updated.
        self.created = created
        # The display name and initial client-facing invocation name.
        self.display_model_name = display_model_name
        # The model registration ID.
        self.model_id = model_id
        # The custom model registration key.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The normalized OSS path.
        self.oss_path = oss_path
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created

        if self.display_model_name is not None:
            result['DisplayModelName'] = self.display_model_name

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('DisplayModelName') is not None:
            self.display_model_name = m.get('DisplayModelName')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

