# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateStoryRequest(DaraModel):
    def __init__(
        self,
        address: main_models.AddressForStory = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notification: main_models.Notification = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        # The address information for the story. IMM filters photos whose shooting locations match the specified address to generate the story. This parameter takes effect only when StoryType is set to TravelMemory.
        # 
        # > Due to regulatory requirements, parsing GPS information into addresses is not supported in Hong Kong (China), Macao (China), Taiwan (China), or regions outside of mainland China.
        self.address = address
        # A custom identifier for the story. This ID can be different from ObjectId. You can use this ID to retrieve or sort stories.
        self.custom_id = custom_id
        # The custom labels. These labels contain custom information about the story and can be used for retrieval.
        self.custom_labels = custom_labels
        # The name of the dataset. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of photos in the generated story. The actual number of photos is between the values of MinFileCount and MaxFileCount. The value must be an integer greater than the value of MinFileCount. To ensure the quality of the generated story, the internal algorithm limits the maximum number of photos to 1,500. If you set MaxFileCount to a value greater than 1,500, the setting does not take effect.
        self.max_file_count = max_file_count
        # The minimum number of photos in the generated story. The actual number of photos is between the values of MinFileCount and MaxFileCount. The value must be an integer greater than 1. If the number of available candidate photos is less than this value, an empty story is returned.
        self.min_file_count = min_file_count
        # The notification configuration. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the topic for asynchronous notifications.
        self.notify_topic_name = notify_topic_name
        # The ID for the story object. This parameter is optional. If you do not specify an ID, IMM generates one. You can use the story ID to query or update the story. If you specify an ID that already exists, the corresponding story is updated.
        self.object_id = object_id
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The end time of the photo collection for the story. This parameter and StoryStartTime define a time range. IMM filters candidate photos within this time range to generate the story. The value must be a string in the RFC 3339 format.
        self.story_end_time = story_end_time
        # The name of the story.
        self.story_name = story_name
        # The start time of the photo collection for the story. This parameter and StoryEndTime define a time range. IMM filters candidate photos within this time range to generate the story. The value must be a string in the RFC 3339 format.
        self.story_start_time = story_start_time
        # The subtype of the story to generate. For more information about story subtypes and their valid values, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        self.story_sub_type = story_sub_type
        # The type of the story to generate. For more information about story types and their valid values, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        # 
        # This parameter is required.
        self.story_type = story_type
        # This parameter provides a tagging mechanism that can be used in the following scenarios:
        # 
        # - Set custom data that is returned in MNS messages.
        # 
        # - Use as a search condition to search for tasks.
        # 
        # - Use as a variable in TargetURI.
        self.tags = tags
        # The custom information that is returned in an asynchronous notification message. You can use this information to associate the notification message with your services. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.address:
            self.address.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address.to_map()

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count

        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time

        if self.story_name is not None:
            result['StoryName'] = self.story_name

        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time

        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type

        if self.story_type is not None:
            result['StoryType'] = self.story_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = main_models.AddressForStory()
            self.address = temp_model.from_map(m.get('Address'))

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')

        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')

        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')

        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

