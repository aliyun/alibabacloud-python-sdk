# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class QueryStoriesRequest(DaraModel):
    def __init__(
        self,
        create_time_range: main_models.TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        story_end_time_range: main_models.TimeRange = None,
        story_name: str = None,
        story_start_time_range: main_models.TimeRange = None,
        story_sub_type: str = None,
        story_type: str = None,
        with_empty_stories: bool = None,
    ):
        # The creation time range of the story.
        self.create_time_range = create_time_range
        # The custom label key-value pairs. Only stories that match the specified label pairs are returned.
        self.custom_labels = custom_labels
        # The name of the dataset. For more information about how to obtain the name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The IDs of the figure clusters.
        self.figure_cluster_ids = figure_cluster_ids
        # The maximum number of entries to return in a single call. Valid values: 1 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token. If this parameter is left empty, the query starts from the beginning. To query the next page, set this parameter to the NextToken value returned in the previous call.
        self.next_token = next_token
        # The ID of the story object.
        self.object_id = object_id
        # The sorting order. Valid values:
        # 
        # - asc: Ascending order.
        # 
        # - desc: Descending order.
        self.order = order
        # The name of the project. For more information about how to obtain the name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The field used for sorting. Valid values:
        # 
        # - CreateTime: Sorts by story creation time.
        # 
        # - StoryName: Sorts by story name.
        # 
        # - StoryStartTime: Sorts by story start time.
        # 
        # - StoryEndTime: Sorts by story end time.
        self.sort = sort
        # The end time range of the photos or videos in the story.
        self.story_end_time_range = story_end_time_range
        # The name of the story.
        self.story_name = story_name
        # The start time range of the photos or videos in the story.
        self.story_start_time_range = story_start_time_range
        # The subtype of the story. For valid values, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        self.story_sub_type = story_sub_type
        # The type of the story. For valid values, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        self.story_type = story_type
        # Specifies whether to return empty stories. Valid values:
        # 
        # - true: Returns empty stories. This is the default value.
        # 
        # - false: Does not return empty stories.
        self.with_empty_stories = with_empty_stories

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.story_end_time_range is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range.to_map()

        if self.story_name is not None:
            result['StoryName'] = self.story_name

        if self.story_start_time_range is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range.to_map()

        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type

        if self.story_type is not None:
            result['StoryType'] = self.story_type

        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.create_time_range = temp_model.from_map(m.get('CreateTimeRange'))

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StoryEndTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.story_end_time_range = temp_model.from_map(m.get('StoryEndTimeRange'))

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        if m.get('StoryStartTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.story_start_time_range = temp_model.from_map(m.get('StoryStartTimeRange'))

        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')

        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')

        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')

        return self

