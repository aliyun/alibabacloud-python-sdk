# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class GetAgenticSpaceResponseBody(DaraModel):
    def __init__(
        self,
        agentic_space: main_models.GetAgenticSpaceResponseBodyAgenticSpace = None,
        request_id: str = None,
    ):
        self.agentic_space = agentic_space
        self.request_id = request_id

    def validate(self):
        if self.agentic_space:
            self.agentic_space.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_space is not None:
            result['AgenticSpace'] = self.agentic_space.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticSpace') is not None:
            temp_model = main_models.GetAgenticSpaceResponseBodyAgenticSpace()
            self.agentic_space = temp_model.from_map(m.get('AgenticSpace'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgenticSpaceResponseBodyAgenticSpace(DaraModel):
    def __init__(
        self,
        agentic_space_id: str = None,
        azone: str = None,
        create_time_utc: str = None,
        description: str = None,
        file_count_usage: int = None,
        file_system_id: str = None,
        file_system_path: str = None,
        quota: main_models.GetAgenticSpaceResponseBodyAgenticSpaceQuota = None,
        space_usage: int = None,
        status: str = None,
        update_time_utc: str = None,
    ):
        self.agentic_space_id = agentic_space_id
        self.azone = azone
        self.create_time_utc = create_time_utc
        self.description = description
        self.file_count_usage = file_count_usage
        self.file_system_id = file_system_id
        self.file_system_path = file_system_path
        self.quota = quota
        self.space_usage = space_usage
        self.status = status
        self.update_time_utc = update_time_utc

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_space_id is not None:
            result['AgenticSpaceId'] = self.agentic_space_id

        if self.azone is not None:
            result['Azone'] = self.azone

        if self.create_time_utc is not None:
            result['CreateTimeUtc'] = self.create_time_utc

        if self.description is not None:
            result['Description'] = self.description

        if self.file_count_usage is not None:
            result['FileCountUsage'] = self.file_count_usage

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.space_usage is not None:
            result['SpaceUsage'] = self.space_usage

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time_utc is not None:
            result['UpdateTimeUtc'] = self.update_time_utc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticSpaceId') is not None:
            self.agentic_space_id = m.get('AgenticSpaceId')

        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        if m.get('CreateTimeUtc') is not None:
            self.create_time_utc = m.get('CreateTimeUtc')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileCountUsage') is not None:
            self.file_count_usage = m.get('FileCountUsage')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('Quota') is not None:
            temp_model = main_models.GetAgenticSpaceResponseBodyAgenticSpaceQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('SpaceUsage') is not None:
            self.space_usage = m.get('SpaceUsage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTimeUtc') is not None:
            self.update_time_utc = m.get('UpdateTimeUtc')

        return self

class GetAgenticSpaceResponseBodyAgenticSpaceQuota(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        self.file_count_limit = file_count_limit
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

