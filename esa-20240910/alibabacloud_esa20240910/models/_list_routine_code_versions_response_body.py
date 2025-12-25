# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRoutineCodeVersionsResponseBody(DaraModel):
    def __init__(
        self,
        code_versions: List[main_models.ListRoutineCodeVersionsResponseBodyCodeVersions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The code versions of the routine.
        self.code_versions = code_versions
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of code versions returned.
        self.total_count = total_count

    def validate(self):
        if self.code_versions:
            for v1 in self.code_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeVersions'] = []
        if self.code_versions is not None:
            for k1 in self.code_versions:
                result['CodeVersions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_versions = []
        if m.get('CodeVersions') is not None:
            for k1 in m.get('CodeVersions'):
                temp_model = main_models.ListRoutineCodeVersionsResponseBodyCodeVersions()
                self.code_versions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRoutineCodeVersionsResponseBodyCodeVersions(DaraModel):
    def __init__(
        self,
        build_id: int = None,
        code_description: str = None,
        code_version: str = None,
        conf_options: main_models.ListRoutineCodeVersionsResponseBodyCodeVersionsConfOptions = None,
        create_time: str = None,
        extra_info: str = None,
        status: str = None,
    ):
        # The ID of the code version build.
        self.build_id = build_id
        # The description of the code version.
        self.code_description = code_description
        # The version of the code.
        self.code_version = code_version
        # Code version configuration items.
        self.conf_options = conf_options
        # The time when the code version was created.
        self.create_time = create_time
        # Additional information about the code version.
        self.extra_info = extra_info
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
            temp_model = main_models.ListRoutineCodeVersionsResponseBodyCodeVersionsConfOptions()
            self.conf_options = temp_model.from_map(m.get('ConfOptions'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListRoutineCodeVersionsResponseBodyCodeVersionsConfOptions(DaraModel):
    def __init__(
        self,
        not_found_strategy: str = None,
    ):
        # Code version configuration items NotFoundStrategy.
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

