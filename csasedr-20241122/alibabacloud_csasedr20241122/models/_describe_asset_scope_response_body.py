# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csasedr20241122 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetScopeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAssetScopeResponseBodyData = None,
        request_id: str = None,
    ):
        # The endpoint asset scope details.
        self.data = data
        # The unique identifier of the request, which is used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAssetScopeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAssetScopeResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
    ):
        # **[Deprecated]** This field is deprecated.
        self.gmt_create = gmt_create
        # **[Deprecated]** This field is deprecated.
        self.gmt_modified = gmt_modified
        # The ID of the asset scope record, which corresponds to the Id request parameter.
        self.id = id
        # The effective scope mode. Valid values:
        # 
        # - **UserGroupAll**: all user groups.
        # - **UserGroupNormal**: specified user groups.
        # - **DeviceGroupNormal**: specified device groups.
        # - **DevTagNormal**: specified device tags.
        # 
        # The meaning of MatchTargetIds is determined by this field.
        self.match_mode = match_mode
        # The list of effective scope targets. All elements are strings. The meaning of each element is determined by MatchMode:
        # 
        # - **UserGroupAll**: Scope matching does not depend on this list.
        # - **UserGroupNormal**: the user group ID.
        # - **DeviceGroupNormal**: the device group ID.
        # - **DevTagNormal**: the device tag value.
        # 
        # This list is not a list of matched endpoint UUIDs.
        self.match_target_ids = match_target_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        return self

