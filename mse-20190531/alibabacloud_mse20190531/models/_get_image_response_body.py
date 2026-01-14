# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetImageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetImageResponseBodyData = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetImageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetImageResponseBodyData(DaraModel):
    def __init__(
        self,
        current_version_full_show_name: str = None,
        max_version_changelog_url: str = None,
        max_version_code: str = None,
        max_version_full_show_name: str = None,
    ):
        # The full version number of the current instance image. The parameter is in the X.X.X.X format.
        self.current_version_full_show_name = current_version_full_show_name
        # The URL of the changelog for the maximum version to which the current version can be upgraded.
        self.max_version_changelog_url = max_version_changelog_url
        # The code of the maximum version to which the current version can be upgraded.
        self.max_version_code = max_version_code
        # The full number of the maximum version to which the current version can be upgraded.
        self.max_version_full_show_name = max_version_full_show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_version_full_show_name is not None:
            result['CurrentVersionFullShowName'] = self.current_version_full_show_name

        if self.max_version_changelog_url is not None:
            result['MaxVersionChangelogUrl'] = self.max_version_changelog_url

        if self.max_version_code is not None:
            result['MaxVersionCode'] = self.max_version_code

        if self.max_version_full_show_name is not None:
            result['MaxVersionFullShowName'] = self.max_version_full_show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersionFullShowName') is not None:
            self.current_version_full_show_name = m.get('CurrentVersionFullShowName')

        if m.get('MaxVersionChangelogUrl') is not None:
            self.max_version_changelog_url = m.get('MaxVersionChangelogUrl')

        if m.get('MaxVersionCode') is not None:
            self.max_version_code = m.get('MaxVersionCode')

        if m.get('MaxVersionFullShowName') is not None:
            self.max_version_full_show_name = m.get('MaxVersionFullShowName')

        return self

