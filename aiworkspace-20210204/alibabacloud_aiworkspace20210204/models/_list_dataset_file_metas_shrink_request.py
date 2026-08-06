# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetFileMetasShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_file_meta_ids_shrink: str = None,
        dataset_version: str = None,
        end_file_update_time: str = None,
        end_tag_update_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_size: int = None,
        query_content_type_include_any_shrink: str = None,
        query_expression: str = None,
        query_file_dir: str = None,
        query_file_name: str = None,
        query_file_type_include_any_shrink: str = None,
        query_image: str = None,
        query_tags_exclude_shrink: str = None,
        query_tags_include_all_shrink: str = None,
        query_tags_include_any_shrink: str = None,
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
        # The list of metadata IDs to query.
        self.dataset_file_meta_ids_shrink = dataset_file_meta_ids_shrink
        # The dataset version name.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The end time for the file update time query range. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # The end time for the tag last update time query range. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        # The maximum number of results to return per request when using NextToken-based pagination. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token.
        # > 
        # > If this parameter is not specified, the first page of data is returned. If a value is returned for this parameter, more pages are available. Pass the returned NextToken value as a request parameter to retrieve the next page, until no NextToken value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The sorting order for the specified sort field in paging queries. Used together with SortBy. Default value: DESC. Valid values:
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order = order
        # The number of entries per page. If MaxResults is also specified, MaxResults takes precedence.
        # > This parameter will be offline soon. Use NextToken and MaxResults to perform paging operations.
        self.page_size = page_size
        # The search condition for "include any of the following content types". You can select multiple content types, and the query results need to match only one of them. If empty, this condition is not applied. Array values are separated by commas.
        self.query_content_type_include_any_shrink = query_content_type_include_any_shrink
        # The query statement (DSL) is a domain-specific language for expressing complex retrieve conditions. It supports grouping, Boolean logic (AND/OR/NOT), range comparisons (>, >=, <, <=), property existence (HAS/NOT HAS), tokenized matching (:), and exact match (=), suitable for advanced retrieve scenarios.
        # Generally used for complex advanced conditional retrieve operations.
        # <notice>To avoid conflicts, after setting this query statement, do not use it together with other query parameters.</notice>
        self.query_expression = query_expression
        # The file directory search condition. Fuzzy match is supported.
        self.query_file_dir = query_file_dir
        # The file name search condition. Fuzzy match is supported.
        self.query_file_name = query_file_name
        # The search condition for "include any of the following file types". You can select multiple file types, and the query results need to match only one of them. If empty, this condition is not applied. Array values are separated by commas.
        self.query_file_type_include_any_shrink = query_file_type_include_any_shrink
        # The image information for image-to-image search.
        # * Supports a public network access OSS URL in the format: oss://{bucket_name}/{object_path}, where bucket_name is the bucket name and object_path is the file path in the bucket.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.query_image = query_image
        # The search condition for "exclude the following tags". You can select multiple tags, and the query results must not contain any of them. If empty, this condition is not applied.
        # > This parameter takes effect only when QueryType is set to TAG or MIX.
        self.query_tags_exclude_shrink = query_tags_exclude_shrink
        # The search condition for "include all of the following tags". You can select multiple tags, and the query results must match all of them. If empty, this condition is not applied. Array values are separated by commas.
        # 
        # > This parameter takes effect only when QueryType is set to TAG or MIX. When QueryType is set to TAG, QueryText is added to this condition.
        self.query_tags_include_all_shrink = query_tags_include_all_shrink
        # The search condition for "include any of the following tags". You can select multiple tags, and the query results need to match only one of them. If empty, this condition is not applied. Array values are separated by commas.
        # > This parameter takes effect only when QueryType is set to TAG or MIX.
        self.query_tags_include_any_shrink = query_tags_include_any_shrink
        # The text content to search for.
        self.query_text = query_text
        # The retrieve type. Valid values:
        # * MIX: hybrid retrieve (default).
        # * TAG: label-only retrieve.
        # * VECTOR: vector retrieve only.
        self.query_type = query_type
        # The video file information for video-based search.
        # * Supports a public network access OSS URL in the format: oss://{bucket_name}/{object_path}, where bucket_name is the bucket name and object_path is the file path in the bucket.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.query_video = query_video
        # The similarity score threshold. Only results with a score greater than ScoreThreshold are returned.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.score_threshold = score_threshold
        # The sorting field for paging queries. By default, results are sorted by retrieve relevance in descending order. Valid values:
        # * FileCreateTime: sorting by file creation time.
        # * FileUpdateTime: sorting by file last modification time.
        self.sort_by = sort_by
        # The start time for the file update time query range. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # The start time for the tag last update time query range. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        # The metadata status to query. Valid values:
        # * ACTIVE: queries only non-deleted data (default).
        # * ALL: queries all data.
        # * DELETED: queries only logically deleted data.
        self.status = status
        # The thumbnail mode for images. Currently, only OSS files support thumbnails:
        # - Proportional scaling: p_{percentage}, where percentage specifies the desired scaling ratio. Valid values: [1, 100]. Example: p_50 uses 50% of the original file size as the thumbnail.
        # - Fixed width with adaptive height: w_{width}, where width specifies the desired image width. Valid values: [1, 16384]. Example: w_200 fixes the image width to 200 pixels and adaptively scales the height.
        # - Fixed height with adaptive width: h_{height}, where height specifies the desired image height. Valid values: [1, 16384]. Example: h_100 fixes the image height to 100 pixels and adaptively scales the width.
        # - Fixed dimensions with padding: m_pad,w_{width},h_{height},color_{RGB}. m_pad scales the image to the largest size that fits within the specified width and height rectangle. RGB specifies the fill color for blank areas. If not specified, white is used by default. width specifies the desired image width and height specifies the desired image height. Valid values for both width and height: [1, 16384].
        # - Fixed dimensions with center cropping: m_fill,w_{width},h_{height}. m_fill proportionally scales the image to the smallest size that extends beyond the specified width and height rectangle, and center-crops the excess. width specifies the desired image width and height specifies the desired image height. Valid values for both width and height: [1, 16384]. Example: m_fill,w_100,h_100 fixes both width and height to 100 pixels with center cropping.
        # - Forced dimensions: m_fixed,w_{width},h_{height}. width specifies the desired image width and height specifies the desired image height. Valid values for both width and height: [1, 16384]. Example: m_fixed,w_100,h_100 forces both width and height to 100 pixels.
        self.thumbnail_mode = thumbnail_mode
        # The maximum number of results to return. Only the top K results are returned.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.top_k = top_k
        # The workspace ID where the dataset resides. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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
        if self.dataset_file_meta_ids_shrink is not None:
            result['DatasetFileMetaIds'] = self.dataset_file_meta_ids_shrink

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

        if self.query_content_type_include_any_shrink is not None:
            result['QueryContentTypeIncludeAny'] = self.query_content_type_include_any_shrink

        if self.query_expression is not None:
            result['QueryExpression'] = self.query_expression

        if self.query_file_dir is not None:
            result['QueryFileDir'] = self.query_file_dir

        if self.query_file_name is not None:
            result['QueryFileName'] = self.query_file_name

        if self.query_file_type_include_any_shrink is not None:
            result['QueryFileTypeIncludeAny'] = self.query_file_type_include_any_shrink

        if self.query_image is not None:
            result['QueryImage'] = self.query_image

        if self.query_tags_exclude_shrink is not None:
            result['QueryTagsExclude'] = self.query_tags_exclude_shrink

        if self.query_tags_include_all_shrink is not None:
            result['QueryTagsIncludeAll'] = self.query_tags_include_all_shrink

        if self.query_tags_include_any_shrink is not None:
            result['QueryTagsIncludeAny'] = self.query_tags_include_any_shrink

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
        if m.get('DatasetFileMetaIds') is not None:
            self.dataset_file_meta_ids_shrink = m.get('DatasetFileMetaIds')

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
            self.query_content_type_include_any_shrink = m.get('QueryContentTypeIncludeAny')

        if m.get('QueryExpression') is not None:
            self.query_expression = m.get('QueryExpression')

        if m.get('QueryFileDir') is not None:
            self.query_file_dir = m.get('QueryFileDir')

        if m.get('QueryFileName') is not None:
            self.query_file_name = m.get('QueryFileName')

        if m.get('QueryFileTypeIncludeAny') is not None:
            self.query_file_type_include_any_shrink = m.get('QueryFileTypeIncludeAny')

        if m.get('QueryImage') is not None:
            self.query_image = m.get('QueryImage')

        if m.get('QueryTagsExclude') is not None:
            self.query_tags_exclude_shrink = m.get('QueryTagsExclude')

        if m.get('QueryTagsIncludeAll') is not None:
            self.query_tags_include_all_shrink = m.get('QueryTagsIncludeAll')

        if m.get('QueryTagsIncludeAny') is not None:
            self.query_tags_include_any_shrink = m.get('QueryTagsIncludeAny')

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

