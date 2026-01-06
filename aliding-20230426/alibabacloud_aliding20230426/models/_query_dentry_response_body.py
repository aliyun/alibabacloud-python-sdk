# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryDentryResponseBody(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        created_time: int = None,
        creator: main_models.QueryDentryResponseBodyCreator = None,
        dentry_id: str = None,
        dentry_type: str = None,
        dentry_uuid: str = None,
        doc_key: str = None,
        extension: str = None,
        has_children: bool = None,
        link_source_info: main_models.QueryDentryResponseBodyLinkSourceInfo = None,
        name: str = None,
        path: str = None,
        request_id: str = None,
        space: main_models.QueryDentryResponseBodySpace = None,
        space_id: str = None,
        updated_time: int = None,
        updater: main_models.QueryDentryResponseBodyUpdater = None,
        url: str = None,
        visitor_info: main_models.QueryDentryResponseBodyVisitorInfo = None,
    ):
        self.content_type = content_type
        self.created_time = created_time
        self.creator = creator
        self.dentry_id = dentry_id
        self.dentry_type = dentry_type
        self.dentry_uuid = dentry_uuid
        self.doc_key = doc_key
        self.extension = extension
        self.has_children = has_children
        self.link_source_info = link_source_info
        self.name = name
        self.path = path
        # requestId
        self.request_id = request_id
        self.space = space
        self.space_id = space_id
        self.updated_time = updated_time
        self.updater = updater
        self.url = url
        self.visitor_info = visitor_info

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.link_source_info:
            self.link_source_info.validate()
        if self.space:
            self.space.validate()
        if self.updater:
            self.updater.validate()
        if self.visitor_info:
            self.visitor_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.creator is not None:
            result['creator'] = self.creator.to_map()

        if self.dentry_id is not None:
            result['dentryId'] = self.dentry_id

        if self.dentry_type is not None:
            result['dentryType'] = self.dentry_type

        if self.dentry_uuid is not None:
            result['dentryUuid'] = self.dentry_uuid

        if self.doc_key is not None:
            result['docKey'] = self.doc_key

        if self.extension is not None:
            result['extension'] = self.extension

        if self.has_children is not None:
            result['hasChildren'] = self.has_children

        if self.link_source_info is not None:
            result['linkSourceInfo'] = self.link_source_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.space is not None:
            result['space'] = self.space.to_map()

        if self.space_id is not None:
            result['spaceId'] = self.space_id

        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time

        if self.updater is not None:
            result['updater'] = self.updater.to_map()

        if self.url is not None:
            result['url'] = self.url

        if self.visitor_info is not None:
            result['visitorInfo'] = self.visitor_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('creator') is not None:
            temp_model = main_models.QueryDentryResponseBodyCreator()
            self.creator = temp_model.from_map(m.get('creator'))

        if m.get('dentryId') is not None:
            self.dentry_id = m.get('dentryId')

        if m.get('dentryType') is not None:
            self.dentry_type = m.get('dentryType')

        if m.get('dentryUuid') is not None:
            self.dentry_uuid = m.get('dentryUuid')

        if m.get('docKey') is not None:
            self.doc_key = m.get('docKey')

        if m.get('extension') is not None:
            self.extension = m.get('extension')

        if m.get('hasChildren') is not None:
            self.has_children = m.get('hasChildren')

        if m.get('linkSourceInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodyLinkSourceInfo()
            self.link_source_info = temp_model.from_map(m.get('linkSourceInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('space') is not None:
            temp_model = main_models.QueryDentryResponseBodySpace()
            self.space = temp_model.from_map(m.get('space'))

        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')

        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')

        if m.get('updater') is not None:
            temp_model = main_models.QueryDentryResponseBodyUpdater()
            self.updater = temp_model.from_map(m.get('updater'))

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('visitorInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodyVisitorInfo()
            self.visitor_info = temp_model.from_map(m.get('visitorInfo'))

        return self

class QueryDentryResponseBodyVisitorInfo(DaraModel):
    def __init__(
        self,
        dentry_actions: List[str] = None,
        role_code: str = None,
        space_actions: List[str] = None,
    ):
        self.dentry_actions = dentry_actions
        self.role_code = role_code
        self.space_actions = space_actions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_actions is not None:
            result['DentryActions'] = self.dentry_actions

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.space_actions is not None:
            result['SpaceActions'] = self.space_actions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryActions') is not None:
            self.dentry_actions = m.get('DentryActions')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('SpaceActions') is not None:
            self.space_actions = m.get('SpaceActions')

        return self

class QueryDentryResponseBodyUpdater(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDentryResponseBodySpace(DaraModel):
    def __init__(
        self,
        cover: str = None,
        description: str = None,
        hd_icon_vo: main_models.QueryDentryResponseBodySpaceHdIconVO = None,
        icon_vo: main_models.QueryDentryResponseBodySpaceIconVO = None,
        id: str = None,
        name: str = None,
        owner: main_models.QueryDentryResponseBodySpaceOwner = None,
        recent_list: List[main_models.QueryDentryResponseBodySpaceRecentList] = None,
        type: int = None,
        url: str = None,
        visitor_info: main_models.QueryDentryResponseBodySpaceVisitorInfo = None,
    ):
        self.cover = cover
        self.description = description
        self.hd_icon_vo = hd_icon_vo
        self.icon_vo = icon_vo
        self.id = id
        self.name = name
        self.owner = owner
        self.recent_list = recent_list
        self.type = type
        self.url = url
        self.visitor_info = visitor_info

    def validate(self):
        if self.hd_icon_vo:
            self.hd_icon_vo.validate()
        if self.icon_vo:
            self.icon_vo.validate()
        if self.owner:
            self.owner.validate()
        if self.recent_list:
            for v1 in self.recent_list:
                 if v1:
                    v1.validate()
        if self.visitor_info:
            self.visitor_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover is not None:
            result['Cover'] = self.cover

        if self.description is not None:
            result['Description'] = self.description

        if self.hd_icon_vo is not None:
            result['HdIconVO'] = self.hd_icon_vo.to_map()

        if self.icon_vo is not None:
            result['IconVO'] = self.icon_vo.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        result['RecentList'] = []
        if self.recent_list is not None:
            for k1 in self.recent_list:
                result['RecentList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.visitor_info is not None:
            result['VisitorInfo'] = self.visitor_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HdIconVO') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceHdIconVO()
            self.hd_icon_vo = temp_model.from_map(m.get('HdIconVO'))

        if m.get('IconVO') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceIconVO()
            self.icon_vo = temp_model.from_map(m.get('IconVO'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        self.recent_list = []
        if m.get('RecentList') is not None:
            for k1 in m.get('RecentList'):
                temp_model = main_models.QueryDentryResponseBodySpaceRecentList()
                self.recent_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VisitorInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceVisitorInfo()
            self.visitor_info = temp_model.from_map(m.get('VisitorInfo'))

        return self

class QueryDentryResponseBodySpaceVisitorInfo(DaraModel):
    def __init__(
        self,
        dentry_actions: List[str] = None,
        role_code: str = None,
        space_actions: List[str] = None,
    ):
        self.dentry_actions = dentry_actions
        self.role_code = role_code
        self.space_actions = space_actions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_actions is not None:
            result['DentryActions'] = self.dentry_actions

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.space_actions is not None:
            result['SpaceActions'] = self.space_actions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryActions') is not None:
            self.dentry_actions = m.get('DentryActions')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('SpaceActions') is not None:
            self.space_actions = m.get('SpaceActions')

        return self

class QueryDentryResponseBodySpaceRecentList(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        created_time: int = None,
        creator: main_models.QueryDentryResponseBodySpaceRecentListCreator = None,
        dentry_id: str = None,
        dentry_type: str = None,
        dentry_uuid: str = None,
        doc_key: str = None,
        extension: str = None,
        has_children: bool = None,
        link_source_info: main_models.QueryDentryResponseBodySpaceRecentListLinkSourceInfo = None,
        name: str = None,
        path: str = None,
        space: Any = None,
        space_id: str = None,
        statistical_info: main_models.QueryDentryResponseBodySpaceRecentListStatisticalInfo = None,
        updated_time: int = None,
        updater: main_models.QueryDentryResponseBodySpaceRecentListUpdater = None,
        url: str = None,
        visitor_info: main_models.QueryDentryResponseBodySpaceRecentListVisitorInfo = None,
    ):
        self.content_type = content_type
        self.created_time = created_time
        self.creator = creator
        self.dentry_id = dentry_id
        self.dentry_type = dentry_type
        self.dentry_uuid = dentry_uuid
        self.doc_key = doc_key
        self.extension = extension
        self.has_children = has_children
        self.link_source_info = link_source_info
        self.name = name
        self.path = path
        self.space = space
        self.space_id = space_id
        self.statistical_info = statistical_info
        self.updated_time = updated_time
        self.updater = updater
        self.url = url
        self.visitor_info = visitor_info

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.link_source_info:
            self.link_source_info.validate()
        if self.statistical_info:
            self.statistical_info.validate()
        if self.updater:
            self.updater.validate()
        if self.visitor_info:
            self.visitor_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.dentry_type is not None:
            result['DentryType'] = self.dentry_type

        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.doc_key is not None:
            result['DocKey'] = self.doc_key

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.has_children is not None:
            result['HasChildren'] = self.has_children

        if self.link_source_info is not None:
            result['LinkSourceInfo'] = self.link_source_info.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.space is not None:
            result['Space'] = self.space

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.statistical_info is not None:
            result['StatisticalInfo'] = self.statistical_info.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.updater is not None:
            result['Updater'] = self.updater.to_map()

        if self.url is not None:
            result['Url'] = self.url

        if self.visitor_info is not None:
            result['VisitorInfo'] = self.visitor_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Creator') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('DentryType') is not None:
            self.dentry_type = m.get('DentryType')

        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('HasChildren') is not None:
            self.has_children = m.get('HasChildren')

        if m.get('LinkSourceInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListLinkSourceInfo()
            self.link_source_info = temp_model.from_map(m.get('LinkSourceInfo'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Space') is not None:
            self.space = m.get('Space')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('StatisticalInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListStatisticalInfo()
            self.statistical_info = temp_model.from_map(m.get('StatisticalInfo'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Updater') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListUpdater()
            self.updater = temp_model.from_map(m.get('Updater'))

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VisitorInfo') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListVisitorInfo()
            self.visitor_info = temp_model.from_map(m.get('VisitorInfo'))

        return self

class QueryDentryResponseBodySpaceRecentListVisitorInfo(DaraModel):
    def __init__(
        self,
        dentry_actions: List[str] = None,
        role_code: str = None,
        space_actions: List[str] = None,
    ):
        self.dentry_actions = dentry_actions
        self.role_code = role_code
        self.space_actions = space_actions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_actions is not None:
            result['DentryActions'] = self.dentry_actions

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.space_actions is not None:
            result['SpaceActions'] = self.space_actions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryActions') is not None:
            self.dentry_actions = m.get('DentryActions')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('SpaceActions') is not None:
            self.space_actions = m.get('SpaceActions')

        return self

class QueryDentryResponseBodySpaceRecentListUpdater(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDentryResponseBodySpaceRecentListStatisticalInfo(DaraModel):
    def __init__(
        self,
        word_count: int = None,
    ):
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.word_count is not None:
            result['WordCount'] = self.word_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        return self

class QueryDentryResponseBodySpaceRecentListLinkSourceInfo(DaraModel):
    def __init__(
        self,
        extension: str = None,
        icon_url: main_models.QueryDentryResponseBodySpaceRecentListLinkSourceInfoIconUrl = None,
        id: str = None,
        link_type: int = None,
        space_id: str = None,
    ):
        self.extension = extension
        self.icon_url = icon_url
        self.id = id
        self.link_type = link_type
        self.space_id = space_id

    def validate(self):
        if self.icon_url:
            self.icon_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.link_type is not None:
            result['LinkType'] = self.link_type

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('IconUrl') is not None:
            temp_model = main_models.QueryDentryResponseBodySpaceRecentListLinkSourceInfoIconUrl()
            self.icon_url = temp_model.from_map(m.get('IconUrl'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        return self

class QueryDentryResponseBodySpaceRecentListLinkSourceInfoIconUrl(DaraModel):
    def __init__(
        self,
        line: str = None,
        small: str = None,
    ):
        self.line = line
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        if self.small is not None:
            result['Small'] = self.small

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        return self

class QueryDentryResponseBodySpaceRecentListCreator(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDentryResponseBodySpaceOwner(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDentryResponseBodySpaceIconVO(DaraModel):
    def __init__(
        self,
        icon: str = None,
        type: str = None,
    ):
        self.icon = icon
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryDentryResponseBodySpaceHdIconVO(DaraModel):
    def __init__(
        self,
        icon: str = None,
        type: str = None,
    ):
        self.icon = icon
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryDentryResponseBodyLinkSourceInfo(DaraModel):
    def __init__(
        self,
        extension: str = None,
        icon_url: main_models.QueryDentryResponseBodyLinkSourceInfoIconUrl = None,
        id: str = None,
        link_type: int = None,
        space_id: str = None,
    ):
        self.extension = extension
        self.icon_url = icon_url
        self.id = id
        self.link_type = link_type
        self.space_id = space_id

    def validate(self):
        if self.icon_url:
            self.icon_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.link_type is not None:
            result['LinkType'] = self.link_type

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('IconUrl') is not None:
            temp_model = main_models.QueryDentryResponseBodyLinkSourceInfoIconUrl()
            self.icon_url = temp_model.from_map(m.get('IconUrl'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        return self

class QueryDentryResponseBodyLinkSourceInfoIconUrl(DaraModel):
    def __init__(
        self,
        line: str = None,
        small: str = None,
    ):
        self.line = line
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        if self.small is not None:
            result['Small'] = self.small

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        return self

class QueryDentryResponseBodyCreator(DaraModel):
    def __init__(
        self,
        name: str = None,
        user_id: str = None,
    ):
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

