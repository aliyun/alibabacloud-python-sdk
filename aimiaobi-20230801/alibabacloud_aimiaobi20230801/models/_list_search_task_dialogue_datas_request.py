# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSearchTaskDialogueDatasRequest(DaraModel):
    def __init__(
        self,
        include_content: bool = None,
        multimodal_search_type: str = None,
        original_session_id: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        search_model: str = None,
        search_model_data_value: str = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # Indicates whether to include the main content.
        self.include_content = include_content
        # The type of data to search.
        self.multimodal_search_type = multimodal_search_type
        # The unique identifier of the historical dialogue. This is the source of all original materials.
        self.original_session_id = original_session_id
        # The current page number.
        self.page_number = page_number
        # The number of entries per page. The default value is 10.
        self.page_size = page_size
        # The query conditions.
        self.query = query
        # The type of search agent.
        self.search_model = search_model
        # The data under the search agent classification.
        self.search_model_data_value = search_model_data_value
        # The unique identifier of the historical dialogue. This is the source of reference materials.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The unique identifier of the task.
        # 
        # > You do not need to specify this parameter. The system automatically generates a task ID. If you specify the same task ID for multiple tasks, the tasks are considered part of the same dialogue group.
        self.task_id = task_id
        # The unique identifier of the Alibaba Cloud Model Studio workspace. For more information, see [Get a workspaceId](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_content is not None:
            result['IncludeContent'] = self.include_content

        if self.multimodal_search_type is not None:
            result['MultimodalSearchType'] = self.multimodal_search_type

        if self.original_session_id is not None:
            result['OriginalSessionId'] = self.original_session_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.search_model is not None:
            result['SearchModel'] = self.search_model

        if self.search_model_data_value is not None:
            result['SearchModelDataValue'] = self.search_model_data_value

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')

        if m.get('MultimodalSearchType') is not None:
            self.multimodal_search_type = m.get('MultimodalSearchType')

        if m.get('OriginalSessionId') is not None:
            self.original_session_id = m.get('OriginalSessionId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SearchModel') is not None:
            self.search_model = m.get('SearchModel')

        if m.get('SearchModelDataValue') is not None:
            self.search_model_data_value = m.get('SearchModelDataValue')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

