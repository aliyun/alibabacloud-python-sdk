# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiskAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        disk_attachments: List[main_models.DescribeDiskAttachmentsResponseBodyDiskAttachments] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of disk attachments.
        self.disk_attachments = disk_attachments
        # The maximum number of attachments returned in a single request.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that all attachments have been returned.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.disk_attachments:
            for v1 in self.disk_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskAttachments'] = []
        if self.disk_attachments is not None:
            for k1 in self.disk_attachments:
                result['DiskAttachments'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_attachments = []
        if m.get('DiskAttachments') is not None:
            for k1 in m.get('DiskAttachments'):
                temp_model = main_models.DescribeDiskAttachmentsResponseBodyDiskAttachments()
                self.disk_attachments.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiskAttachmentsResponseBodyDiskAttachments(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        device: str = None,
        disk_id: str = None,
        instance_id: str = None,
    ):
        # The time when the disk was successfully attached, in ISO 8601 format (UTC).
        self.attached_time = attached_time
        # The device name on the instance.
        self.device = device
        # The disk ID.
        self.disk_id = disk_id
        # The ID of the instance to which the disk is attached.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

