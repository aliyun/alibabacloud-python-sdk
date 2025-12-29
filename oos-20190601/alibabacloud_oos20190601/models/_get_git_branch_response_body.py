# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class GetGitBranchResponseBody(DaraModel):
    def __init__(
        self,
        commit: main_models.GetGitBranchResponseBodyCommit = None,
        request_id: str = None,
    ):
        self.commit = commit
        self.request_id = request_id

    def validate(self):
        if self.commit:
            self.commit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commit') is not None:
            temp_model = main_models.GetGitBranchResponseBodyCommit()
            self.commit = temp_model.from_map(m.get('Commit'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGitBranchResponseBodyCommit(DaraModel):
    def __init__(
        self,
        message: str = None,
        sha: str = None,
    ):
        # git commit message
        self.message = message
        # git commit hash
        self.sha = sha

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.sha is not None:
            result['Sha'] = self.sha

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Sha') is not None:
            self.sha = m.get('Sha')

        return self

