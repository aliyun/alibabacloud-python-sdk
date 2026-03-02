# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSavepointRequest(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        description: str = None,
        native_format: bool = None,
    ):
        # The deployment ID.
        # 
        # This parameter is required.
        self.deployment_id = deployment_id
        # The description of the savepoint.
        self.description = description
        # Specifies whether to use the native format mode. Valid values:
        # 
        # *   true: The native format mode is used.
        # *   false: The native format mode is not used.
        self.native_format = native_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.description is not None:
            result['description'] = self.description

        if self.native_format is not None:
            result['nativeFormat'] = self.native_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')

        return self

