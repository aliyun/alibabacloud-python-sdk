# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetSkillDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSkillDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetSkillDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSkillDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        description: str = None,
        download_count: int = None,
        editing_version: str = None,
        enable: bool = None,
        from_: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        online_cnt: int = None,
        owner: str = None,
        reviewing_version: str = None,
        scope: str = None,
        update_time: int = None,
        versions: List[main_models.GetSkillDetailResponseBodyDataVersions] = None,
        workspace_id: str = None,
        writeable: bool = None,
    ):
        # The business tag JSON array string.
        self.biz_tags = biz_tags
        # The description.
        self.description = description
        # The total number of downloads.
        self.download_count = download_count
        # The version currently being edited.
        self.editing_version = editing_version
        # Indicates whether the Skill is enabled.
        self.enable = enable
        # The source tag.
        self.from_ = from_
        # The label mapping.
        self.labels = labels
        # The name.
        self.name = name
        # The number of online versions.
        self.online_cnt = online_cnt
        # The resource owner.
        self.owner = owner
        # The version currently under review.
        self.reviewing_version = reviewing_version
        # The visibility scope.
        self.scope = scope
        # The update time. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The list of all version summaries.
        self.versions = versions
        # The workspace ID.
        self.workspace_id = workspace_id
        # Indicates whether the current user has write permissions.
        self.writeable = writeable

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['bizTags'] = self.biz_tags

        if self.description is not None:
            result['description'] = self.description

        if self.download_count is not None:
            result['downloadCount'] = self.download_count

        if self.editing_version is not None:
            result['editingVersion'] = self.editing_version

        if self.enable is not None:
            result['enable'] = self.enable

        if self.from_ is not None:
            result['from'] = self.from_

        if self.labels is not None:
            result['labels'] = self.labels

        if self.name is not None:
            result['name'] = self.name

        if self.online_cnt is not None:
            result['onlineCnt'] = self.online_cnt

        if self.owner is not None:
            result['owner'] = self.owner

        if self.reviewing_version is not None:
            result['reviewingVersion'] = self.reviewing_version

        if self.scope is not None:
            result['scope'] = self.scope

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.writeable is not None:
            result['writeable'] = self.writeable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTags') is not None:
            self.biz_tags = m.get('bizTags')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadCount') is not None:
            self.download_count = m.get('downloadCount')

        if m.get('editingVersion') is not None:
            self.editing_version = m.get('editingVersion')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('onlineCnt') is not None:
            self.online_cnt = m.get('onlineCnt')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('reviewingVersion') is not None:
            self.reviewing_version = m.get('reviewingVersion')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.GetSkillDetailResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('writeable') is not None:
            self.writeable = m.get('writeable')

        return self

class GetSkillDetailResponseBodyDataVersions(DaraModel):
    def __init__(
        self,
        author: str = None,
        commit_msg: str = None,
        create_time: int = None,
        description: str = None,
        download_count: int = None,
        publish_pipeline_info: str = None,
        status: str = None,
        update_time: int = None,
        version: str = None,
    ):
        # The version author.
        self.author = author
        # The commit message.
        self.commit_msg = commit_msg
        # The creation time. This value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description.
        self.description = description
        # The download count.
        self.download_count = download_count
        # The publish pipeline information.
        self.publish_pipeline_info = publish_pipeline_info
        # The status.
        self.status = status
        # The update time. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['author'] = self.author

        if self.commit_msg is not None:
            result['commitMsg'] = self.commit_msg

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.download_count is not None:
            result['downloadCount'] = self.download_count

        if self.publish_pipeline_info is not None:
            result['publishPipelineInfo'] = self.publish_pipeline_info

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')

        if m.get('commitMsg') is not None:
            self.commit_msg = m.get('commitMsg')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadCount') is not None:
            self.download_count = m.get('downloadCount')

        if m.get('publishPipelineInfo') is not None:
            self.publish_pipeline_info = m.get('publishPipelineInfo')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

