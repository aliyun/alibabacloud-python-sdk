# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentretailvision20260506 import models as main_models
from darabonba.model import DaraModel

class UpdateProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateProductResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateProductResponseBodyData(DaraModel):
    def __init__(
        self,
        item_unique_id: str = None,
        platform_item_id: str = None,
    ):
        self.item_unique_id = item_unique_id
        self.platform_item_id = platform_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_unique_id is not None:
            result['ItemUniqueId'] = self.item_unique_id

        if self.platform_item_id is not None:
            result['PlatformItemId'] = self.platform_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemUniqueId') is not None:
            self.item_unique_id = m.get('ItemUniqueId')

        if m.get('PlatformItemId') is not None:
            self.platform_item_id = m.get('PlatformItemId')

        return self

