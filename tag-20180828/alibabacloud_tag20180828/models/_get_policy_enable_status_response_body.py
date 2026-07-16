# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class GetPolicyEnableStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_models: List[main_models.GetPolicyEnableStatusResponseBodyStatusModels] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the Tag Policy feature.
        self.status_models = status_models

    def validate(self):
        if self.status_models:
            for v1 in self.status_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatusModels'] = []
        if self.status_models is not None:
            for k1 in self.status_models:
                result['StatusModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.status_models = []
        if m.get('StatusModels') is not None:
            for k1 in m.get('StatusModels'):
                temp_model = main_models.GetPolicyEnableStatusResponseBodyStatusModels()
                self.status_models.append(temp_model.from_map(k1))

        return self

class GetPolicyEnableStatusResponseBodyStatusModels(DaraModel):
    def __init__(
        self,
        status: str = None,
        user_type: str = None,
    ):
        # The status of the Tag Policy feature. Valid values:
        # 
        # *   PendingEnable: The feature is being enabled.
        # *   Enabled: The feature is enabled.
        # *   Closing: The feature is being disabled.
        # *   Disabled: The feature is disabled.
        self.status = status
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

