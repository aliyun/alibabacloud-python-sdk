# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSparkAppRequest(DaraModel):
    def __init__(
        self,
        agent_source: str = None,
        agent_version: str = None,
        app_name: str = None,
        app_type: str = None,
        dbcluster_id: str = None,
        data: str = None,
        resource_group_name: str = None,
        template_file_id: int = None,
    ):
        # The type of the client. The value can be up to 64 characters in length.
        self.agent_source = agent_source
        # The version of the client. The value can be up to 64 characters in length.
        self.agent_version = agent_version
        # The name of the application. The value can be up to 64 characters in length.
        self.app_name = app_name
        # The type of the application. Valid values:
        # 
        # *   **SQL**
        # *   **STREAMING**
        # *   **BATCH** (default)
        self.app_type = app_type
        # The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The data of the application template.
        # 
        # > For information about the application template configuration, see [Spark application configuration guide](https://help.aliyun.com/document_detail/452402.html).
        # 
        # This parameter is required.
        self.data = data
        # The name of the job resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/612410.html) operation to query the name of a resource group within a cluster.
        # 
        # This parameter is required.
        self.resource_group_name = resource_group_name
        # The ID of the application template.
        # 
        # > You can call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/456205.html) operation to query the application template ID.
        self.template_file_id = template_file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_source is not None:
            result['AgentSource'] = self.agent_source

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data is not None:
            result['Data'] = self.data

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.template_file_id is not None:
            result['TemplateFileId'] = self.template_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSource') is not None:
            self.agent_source = m.get('AgentSource')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('TemplateFileId') is not None:
            self.template_file_id = m.get('TemplateFileId')

        return self

