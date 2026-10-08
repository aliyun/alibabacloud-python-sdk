# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertDeployGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group_name: str = None,
        init_package_version_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the instance group. The name can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The version of the initial deployment package associated with the instance group. You can call the ListHistoryDeployVersion operation to query the version. For more information, see [ListHistoryDeployVersion](https://help.aliyun.com/document_detail/149392.html).
        self.init_package_version_id = init_package_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.init_package_version_id is not None:
            result['InitPackageVersionId'] = self.init_package_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InitPackageVersionId') is not None:
            self.init_package_version_id = m.get('InitPackageVersionId')

        return self

