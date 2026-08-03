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
        # The zone ID.
        # 
        # This parameter is required.
        self.azone = azone
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The description of the Agentic space.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request. A dry run checks parameter validity and dependencies without actually modifying the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without modifying the protocol service. The system checks required parameters, request format, and business limit dependencies. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # - false (default): Sends a normal request. After the check passes, the protocol service is directly modified.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the file. Only first-level directories are supported.
        # 
        # This parameter is required.
        self.file_system_path = file_system_path
        # The quota information.
        # 
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
        # The maximum number of files allowed by the quota. Valid values:
        # 
        # - Minimum value: 10,000.
        # 
        # - Maximum value: 100,000,000.
        # 
        # This parameter is required.
        self.file_count_limit = file_count_limit
        # The total capacity limit of the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # - Minimum value: 10,737,418,240 (10 GiB).
        # - Maximum value: 1,099,511,627,776,000 (1,024,000 GiB).
        # - Increment: 1,073,741,824 (1 GiB).
        # 
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

