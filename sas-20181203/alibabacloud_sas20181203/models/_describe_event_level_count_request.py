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
        target_type: str = None,
    ):
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The key of the condition that is used to query alert events on containers. Valid values:
        # 
        # *   **instanceId**: the ID of the asset
        # *   **appName**: the name of the application
        # *   **clusterId**: the ID of the cluster
        # *   **regionId**: the ID of the region
        # *   **nodeName**: the name of the node
        # *   **namespace**: the namespace
        # *   **clusterName**: the name of the cluster
        # *   **image**: the name of the image
        # *   **imageRepoName**: the name of the image repository
        # *   **imageRepoNamespace**: the namespace to which the image repository belongs
        # *   **imageRepoTag**: the tag that is added to the image
        # *   **imageDigest**: the digest of the image
        self.container_field_name = container_field_name
        # The value of the condition that is used to query alert events on containers. If you specify multiple values, separate them with commas (,).
        self.container_field_value = container_field_value
        # The ID of the container.
        self.container_ids = container_ids
        # The ID of the request source. Set the value to **sas**.
        self.from_ = from_
        # The type of the accounts that you want to query. Default value: **0**. Valid values:
        # 
        # *   **0**: the current account.
        # *   **1**: all accounts.
        self.multi_account_action_type = multi_account_action_type
        # The type of the query condition. Valid values:
        # 
        # *   **containerId**: the ID of the container
        # *   **uuid**: the UUID of the asset
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

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

