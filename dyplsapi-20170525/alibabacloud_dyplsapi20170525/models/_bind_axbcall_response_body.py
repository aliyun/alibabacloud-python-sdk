# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class BindAXBCallResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.BindAXBCallResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The details of the access denied error.
        self.access_denied_detail = access_denied_detail
        # The response status code. Valid values:
        # 
        # - 0000: Success.
        # 
        # - Other values: Failure.
        self.code = code
        # The AXB call binding result.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: Success.
        # 
        # - false: Failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.BindAXBCallResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BindAXBCallResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_id: str = None,
    ):
        # The ID of the binding relationship.
        self.bind_id = bind_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        return self

