# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class InitResourceDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: main_models.InitResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource directory.
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceDirectory') is not None:
            temp_model = main_models.InitResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m.get('ResourceDirectory'))

        return self

class InitResourceDirectoryResponseBodyResourceDirectory(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        # The time when the resource directory was enabled.
        self.create_time = create_time
        # The ID of the enterprise management account.
        self.master_account_id = master_account_id
        # The name of the enterprise management account.
        self.master_account_name = master_account_name
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The ID of the root folder.
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id

        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')

        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')

        return self

