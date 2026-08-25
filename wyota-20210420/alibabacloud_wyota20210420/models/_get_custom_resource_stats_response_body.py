# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class GetCustomResourceStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomResourceStatsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. 200 is returned if the call is successful. An error code is returned if the call fails.
        self.code = code
        # The custom resource statistics information.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. This parameter is empty if the call is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetCustomResourceStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomResourceStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        custom_resource_count: int = None,
        effective_count: int = None,
        no_custom_resource_count: int = None,
        un_effective_count: int = None,
    ):
        # The number of terminals with custom resources configured.
        self.custom_resource_count = custom_resource_count
        # The number of terminals on which custom resources have taken effect.
        self.effective_count = effective_count
        # The number of terminals without custom resources configured.
        self.no_custom_resource_count = no_custom_resource_count
        # The number of terminals on which custom resources have not taken effect.
        self.un_effective_count = un_effective_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_resource_count is not None:
            result['CustomResourceCount'] = self.custom_resource_count

        if self.effective_count is not None:
            result['EffectiveCount'] = self.effective_count

        if self.no_custom_resource_count is not None:
            result['NoCustomResourceCount'] = self.no_custom_resource_count

        if self.un_effective_count is not None:
            result['UnEffectiveCount'] = self.un_effective_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomResourceCount') is not None:
            self.custom_resource_count = m.get('CustomResourceCount')

        if m.get('EffectiveCount') is not None:
            self.effective_count = m.get('EffectiveCount')

        if m.get('NoCustomResourceCount') is not None:
            self.no_custom_resource_count = m.get('NoCustomResourceCount')

        if m.get('UnEffectiveCount') is not None:
            self.un_effective_count = m.get('UnEffectiveCount')

        return self

