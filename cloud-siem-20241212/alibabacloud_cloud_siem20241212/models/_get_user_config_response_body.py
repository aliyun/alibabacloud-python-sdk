# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetUserConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserConfigResponseBodyUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.GetUserConfigResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserConfigResponseBodyUser(DaraModel):
    def __init__(
        self,
        ctdr_version: str = None,
        data_storage_version: str = None,
        upgrade_ctdr_version: str = None,
        upgrade_status: str = None,
    ):
        self.ctdr_version = ctdr_version
        self.data_storage_version = data_storage_version
        self.upgrade_ctdr_version = upgrade_ctdr_version
        self.upgrade_status = upgrade_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ctdr_version is not None:
            result['CtdrVersion'] = self.ctdr_version

        if self.data_storage_version is not None:
            result['DataStorageVersion'] = self.data_storage_version

        if self.upgrade_ctdr_version is not None:
            result['UpgradeCtdrVersion'] = self.upgrade_ctdr_version

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CtdrVersion') is not None:
            self.ctdr_version = m.get('CtdrVersion')

        if m.get('DataStorageVersion') is not None:
            self.data_storage_version = m.get('DataStorageVersion')

        if m.get('UpgradeCtdrVersion') is not None:
            self.upgrade_ctdr_version = m.get('UpgradeCtdrVersion')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        return self

