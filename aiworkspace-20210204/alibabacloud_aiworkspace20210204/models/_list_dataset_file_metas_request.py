# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDatasetFileMetasRequest(DaraModel):
    def __init__(
        self,
        dataset_file_meta_ids: List[str] = None,
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
        # The list of metadata IDs to query.
        self.dataset_file_meta_ids = dataset_file_meta_ids
        # The dataset version name.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The end time of the file update time range for the query. Specify the time in the ISO 8601 standard in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # The end time of the tag last update time range for the query. Specify the time in the ISO 8601 standard in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        # The maximum number of results to return per query when NextToken is used. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination cursor.
        # > 
        # > If this parameter is not specified, the first page of data is returned. If this parameter has a return value, it indicates that there is a next page. You can use the returned NextToken as a parameter to request the next page of data until Null is returned, which indicates that all data is retrieved.
        self.next_token = next_token
        # The ascending or descending order for the specified sorting field in a paged query. This parameter is used together with SortBy during paging. Default value: DESC. Valid values:
        # - ASC: Ascending order.
        # - DESC: Descending order.
        self.order = order
        # The number of entries per page. If MaxResults is also specified, MaxResults prevails.
        # > This parameter will soon be offline. We recommend that you use NextToken and MaxResults for paging in paged query operations.
        self.page_size = page_size
        # The search condition for "including any of the following file content types". You can select multiple file content types, and the search results only need to meet one of them. If this parameter is empty, this condition is not applied. Separate multiple file content types with commas.
        self.query_content_type_include_any = query_content_type_include_any
        # The query statement (DSL) is a domain-specific language used to express complex search conditions. It supports grouping, Boolean logic (AND/OR/NOT), range comparison (>, >=, <, <=), property existence (HAS/NOT HAS), token matching (:), and exact matching (=), and is suitable for advanced search scenarios.
        # It is generally used for complex advanced search conditions.
        # <notice>To avoid conflicts, do not mix this query statement with other query parameters.</notice>
        self.query_expression = query_expression
        # The file directory search condition. Fuzzy search is supported.
        self.query_file_dir = query_file_dir
        # The file name search condition. Fuzzy search is supported.
        self.query_file_name = query_file_name
        # The search condition for "including any of the following file types". You can select multiple file types, and the search results only need to meet one of them. If this parameter is empty, this condition is not applied. Separate multiple file types with commas.
        self.query_file_type_include_any = query_file_type_include_any
        # The image information for image-to-image search.
        # * Supports passing an OSS URL that allows public network access for the image. Format: oss://{bucket_name}/{object_path}. bucket_name is the bucket name, and object_path is the path of the file in the bucket.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.query_image = query_image
        # The search condition for "excluding the following tags". You can select multiple tags, and the search results must not contain these tags. If this parameter is empty, this condition is not applied.
        # > This parameter takes effect only when QueryType is set to TAG or MIX.
        self.query_tags_exclude = query_tags_exclude
        # The search condition for "including all of the following tags". You can select multiple tags, and the search results must meet all these tags simultaneously. If this parameter is empty, this condition is not applied. Separate multiple tags with commas.
        # > This parameter takes effect only when QueryType is set to TAG or MIX. When QueryType is set to TAG, QueryText is added to this condition.
        self.query_tags_include_all = query_tags_include_all
        # The search condition for "including any of the following tags". You can select multiple tags, and the search results only need to meet one of them. If this parameter is empty, this condition is not applied. Separate multiple tags with commas.
        # > This parameter takes effect only when QueryType is set to TAG or MIX.
        self.query_tags_include_any = query_tags_include_any
        # The text content to search.
        self.query_text = query_text
        # The retrieve type. Valid values:
        # * MIX: Hybrid retrieve. This is the default value.
        # * TAG: Label-only retrieve.
        # * VECTOR: AISearch-only retrieve.
        self.query_type = query_type
        # The video file information for video search.
        # * Supports passing an OSS URL that allows public network access for the video. Format: oss://{bucket_name}/{object_path}. bucket_name is the bucket name, and object_path is the path of the file in the bucket.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.query_video = query_video
        # The similarity score threshold for filtering. Only results with a score greater than ScoreThreshold are returned.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.score_threshold = score_threshold
        # The sorting field for paged query. If this parameter is not specified, the results are sorted by retrieve relevance in descending order during paging. Valid values:
        # * FileCreateTime: Sort by file creation time.
        # * FileUpdateTime: Sort by file last modification time.
        self.sort_by = sort_by
        # The start time of the file update time range for the query. Specify the time in the ISO 8601 standard in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # The start time of the tag last update time range for the query. Specify the time in the ISO 8601 standard in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        # The metadata status to query. Valid values:
        # * ACTIVE: Query only undeleted data. This is the default value.
        # * ALL: Query all data.
        # * DELETED: Query only logically deleted data.
        self.status = status
        # The thumbnail mode for images. Currently, only OSS files support thumbnails. Valid values:
        # - Proportional scaling: p_{percentage}. percentage indicates the expected scaling ratio. Valid values: [1, 100]. Example: p_50 indicates that the thumbnail size is 50% of the original file size.
        # - Fixed width and adaptive height: w_{width}. width indicates the expected image width. Valid values: [1, 16384]. Example: w_200 indicates that the image width is fixed at 200 pixels and the height is adaptively scaled.
        # - Fixed height and adaptive width: h_{height}. height indicates the expected image height. Valid values: [1, 16384]. Example: h_100 indicates that the image height is fixed at 100 pixels and the width is adaptively scaled.
        # - Fixed width and height with padding: m_pad,w_{width},h_{height},color_{RGB}. m_pad indicates that the image is scaled to the maximum size within the specified w and h rectangle. RGB specifies the color used to fill the blank space in the center. If this parameter is not specified, white is used by default. width indicates the expected image width, and height indicates the expected image height. Valid values of width and height: [1, 16384]. Example:
        # - Fixed width and height with center cropping: m_fill,w_{width},h_{height}. m_fill indicates that the image is proportionally scaled to the minimum size that extends beyond the specified w and h rectangle, and the excess part is center-cropped. width indicates the expected image width, and height indicates the expected image height. Valid values of width and height: [1, 16384]. Example: m_fill,w_100,h_100 indicates that the image width and height are both fixed at 100 pixels for center cropping and scaling.
        # - Forced width and height scaling: m_fixed,w_{width},h_{height}. width indicates the expected image width, and height indicates the expected image height. Valid values of width and height: [1, 16384]. Example: m_fixed,w_100,h_100 indicates that the image width and height are both fixed at 100 pixels for forced scaling.
        self.thumbnail_mode = thumbnail_mode
        # The number of search results to return. A maximum of TopK search results are returned.
        # > This parameter takes effect only when QueryType is set to VECTOR or MIX.
        self.top_k = top_k
        # The ID of the workspace to which the dataset belongs. For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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
        if self.dataset_file_meta_ids is not None:
            result['DatasetFileMetaIds'] = self.dataset_file_meta_ids

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
        if m.get('DatasetFileMetaIds') is not None:
            self.dataset_file_meta_ids = m.get('DatasetFileMetaIds')

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

