# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUserBaselineAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_baseline_authorization: main_models.DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The authorization information for cloud baseline configuration check.
        self.user_baseline_authorization = user_baseline_authorization

    def validate(self):
        if self.user_baseline_authorization:
            self.user_baseline_authorization.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_baseline_authorization is not None:
            result['UserBaselineAuthorization'] = self.user_baseline_authorization.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserBaselineAuthorization') is not None:
            temp_model = main_models.DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization()
            self.user_baseline_authorization = temp_model.from_map(m.get('UserBaselineAuthorization'))

        return self

class DescribeUserBaselineAuthorizationResponseBodyUserBaselineAuthorization(DaraModel):
    def __init__(
        self,
        status: int = None,
    ):
        # The authorization status of the cloud platform configuration check. Valid values:
        # - **0**: Authorization is disabled. If authorization is disabled, you cannot use the cloud platform configuration check feature.
        # - **1**: Authorization is enabled. If authorization is enabled, you can use the cloud platform configuration check feature.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

