# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class UpgradeRenderingInstanceImageResponseBody(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        failed_items: List[main_models.UpgradeRenderingInstanceImageResponseBodyFailedItems] = None,
        request_id: str = None,
        success_count: int = None,
        success_items: List[main_models.UpgradeRenderingInstanceImageResponseBodySuccessItems] = None,
    ):
        # The number of failed instances.
        self.failed_count = failed_count
        # The information about failed instances.
        self.failed_items = failed_items
        # The request ID.
        self.request_id = request_id
        # The number of successful instances.
        self.success_count = success_count
        # The information about successful instances.
        self.success_items = success_items

    def validate(self):
        if self.failed_items:
            for v1 in self.failed_items:
                 if v1:
                    v1.validate()
        if self.success_items:
            for v1 in self.success_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['FailedItems'] = []
        if self.failed_items is not None:
            for k1 in self.failed_items:
                result['FailedItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['SuccessItems'] = []
        if self.success_items is not None:
            for k1 in self.success_items:
                result['SuccessItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.failed_items = []
        if m.get('FailedItems') is not None:
            for k1 in m.get('FailedItems'):
                temp_model = main_models.UpgradeRenderingInstanceImageResponseBodyFailedItems()
                self.failed_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_items = []
        if m.get('SuccessItems') is not None:
            for k1 in m.get('SuccessItems'):
                temp_model = main_models.UpgradeRenderingInstanceImageResponseBodySuccessItems()
                self.success_items.append(temp_model.from_map(k1))

        return self

class UpgradeRenderingInstanceImageResponseBodySuccessItems(DaraModel):
    def __init__(
        self,
        rendering_instance_id: str = None,
    ):
        # The cloud application service instance ID.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class UpgradeRenderingInstanceImageResponseBodyFailedItems(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        rendering_instance_id: str = None,
    ):
        # The error code of the failure.
        self.err_code = err_code
        # The error message of the failure.
        self.err_message = err_message
        # The cloud application service instance ID.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

