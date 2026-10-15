# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        reason: str = None,
        user_config: str = None,
        body: main_models.ModifyInstanceConfigRequestBody = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The reason for the update.
        # 
        # This parameter is required.
        self.reason = reason
        # The custom configuration.
        self.user_config = user_config
        # Submits the instance configurations to be updated as a JSON object.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.user_config is not None:
            result['UserConfig'] = self.user_config

        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')

        if m.get('body') is not None:
            temp_model = main_models.ModifyInstanceConfigRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class ModifyInstanceConfigRequestBody(DaraModel):
    def __init__(
        self,
        user_config: str = None,
    ):
        # The configuration content to write to the instance, formatted as a YAML string.
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_config is not None:
            result['userConfig'] = self.user_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userConfig') is not None:
            self.user_config = m.get('userConfig')

        return self

