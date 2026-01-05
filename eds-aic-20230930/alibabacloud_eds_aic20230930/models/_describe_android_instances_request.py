# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeAndroidInstancesRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        android_instance_name: str = None,
        app_manage_policy_id: str = None,
        authorized_user_id: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        instance_group_id: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_id: str = None,
        node_name: str = None,
        office_site_ids: List[str] = None,
        private_ip_address: str = None,
        qos_rule_ids: List[str] = None,
        sale_mode: str = None,
        status: str = None,
        tag: List[main_models.DescribeAndroidInstancesRequestTag] = None,
    ):
        # The IDs of the instances.
        self.android_instance_ids = android_instance_ids
        # The name of the instance.
        self.android_instance_name = android_instance_name
        self.app_manage_policy_id = app_manage_policy_id
        self.authorized_user_id = authorized_user_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2807298.html) operation to query the regions where Cloud Phone is supported.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.charge_type = charge_type
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The name of the instance group.
        self.instance_group_name = instance_group_name
        # The ID of the bound key pair.
        self.key_pair_id = key_pair_id
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        self.office_site_ids = office_site_ids
        self.private_ip_address = private_ip_address
        self.qos_rule_ids = qos_rule_ids
        # The sales mode.
        # 
        # Valid values:
        # 
        # *   Instance: the standard mode.
        # *   Node: the node mode.
        self.sale_mode = sale_mode
        # The state of the instance.
        # 
        # Valid values:
        # 
        # *   BACKUPING: The instance is being backed up.
        # *   STARTING: The instance is being started.
        # *   RUNNING: The instance group is available.
        # *   DELETING: The instance is being deleted.
        # *   BACKUP_FAILED: The backup operation failed.
        # *   DELETED: The instance is deleted.
        # *   FAILED: The instance failed to be created.
        # *   STOPPED: The instance is stopped.
        # *   RECOVERING: The instance has an ongoing file recovery task.
        # *   UNAVAILABLE: The instance has an exception.
        # *   REBOOTING: The instance is being restarted.
        # *   RESETTING: The instance is being reset.
        # *   STOPPING: The instance is being stopped.
        # *   RECOVER_FAILED: The file recovery task failed.
        # *   CREATING: The instance is being created.
        self.status = status
        # The tags of the resources.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name

        if self.app_manage_policy_id is not None:
            result['AppManagePolicyId'] = self.app_manage_policy_id

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.office_site_ids is not None:
            result['OfficeSiteIds'] = self.office_site_ids

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.qos_rule_ids is not None:
            result['QosRuleIds'] = self.qos_rule_ids

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')

        if m.get('AppManagePolicyId') is not None:
            self.app_manage_policy_id = m.get('AppManagePolicyId')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OfficeSiteIds') is not None:
            self.office_site_ids = m.get('OfficeSiteIds')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('QosRuleIds') is not None:
            self.qos_rule_ids = m.get('QosRuleIds')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAndroidInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAndroidInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

