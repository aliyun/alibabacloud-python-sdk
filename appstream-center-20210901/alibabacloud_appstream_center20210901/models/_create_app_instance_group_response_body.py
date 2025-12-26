# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateAppInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_model: main_models.CreateAppInstanceGroupResponseBodyAppInstanceGroupModel = None,
        request_id: str = None,
    ):
        # The delivery group.
        self.app_instance_group_model = app_instance_group_model
        # The request ID.
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
            temp_model = main_models.CreateAppInstanceGroupResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m.get('AppInstanceGroupModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_id: str = None,
        order_id: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the resource group. This parameter is returned if a resource group was created.
        self.node_pool_id = node_pool_id
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        return self

