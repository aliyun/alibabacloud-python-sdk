# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateJenkinsImageScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateJenkinsImageScanTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateJenkinsImageScanTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateJenkinsImageScanTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        image_scan_capacity: int = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_region_id: str = None,
        task_id: str = None,
        uuid: str = None,
    ):
        # The quota for image scan.
        self.image_scan_capacity = image_scan_capacity
        # The ID of the image repository.
        self.repo_id = repo_id
        # The instance ID of the image repository.
        self.repo_instance_id = repo_instance_id
        # The ID of the region.
        self.repo_region_id = repo_region_id
        # The ID of the scan task.
        self.task_id = task_id
        # The UUID of the image asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

