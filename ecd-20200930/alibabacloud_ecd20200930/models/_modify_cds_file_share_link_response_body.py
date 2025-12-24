# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyCdsFileShareLinkResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CdsFileShareLinkModel = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The modification result. The value success indicates that the modification is successful. If the modification failed, an error message is returned.
        self.code = code
        # The data information.
        self.data = data
        # The error message that is returned. This parameter is not returned if the value of Code is success.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The request status.
        # 
        # Valid values:
        # 
        # *   true: The request is successful.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false: The request fails.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
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
            temp_model = main_models.CdsFileShareLinkModel()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

