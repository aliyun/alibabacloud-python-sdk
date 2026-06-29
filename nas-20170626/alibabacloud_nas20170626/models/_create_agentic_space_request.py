# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateAgenticSpaceRequest(DaraModel):
    def __init__(
        self,
        azone: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        file_system_path: str = None,
        quota: main_models.CreateAgenticSpaceRequestQuota = None,
    ):
        # This parameter is required.
        self.azone = azone
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.file_system_path = file_system_path
        # This parameter is required.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.azone is not None:
            result['Azone'] = self.azone

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('Quota') is not None:
            temp_model = main_models.CreateAgenticSpaceRequestQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        return self

class CreateAgenticSpaceRequestQuota(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # This parameter is required.
        self.file_count_limit = file_count_limit
        # This parameter is required.
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

