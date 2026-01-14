# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetAppMessageQueueRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAppMessageQueueRouteResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false. The value true indicates that the request was successful. The value false indicates that the request failed.
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
            temp_model = main_models.GetAppMessageQueueRouteResponseBodyData()
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

class GetAppMessageQueueRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable: bool = None,
        filter_side: str = None,
        gray_base_tags: List[str] = None,
        region: str = None,
        tags: List[str] = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # Indicates whether the canary release for messaging feature is enabled.
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable = enable
        # The side for message filtering when the canary release for messaging feature is enabled.
        self.filter_side = filter_side
        self.gray_base_tags = gray_base_tags
        # The region ID.
        self.region = region
        # The tags used to ignore message consumption for nodes in untagged environments.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.filter_side is not None:
            result['FilterSide'] = self.filter_side

        if self.gray_base_tags is not None:
            result['GrayBaseTags'] = self.gray_base_tags

        if self.region is not None:
            result['Region'] = self.region

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FilterSide') is not None:
            self.filter_side = m.get('FilterSide')

        if m.get('GrayBaseTags') is not None:
            self.gray_base_tags = m.get('GrayBaseTags')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

