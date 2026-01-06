# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSparkTemplateFileRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        dbcluster_id: str = None,
        id: int = None,
        resource_group_name: str = None,
    ):
        # The template data to be updated.
        # 
        # >  If you do not specify this parameter, the application template is not updated. For information about how to configure a Spark application template, see [Configure a Spark application](https://help.aliyun.com/document_detail/452402.html).
        self.content = content
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The application template ID.
        # 
        # >  You can call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/456205.html) operation to query the application template ID.
        # 
        # This parameter is required.
        self.id = id
        # The name of the job resource group.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.id is not None:
            result['Id'] = self.id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

