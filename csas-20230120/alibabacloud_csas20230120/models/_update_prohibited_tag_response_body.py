# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateProhibitedTagResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tag: main_models.UpdateProhibitedTagResponseBodyTag = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The prohibited software tag.
        self.tag = tag

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag is not None:
            result['Tag'] = self.tag.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tag') is not None:
            temp_model = main_models.UpdateProhibitedTagResponseBodyTag()
            self.tag = temp_model.from_map(m.get('Tag'))

        return self

class UpdateProhibitedTagResponseBodyTag(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        # The creation time of the prohibited software tag, in the yyyy-MM-dd HH:mm:ss format. The time is displayed in UTC+8.
        self.create_time = create_time
        # The description of the prohibited software tag.
        self.description = description
        # The name of the prohibited software tag.
        self.name = name
        # The ID of the prohibited software tag.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

