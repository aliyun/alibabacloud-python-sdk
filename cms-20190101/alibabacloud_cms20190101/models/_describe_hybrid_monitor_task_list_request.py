# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridMonitorTaskListRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        include_aliyun_task: bool = None,
        keyword: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        target_user_id: int = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The ID of the application group.
        # 
        # For information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.group_id = group_id
        # Specifies whether the returned result includes metric import tasks for Alibaba Cloud services. Valid values:
        # 
        # *   true (default): The returned result includes metric import tasks for Alibaba Cloud services.
        # *   false: The returned result excludes metric import tasks for Alibaba Cloud services.
        self.include_aliyun_task = include_aliyun_task
        # The keyword that is used for the search.
        self.keyword = keyword
        # The name of the namespace.
        # 
        # For information about how to obtain the name of a namespace, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        self.namespace = namespace
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Pages start from page 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the member account.
        # 
        # > This parameter is required only if you use a management account to call this operation to delete the metric import tasks that belong to a member in a resource directory. In this case, the `TaskType` parameter is set to `aliyun_fc`.
        self.target_user_id = target_user_id
        # The ID of the metric import task.
        self.task_id = task_id
        # The type of the metric import task. Valid values:
        # 
        # *   aliyun_fc: metric import tasks for Alibaba Cloud services
        # *   aliyun_sls: metrics for logs imported from Log Service
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.include_aliyun_task is not None:
            result['IncludeAliyunTask'] = self.include_aliyun_task

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IncludeAliyunTask') is not None:
            self.include_aliyun_task = m.get('IncludeAliyunTask')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

