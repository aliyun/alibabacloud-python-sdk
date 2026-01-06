# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        edition: str = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        sharing_config: main_models.UpdateDatasetRequestSharingConfig = None,
    ):
        # The description of the dataset.
        self.description = description
        self.edition = edition
        # The list of role names in the workspace that have read and write permissions on the mounted database. The names starting with PAI are basic role names, and the names starting with role- are custom role names. If the list contains asterisks (\\*), all roles have read and write permissions.
        # 
        # *   If you set the value to ["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"], the account of the specified role is granted the read and write permissions.
        # *   If you set the value to ["\\*"], all accounts are granted the read and write permissions.
        # *   If you set the value to [], only the creator of the dataset has the read and write permissions.
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The dataset name. You can call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to obtain the dataset name.
        self.name = name
        # The extended field, which is a JSON string. When you use the dataset in Deep Learning Containers (DLC), you can set mountPath to specify the default mount path of the dataset.
        self.options = options
        self.sharing_config = sharing_config

    def validate(self):
        if self.sharing_config:
            self.sharing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.mount_access_read_write_role_id_list is not None:
            result['MountAccessReadWriteRoleIdList'] = self.mount_access_read_write_role_id_list

        if self.name is not None:
            result['Name'] = self.name

        if self.options is not None:
            result['Options'] = self.options

        if self.sharing_config is not None:
            result['SharingConfig'] = self.sharing_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('MountAccessReadWriteRoleIdList') is not None:
            self.mount_access_read_write_role_id_list = m.get('MountAccessReadWriteRoleIdList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('SharingConfig') is not None:
            temp_model = main_models.UpdateDatasetRequestSharingConfig()
            self.sharing_config = temp_model.from_map(m.get('SharingConfig'))

        return self

class UpdateDatasetRequestSharingConfig(DaraModel):
    def __init__(
        self,
        shared_to: List[main_models.DatasetShareRelationship] = None,
    ):
        self.shared_to = shared_to

    def validate(self):
        if self.shared_to:
            for v1 in self.shared_to:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SharedTo'] = []
        if self.shared_to is not None:
            for k1 in self.shared_to:
                result['SharedTo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_to = []
        if m.get('SharedTo') is not None:
            for k1 in m.get('SharedTo'):
                temp_model = main_models.DatasetShareRelationship()
                self.shared_to.append(temp_model.from_map(k1))

        return self

