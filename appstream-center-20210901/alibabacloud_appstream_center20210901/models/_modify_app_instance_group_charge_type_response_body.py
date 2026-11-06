# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyAppInstanceGroupChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_model: main_models.ModifyAppInstanceGroupChargeTypeResponseBodyAppInstanceGroupModel = None,
        request_id: str = None,
    ):
        # The task information for the billing method conversion.
        self.app_instance_group_model = app_instance_group_model
        # The unique ID of the request. You can use the ID to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.app_instance_group_model:
            self.app_instance_group_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_model is not None:
            result['AppInstanceGroupModel'] = self.app_instance_group_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModel') is not None:
            temp_model = main_models.ModifyAppInstanceGroupChargeTypeResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m.get('AppInstanceGroupModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyAppInstanceGroupChargeTypeResponseBodyAppInstanceGroupModel(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the billing conversion order task, used to associate with the current conversion. It is returned only when a related order task is required and created. It does not indicate that the payment is completed or the new billing method has taken effect.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

