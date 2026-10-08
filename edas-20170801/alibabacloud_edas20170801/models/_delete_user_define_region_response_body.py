# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class DeleteUserDefineRegionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        region_define: main_models.DeleteUserDefineRegionResponseBodyRegionDefine = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The custom namespace.
        self.region_define = region_define
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.region_define:
            self.region_define.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.region_define is not None:
            result['RegionDefine'] = self.region_define.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionDefine') is not None:
            temp_model = main_models.DeleteUserDefineRegionResponseBodyRegionDefine()
            self.region_define = temp_model.from_map(m.get('RegionDefine'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteUserDefineRegionResponseBodyRegionDefine(DaraModel):
    def __init__(
        self,
        belong_region: str = None,
        description: str = None,
        id: int = None,
        region_id: str = None,
        region_name: str = None,
        user_id: str = None,
    ):
        # The ID of the region to which the custom namespace belongs.
        self.belong_region = belong_region
        # The description of the custom namespace.
        self.description = description
        # The unique identifier of the custom namespace.
        self.id = id
        # The ID of the custom namespace. The ID cannot be changed after the custom namespace is created. The format is `region ID:custom namespace ID`.
        self.region_id = region_id
        # The name of the custom namespace.
        self.region_name = region_name
        # The ID of the Alibaba Cloud account to which the custom namespace belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

