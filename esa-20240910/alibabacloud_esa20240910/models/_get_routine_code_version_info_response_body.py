# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetRoutineCodeVersionInfoResponseBody(DaraModel):
    def __init__(
        self,
        build_id: int = None,
        code_description: str = None,
        code_version: str = None,
        conf_options: main_models.GetRoutineCodeVersionInfoResponseBodyConfOptions = None,
        create_time: str = None,
        extra_info: str = None,
        has_assets: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        # The build ID of the code.
        self.build_id = build_id
        # The description of the code version.
        self.code_description = code_description
        # The code version number.
        self.code_version = code_version
        # The list of configuration items for the code version.
        self.conf_options = conf_options
        # The time when the code version was created.
        self.create_time = create_time
        # The additional information about the code version. The value is in JSON string format.
        self.extra_info = extra_info
        # Indicates whether the code version contains asset files.
        self.has_assets = has_assets
        # The request ID.
        self.request_id = request_id
        # The status of the code version.
        self.status = status

    def validate(self):
        if self.conf_options:
            self.conf_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.code_description is not None:
            result['CodeDescription'] = self.code_description

        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.conf_options is not None:
            result['ConfOptions'] = self.conf_options.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.has_assets is not None:
            result['HasAssets'] = self.has_assets

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')

        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('ConfOptions') is not None:
            temp_model = main_models.GetRoutineCodeVersionInfoResponseBodyConfOptions()
            self.conf_options = temp_model.from_map(m.get('ConfOptions'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('HasAssets') is not None:
            self.has_assets = m.get('HasAssets')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetRoutineCodeVersionInfoResponseBodyConfOptions(DaraModel):
    def __init__(
        self,
        not_found_strategy: str = None,
    ):
        # The NotFoundStrategy configuration item.
        self.not_found_strategy = not_found_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_found_strategy is not None:
            result['NotFoundStrategy'] = self.not_found_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotFoundStrategy') is not None:
            self.not_found_strategy = m.get('NotFoundStrategy')

        return self

