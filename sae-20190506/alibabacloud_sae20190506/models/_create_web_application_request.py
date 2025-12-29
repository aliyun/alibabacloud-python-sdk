# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateWebApplicationRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        body: main_models.CreateWebApplicationInput = None,
    ):
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The information about the application.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('body') is not None:
            temp_model = main_models.CreateWebApplicationInput()
            self.body = temp_model.from_map(m.get('body'))

        return self

