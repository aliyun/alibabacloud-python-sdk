# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSparkTemplateRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        dbcluster_id: str = None,
        name: str = None,
        parent_id: int = None,
        type: str = None,
    ):
        # The templatetype of the application. Valid values:
        # - **SQL**: SQL application
        # - **STREAMING**: streaming application
        # - **BATCH**: batch application
        # 
        # > You do not need to configure this parameter when the application template type is folder.
        self.app_type = app_type
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the application template. The name can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the folder to which the application template belongs.
        # > Call the [GetSparkTemplateFolderTree](https://help.aliyun.com/document_detail/456218.html) operation to query the folder ID.
        # 
        # This parameter is required.
        self.parent_id = parent_id
        # The templatetype of the application template. Valid values:
        # - **folder**: folder
        # - **file**: application
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

