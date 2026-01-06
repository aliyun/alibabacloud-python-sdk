# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDatasetFileMetasRequest(DaraModel):
    def __init__(
        self,
        dataset_version: str = None,
        end_file_update_time: str = None,
        end_tag_update_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_size: int = None,
        query_content_type_include_any: List[str] = None,
        query_expression: str = None,
        query_file_dir: str = None,
        query_file_name: str = None,
        query_file_type_include_any: List[str] = None,
        query_image: str = None,
        query_tags_exclude: List[str] = None,
        query_tags_include_all: List[str] = None,
        query_tags_include_any: List[str] = None,
        query_text: str = None,
        query_type: str = None,
        query_video: str = None,
        score_threshold: float = None,
        sort_by: str = None,
        start_file_update_time: str = None,
        start_tag_update_time: str = None,
        status: str = None,
        thumbnail_mode: str = None,
        top_k: int = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The update time range to query. The end time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        self.max_results = max_results
        # The pagination token.
        # 
        # >  If you do not configure this parameter, the data on the first page is returned. A return value other than Null of this parameter indicates that not all entries have been returned. You can use this value as an input parameter to obtain entries on the next page. The value Null indicates that all query results have been returned.
        self.next_token = next_token
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The number of entries per page. Default value: 10. Maximum value: 1000.
        self.page_size = page_size
        self.query_content_type_include_any = query_content_type_include_any
        self.query_expression = query_expression
        self.query_file_dir = query_file_dir
        self.query_file_name = query_file_name
        self.query_file_type_include_any = query_file_type_include_any
        self.query_image = query_image
        self.query_tags_exclude = query_tags_exclude
        self.query_tags_include_all = query_tags_include_all
        self.query_tags_include_any = query_tags_include_any
        # The text content to be queried.
        self.query_text = query_text
        # The retrieval type.
        # 
        # *   TAG (default)
        # *   VECTOR
        self.query_type = query_type
        self.query_video = query_video
        # The similarity score. Only dataset files whose similarity score is greater than the value of ScoreThreshold are returned. This parameter is valid only when QueryType is set to VECTOR.
        self.score_threshold = score_threshold
        # The field used to sort the results. Default value: GmtCreateTime. Valid values:
        # 
        # *   FileCreateTime (default): The results are sorted by the time when the file is created.
        # *   FileUpdateTime: The results are sorted by the time when the file is last modified.
        self.sort_by = sort_by
        # The update time range to query. The start time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        self.status = status
        self.thumbnail_mode = thumbnail_mode
        # The number of search results to return. A maximum of Top K search results can be returned. This parameter is valid only when QueryType is set to VECTOR.
        self.top_k = top_k
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.end_file_update_time is not None:
            result['EndFileUpdateTime'] = self.end_file_update_time

        if self.end_tag_update_time is not None:
            result['EndTagUpdateTime'] = self.end_tag_update_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_content_type_include_any is not None:
            result['QueryContentTypeIncludeAny'] = self.query_content_type_include_any

        if self.query_expression is not None:
            result['QueryExpression'] = self.query_expression

        if self.query_file_dir is not None:
            result['QueryFileDir'] = self.query_file_dir

        if self.query_file_name is not None:
            result['QueryFileName'] = self.query_file_name

        if self.query_file_type_include_any is not None:
            result['QueryFileTypeIncludeAny'] = self.query_file_type_include_any

        if self.query_image is not None:
            result['QueryImage'] = self.query_image

        if self.query_tags_exclude is not None:
            result['QueryTagsExclude'] = self.query_tags_exclude

        if self.query_tags_include_all is not None:
            result['QueryTagsIncludeAll'] = self.query_tags_include_all

        if self.query_tags_include_any is not None:
            result['QueryTagsIncludeAny'] = self.query_tags_include_any

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.query_video is not None:
            result['QueryVideo'] = self.query_video

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_file_update_time is not None:
            result['StartFileUpdateTime'] = self.start_file_update_time

        if self.start_tag_update_time is not None:
            result['StartTagUpdateTime'] = self.start_tag_update_time

        if self.status is not None:
            result['Status'] = self.status

        if self.thumbnail_mode is not None:
            result['ThumbnailMode'] = self.thumbnail_mode

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('EndFileUpdateTime') is not None:
            self.end_file_update_time = m.get('EndFileUpdateTime')

        if m.get('EndTagUpdateTime') is not None:
            self.end_tag_update_time = m.get('EndTagUpdateTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryContentTypeIncludeAny') is not None:
            self.query_content_type_include_any = m.get('QueryContentTypeIncludeAny')

        if m.get('QueryExpression') is not None:
            self.query_expression = m.get('QueryExpression')

        if m.get('QueryFileDir') is not None:
            self.query_file_dir = m.get('QueryFileDir')

        if m.get('QueryFileName') is not None:
            self.query_file_name = m.get('QueryFileName')

        if m.get('QueryFileTypeIncludeAny') is not None:
            self.query_file_type_include_any = m.get('QueryFileTypeIncludeAny')

        if m.get('QueryImage') is not None:
            self.query_image = m.get('QueryImage')

        if m.get('QueryTagsExclude') is not None:
            self.query_tags_exclude = m.get('QueryTagsExclude')

        if m.get('QueryTagsIncludeAll') is not None:
            self.query_tags_include_all = m.get('QueryTagsIncludeAll')

        if m.get('QueryTagsIncludeAny') is not None:
            self.query_tags_include_any = m.get('QueryTagsIncludeAny')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('QueryVideo') is not None:
            self.query_video = m.get('QueryVideo')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartFileUpdateTime') is not None:
            self.start_file_update_time = m.get('StartFileUpdateTime')

        if m.get('StartTagUpdateTime') is not None:
            self.start_tag_update_time = m.get('StartTagUpdateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThumbnailMode') is not None:
            self.thumbnail_mode = m.get('ThumbnailMode')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

