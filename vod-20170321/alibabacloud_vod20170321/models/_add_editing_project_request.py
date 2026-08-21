# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddEditingProjectRequest(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        description: str = None,
        division: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        timeline: str = None,
        title: str = None,
    ):
        # The thumbnail of the online editing project. If this parameter is left empty and the video track on the timeline already contains materials, the thumbnail of the first material on the timeline is used by default.
        self.cover_url = cover_url
        # The description of the online editing project.
        self.description = description
        # The service region.
        self.division = division
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The timeline of the online editing project. JSON format. For the specific structure definition, see [Timeline](https://help.aliyun.com/document_detail/52839.html).
        # 
        # If this parameter is left empty, an empty timeline is created and the total duration of the online editing project is 0.
        self.timeline = timeline
        # The title of the online editing project.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.division is not None:
            result['Division'] = self.division

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Division') is not None:
            self.division = m.get('Division')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

