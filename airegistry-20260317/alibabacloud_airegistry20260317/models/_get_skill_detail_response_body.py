# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetSkillDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSkillDetailResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSkillDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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
        namespace_id: str = None,
        online_cnt: int = None,
        owner: str = None,
        reviewing_version: str = None,
        scope: str = None,
        update_time: int = None,
        versions: List[main_models.GetSkillDetailResponseBodyDataVersions] = None,
        writeable: bool = None,
    ):
        self.biz_tags = biz_tags
        self.description = description
        self.download_count = download_count
        self.editing_version = editing_version
        self.enable = enable
        self.from_ = from_
        self.labels = labels
        self.name = name
        self.namespace_id = namespace_id
        self.online_cnt = online_cnt
        self.owner = owner
        self.reviewing_version = reviewing_version
        self.scope = scope
        self.update_time = update_time
        self.versions = versions
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
            result['BizTags'] = self.biz_tags

        if self.description is not None:
            result['Description'] = self.description

        if self.download_count is not None:
            result['DownloadCount'] = self.download_count

        if self.editing_version is not None:
            result['EditingVersion'] = self.editing_version

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.from_ is not None:
            result['From'] = self.from_

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.online_cnt is not None:
            result['OnlineCnt'] = self.online_cnt

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.reviewing_version is not None:
            result['ReviewingVersion'] = self.reviewing_version

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        if self.writeable is not None:
            result['Writeable'] = self.writeable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags = m.get('BizTags')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')

        if m.get('EditingVersion') is not None:
            self.editing_version = m.get('EditingVersion')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OnlineCnt') is not None:
            self.online_cnt = m.get('OnlineCnt')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ReviewingVersion') is not None:
            self.reviewing_version = m.get('ReviewingVersion')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.GetSkillDetailResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k1))

        if m.get('Writeable') is not None:
            self.writeable = m.get('Writeable')

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
        self.author = author
        self.commit_msg = commit_msg
        self.create_time = create_time
        self.description = description
        self.download_count = download_count
        self.publish_pipeline_info = publish_pipeline_info
        self.status = status
        self.update_time = update_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.download_count is not None:
            result['DownloadCount'] = self.download_count

        if self.publish_pipeline_info is not None:
            result['PublishPipelineInfo'] = self.publish_pipeline_info

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')

        if m.get('PublishPipelineInfo') is not None:
            self.publish_pipeline_info = m.get('PublishPipelineInfo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

