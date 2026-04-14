# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBaseJobsRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        job_action: str = None,
        knowledge_base_job_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # 任务操作类型。
        # - SyncIndex：更新知识库索引
        self.job_action = job_action
        # 知识库任务ID。
        self.knowledge_base_job_id = knowledge_base_job_id
        # 使用 NextToken 方式查询时，每次最多返回的结果数。
        self.max_results = max_results
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 排序方式。
        # 
        # - ASC：升序。
        # - DESC：降序。
        self.order = order
        # 当前页数。 取值范围：大于0。 默认值：1。如果同时传入MaxResults，则使用NextToken查询方式，忽略此字段值。
        self.page_number = page_number
        # 每页查询的数量。如果同时传入 MaxResults，则以 MaxResults 数量为准。
        self.page_size = page_size
        # 排序字段。目前只支持GmtCreateTime。
        self.sort_by = sort_by
        # 知识库任务状态。
        # - Running: 运行中。
        # - Success: 运行成功。
        # - Failed: 运行失败。
        self.status = status
        # 知识库所在工作空间ID。
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.knowledge_base_job_id is not None:
            result['KnowledgeBaseJobId'] = self.knowledge_base_job_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('KnowledgeBaseJobId') is not None:
            self.knowledge_base_job_id = m.get('KnowledgeBaseJobId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

