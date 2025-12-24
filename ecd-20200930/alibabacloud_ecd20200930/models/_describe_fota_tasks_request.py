# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeFotaTasksRequest(DaraModel):
    def __init__(
        self,
        fota_status: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_uid: List[str] = None,
        user_status: str = None,
    ):
        # >  This parameter is not publicly available.
        self.fota_status = fota_status
        # The language of the image version to update.
        # 
        # Valid values:
        # 
        # *   en: English.
        # *   zh: Simplified Chinese.
        self.lang = lang
        # The number of entries per page.
        # 
        # *   Valid values: 1 to 100
        # *   Default value: 20
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the image update tasks.
        self.task_uid = task_uid
        # Specifies whether to automatically push the image update task.
        # 
        # Valid values:
        # 
        # *   Running: automatically pushes the image update task.
        # *   Pending: does not automatically push the image update task.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fota_status is not None:
            result['FotaStatus'] = self.fota_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FotaStatus') is not None:
            self.fota_status = m.get('FotaStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

