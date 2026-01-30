# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListCloudAppPatchesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        patches: List[main_models.ListCloudAppPatchesResponseBodyPatches] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.patches = patches
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.patches:
            for v1 in self.patches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Patches'] = []
        if self.patches is not None:
            for k1 in self.patches:
                result['Patches'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.patches = []
        if m.get('Patches') is not None:
            for k1 in m.get('Patches'):
                temp_model = main_models.ListCloudAppPatchesResponseBodyPatches()
                self.patches.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAppPatchesResponseBodyPatches(DaraModel):
    def __init__(
        self,
        patch_id: str = None,
        patch_name: str = None,
        status: str = None,
        status_description: str = None,
        update_time: str = None,
        upload_time: str = None,
    ):
        self.patch_id = patch_id
        self.patch_name = patch_name
        self.status = status
        self.status_description = status_description
        self.update_time = update_time
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.patch_name is not None:
            result['PatchName'] = self.patch_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_description is not None:
            result['StatusDescription'] = self.status_description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('PatchName') is not None:
            self.patch_name = m.get('PatchName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

