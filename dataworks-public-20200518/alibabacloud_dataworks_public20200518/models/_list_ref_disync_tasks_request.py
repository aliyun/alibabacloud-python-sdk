# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRefDISyncTasksRequest(DaraModel):
    def __init__(
        self,
        datasource_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        ref_type: str = None,
        task_type: str = None,
    ):
        # The name of the data source. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to query the name of the data source.
        # 
        # This parameter is required.
        self.datasource_name = datasource_name
        # The page number. Valid values: 1 to 100.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The condition used to filter synchronization tasks. Valid values:
        # 
        # *   from: queries the synchronization tasks that use the data source as the source.
        # *   to: queries the synchronization tasks that use the data source as the destination.
        # 
        # This parameter is required.
        self.ref_type = ref_type
        # The type of the synchronization task that you want to query. Valid values:
        # 
        # *   DI_OFFLINE: batch synchronization task
        # *   DI_REALTIME: real-time synchronization task
        # 
        # You can call the ListRefDISyncTasks operation to query only one type of the task.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.ref_type is not None:
            result['RefType'] = self.ref_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

