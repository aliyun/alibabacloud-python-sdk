# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetUserByDeviceIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetUserByDeviceIdResponseBodyResult = None,
    ):
        # The error code returned. A value of 200 indicates that the call succeeded.
        self.code = code
        # The return result of invoking this API.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The list of user information returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetUserByDeviceIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetUserByDeviceIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        user_open_id: str = None,
        user_union_ids: List[main_models.GetUserByDeviceIdResponseBodyResultUserUnionIds] = None,
    ):
        # The openID corresponding to the user information.
        self.user_open_id = user_open_id
        # The list of organization IDs and UnionIDs for the user.
        self.user_union_ids = user_union_ids

    def validate(self):
        if self.user_union_ids:
            for v1 in self.user_union_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        result['UserUnionIds'] = []
        if self.user_union_ids is not None:
            for k1 in self.user_union_ids:
                result['UserUnionIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        self.user_union_ids = []
        if m.get('UserUnionIds') is not None:
            for k1 in m.get('UserUnionIds'):
                temp_model = main_models.GetUserByDeviceIdResponseBodyResultUserUnionIds()
                self.user_union_ids.append(temp_model.from_map(k1))

        return self

class GetUserByDeviceIdResponseBodyResultUserUnionIds(DaraModel):
    def __init__(
        self,
        organization_id: str = None,
        user_union_id: str = None,
    ):
        # The organization ID.
        self.organization_id = organization_id
        # The user\\"s UnionID.
        self.user_union_id = user_union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.user_union_id is not None:
            result['UserUnionId'] = self.user_union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('UserUnionId') is not None:
            self.user_union_id = m.get('UserUnionId')

        return self

