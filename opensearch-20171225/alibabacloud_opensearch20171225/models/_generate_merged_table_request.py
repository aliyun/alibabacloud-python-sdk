# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GenerateMergedTableRequest(DaraModel):
    def __init__(
        self,
        body: main_models.Schema = None,
        spec: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The specifications of the OpenSearch instance. This parameter is used to check whether the OpenSearch instance meets the special limits on an exclusive instance.
        # 
        # Default value: opensearch.share.common.
        # 
        # For more information, see the description of the spec field in the Quota topic.
        self.spec = spec

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.Schema()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

