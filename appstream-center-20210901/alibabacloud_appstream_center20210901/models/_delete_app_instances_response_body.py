# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DeleteAppInstancesResponseBody(DaraModel):
    def __init__(
        self,
        delete_app_instance_models: List[main_models.DeleteAppInstancesResponseBodyDeleteAppInstanceModels] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.delete_app_instance_models = delete_app_instance_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delete_app_instance_models:
            for v1 in self.delete_app_instance_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeleteAppInstanceModels'] = []
        if self.delete_app_instance_models is not None:
            for k1 in self.delete_app_instance_models:
                result['DeleteAppInstanceModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_app_instance_models = []
        if m.get('DeleteAppInstanceModels') is not None:
            for k1 in m.get('DeleteAppInstanceModels'):
                temp_model = main_models.DeleteAppInstancesResponseBodyDeleteAppInstanceModels()
                self.delete_app_instance_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteAppInstancesResponseBodyDeleteAppInstanceModels(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # Specifies whether the application instance is deleted.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

