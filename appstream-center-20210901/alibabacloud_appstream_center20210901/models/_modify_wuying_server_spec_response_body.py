# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyWuyingServerSpecResponseBody(DaraModel):
    def __init__(
        self,
        modify_wuying_server_spec_model: main_models.ModifyWuyingServerSpecResponseBodyModifyWuyingServerSpecModel = None,
        request_id: str = None,
    ):
        # The processing result of the specification change.
        self.modify_wuying_server_spec_model = modify_wuying_server_spec_model
        # The ID of the request. It is used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.modify_wuying_server_spec_model:
            self.modify_wuying_server_spec_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_wuying_server_spec_model is not None:
            result['ModifyWuyingServerSpecModel'] = self.modify_wuying_server_spec_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyWuyingServerSpecModel') is not None:
            temp_model = main_models.ModifyWuyingServerSpecResponseBodyModifyWuyingServerSpecModel()
            self.modify_wuying_server_spec_model = temp_model.from_map(m.get('ModifyWuyingServerSpecModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyWuyingServerSpecResponseBodyModifyWuyingServerSpecModel(DaraModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        # The ID of the order generated for this specification change. Returning an order ID does not mean that the specification change is complete.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        return self

