# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class UpdateDeploymentByNameRequest(DaraModel):
    def __init__(
        self,
        body: main_models.Deployment = None,
        deployment_name: str = None,
    ):
        # The collection of fields to update. Partial updates are supported.
        # 
        # This parameter is required.
        self.body = body
        # The deployment job name.
        # 
        # This parameter is required.
        self.deployment_name = deployment_name

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

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.Deployment()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        return self

