# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListInstancePatchesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patches: List[main_models.ListInstancePatchesResponseBodyPatches] = None,
        request_id: str = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The information about the patch.
        self.patches = patches
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patches:
            for v1 in self.patches:
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

        result['Patches'] = []
        if self.patches is not None:
            for k1 in self.patches:
                result['Patches'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.patches = []
        if m.get('Patches') is not None:
            for k1 in m.get('Patches'):
                temp_model = main_models.ListInstancePatchesResponseBodyPatches()
                self.patches.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancePatchesResponseBodyPatches(DaraModel):
    def __init__(
        self,
        classification: str = None,
        installed_time: str = None,
        kbid: str = None,
        severity: str = None,
        status: str = None,
        title: str = None,
    ):
        # The classification of the patch.
        self.classification = classification
        # The time when the patch was installed.
        self.installed_time = installed_time
        # The Id of KBId.
        self.kbid = kbid
        # The level of the severity.
        self.severity = severity
        # The status of the installation.
        self.status = status
        # The name of the patch.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classification is not None:
            result['Classification'] = self.classification

        if self.installed_time is not None:
            result['InstalledTime'] = self.installed_time

        if self.kbid is not None:
            result['KBId'] = self.kbid

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('InstalledTime') is not None:
            self.installed_time = m.get('InstalledTime')

        if m.get('KBId') is not None:
            self.kbid = m.get('KBId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

