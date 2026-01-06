# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListTeamsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        teams: List[main_models.ListTeamsResponseBodyTeams] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.teams = teams
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.teams:
            for v1 in self.teams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['teams'] = []
        if self.teams is not None:
            for k1 in self.teams:
                result['teams'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.teams = []
        if m.get('teams') is not None:
            for k1 in m.get('teams'):
                temp_model = main_models.ListTeamsResponseBodyTeams()
                self.teams.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListTeamsResponseBodyTeams(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        cover: str = None,
        create_time: str = None,
        creator_id: str = None,
        description: str = None,
        icon: main_models.ListTeamsResponseBodyTeamsIcon = None,
        modified_time: str = None,
        modifier_id: str = None,
        name: str = None,
        team_id: str = None,
    ):
        self.corp_id = corp_id
        self.cover = cover
        self.create_time = create_time
        self.creator_id = creator_id
        self.description = description
        self.icon = icon
        self.modified_time = modified_time
        self.modifier_id = modifier_id
        self.name = name
        self.team_id = team_id

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.cover is not None:
            result['Cover'] = self.cover

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon.to_map()

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.team_id is not None:
            result['TeamId'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('Cover') is not None:
            self.cover = m.get('Cover')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            temp_model = main_models.ListTeamsResponseBodyTeamsIcon()
            self.icon = temp_model.from_map(m.get('Icon'))

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TeamId') is not None:
            self.team_id = m.get('TeamId')

        return self

class ListTeamsResponseBodyTeamsIcon(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

