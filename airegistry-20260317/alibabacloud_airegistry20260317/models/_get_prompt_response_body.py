# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetPromptResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPromptResponseBodyData = None,
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
            temp_model = main_models.GetPromptResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPromptResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_tags: List[str] = None,
        description: str = None,
        editing_version: str = None,
        gmt_modified: int = None,
        labels: Dict[str, str] = None,
        latest_version: str = None,
        online_cnt: int = None,
        prompt_key: str = None,
        reviewing_version: str = None,
        schema_version: int = None,
        version_details: List[main_models.GetPromptResponseBodyDataVersionDetails] = None,
        versions: List[str] = None,
    ):
        self.biz_tags = biz_tags
        self.description = description
        self.editing_version = editing_version
        self.gmt_modified = gmt_modified
        self.labels = labels
        self.latest_version = latest_version
        self.online_cnt = online_cnt
        self.prompt_key = prompt_key
        self.reviewing_version = reviewing_version
        self.schema_version = schema_version
        self.version_details = version_details
        self.versions = versions

    def validate(self):
        if self.version_details:
            for v1 in self.version_details:
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

        if self.editing_version is not None:
            result['EditingVersion'] = self.editing_version

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.online_cnt is not None:
            result['OnlineCnt'] = self.online_cnt

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.reviewing_version is not None:
            result['ReviewingVersion'] = self.reviewing_version

        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version

        result['VersionDetails'] = []
        if self.version_details is not None:
            for k1 in self.version_details:
                result['VersionDetails'].append(k1.to_map() if k1 else None)

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags = m.get('BizTags')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditingVersion') is not None:
            self.editing_version = m.get('EditingVersion')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('OnlineCnt') is not None:
            self.online_cnt = m.get('OnlineCnt')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('ReviewingVersion') is not None:
            self.reviewing_version = m.get('ReviewingVersion')

        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')

        self.version_details = []
        if m.get('VersionDetails') is not None:
            for k1 in m.get('VersionDetails'):
                temp_model = main_models.GetPromptResponseBodyDataVersionDetails()
                self.version_details.append(temp_model.from_map(k1))

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

class GetPromptResponseBodyDataVersionDetails(DaraModel):
    def __init__(
        self,
        commit_msg: str = None,
        gmt_modified: int = None,
        prompt_key: str = None,
        src_user: str = None,
        status: str = None,
        version: str = None,
    ):
        self.commit_msg = commit_msg
        self.gmt_modified = gmt_modified
        self.prompt_key = prompt_key
        self.src_user = src_user
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.src_user is not None:
            result['SrcUser'] = self.src_user

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('SrcUser') is not None:
            self.src_user = m.get('SrcUser')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

