# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        request_definition: bool = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to return original request parameters specified to create the task.
        # 
        # *   true
        # *   false (default)
        # 
        # This parameter applies only to the following tasks:
        # 
        # *   MediaConvert
        # *   VideoLabelClassification
        # *   FaceClustering
        # *   FileCompression
        # *   ArchiveFileInspection
        # *   FileUncompression
        # *   PointCloudCompress
        # *   ImageToPDF
        # *   StoryCreation
        # *   LocationDateClustering
        # *   ImageSplicing
        # *   FacesSearching
        self.request_definition = request_definition
        # The ID of the task. You can obtain the ID of a task after you create the task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The type of the task. For information about valid values, see [Task types](https://help.aliyun.com/document_detail/2743993.html).
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
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

