# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventLevelCountRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        container_ids: str = None,
        from_: str = None,
        multi_account_action_type: int = None,
        resource_directory_account_id: int = None,
        target_type: str = None,
    ):
        # The ID of the container cluster that you want to query.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The container search field. Valid values:
        # 
        # - **instanceId**: instance ID
        # - **appName**: application name
        # - **clusterId**: cluster ID
        # - **regionId**: region
        # - **nodeName**: node name
        # - **namespace**: namespace
        # - **clusterName**: cluster name
        # - **image**: image name
        # - **imageRepoName**: image repository name
        # - **imageRepoNamespace**: image repository namespace
        # - **imageRepoTag**: image tag
        # - **imageDigest**: image digest
        self.container_field_name = container_field_name
        # The value of the field that you want to query. Separate multiple values with commas (,).
        self.container_field_value = container_field_value
        # The container IDs.
        self.container_ids = container_ids
        # The source identifier of the request. Set this parameter to **sas**.
        self.from_ = from_
        # The multi-account query type. Default value: **0**. Valid values:
        # - **0**: Query data of the current account.
        # - **1**: Query data of all accounts.
        self.multi_account_action_type = multi_account_action_type
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The query type. Valid values:
        # 
        # - **containerId**: container ID
        # - **uuid**: asset ID
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.container_ids is not None:
            result['ContainerIds'] = self.container_ids

        if self.from_ is not None:
            result['From'] = self.from_

        if self.multi_account_action_type is not None:
            result['MultiAccountActionType'] = self.multi_account_action_type

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('ContainerIds') is not None:
            self.container_ids = m.get('ContainerIds')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('MultiAccountActionType') is not None:
            self.multi_account_action_type = m.get('MultiAccountActionType')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

