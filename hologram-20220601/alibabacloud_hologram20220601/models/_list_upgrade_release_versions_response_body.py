# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListUpgradeReleaseVersionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUpgradeReleaseVersionsResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUpgradeReleaseVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUpgradeReleaseVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        release_notes_url: str = None,
        type: str = None,
        upgrade_strategy: List[str] = None,
        version: str = None,
    ):
        self.release_notes_url = release_notes_url
        self.type = type
        self.upgrade_strategy = upgrade_strategy
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_notes_url is not None:
            result['ReleaseNotesUrl'] = self.release_notes_url

        if self.type is not None:
            result['Type'] = self.type

        if self.upgrade_strategy is not None:
            result['UpgradeStrategy'] = self.upgrade_strategy

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseNotesUrl') is not None:
            self.release_notes_url = m.get('ReleaseNotesUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpgradeStrategy') is not None:
            self.upgrade_strategy = m.get('UpgradeStrategy')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

