# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeFotaTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        fota_tasks: List[main_models.DescribeFotaTasksResponseBodyFotaTasks] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The returned message. If the request was successful, a `success` is returned. If the request failed, an error message is returned.
        self.code = code
        # Details about the image update task.
        self.fota_tasks = fota_tasks
        # The returned error message. This parameter is not returned if the Code value is a `success` message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fota_tasks:
            for v1 in self.fota_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['FotaTasks'] = []
        if self.fota_tasks is not None:
            for k1 in self.fota_tasks:
                result['FotaTasks'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.fota_tasks = []
        if m.get('FotaTasks') is not None:
            for k1 in m.get('FotaTasks'):
                temp_model = main_models.DescribeFotaTasksResponseBodyFotaTasks()
                self.fota_tasks.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFotaTasksResponseBodyFotaTasks(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        fota_project: str = None,
        pending_custom_image_count: int = None,
        pending_desktop_count: int = None,
        publish_time: str = None,
        release_note: str = None,
        size: int = None,
        status: str = None,
        task_uid: str = None,
    ):
        # The image version. You can call the [DescribeImages](https://help.aliyun.com/document_detail/188895.html) operation to obtain the value of this parameter.
        self.app_version = app_version
        # >  This parameter is not publicly available.
        self.fota_project = fota_project
        # The number of custom images that can be updated to this version.
        self.pending_custom_image_count = pending_custom_image_count
        # The number of cloud computers whose images can be updated to this version.
        self.pending_desktop_count = pending_desktop_count
        # The time when the image version available for update was published.
        self.publish_time = publish_time
        # The description of the image version available for update.
        self.release_note = release_note
        # The size of the update package. Unit: KB.
        self.size = size
        # Indicates whether the image update task is automatically pushed.
        # 
        # Valid values:
        # 
        # *   Running: automatically pushes the image update task.
        # *   Pending: does not automatically push the image update task.
        self.status = status
        # The ID of the image upgrade task.
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.fota_project is not None:
            result['FotaProject'] = self.fota_project

        if self.pending_custom_image_count is not None:
            result['PendingCustomImageCount'] = self.pending_custom_image_count

        if self.pending_desktop_count is not None:
            result['PendingDesktopCount'] = self.pending_desktop_count

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('FotaProject') is not None:
            self.fota_project = m.get('FotaProject')

        if m.get('PendingCustomImageCount') is not None:
            self.pending_custom_image_count = m.get('PendingCustomImageCount')

        if m.get('PendingDesktopCount') is not None:
            self.pending_desktop_count = m.get('PendingDesktopCount')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')

        return self

