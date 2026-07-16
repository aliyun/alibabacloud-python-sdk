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
        # A list of metadata IDs to query.
        self.dataset_file_meta_ids_shrink = dataset_file_meta_ids_shrink
        # The version name of the dataset.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The start time for the query that filters files by update time. The time must be a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # The start time for querying tags by their last update time. The time must be in UTC and in the ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        # The end of the time range for a query that filters tags by their last update time. The time is a UTC timestamp in ISO 8601 format.
        self.max_results = max_results
        # The pagination token.
        # 
        # > If you do not specify this parameter, the first page of results is returned. If a value is returned for this parameter, more results are available. To get the next page, use the returned token in your next request. Repeat this process until no token is returned, which indicates that all results have been retrieved.
        self.next_token = next_token
        # The sort order for the specified field in a paginated query. Use this parameter with \\`SortBy\\`. The default value is \\`DESC\\`. Valid values:
        # 
        # - ASC: Ascending.
        # 
        # - DESC: Descending.
        self.order = order
        # The number of entries per page. If you also specify \\`MaxResults\\`, the value of \\`MaxResults\\` takes precedence.
        # 
        # > This parameter is deprecated. Use \\`NextToken\\` and \\`MaxResults\\` for paginated queries.
        self.page_size = page_size
        # A search condition to include any of the specified content types. The search results must match at least one of these types. You can specify multiple content types. If this parameter is empty, this condition is not applied. Use commas to separate multiple types in the array.
        self.query_content_type_include_any_shrink = query_content_type_include_any_shrink
        # The maximum number of results to return per page. Valid values: 1 to 100. Default value: 10.
        self.query_expression = query_expression
        # The name of the file to retrieve. This parameter supports fuzzy search.
        self.query_file_dir = query_file_dir
        # The tags to exclude from the query results. If you do not specify any tags, this filter is not applied.
        # 
        # > This parameter is valid only when QueryType is set to TAG or MIX.
        self.query_file_name = query_file_name
        # The search keyword for the file directory. Fuzzy search is supported.
        self.query_file_type_include_any_shrink = query_file_type_include_any_shrink
        # The image information to use for an image-based search.
        # 
        # - Specify the public URL of an image in an OSS bucket. The format is \\`oss\\://{bucket_name}/{object_path}\\`. \\`bucket_name\\` is the name of the bucket, and \\`object_path\\` is the path of the file in the bucket.
        # 
        # > This parameter is valid only when \\`QueryType\\` is set to \\`VECTOR\\` or \\`MIX\\`.
        self.query_image = query_image
        # A comma-separated list of tags. The query returns files that match at least one of the specified tags. If you do not specify this parameter, this filter is ignored.
        # 
        # > This parameter is valid only when QueryType is set to TAG or MIX.
        self.query_tags_exclude_shrink = query_tags_exclude_shrink
        # The metadata IDs to query.
        self.query_tags_include_all_shrink = query_tags_include_all_shrink
        # A condition that retrieves items that have all of the specified tags. The tags are specified as a comma-separated array. This condition is not applied if the parameter is empty.
        # 
        # > This parameter takes effect only when QueryType is set to TAG or MIX. If QueryType is set to TAG, the value of QueryText is also added to this condition.
        self.query_tags_include_any_shrink = query_tags_include_any_shrink
        # The text to search for.
        self.query_text = query_text
        # The search type. Valid values:
        # 
        # - MIX: Mixed search. This is the default value.
        # 
        # - TAG: Searches by tag only.
        # 
        # - VECTOR: Searches by vector only.
        self.query_type = query_type
        # The status of the metadata to query.
        # 
        # - ACTIVE: Returns metadata for active files. This is the default value.
        # 
        # - ALL: Returns metadata for all files.
        # 
        # - DELETED: Returns metadata for logically deleted files.
        self.query_video = query_video
        # The similarity score threshold. Only results with a score greater than this threshold are returned.
        # 
        # > This parameter is valid only when \\`QueryType\\` is set to \\`VECTOR\\` or \\`MIX\\`.
        self.score_threshold = score_threshold
        # The field to sort by for paginated queries. If you do not specify this parameter, results are sorted by relevance from high to low. Other valid values are as follows:
        # 
        # - FileCreateTime: Sort by file creation time.
        # 
        # - FileUpdateTime: Sort by file last modified time.
        self.sort_by = sort_by
        # The end of the time range for a query based on file update time. The value is a UTC timestamp in ISO 8601 format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # The file content types. The query returns files that match any of the specified types. You can specify multiple types and separate them with commas. If this parameter is empty, this filter is ignored.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        # A query statement, also known as a Domain-Specific Language (DSL) query, lets you express complex retrieval conditions. It supports grouping, Boolean logic (AND/OR/NOT), range comparisons (>, >=, <, <=), property existence (HAS/NOT HAS), tokenized matches (:), and exact matches (=). Use DSL for advanced retrieval scenarios.
        # >Notice: To avoid conflicts, do not use this query statement with other query parameters.
        self.status = status
        # The mode for generating image thumbnails. Thumbnails are supported only for files in OSS.
        # 
        # - Proportional scaling: \\`p_{percentage}\\`. The \\`percentage\\` parameter specifies the scaling ratio. Valid values: 1 to 100. For example, \\`p_50\\` scales the image to 50% of its original size.
        # 
        # - Fixed width, adaptive height: \\`w_{width}\\`. The \\`width\\` parameter specifies the image width. Valid values: 1 to 16,384. For example, \\`w_200\\` sets the image width to 200 pixels and scales the height adaptively.
        # 
        # - Fixed height, adaptive width: \\`h_{height}\\`. The \\`height\\` parameter specifies the image height. Valid values: 1 to 16,384. For example, \\`h_100\\` sets the image height to 100 pixels and scales the width adaptively.
        # 
        # - Fixed width and height with padding: \\`m_pad,w_{width},h_{height},color_{RGB}\\`. The \\`m_pad\\` parameter scales the image to the maximum size that fits within a rectangle of the specified width and height. The \\`RGB\\` parameter specifies the color for the centered padding in the empty areas. If you do not specify this parameter, the empty areas are filled with white by default. The \\`width\\` and \\`height\\` parameters specify the image width and height. The values for both \\`width\\` and \\`height\\` must be between 1 and 16,384.
        # 
        # - Fixed width and height with center crop: \\`m_fill,w_{width},h_{height}\\`. The \\`m_fill\\` parameter proportionally scales the image to the minimum size that covers the specified width and height, and then crops the excess from the center. The \\`width\\` and \\`height\\` parameters specify the image width and height. The values for both \\`width\\` and \\`height\\` must be between 1 and 16,384. For example, \\`m_fill,w_100,h_100\\` scales and crops the image to 100 × 100 pixels from the center.
        # 
        # - Forced width and height scaling: \\`m_fixed,w_{width},h_{height}\\`. The \\`width\\` and \\`height\\` parameters specify the image width and height. The values for both \\`width\\` and \\`height\\` must be between 1 and 16,384. For example, \\`m_fixed,w_100,h_100\\` forces the image to be scaled to 100 × 100 pixels.
        self.thumbnail_mode = thumbnail_mode
        # The maximum number of search results to return.
        # 
        # > This parameter is valid only when \\`QueryType\\` is set to \\`VECTOR\\` or \\`MIX\\`.
        self.top_k = top_k
        # The ID of the workspace where the dataset is located. For more information, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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

