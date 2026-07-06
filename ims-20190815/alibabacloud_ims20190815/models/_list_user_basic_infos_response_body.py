# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListUserBasicInfosResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        user_basic_infos: main_models.ListUserBasicInfosResponseBodyUserBasicInfos = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.\\`\\`
        self.marker = marker
        # The request ID.
        self.request_id = request_id
        self.user_basic_infos = user_basic_infos

    def validate(self):
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserBasicInfos') is not None:
            temp_model = main_models.ListUserBasicInfosResponseBodyUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(m.get('UserBasicInfos'))

        return self

class ListUserBasicInfosResponseBodyUserBasicInfos(DaraModel):
    def __init__(
        self,
        user_basic_info: List[main_models.ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo] = None,
    ):
        self.user_basic_info = user_basic_info

    def validate(self):
        if self.user_basic_info:
            for v1 in self.user_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserBasicInfo'] = []
        if self.user_basic_info is not None:
            for k1 in self.user_basic_info:
                result['UserBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_basic_info = []
        if m.get('UserBasicInfo') is not None:
            for k1 in m.get('UserBasicInfo'):
                temp_model = main_models.ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k1))

        return self

class ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        status: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        self.display_name = display_name
        self.status = status
        self.user_id = user_id
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

