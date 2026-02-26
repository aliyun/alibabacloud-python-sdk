# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStoryShrinkRequest(DaraModel):
    def __init__(
        self,
        address_shrink: str = None,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notification_shrink: str = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # The address of the story. IMM filters candidate photos to generate a story based on the value of this parameter. This parameter takes effect only if you set StoryType to TravelMemory.
        # 
        # >  If the caller of the operation is located in Hong Kong (China), Macao (China), Taiwan (China), or another region outside the Chinese mainland, the system cannot convert the GPS information in the Chinese mainland into the textual address version.
        self.address_shrink = address_shrink
        # The custom ID. A custom ID of a generated story may differ from the value of ObjectID and can be utilized for subsequent retrieval and sorting of stories.
        self.custom_id = custom_id
        # The custom labels. Labels specify the custom information of the story. This enables retrieval based on your business requirements.
        self.custom_labels_shrink = custom_labels_shrink
        # The name of the dataset. For information about how to obtain the name of a dataset, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of photo files in the story. The actual number of photo files ranges from the value of MinFileCount to the value of MaxFileCount. The value of this parameter must be an integer greater than the value of MinFileCount. To provide the desired effect, the algorithm limits the maximum number of photo files to 1,500. If you set MaxFileCount to a value greater than 1,500, this parameter does not take effect.
        self.max_file_count = max_file_count
        # The minimum number of photo files in the story. The actual number of photo files ranges from the value of MinFileCount to the value of MaxFileCount. The value of this parameter must be an integer greater than 1. If the actual number of candidate photos is less than the value of this parameter, a null story is returned.
        self.min_file_count = min_file_count
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The topic name of the asynchronous reverse notification.
        self.notify_topic_name = notify_topic_name
        # The ID of the story. This parameter is optional. If you leave this parameter empty, IMM assigns a unique identifier to the story. You can query and update a story based on its ID. You can also manually create an ID for a story. After you create an ID for a story, you must specify this parameter to pass the ID into the system. This way, IMM can record the ID as the unique identifier of the story. If you pass an existing ID into the system, IMM updates the story that corresponds to the ID.
        self.object_id = object_id
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The end time of the photo collection for which you want to create the story. StoryStartTime and StoryEndTime form a time interval based on which IMM filters candidate photos to generate a story. The value must be a string in the RFC3339 format.
        self.story_end_time = story_end_time
        # The name of the story.
        self.story_name = story_name
        # The start time of the photo collection for which you want to create the story. StoryStartTime and StoryEndTime form a time interval based on which IMM filters candidate photos to generate a story. The value must be a string in the RFC3339 format.
        self.story_start_time = story_start_time
        # The subtype of the story. For information about valid subtypes, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        self.story_sub_type = story_sub_type
        # The type of the story. For information about valid types, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        # 
        # This parameter is required.
        self.story_type = story_type
        # The tags. You can specify this parameter in one of the following scenarios:
        # 
        # *   Specify tags as custom data, which is returned in messages provided by Simple Message Queue.
        # *   Search for tasks by tag.
        # *   Specify tags as variables in destination URIs.
        self.tags_shrink = tags_shrink
        # The custom information, which is returned as asynchronous notifications to facilitate notification management in your system. The maximum information length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count

        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

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

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')

        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

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
            self.tags_shrink = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

