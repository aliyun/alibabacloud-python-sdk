# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaConnectAvailableRegionResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.GetMediaConnectAvailableRegionResponseBodyContent = None,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The rsponse body.
        self.content = content
        # The call description.
        self.description = description
        # The ID of the request.
        self.request_id = request_id
        # The returned error code. A value of 0 indicates the call is successful.
        self.ret_code = ret_code

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.GetMediaConnectAvailableRegionResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

class GetMediaConnectAvailableRegionResponseBodyContent(DaraModel):
    def __init__(
        self,
        default_region: str = None,
        region_list: List[str] = None,
    ):
        # The default region. You can ignore the parameter.
        self.default_region = default_region
        # The supported regions.
        self.region_list = region_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_region is not None:
            result['DefaultRegion'] = self.default_region

        if self.region_list is not None:
            result['RegionList'] = self.region_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRegion') is not None:
            self.default_region = m.get('DefaultRegion')

        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')

        return self

