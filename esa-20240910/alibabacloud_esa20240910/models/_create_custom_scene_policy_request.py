# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomScenePolicyRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        objects: str = None,
        site_ids: str = None,
        start_time: str = None,
        template: str = None,
    ):
        # The end time of the policy.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The policy name.
        # 
        # This parameter is required.
        self.name = name
        # The IDs of the websites to be associated. Separate multiple IDs with commas (,).
        # 
        # > **[Deprecated]** This parameter is deprecated. Use the SiteIds parameter instead. If the SiteIds parameter is specified, the value of the SiteIds parameter takes precedence and the value of the Objects parameter does not take effect. To avoid ambiguity in update operations, you must specify at least one of the SiteIds and Objects parameters.
        self.objects = objects
        # The IDs of the websites to be associated. Separate multiple IDs with commas (,).
        self.site_ids = site_ids
        # The start time of the policy.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the template. Valid values:
        # - **promotion**: Important Activity.
        # 
        # This parameter is required.
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

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

