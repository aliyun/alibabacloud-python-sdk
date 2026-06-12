# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListSkillFilesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        skill_files: List[main_models.ListSkillFilesResponseBodySkillFiles] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token to retrieve the next page of results. This token is returned only when more results are available.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The Skill files.
        self.skill_files = skill_files
        # The total number of entries that match the query.
        self.total_count = total_count

    def validate(self):
        if self.skill_files:
            for v1 in self.skill_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillFiles'] = []
        if self.skill_files is not None:
            for k1 in self.skill_files:
                result['SkillFiles'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_files = []
        if m.get('SkillFiles') is not None:
            for k1 in m.get('SkillFiles'):
                temp_model = main_models.ListSkillFilesResponseBodySkillFiles()
                self.skill_files.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillFilesResponseBodySkillFiles(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        signed_url: str = None,
    ):
        # The relative path of the file within the Skill.
        self.file_path = file_path
        # The pre-signed URL for accessing the file in OSS.
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')

        return self

