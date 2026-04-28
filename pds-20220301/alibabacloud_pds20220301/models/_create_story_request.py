# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CreateStoryRequest(DaraModel):
    def __init__(
        self,
        address: main_models.Address = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        max_image_count: int = None,
        min_image_count: int = None,
        story_end_time: str = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        self.address = address
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        self.max_image_count = max_image_count
        self.min_image_count = min_image_count
        self.story_end_time = story_end_time
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        if self.address:
            self.address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address.to_map()

        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.max_image_count is not None:
            result['max_image_count'] = self.max_image_count

        if self.min_image_count is not None:
            result['min_image_count'] = self.min_image_count

        if self.story_end_time is not None:
            result['story_end_time'] = self.story_end_time

        if self.story_id is not None:
            result['story_id'] = self.story_id

        if self.story_name is not None:
            result['story_name'] = self.story_name

        if self.story_start_time is not None:
            result['story_start_time'] = self.story_start_time

        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type

        if self.story_type is not None:
            result['story_type'] = self.story_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            temp_model = main_models.Address()
            self.address = temp_model.from_map(m.get('address'))

        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('max_image_count') is not None:
            self.max_image_count = m.get('max_image_count')

        if m.get('min_image_count') is not None:
            self.min_image_count = m.get('min_image_count')

        if m.get('story_end_time') is not None:
            self.story_end_time = m.get('story_end_time')

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')

        if m.get('story_start_time') is not None:
            self.story_start_time = m.get('story_start_time')

        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')

        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')

        return self

