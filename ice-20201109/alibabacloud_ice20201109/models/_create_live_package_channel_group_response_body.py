# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateLivePackageChannelGroupResponseBody(DaraModel):
    def __init__(
        self,
        live_package_channel_group: main_models.CreateLivePackageChannelGroupResponseBodyLivePackageChannelGroup = None,
        request_id: str = None,
    ):
        # The information about the channel group.
        self.live_package_channel_group = live_package_channel_group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_package_channel_group:
            self.live_package_channel_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_package_channel_group is not None:
            result['LivePackageChannelGroup'] = self.live_package_channel_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivePackageChannelGroup') is not None:
            temp_model = main_models.CreateLivePackageChannelGroupResponseBodyLivePackageChannelGroup()
            self.live_package_channel_group = temp_model.from_map(m.get('LivePackageChannelGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateLivePackageChannelGroupResponseBodyLivePackageChannelGroup(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_name: str = None,
        last_modified: str = None,
        origin_domain: str = None,
    ):
        # The time when the channel group was created. It is in the yyyy-MM-ddTHH:mm:ssZ format and displayed in UTC.
        self.create_time = create_time
        # The channel group description.
        self.description = description
        # The channel group name.
        self.group_name = group_name
        # The time when the channel group was last modified. It is in the yyyy-MM-ddTHH:mm:ssZ format and displayed in UTC.
        self.last_modified = last_modified
        # The origin domain.
        self.origin_domain = origin_domain

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

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.origin_domain is not None:
            result['OriginDomain'] = self.origin_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('OriginDomain') is not None:
            self.origin_domain = m.get('OriginDomain')

        return self

