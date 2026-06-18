# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCustomScenePolicyResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: List[str] = None,
        policy_id: int = None,
        request_id: str = None,
        site_ids: str = None,
        start_time: str = None,
        template: str = None,
    ):
        # The policy end time.
        # 
        # The time must be in UTC and in ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        self.end_time = end_time
        # The policy name.
        self.name = name
        # A list of associated site IDs.
        # 
        # > This field is deprecated. Read the value from the `SiteIds` field instead.
        self.objects = objects
        # The policy ID.
        self.policy_id = policy_id
        # The request ID.
        self.request_id = request_id
        # The associated site IDs, separated by commas.
        self.site_ids = site_ids
        # The policy start time.
        # 
        # The time must be in UTC and in ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        self.start_time = start_time
        # The template name.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.objects is not None:
            result['Objects'] = self.objects

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Objects') is not None:
            self.objects = m.get('Objects')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

